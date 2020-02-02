import pandas
import requests
url = 'https://api.meraki.com/api/v0/devices/Q2FV-VVSR-NQ8U/camera/analytics/zones'
headers = {
  'X-Cisco-Meraki-API-Key': 'eb4284952dd7d18006745dd828b4e919030f7fec',
  'Accept': '*/*'
}
response = requests.get(url, headers = headers,allow_redirects="true")
history=pandas.read_json(response.text,encoding='utf-8')
history.to_csv("./data-zone1.csv",encoding='utf-8',sep='\t',index=False)
