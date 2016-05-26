#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
url="http://stackoverflow.com"


# url="http://stackoverflow.com/questions/37188212/implementing-logout-in-a-restful-webservice"
# url="http://stackoverflow.com/questions/37210656/fragment-is-in-backstack"

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



# --------------------------------------------------


# print the questions
question_data1 = soup.find_all("td",{"class":"postcell"})
question_data = question_data1[0].contents[1].find_all("div", {"class":"post-text"})
try:
	real_question = question_data[0].get_text()
	print real_question
except: 
	pass



# print the answers
answer_data1 = soup.find_all("td",{"class":"answercell"})
for item in answer_data1:
	try:
		real_answer = item.contents[1].get_text()
		print '------------'
		print real_answer
	except: 
		pass








# backup


# a = soup.find_all("meta",{"name":"twitter:description"})


# question_data = soup.find_all("div",{"class":"post-text"})
# question_data = soup.find_all("div",{"class":"answercell"})




# links = soup.find_all("div",{"class":"status unanswered"})
# links = soup.find_all("div",{"class":"status answered-accepted"})
# links = soup.find_all("div",{"class":"status answered-accepted"})


# To do list:
#  class="vote-count-post "

# <div class="vote">
#         <input name="_id_" value="37188212" type="hidden">
#         <a class="vote-up-off" title="This question shows research effort; it is useful and clear">up vote</a>
#         <span itemprop="upvoteCount" class="vote-count-post ">7</span>
#         <a class="vote-down-off" title="This question does not show any research effort; it is unclear or not useful">down vote</a>

#         <a class="star-off" href="#">favorite</a>
#         <div class="favoritecount"><b></b></div>
# </div>



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