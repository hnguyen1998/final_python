#!/usr/bin/python3
#I import the requests to make the requests to web servers.
#json to read the response 

#post url: https://sandboxdnac2.cisco.com/api/system/v1/auth/token
      #username : devnetuser
      #password: Cisco123!
#get url: https://sandboxdnac2.cisco.com/dna/intent/api/v1/template-programmer/project


import requests
import json 
from pprint import pprint

#this is the code from postman API

import requests

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/template-programmer/project"

payload={}
headers = {
  'x-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MjQxOTIzZTU3MjU5NTA2YTU2YjRhYTEiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYyM2YwMjlhNTcyNTk1MDZhNTZhZDljNCJdLCJ0ZW5hbnRJZCI6IjYyM2YwMjk4NTcyNTk1MDZhNTZhZDliZCIsImV4cCI6MTY1MTA4Mjc3MCwiaWF0IjoxNjUxMDc5MTcwLCJqdGkiOiJiMTNiOWVkNi03MmE4LTRmZmItYjg2Yy1mNGQxMWFmZWNlYjAiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.jzrS4f2993ZaGTAZeovn5vFDRyMXFk6JqDmQ17jclc5mCcOIyAbbuzrtKiKhuLgawQvBPTwGNu7czB8d9Ma_kcrqnoPdr-O-VMvuDuwJE9CUnW4q9GvoiUGSrWKtjd7aSp5hH-lJh_ozzUvevEZGXwQ83G7M8dO15hw74U5H8pGsPZGvz5lvV0NxCNMEsfY0Hgiuv8D_vYuaqGq7UjuyvDJ8_NwL4QmQbPywPuvDWpZzQ6S4rXxq4X0y8zO0ZQgWyRW0bFMXFqZ6LCrc2Mu35g4eYgNyg20inJiu8HC8pRx4dM29fyACqg6cjaMKAYMARvKxJ-MOKNjv7CplevkzHQ',
  'Cookie': 'JSESSIONID=802qhtkus6bv9oz5boncp3b'
}



response = requests.request("GET", url, headers=headers, data=payload, verify=False )
response_converted = json.loads(response.text)
#create the new variable 
results = response_converted


#show the project name to select.
#create an empty list named project
project = []
for i in results:
  #for loop to take the data in the dictionaries that we wanted
  project.append(i['name'])
  print(f'Name: {project[-1]}')


#make the input to check the name of project that we want, then output we should have name and id of the project.
#input will assign as string 
input = input(f'Please, input the name of project: ')

#make the loop to check every single dictionaries
for i in results:
  #output will provide the id that match name of project.
  if input == i['name']:
    #create the new list to the data, we will use 
    id = i['id']
    print(f'The project {input} has id: {id}')


 


    










