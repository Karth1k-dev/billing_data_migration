from scripts.extractor import extract_data
from scripts.transformer import transform_data, convert_to_json
from scripts.loader import load_to_database
from api.api_client import send_to_api

file_path = "data/customers.csv"

# Step 1: extract data from csv
data = extract_data(file_path)

# Step 2: clean and transform data
data = transform_data(data)

# Step 3: convert data to json format
json_data = convert_to_json(data)

# Step 4: store data in database
load_to_database(json_data)

# Step 5: send data to api
response = send_to_api(json_data)

print("API Responses:", response)

print("Data migration completed")