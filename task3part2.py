import requests


import json

controller='sandboxapic.cisco.com'

url = "https://sandboxapic.cisco.com/api/v1/ticket"


payload = {"username":"devnetuser","password":"Cisco123!"}


header = {"content-type": "application/json"}

#Performs a POST on the specified url to get the service ticket
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)


r_json=response.json()

print(r_json)
ticket = r_json["response"]["serviceTicket"]


url = "https://sandboxapic.cisco.com/api/v1/host"
header = {"content-type": "application/json", "X-Auth-Token":"ST-112-UcRk2hJkrYVlylTVgEmq-cas)
response = requests.get(url, headers=header, verify=False)

print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

r_resp=response.json()
d={}
for item in r_resp['response']:

	d[(item["connectedNetworkDeviceId"],item["hostIp"])]=item["hostMac"]  #as all the three responce doesnot have hostname i took networkid of devices
print(d)

def getnetworkdevicecount(response):
	c=0
	for item in response["response"]:
		c=c+1
	return c
d=getnetworkdevicecount(r_resp)
print(d)
