import requests

url = 'http://127.0.0.1:5050/upload'
file = {'file': open('tests/audio.mp3', 'rb')}
resp = requests.post(url=url, files=file) 
print(resp.json())