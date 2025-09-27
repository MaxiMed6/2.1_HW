import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging
import os


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)


log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_search.log')


file_handler = logging.FileHandler(log_file_path, mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope='class')
def auth_session():
    logger.debug("Створення аутентифікованої сесії")

    session = requests.Session()

    username = 'test_user'
    password = 'test_pass'

    try:
        auth_response = session.post(
        f'{BASE_URL}/auth',
            auth=HTTPBasicAuth(username, password)
        )
        auth_response.raise_for_status()

        data = auth_response.json()
        access_token = data.get('access_token')

        if not access_token:
            pytest.fail("Токен доступу не отримано з /auth")

        logger.info(f"Аутентифікація пройшла успішно.")


        session.headers.update({'Authorization': f'Bearer {access_token}'})

        yield session

    except requests.exceptions.RequestException as e:
        logger.error(f"Помилка під час аутентифікації: {e}")
        pytest.fail(f"Не вдалося аутентифікуватися: {e}")
    except ValueError as e:
        logger.error(f"Помилка парсингу JSON з /auth: {e}")
        pytest.fail(f"Некоректна відповідь від /auth: {e}")

    finally:
        session.close()
        logger.debug("Сесія закрита")



test_data = [
    (None, None, "Без параметрів"),
    ("price", 5, "Сортування за ціною, ліміт 5"),
    ("brand", 3, "Сортування за маркою, ліміт 3"),
    ("year", 10, "Сортування за роком, ліміт 10"),
    ("engine_volume", 7, "Сортування за об'ємом, ліміт 7"),
    ("price", None, "Тільки сортування за ціною"),
    (None, 4, "Тільки ліміт 4"),
]


class TestCarSearch:
    @pytest.mark.parametrize("sort_by, limit, description", test_data)
    def test_search_cars(self, auth_session, sort_by, limit, description):

        logger.info(f"Початок тесту: {description}")

        params = {}
        if sort_by is not None:
            params['sort_by'] = sort_by
        if limit is not None:
            params["limit"] = int(limit)

        try:
            response = auth_session.get(f"{BASE_URL}/cars", params=params)

            logger.info(f"Статус-код відповіді: {response.status_code}")
            assert response.status_code == 200

            response_data = response.json()
            assert isinstance(response_data, list)

            logger.info(f"Отримано {len(response_data)} автомобілів")

            if limit is not None:
                assert len(response_data) <= limit

            if response_data:
                first_car = response_data[0]
                expected_keys = {'brand', 'year', 'engine_volume', 'price'}
                actual_keys = set(first_car.keys())
                assert expected_keys.issubset(actual_keys)

                assert isinstance(first_car['brand'], str)
                assert isinstance(first_car['year'], int)
                assert isinstance(first_car['engine_volume'], (int, float))
                assert isinstance(first_car['price'], (int, float))

            logger.info(f"Тест '{description}' пройдено успішно.")

        except requests.exceptions.RequestException as e:
            logger.error(f"Помилка мережевого запиту під час тесту '{description}': {e}")
            pytest.fail(f"Помилка запиту: {e}")
        except ValueError as e:
            logger.error(f"Помилка парсингу JSON під час тесту '{description}': {e}")
            pytest.fail("Некоректна відповідь JSON")
        except AssertionError as e:
            logger.error(f"Помилка перевірки твердження під час тесту '{description}': {e}")
            raise
