import requests
import sys 
import webbrowser
import os 
import bs4
#comicElem = soup.select("#comic img")

url = 'https://t.me/s/nerkh_news'
res = requests.get(url)
res.raise_for_status()
#read it by soup 
soup = bs4.BeautifulSoup(res.text)
# to list 
pElem = exampleSoup.select("p")
