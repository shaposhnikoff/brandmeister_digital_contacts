#!/usr/bin/python3

import json,csv,requests,sys
from datetime import datetime, timedelta
from os import path

'''Specify the country ( Ukraine of Belarus ) for selection by country '''
country = "Belarus"
fileInput = "users.json"
fileOutput = "users."+str(country)+"-"+str(datetime.now().strftime("%Y.%m.%d-%H:%M:%S"))+".csv"
fileage = 60
source_file = "https://database.radioid.net/static/users.json"

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

print("checking file...")
try:
    f=open("users.json")
except FileNotFoundError:
    print("file is not exist,need to download it")
    download_file(source_file)

age = datetime.now() - timedelta(minutes=fileage)
filetime = datetime.fromtimestamp(path.getctime(fileInput))

if filetime < age:
    print ("File is more than "+ str(fileage) + " minutes old.")
    download_file(source_file)
else:
    print("file timestamp is ok")

inputFile = open(fileInput)
outputFile = open(fileOutput, 'w')
data = json.load(inputFile)
users_data = data['users']
inputFile.close()
output = csv.writer(outputFile)
output.writerow(["No.","Radio ID","Callsign","Name","City","State","Country","Remarks","Call Type","Call Alert"])

num = 0
for row in users_data:
    if row["country"] == country:
       row["call_type"] = "Private Call"
       row["call_alert"] = "None"
       row["num"] = num = num + 1
       output.writerow([row["num"],
                     row["radio_id"],
                     row["callsign"],
                     row["fname"],
                     row["city"],
                     row["city"],
                     row["country"],
                     row["remarks"],
                     row["call_type"],
                     row["call_alert"]])
