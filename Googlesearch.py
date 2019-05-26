#1 usr/env/bin/python3

import requests
import sys 
import webbrowser
import bs4

print("Googling")  #displey the googling while downloading the contend
res = requests.get("http://google.com/search?q=" + ' '.join(sys.argv[1:])
res.raise_for_status()
soup =  bs4.BeaufifulSoup(res.text)

linkElems = soup.select(".r a")
