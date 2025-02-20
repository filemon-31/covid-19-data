# COVID-19 ETL Pipeline

This project automates the extraction, transformation, and loading (ETL) of COVID-19 data.

## Workflow Overview
1. **Extract**: Fetches data from the COVID-19 API.
2. **Transform**: Cleans and structures the data.
3. **Load**: Saves data to a CSV file (can be modified for databases).

## Running Locally
```bash
pip install -r requirements.txt
python etl_script.py