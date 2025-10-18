from dynaconf import Dynaconf
from os.path import join
from constants import BASE_PATH

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[join(BASE_PATH, "base_settings.ini")],
    load_dotenv=True,
    environments=True
)


print(settings.BASE_URL)