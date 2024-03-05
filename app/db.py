from datetime import datetime

import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Weather(ormar.Model):
    class Meta(BaseMeta):
        tablename = "weather"

    id: int = ormar.Integer(primary_key=True)
    country: str = ormar.String(max_length=100, nullable=False)
    city: str = ormar.String(max_length=100, nullable=False)
    weather: str = ormar.String(max_length=150, nullable=False)
    description: str = ormar.String(max_length=200, nullable=True)
    temperature: int = ormar.Integer()
    feels_like: int = ormar.Integer()
    wind: int = ormar.Float()
    user_notes: str = ormar.String(max_length=1200, nullable=True)
    created_on = ormar.DateTime(default=datetime.now())


class WeatherUser(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=128, unique=True, nullable=False)
    surname: str = ormar.String(max_length=128, unique=True, nullable=False)
    created_on = ormar.DateTime(default=datetime.now())


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
