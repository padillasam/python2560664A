import requests
import json
#url="http://httpbin.org/get?formacion=adso&ficha=2566404"
url='http://httpbin.org/post'
argumentos={'formacion':'adso','ficha':2566404}
#response=requests.post(url, params=argumentos)
#response=requests.post(url, json=argumentos)
#response=requests.post(url, data=argumentos)
response=requests.post(url, data=json.dumps(argumentos))
#response=requests.post(url)
rtastr=response.content.decode()
print(rtastr)