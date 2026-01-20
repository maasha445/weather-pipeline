# End-to-End Weather Data Pipeline

This project demonstrates a complete batch data pipeline built using Python, PostgreSQL, Google BigQuery, and Prefect. 
Raw data is collected from an external API, stored, cleaned, loaded into a cloud data warehouse, and automated through orchestration.

# Project Overview

The pipeline performs the following steps:

1. Extracts real-time weather data from the OpenWeather API  
2. Stores raw data in a local PostgreSQL database  
3. Cleans and transforms the data using Python (Pandas)  
4. Loads processed data into Google BigQuery for cloud storage  
5. Visualizes data through Looker Studio dashboards  
6. Automates the workflow using Prefect orchestration

# Tools & Technologies

- Python  
- Pandas  
- Requests (API calls)  
- PostgreSQL  
- SQLAlchemy  
- Google BigQuery  
- Looker Studio  
- Prefect (workflow orchestration)  
- OpenWeather API  


# Project Structure
weather_pipeline/

├── get_weather.py # Extracts weather data from API
├── load_to_postgres.py # Loads raw data into PostgreSQL
├── clean_data.py # Cleans and transforms data
├── pipeline_flow.py # Prefect workflow automation
├── requirements.txt # Project dependencies
├── .gitignore # Ignored files

# How It Works

**Extract:**  
`get_weather.py` connects to the OpenWeather API and saves raw weather data as a CSV file.

**Load (Local Storage):**  
`load_to_postgres.py` inserts raw data into a PostgreSQL database for structured storage.

**Transform:**  
`clean_data.py` processes and cleans raw data using Pandas.

**Load (Cloud Warehouse):**  
The cleaned data is uploaded to Google BigQuery for scalable cloud-based analytics.

**Automate:**  
`pipeline_flow.py` uses Prefect to orchestrate the full workflow in the correct order.


# Visualization

Google Looker Studio is connected to BigQuery to create an interactive dashboard displaying:

- City  
- Temperature  
- Humidity  
- Weather condition  


# Skills Demonstrated

- API data extraction  
- Relational database management (PostgreSQL)  
- Data cleaning and transformation  
- Cloud data warehousing (BigQuery)  
- Workflow orchestration with Prefect  
- End-to-end pipeline development
  

# How to Run Locally

1. Clone repository:

git clone https://github.com/maasha445/weather-pipeline.git
cd weather-pipeline

markdown
Copy code

2. Install dependencies:

pip install -r requirements.txt

markdown
Copy code

3. Add your OpenWeather API key in `get_weather.py`

4. Run pipeline:

python pipeline_flow.py


# Future Improvements

- Schedule daily runs with Prefect Cloud  
- Add error handling & logging  
- Load clean data automatically to BigQuery  
- Expand to multi-city weather tracking  


# Author

**Maasha Salih**  
Aspiring Data Engineer based in Canada 

