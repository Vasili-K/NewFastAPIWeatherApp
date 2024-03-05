import json

import pytest
from pytest_bdd import scenario, given, when, then, parsers

from app.data_parser import parse_weather_data


@pytest.fixture
def context():
    yield {}


@pytest.fixture
def request_data():
    with open('tests/weather_service/fixtures/weather_data.json') as data:
        weather_data = json.load(data)
        yield weather_data


@scenario('data_parser.feature', 'Parse data - Successful')
def test_parse_data():
    pass


@given(parsers.parse('Receive weather data for parsing'))
def step_receive_data(context, request_data):
    context['data'] = request_data
    assert type(request_data) == dict


@when('Service parse the received data')
def step_parse_data(context):
    data = context['data']
    result = parse_weather_data(data)
    context['result'] = result


@then('Result is successful and equal to expected response')
def step_compare_parse_results(context):
    expected_response = {
        'city': 'Warsaw',
        'country': 'PL',
        'description': 'light rain',
        'feels_like': 2,
        'temperature': 6,
        'weather': 'Rain',
        'wind': 4.63
    }
    actual_response = context['result']
    assert expected_response == actual_response


@when(parsers.parse('Field {field} remove from weather data'))
def step_remove_field(context, field):
    data = context['data']
    data.pop(field)
    context['error_data'] = data


@then("I should see a KeyError error message")
def get_error_message(context):
    with pytest.raises(KeyError) as exp:
        parse_weather_data(context['error_data'])
