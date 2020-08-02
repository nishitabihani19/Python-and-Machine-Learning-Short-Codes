import requests,json
url="https://api.thingspeak.com/update?api_key=SPYLYPBOT19G7GB9&field1=python"
result=requests.get(url)
result=result.json()
print(result)
