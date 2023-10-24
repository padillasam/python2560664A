import requests
import json
#url="http://httpbin.org/get?formacion=adso&ficha=2566404"
#url='http://httpbin.org/put'
url='http://httpbin.org/delete'
argumentos={'formacion':'adso','ficha':2566404}
#response=requests.post(url, params=argumentos)
#response=requests.post(url, json=argumentos)
#response=requests.post(url, data=argumentos)
#response=requests.put(url, data=json.dumps(argumentos))
response=requests.delete(url, data=json.dumps(argumentos))
#response=requests.post(url)
rtastr=response.content.decode()
print(rtastr)