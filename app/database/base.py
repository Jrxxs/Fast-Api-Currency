from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.config import db_settings


engine = create_async_engine(
    db_settings.DATABASE_URL_asyncpg,
    echo=True
)

session_factory = async_sessionmaker(engine)

class Base(DeclarativeBase):

    repr_col_num = 1
    repr_cols_name = tuple()
    
    def __repr__(self) -> str:
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols_name or idx < self.repr_col_num:
                cols.append(f"{col}:{getattr(self, col)}")
        return f"<{self.__class__.__name__}: {', '.join(cols)}>"
