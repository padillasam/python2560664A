import requests
url='https://miro.medium.com/v2/resize:fit:512/format:webp/1*ztqS5rRI29GHxZa6uPF2UA.png'
response=requests.get(url,stream=True)

with open('httppractice/imgpython.png','wb') as pythonimg:
    for i in response.iter_content():
        pythonimg.write(i)
