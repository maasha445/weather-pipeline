import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("raw_weather.csv")

engine = create_engine("postgresql://postgres:maasha123@localhost:5432/weather_db")
connection = engine.raw_connection()
df.to_sql("raw_weather", engine, if_exists="append", index=False)

print("Loaded into PostgreSQL")
