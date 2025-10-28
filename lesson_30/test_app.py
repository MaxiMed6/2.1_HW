import pytest
import allure
from app import connect_to_db, create_table, insert_record, update_record, delete_record, select_records


@pytest.fixture(scope="session")
def db_connection():
    conn = connect_to_db()
    create_table(conn)
    yield conn
    conn.close()


@pytest.fixture(scope="function", autouse=True)
def clean_table(db_connection):
    cur = db_connection.cursor()
    cur.execute("TRUNCATE TABLE test_table RESTART IDENTITY")
    db_connection.commit()
    cur.close()
    yield


@allure.feature("Database Operations")
def test_connection(db_connection):
    with allure.step("Проверка подключения к БД"):
        assert db_connection is not None


@allure.feature("Database Operations")
def test_insert_and_select(db_connection):
    with allure.step("Вставка записи"):
        insert_record(db_connection, "Test1")
    with allure.step("Проверка, что запись добавлена"):
        records = select_records(db_connection)
        assert len(records) == 1
        assert records[0][1] == "Test1"


@allure.feature("Database Operations")
def test_update(db_connection):
    with allure.step("Вставка записи"):
        insert_record(db_connection, "Old")
    with allure.step("Получение ID"):
        records = select_records(db_connection)
        id_val = records[0][0]
    with allure.step("Обновление записи"):
        update_record(db_connection, id_val, "New")
    with allure.step("Проверка обновления"):
        records = select_records(db_connection)
        assert len(records) == 1
        assert records[0][1] == "New"


@allure.feature("Database Operations")
def test_delete(db_connection):
    with allure.step("Вставка записи"):
        insert_record(db_connection, "ToDelete")
    with allure.step("Получение ID"):
        records = select_records(db_connection)
        id_val = records[0][0]
    with allure.step("Удаление записи"):
        delete_record(db_connection, id_val)
    with allure.step("Проверка, что запись удалена"):
        records = select_records(db_connection)
        assert len(records) == 0