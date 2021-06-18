import requests
import re

def ImageParse(name, img):
    imgName = re.search(r"\d{9}.*\...g", img)

    print(imgName.group(0))

    r = requests.get(img).content
    
    with open(f"Images\{name}.jpg", "bw+") as imgWriter:
        imgWriter.write(r)
