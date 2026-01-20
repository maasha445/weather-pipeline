from prefect import flow, task
import subprocess

@task
def extract():
    subprocess.run(["python", "get_weather.py"], check=True)

@task
def transform():
    subprocess.run(["python", "clean_data.py"], check=True)

@task
def load():
    # subprocess.run(["python", "load_to_bigquery.py"], check=True)
        print("Skipping BigQuery load step")
@flow
def weather_pipeline():
    extract()
    transform()
    load()

if __name__ == "__main__":
    weather_pipeline()
