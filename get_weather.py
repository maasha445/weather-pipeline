import requests
import pandas as pd

API_KEY = "71a646c0f8fa52db864694951ddc1cd1"
CITY = "Toronto"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

weather = {
    "city": CITY,
    "temperature": data["main"]["temp"],
    "humidity": data["main"]["humidity"],
    "weather": data["weather"][0]["description"]
}

df = pd.DataFrame([weather])
df.to_csv("raw_weather.csv", index=False)

print("Saved raw_weather.csv")
