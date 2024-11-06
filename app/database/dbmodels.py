import datetime
from typing import Annotated
from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
ticker = Annotated[str, mapped_column(String(100))]
gained_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE ('utc', now())"))]

class Currencies(Base):
    __tablename__ = 'currencies'

    id: Mapped[intpk]
    ticker: Mapped[ticker]
    price: Mapped[float]
    gained_at: Mapped[gained_at]

    repr_col_num = 4
