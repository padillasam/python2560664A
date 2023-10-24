import requests
import json
#url="http://httpbin.org/get?formacion=adso&ficha=2566404"
url='http://httpbin.org/post'
argumentos={'formacion':'adso','ficha':2566404}
myheader={
     'content-type': 'application/json',
     'access-token':b'12345'
}
response=requests.post(url, data=json.dumps(argumentos),headers=myheader)
#response=requests.post(url)
rtastr=response.content.decode()
print(rtastr)