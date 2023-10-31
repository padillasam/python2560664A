import requests

s = requests.Session()
s.auth=('cidesenadev@gmail.com','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')
response=s.get('https://api.github.com/users')
print(response.status_code)
if response.status_code==200:
    response1=s.get('https://github.com/cidesena')
    print(response1.cookies)
