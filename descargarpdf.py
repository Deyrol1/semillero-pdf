import os
import requests
from time import time
import json
from multiprocessing.pool import ThreadPool

def url_response(url):
    path, url = url
    r = requests.get(url, stream = True)
 
    with open(path, 'wb') as f:
 
        for ch in r:
            f.write(ch)

def url_response(url):
    path, url = url
    r = requests.get(url, stream = True)

    with open(path, 'wb') as f:

        for ch in r:
            f.write(ch)


urls = []


with open('urlpdf.json') as file:
    data = json.load(file)

    for urlpdfs in data['urlpdf']:
        urls.append([urlpdfs['nombre'],urlpdfs['urlpdf']])
start = time()
for x in urls:
    url_response (x)
