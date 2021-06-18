import requests

def ImageParse(name, img):
    r = requests.get(img).content
    with open(f"Images\{name}.jpg", "bw+") as imgWriter:
        imgWriter.write(r)
