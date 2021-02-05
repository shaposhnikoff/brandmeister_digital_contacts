#!/usr/bin/python3

import json,csv,requests,sys
from datetime import datetime, timedelta
from os import path

fileInput = "users.json"
#fileOutput = "users."+str(datetime.now().strftime("%Y.%m.%d-%H:%M:%S"))+".csv"
fileOutput = "users."+str(datetime.now().strftime("%Y%m%d-%H%M%S"))+".csv"



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
    download_file("https://database.radioid.net/static/users.json")

two_minutes_ago = datetime.now() - timedelta(minutes=2)
filetime = datetime.fromtimestamp(path.getctime(fileInput))

if filetime < two_minutes_ago:
    print ("File is more than two minutes old.")
    download_file("https://database.radioid.net/static/users.json")
else:
    print("file timestamp is ok")


inputFile = open(fileInput)
outputFile = open(fileOutput, 'w')
data = json.load(inputFile)

users_data = data['users']
inputFile.close()
output = csv.writer(outputFile,quotechar='"')
output.writerow(["No.","Radio ID","Callsign","Name","City","State","Country","Remarks","Call Type","Call Alert"])

num = 0
for row in users_data:
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




