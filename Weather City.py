import requests

def get_weather(city):
    try:
        # Step 1: Get city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(geo_url, params=geo_params, timeout=10)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if "results" not in geo_data:
            print("City not found!")
            return

        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "")

        # Step 2: Get weather information
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "weather_code",
                "wind_speed_10m"
            ]
        }

        weather_response = requests.get(
            weather_url, params=weather_params, timeout=10
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current"]

        print("\n========== WEATHER REPORT ==========")
        print("City:", city_name, country)
        print("Temperature:", current["temperature_2m"], "°C")
        print("Feels Like:", current["apparent_temperature"], "°C")
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Wind Speed:", current["wind_speed_10m"], "km/h")
        print("Weather Code:", current["weather_code"])
        print("====================================")

    except requests.exceptions.RequestException:
        print("Network error! Please check your internet connection.")

    except (KeyError, IndexError, ValueError):
        print("Unable to process weather information.")


print("WELCOME TO WEATHER APP")

city = input("Enter city name: ")

get_weather(city)