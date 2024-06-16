from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

USER = "jesper"
PASSWORD = "jesper"
HOST = "localhost"
PORT = 5432
DATABASE = "planerek"


class PostgresClient:
    def __init__(self) -> None:
        self.engine = create_engine(
            f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
        )
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        session = self.SessionLocal()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def execute_raw_query(self, query: str) -> None:
        # Replace with comething usefule
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            for row in result:
                print(row)

    def execute_sql_file(self) -> None:
        pass
