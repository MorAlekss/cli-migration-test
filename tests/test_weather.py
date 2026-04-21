from unittest.mock import patch, MagicMock
from src.weather import get_weather, get_temperature, get_forecast

def test_get_weather():
    mock_response = MagicMock()
    mock_response.json.return_value = {"current_condition": [{"temp_C": "20"}], "weather": []}
    mock_response.raise_for_status.return_value = None
    with patch('src.weather.requests.get', return_value=mock_response):
        result = get_weather("London")
        assert "current_condition" in result

def test_get_temperature():
    mock_response = MagicMock()
    mock_response.json.return_value = {"current_condition": [{"temp_C": "20"}], "weather": []}
    mock_response.raise_for_status.return_value = None
    with patch('src.weather.requests.get', return_value=mock_response):
        result = get_temperature("London")
        assert result == "20"

def test_get_forecast():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "current_condition": [{"temp_C": "20"}],
        "weather": [
            {"date": "2026-04-20", "maxtempC": "22", "mintempC": "15"},
            {"date": "2026-04-21", "maxtempC": "19", "mintempC": "12"},
        ]
    }
    mock_response.raise_for_status.return_value = None
    with patch('src.weather.requests.get', return_value=mock_response):
        result = get_forecast("London", days=2)
        assert len(result) == 2
