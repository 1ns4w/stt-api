import requests

url = 'http://127.0.0.1:5050/api/upload'
file = {'file': open('tests/audio.mp3', 'rb')}
print('sending')
resp = requests.post(url=url, files=file) 
print(resp.json())