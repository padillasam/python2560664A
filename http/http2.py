import requests
import json
#url="http://httpbin.org/get?formacion=adso&ficha=2566404"
url='http://httpbin.org/get'
argumentos={'formacion':'adso','ficha':2566404}
response=requests.get(url, params=argumentos)
rtastr=response.content.decode()
print(type(rtastr))
rta=json.loads(rtastr)
#rta=response.json()
print(type(rtastr))
print(rtastr)