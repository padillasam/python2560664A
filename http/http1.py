import requests
url="https://hotelskiline.000webhostapp.com/index.html"
#url="http://httpstat.us/"

response=requests.get(url)
#print(type(response))
#print(response.content)
#print(response.status_code)
# if response.status_code==200:
#     print(response.status_code)
#     flujo=open('http/index.html','wb')
#     flujo.write(response.content)
    



# Verifica si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Encuentra el contenido CSS dentro del HTML
    css_content = ''
    for line in response.text.split('\n'):
        if '<link rel="stylesheet"' in line:
            start = line.find('href="') + 6
            end = line.find('"', start)
            css_url = line[start:end]
            if not css_url.startswith('http'):
                # Construye la URL completa si es una URL relativa
                css_url = url + '/' + css_url.lstrip('/')
            css_response = requests.get(css_url)
            if css_response.status_code == 200:
                css_content += css_response.text

    # Guarda el contenido CSS en un archivo
    with open('styles.css', 'w', encoding='utf-8') as css_file:
        css_file.write(css_content)

    print('El CSS ha sido descargado y guardado en "styles.css".')

else:
    print(f'Error al realizar la solicitud. Código de respuesta: {response.status_code}')
