# run_pipeline.py
import os

# Step 1: Pull data
os.system("python get_weather.py")

# Step 2: Clean data
os.system("python clean_data.py")

# Step 3: Load to PostgreSQL
os.system("python load_to_postgres.py")

print("Pipeline completed successfully!")
