from aiohttp import ClientSession

from .data_parser import parse_weather_data


async def request_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            try:
                result = parse_weather_data(weather_json)
                return result
            except KeyError:
                return "No data"
