#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
url="http://stackoverflow.com"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

main_data = soup.find_all("div",{"class":"summary"})
votes_data = soup.find_all("div",{"class":"votes"})
view_data = soup.find_all("div",{"class":"views"})

# all the titles and link
for item in main_data:
	try:
		print item.contents[1].text
		print url+item.contents[1].find_all("a",{"class":"question-hyperlink"})[0].get("href") 
		print "\n"
	except: 
		pass











# backup
# links = soup.find_all("div",{"class":"status unanswered"})
# links = soup.find_all("div",{"class":"status answered-accepted"})
# links = soup.find_all("div",{"class":"status answered-accepted"})


# backup
# links = soup.find_all("a")
# question_link=[]
# question_title=[]
# for link in links:
# 	try:
# 		if "http:" in link.get("href"):
# 			if "questions" in link.get("href"):
# 				# print "<a href='%s'>%s</a>" %(link.get("href"),link.text)
# 				question_link.append( link.get("href") )
# 				question_title.append( link.text )
# 	except Exception, e:
# 		pass