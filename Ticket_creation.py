import requests, json
from requests.auth import HTTPBasicAuth


URL = "https://dev98790.service-now.com/api/now/table/incident"
RequestBody =  {
                    "short_description": "Fourth ticket testing from Rest API not with Manual",
                    "description": "Snow Rest API",
                    "caller_id": "anjan4273"
                }
Hedaers =   {
             "Content-Type": "application/json",
             "Accept": "application/json"
            }

response = requests.post(url = URL, headers = Hedaers, data = json.dumps(RequestBody), auth = HTTPBasicAuth("admin", "ebNqr9AJMPw3"))

if response.status_code == 201:
    IncidentNumber = response.json()['result']['number']
    SysId = response.json()['result']['sys_id']
else:
    print("Failed to create Incident")

print(IncidentNumber)
print(SysId)
