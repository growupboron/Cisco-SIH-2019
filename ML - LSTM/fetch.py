import pandas
import requests
url = 'https://api.meraki.com/api/v0/devices/Q2FV-VVSR-NQ8U/camera/analytics/zones/0/history?t0=2019-03-03T05:00:00.000Z&t1=2019-03-03T19:00:00.000Z'
headers = {
  'X-Cisco-Meraki-API-Key': '95fd3d5813312dc8f7ff283181b58b97b5ffb51d',
  'Accept': '*/*'
}
response = requests.get(url, headers = headers,allow_redirects="true")
history=pandas.read_json(response.text,encoding='utf-8')
history.to_csv("./5-19PST.csv",encoding='utf-8',sep='\t',index=False)
