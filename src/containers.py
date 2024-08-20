from os import environ

from dependency_injector.containers import Container
from dependency_injector.providers import Singleton, Factory

from auth.secrets import Secrets
from database import Database


class Kernel(Container):
    secrets = Factory(
        Secrets,
        path_to_secrets=environ.get("PATH_TO_SECRETS"),
    )
    database = Singleton(
        Database,
        db_name=environ.get("DB_NAME"),
        db_user=environ.get("DB_USER"),
        db_pass=secrets().get("DB_PASS"),
        async_=False,
    )
