from copy import deepcopy

import pytest

from app.data_parser import parse_weather_data


class TestParseWeatherData:
    TEST_ERROR_MSG = 'Impossible to parse weather data.'
    TEST_REQUEST = {
        'coord': {'lon': 21.0118, 'lat': 52.2298},
        'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}],
        'base': 'stations',
        'main': {
            'temp': 278.89,
            'feels_like': 275.59,
            'temp_min': 277.05,
            'temp_max': 279.94,
            'pressure': 994,
            'humidity': 88
        },
        'visibility': 9000,
        'wind': {'speed': 4.63, 'deg': 90},
        'rain': {'1h': 0.42},
        'clouds': {'all': 40},
        'dt': 1707640963,
        'sys': {
            'type': 2,
            'id': 2035775,
            'country': 'PL',
            'sunrise': 1707631245,
            'sunset': 1707665986
        },
        'timezone': 3600,
        'id': 756135,
        'name': 'Warsaw',
        'cod': 200
    }
    EXPECTED_RESPONSE = {
        'city': 'Warsaw',
        'country': 'PL',
        'description': 'light rain',
        'feels_like': 2,
        'temperature': 6,
        'weather': 'Rain',
        'wind': 4.63
    }

    def test_parse_weather_data(self):
        actual = parse_weather_data(self.TEST_REQUEST)
        assert actual == self.EXPECTED_RESPONSE

    @pytest.mark.parametrize('absent_field, ', ['name', 'sys', 'weather', 'main', 'wind'])
    def test_parse_weather_data_error(self, absent_field):
        data = deepcopy(self.TEST_REQUEST)
        data.pop(absent_field)

        with pytest.raises(KeyError, match=self.TEST_ERROR_MSG):
            parse_weather_data(data)
