from spider_question import spider_question
from spider_index import spider_index
import requests
from bs4 import BeautifulSoup
import random
import numpy
import redis
import threading
import time
from getIndexPage import *
from getQuestionPage import *

r = redis.StrictRedis(host='localhost', port=6379, db=0)

Num_indexPage = 2

for i in range(1, Num_indexPage+1):
	r.rpush('wait_index_list',i)


def job_IndexPage(Nprocess):
	while getIndexPage():
		pass
	return 'Get Index Page Process ' + str(Nprocess) + ' is done !'

def job_QuestionPage(Nprocess):
	while getQuestionPage():
		pass
	return 'Get Question Page Process ' + str(Nprocess) + ' is done !'

# def job_QuestionPage():
# 	while getQuestionPage():
# 		pass




Nproc = 2
if __name__ == '__main__':


	Nproc_index_page = 2
	Nproc_question_page = 6

	threads_index=[]
	for i in range(Nproc_index_page):
		t=threading.Thread(target = job_IndexPage, args=(i,))
		threads_index.append(t)
		t.start()

	# This is necessary:
	# If network is slow, you may need to increase the sleep time.
	# Will find another better way.
	initial_question_page_wait_time = 8
	time.sleep(initial_question_page_wait_time)

	threads_question=[]
	for i in range(Nproc_question_page):
		t=threading.Thread(target = job_QuestionPage, args=(i,))
		threads_question.append(t)
		t.start()


	for item in threads_index:
		item.join()

	for item in threads_question:
		item.join()

	print "You are ALL set!"



















# maxpage=29981   # real
# maxpage=2     # test purpose
# for page in xrange(1,maxpage):
# 	url="http://stackoverflow.com/questions/tagged/c%2b%2b?page="+str(page)+"&sort=newest&pagesize=15"
# 	[titles, links] = spider_index(url)


# link_filter='myset'
# for (t,l) in zip(titles,links):
# 	if r.sadd(link_filter,l) :	
# 		r.set(t,l)
# 		print 'Found a new question link!'
# 	else:
# 		print 'Filter out a duplicate link!'



# for link in r.smembers(link_filter):
#     [question, answers] = spider_question(link)
#     print "\n"
#     print question
#     print answers





# for key in r.scan_iter():
# 	print key






# quick backup:
# url="http://stackoverflow.com/questions/37210656/fragment-is-in-backstack"
# for key in r.scan_iter():
#     print "\n key, r.get(key): "
#     print key
	# print r.get(key)

	# mainurl="http://stackoverflow.com"
	# Npage=numpy.arange(29981)
	
	# url="http://stackoverflow.com/questions/"+ str(a)
	# [question, answers] = spider_question(url)