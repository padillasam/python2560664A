import requests
url='https://api.covidtracking.com/v2/states.json'
response=requests.get(url)
#print(response.content.decode())
rta=response.json()

# print(type(rta))
# print(rta['data'][0]['name'])
# lista=[state for state in rta['data'][0]['name']]
# print(lista)
i=0
for key in rta.keys():
    print(rta['data'][i]['name'])
    i=i+1



# for key in rta.keys():
#      if key=='data':
#          for k in rta[key]:
#              print(type(k))
#              for clave in k.keys():
#                  print(clave)   


