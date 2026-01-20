import pandas as pd

df = pd.read_csv("raw_weather.csv")

df["temperature"] = df["temperature"].round(1)

df.to_csv("clean_weather.csv", index=False)

print("Saved clean_weather.csv")
