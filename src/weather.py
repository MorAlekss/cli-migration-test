import httpx

BASE_URL = "https://wttr.in"

async def get_weather(city):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{city}?format=j1")
        response.raise_for_status()
        return response.json()

async def get_temperature(city):
    data = await get_weather(city)
    return data["current_condition"][0]["temp_C"]

async def get_forecast(city, days=3):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{city}?format=j1")
        response.raise_for_status()
        data = response.json()
        return data["weather"][:days]
