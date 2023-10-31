import requests
url='http://httpbin.org/cookies'
#sesion=requests.session()
mycookies={
    'my-cookie':'True'
}
response=requests.get(url,cookies=mycookies)
print(response.content)
print('-'*50)
print(response.cookies)