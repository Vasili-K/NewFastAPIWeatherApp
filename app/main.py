from fastapi import APIRouter, FastAPI

from app.db import database, WeatherUser, Weather
from app.models.weather_models import WeatherResponse
from app.weather_request import request_weather

# weather_router = APIRouter()

# main point of interaction to create API
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello From Weather Application"}


@app.get("/users")
async def read_root():
    return await WeatherUser.objects.all()


@app.get("/weather")
async def get_weather(city: str, save: bool = True) -> WeatherResponse | str:
    result = await request_weather(city)
    try:
        weather_description = WeatherResponse(**result)
    except Exception:
        return "Probably you asked for something unexpected. Try another request."

    if save:
        await Weather.objects.create(**weather_description.dict())

    return weather_description


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await WeatherUser.objects.get_or_create(name="Tony", surname="Stark")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


# app.include_router(weather_router, prefix="/api/v1", tags=["Weather Endpoint"])

