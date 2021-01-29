import requests
import json

res_get = requests.get('http://httpbin.org/')
res_post = requests.post('http://httpbin.org/post', data={'key': 'value'})
res_jpeg = requests.get('https://httpbin.org/image/jpeg')
with open('image.jpeg', 'wb') as image:
    image.write(res_jpeg.content)
res_json = requests.get('https://httpbin.org/json').json()
with open('data_file.json', 'w') as data_file:
    json.dump(res_json, data_file)
