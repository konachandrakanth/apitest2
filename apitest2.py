import requests


api_endpoint="https://nouveau.qtestnet.com/api/v3/projects"
r = requests.get(url = api_endpoint,headers={"Authorization":"bearer 75bc2379-393a-48a2-b656-c2f32bd08f94"})
print(r.text)
#print("data:%s"%data)
