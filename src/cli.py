import sys
from src.weather import get_temperature, get_forecast

def main():
    if len(sys.argv) < 2:
        print("Usage: weather <city> [--forecast]")
        sys.exit(1)
    city = sys.argv[1]
    if "--forecast" in sys.argv:
        forecast = get_forecast(city)
        print(f"Forecast for {city}:")
        for day in forecast:
            print(f"  {day['date']}: max {day['maxtempC']}C, min {day['mintempC']}C")
    else:
        temp = get_temperature(city)
        print(f"Temperature in {city}: {temp}C")

if __name__ == "__main__":
    main()
