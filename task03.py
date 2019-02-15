import requests
import json

url = 'https://sandboxapicem.cisco.com/api/v1/ticket'


body = {"username":"devnetuser","password":"Cisco123!"}


header = {"content-type": "application/json"}

response= requests.post(url,data=json.dumps(body), headers=header, verify=False)

res=response.json()
print(json.dumps(res,indent=4))
print('=====')
serviceticket=res['response']['serviceTicket']


url = "https://sandboxapicem.cisco.com/api/v1/host"

header["X-Auth-Token"]=serviceticket
response = requests.get(url, headers=header, verify=False)

print (response)
