#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

# url="http://stackoverflow.com/questions/37188212/implementing-logout-in-a-restful-webservice"
# url="http://stackoverflow.com/questions/37210656/fragment-is-in-backstack"


def spider_question(url, verbose=1):
	
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'html.parser')

	# find the question, each page has only one question
	question_data1 = soup.find_all("td",{"class":"postcell"})
	# this is necessary, otherwise, some extra data and words will come.
	question_data = question_data1[0].contents[1].find_all("div", {"class":"post-text"})
	try:
		raw_question = question_data[0].get_text()
		if verbose:
			print raw_question
	except: 
		pass


	# find the answers. Each page may have no answer or multiple answers. 
	answer_data1 = soup.find_all("td",{"class":"answercell"})
	for item in answer_data1:
		try:
			raw_answers = item.contents[1].get_text()
			if verbose:
				print '------------'
				print raw_answers
		except: 
			pass

	return [raw_question, raw_answers]
