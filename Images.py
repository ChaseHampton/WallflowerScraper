from bs4 import BeautifulSoup
import requests
import re
import json

headers = {'Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
source = requests.get('https://www.bathandbodyworks.com/c/home-fragrance/wallflowers-refills', headers=headers)

soup = BeautifulSoup(source.text, 'lxml')
div = soup.find(id='search-result-items')

print(div.find('img')['src'])

def ImageParse(name, img):
    r = requests.get(img).content
    with open(f"Images\{name}.jpg", "bw+") as imgWriter:
        imgWriter.write(r)
