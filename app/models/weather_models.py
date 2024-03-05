from typing import Optional

from pydantic import BaseModel


# class WeatherRequest(BaseModel):
#     city: str
#     save: Optional[bool] = False


class WeatherResponse(BaseModel):
    country: str
    city: str
    weather: str
    description: str
    temperature: int
    feels_like: int
    wind: float
