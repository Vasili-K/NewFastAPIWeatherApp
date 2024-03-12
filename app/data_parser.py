def parse_weather_data(weather_row_data: dict) -> dict:
    """
    This function is responsible for preparation of information about requested weather

    :param weather_row_data: dict with all the data received from weather API
    :return: dict with a set of required weather data
    """
    try:
        weather_city = weather_row_data["name"]
        weather_country = weather_row_data["sys"]["country"]
        weather = weather_row_data["weather"][0]["main"]
        weather_description = weather_row_data["weather"][0]["description"]
        temperature = round(weather_row_data["main"]["temp"] - 273.15)
        feels_like = round(weather_row_data["main"]["feels_like"] - 273.15)
        wind = weather_row_data["wind"]["speed"]
        result = {
            'city': weather_city,
            'country': weather_country,
            'weather': weather,
            'description': weather_description,
            'temperature': temperature,
            'feels_like': feels_like,
            'wind': wind
        }
    except KeyError as exc:
        raise KeyError("Impossible to parse weather data.") from exc
    return result
