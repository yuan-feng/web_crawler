#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

def spider_question(url, verbose=1):
	# url="http://stackoverflow.com/questions/37210656/fragment-is-in-backstack"
	# url="http://stackoverflow.com/questions/37448339/cuda-cpu-to-gpu-c-please-advise"
	# verbose=1
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'html.parser')
	
	# find the question, each page has only one question
	question_data1 = soup.find_all("td",{"class":"postcell"})

	# find the answers. Each page may have no answer or multiple answers. 
	answer_data1 = soup.find_all("td",{"class":"answercell"})
	raw_answers=[]

	# this is necessary, sometimes, the author delete their posts quickly.
	try:
		# get question
		question_data = question_data1[0].contents[1].find_all("div", {"class":"post-text"})
		raw_question = question_data[0].get_text()
		if verbose:
			print raw_question

		# get answers
		for item in answer_data1:
			raw_answers.append(item.contents[1].get_text())
			if verbose:
				print 'New answer:'
				print raw_answers

	except IndexError:
		print "\nThis question link below has been deleted!"
		print url
		raw_question="Qustion deleted!"

	if not raw_answers:
		print "No answers for this question!"

	return [raw_question, raw_answers]










# try:
# 	pass
# except Exception, e:
# 	raise
# else:
# 	pass
# finally:
# 	pass
	
	# for item in answer_data1:
	# 	try:
	# 		raw_answers = item.contents[1].get_text()
	# 	except: 
	# 		raw_answers= "NO ANSWERs YET!"
	# 	if verbose:
	# 		print '------------'
	# 		print raw_answers