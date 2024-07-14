import openmeteo_requests

def getWeatherData() -> str:
    openmeteo = openmeteo_requests.Client()
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"current": ["is_day", "rain"],
}
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    current = response.Current()
    current_is_day = current.Variables(0).Value()
    current_is_raining = current.Variables(1).Value()

    day_or_not = "Tag" if current_is_day == 1.0 else "Nacht"
    rain_or_not = "regnet" if current_is_raining == 0.0 else "regnet nicht"

    return f"Lat: {response.Latitude()}\nLong: {response.Longitude()}\nEs ist {day_or_not} und es {rain_or_not}!"

    
