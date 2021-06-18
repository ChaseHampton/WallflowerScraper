from bs4 import BeautifulSoup
import requests
import re
import json
import Images
import os


headers = {'Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
source = requests.get('https://www.bathandbodyworks.com/c/home-fragrance/wallflowers-refills', headers=headers)
soup = BeautifulSoup(source.text, 'lxml')
div = soup.find(id='search-result-items')
wfs = []     
imgList = []

if not os.path.isdir('Images'):
    os.mkdir('Images')
    
def CreateJson(data):
    with open('wallflowers.json','w') as writer:
        json.dump(data, writer)


def NextPage(soup):
    next = soup.find('a', attrs={"class": 'page-next'})
    if next:
        return next['href']
    else:
        return False


def ParseWFs(list):
    for item in list:
        wfName = item.find(class_="product-name").text.replace('\n\n','')
        wfPrice = item.find('div', attrs={'class': 'product-pricing'}).span.text
        wfType = item.find(class_='product-type').text.replace('\n\n','')
        wfs.append({'name': wfName,'price':wfPrice,'type':wfType})
        imgList.append((item.find('img')['src'],wfName))
        


ParseWFs(div.find_all('li', attrs={'class': re.compile('^grid-tile.*')}))
while NextPage(soup):
    source = requests.get(NextPage(soup), headers=headers)
    soup = BeautifulSoup(source.text, 'lxml')
    div = soup.find(id='search-result-items')
    ParseWFs(div.find_all('li', attrs={'class': re.compile('^grid-tile.*')}))

CreateJson(wfs)

for img in imgList:
    Images.ImageParse(img[1],img[0])
