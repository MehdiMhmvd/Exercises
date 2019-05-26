import webbrowser
import requests
import bs4
import loggings

logging.basicConfig( level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')



exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile)
#elements = exampleSoup.select("#author")
pElem = exampleSoup.select("#class")

logging.debug("length : %d" %len(pElem))
for i in range(len(pElem)) :

	print(pElem[i].getText())

#webbrowser.open('http://inventwithpython.com/')
'''
res = requests.get("https://t.me/s/nerkh_news")
#res = requests.get("http://inventwithpython.com/page_that_does_not_exist")
try:
	res.raise_for_status()
except Exception as err:
	print('There was a problem: %s' % (err))

with open("dollar.txt","wb") as f:
	for ch in res.iter_content(10000):
		f.write(ch)


print(len(res.text))
if res.status_code == requests.codes.ok :
	print("Ok")
	'''

