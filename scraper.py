#Python 3.11.9
#Oct 14 2024
#Aaron Beckley
#
#Downloads all pdf and pptx files from CHIA guides website

import requests
import os
from bs4 import BeautifulSoup

workgrouppresentations = "https://www.chiamass.gov/chia-data-user-workgroup-information/"
previousworkgrouppresentations = "https://www.chiamass.gov/previous-chia-data-user-workgroup-presentations/"

if not os.path.exists('chiafiles'):
    os.makedirs('chiafiles')


#first
html = requests.get(workgrouppresentations)
hreflinks = BeautifulSoup(html.text)
for link in hreflinks.findAll("a"):
    if "/assets" in str(link.get("href")):
        download = "https://www.chiamass.gov" + str(link.get("href"))
        with open("chiafiles/"+str(download.rsplit('/', 1)[1]), 'wb') as f:
            r = requests.get(download)
            f.write(r.content)

#second
html = requests.get(previousworkgrouppresentations)
hreflinks = BeautifulSoup(html.text)
for link in hreflinks.findAll("a"):
    if "/assets" in str(link.get("href")):
        download = "https://www.chiamass.gov" + str(link.get("href"))
        with open("chiafiles/"+str(download.rsplit('/', 1)[1]), 'wb') as f:
            r = requests.get(download)
            f.write(r.content)