from namara_python import Client
import pandas as pd
import numpy as np

# def readIntoCSV(data):
    # d = {'col1': [1, 2], 'col2': [3, 4]}

client = Client(
    api_key='a4f37d48d306c1833be0cf951e190b8480a964de69a4fa61c68e67d5d582698d',  
    auth_url='https://account.dataxch.ai',
    api_url='https://api.dataxch.ai'
)

resp = client.query(statement="SELECT * from 7ea47825-53c0-4dd3-9b37-e0a20c074c5a")
keys = []
dataSet = {}

#this follow block creates the format needed to make a csv via pandas
for row in resp:
    if(len(keys) == 0 ):
        dataSetColHeaders = row.keys()
        for header in dataSetColHeaders:
            keys.append(header)
            dataSet[header] = []
    for key in keys:
        dataSet[key].append(row[key])

df = pd.DataFrame(dataSet)

#saves to your current directoy where you are running from. Change the csv file to something of yhour liking
df.to_csv(r'.\insertfilename.csv', index = False)