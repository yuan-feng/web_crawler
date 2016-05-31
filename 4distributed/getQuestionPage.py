from spider_question import spider_question
from spider_index import spider_index
import requests
from bs4 import BeautifulSoup
import random
import numpy
import redis

# maxpage=29981   # real
# maxpage=2       # test purpose  
def getQuestionPage():
	flag=1

	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	Npage=0
	link=r.lpop('wait_link_list')
	# get question
	if not link:
		print "All waiting link lists are done!"
		flag=0
	else:
		[question, answers] = spider_question(link)
		
		r.hset(link,'2',question)
		r.hset(link,'3',answers)

		# print "\n"
		# print question
		# print answers
		print 'Get a new question page!'

	return flag
