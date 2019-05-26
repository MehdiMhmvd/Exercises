from bs4 import BeautifulSoup

openFile = open("html_doc.html")
soup = BeautifulSoup(openFile)
#print(soup.title)
#print(soup.title.name)
#print(soup.div.title)
#print(soup.div['class'])
#listof_a = soup.find_all("a")  ## using the .get for extraxting from tag 
'''
for link in listof_a:
	print(link)
	print("--" * 5)
	print(link.get("class"))
	print(link.get("href"))
	print(link.get("id"))
	print(link.text)
	'''

div_tag = soup.div
print(div_tag.text.strip())
#print(div_tag["class"])
#print(div_tag.attrs)
#print(soup.div.text)
#if soup.div['class'][0] +soup.div['class'][1] == "tgme_widget_message_textjs-message_text":
#	print("ok" )
