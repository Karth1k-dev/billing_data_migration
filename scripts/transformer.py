def transform_data(data):

    # fill missing emails with default value
    data['email'] = data['email'].fillna("unknown@email.com")

    # convert price column to integer
    data['price'] = data['price'].astype(int)

    return data

def convert_to_json(data):

    # convert dataframe into list of dictionaries
    json_data = data.to_dict(orient="records")

    return json_data

"""
Explanation
data['email']

means email column

fillna()
fillna("unknown@email.com")

Replaces missing values.

Before:

Mary, NaN

After:

Mary, unknown@email.com
astype(int)

Ensures price is numeric.

"10"  →  10

Important for database storage.

-----------------------------------------------------------

Why JSON?

Most APIs accept JSON format.

Example JSON output:

[
 {
  "customer_id":1,
  "name":"John",
  "email":"john@email.com",
  "plan":"Basic",
  "price":10
 },
"""