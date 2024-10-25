from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource indentifier
uri = "mongodb+srv://piyush:12345@softwaredata.vlfws.mongodb.net/?retryWrites=true&w=majority&appName=Softwaredata"

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="SoftwareDefects"

# read the data as a dataframe
df=pd.read_csv(r"E:\Software_defects_detection\notebooks\encoded_software_defect_detection_3.csv")
df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
