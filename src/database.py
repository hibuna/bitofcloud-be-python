from asyncio import current_task

from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.asyncio import async_scoped_session, async_sessionmaker, create_async_engine, AsyncEngine
from sqlalchemy.orm import scoped_session, sessionmaker


class Database:
    engine: Engine = None
    async_engine: AsyncEngine = None

    def __init__(self, db_user: str, db_pass: str, db_name: str, async_: bool) -> None:
        url = f"postgresql+psycopg://{db_user}:{db_pass}@db:5432/{db_name}"
        if async_:
            self.async_engine = create_async_engine(url=url)
        self.engine = create_engine(url=url)

    def scoped_session(self) -> scoped_session:
        if not self.engine:
            raise Exception  # TODO: specify error
        return scoped_session(session_factory=sessionmaker(bind=self.engine))

    def async_scoped_session(self) -> async_scoped_session:
        if not self.async_engine:
            raise Exception  # TODO: specify error
        return async_scoped_session(session_factory=async_sessionmaker(bind=self.async_engine), scopefunc=current_task)
