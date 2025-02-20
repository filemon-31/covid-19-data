import requests
import pandas as pd

# Extract
URL = "https://api.covid19api.com/summary"
response = requests.get(URL)
data = response.json()

# Transform
df = pd.DataFrame(data["Countries"])
df = df[["Country", "TotalConfirmed", "TotalDeaths", "Date"]]

# Load (Save to CSV for now, can be updated to store in a database)
df.to_csv("covid_data.csv", index=False)
print("ETL process completed and data saved to covid_data.csv")