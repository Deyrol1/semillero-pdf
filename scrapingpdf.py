#importando librerias
import requests
import json
import os
from bs4 import BeautifulSoup
#Haciendo la peticón para extraer el html y se pone la página que quiero hacer el scraping


datos = []
with open("urls.txt") as fname:
	lineas = fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))

num_paginas=len(datos)

data = {}
data['urlpdf'] = []
sitios = []
for i in range(num_paginas):
    url=datos[i]
    pagina= requests.get(url)
    #leyendo la información guardada en page
    soup = BeautifulSoup(pagina.content,'html.parser')
    #buscando las etiquetas que quiero 
    info = soup.find_all('a')
    #recorriendo las etiquetas
    
    for tag in info:
        prueba= tag.get('href')
        if prueba.startswith("http") and prueba.endswith("pdf"):
            sitios.append([tag.get('href'),url])



for i in range(len(sitios)):
    
    try:
        
        data['urlpdf'].append({
            'numero': i+1,
            'urlpdf':sitios[i][0],
            'nombre': os.path.split(sitios[i][0])[1],
            'pag_origen':sitios[i][1]
        })
        
        with open('urlpdf.json', 'w') as file:
            json.dump(data, file, indent=1)
    except:
        print("error",i)


            

