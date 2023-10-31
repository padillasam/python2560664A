import requests

s = requests.Session()
response=s.get('https://api.github.com/users')
s.auth('cidesenadev@gmail.com','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')
print(response.status_code)