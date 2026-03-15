import pandas as pd   # library used for data processing

file_path = "data/customers.csv"
def extract_data(file_path):

    # read csv file
    data = pd.read_csv(file_path)

    # return dataframe
    return data

''' 
example data frame output :
        customer_id name email plan price
        1 John john@email.com Basic 10
        2 Mary NaN Premium 30
'''
# NaN = missing value
