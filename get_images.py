import re
import requests
from bs4 import BeautifulSoup
from os.path import basename
from urllib.request import urlopen

# Replace site, base_url with wherever images will be downloaded from
site = 'https://www.zeldadungeon.net/breath-of-the-wild-walkthrough/korok-seed-locations/ridgeland-korok-seed-locations/'
base_url = 'https://www.zeldadungeon.net'
response = requests.get(site)
html = response.text

bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
urls = []
for image in images:
    # Filter out maps
    if "map" not in image['src'] and "site" not in image['src']:
        urls.append(image['src'])
for url in urls:
    lnk = base_url + url
    with open(basename(lnk), "wb") as f:
        f.write(requests.get(lnk).content)

