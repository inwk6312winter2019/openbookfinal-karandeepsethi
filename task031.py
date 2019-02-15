mport requests

import json

controller='sandboxapic.cisco.com'

url = "https://" + controller + "/api/v1/ticket"

payload = {"username":"devnetuser","password":"Cisco123!"}

header = {"content-type": "application/json"}

response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

r_json=response.json()

print(r_json)

ticket = r_json["response"]["serviceTicket"]

url = "https://sandboxapic.cisco.com/api/v1/host"

header = {"content-type": "application/json", "X-Auth-Token":"ST-112-UcRk2hJkrYVlylTVgEmq-cas"}

response = requests.get(url, headers=header, verify=False)

print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

r_resp=response.json()
d={}
for item in r_resp['response']:
	d[(item["connectedNetworkDeviceId"],item["hostIp"])]=item["hostMac"]
print(d)

