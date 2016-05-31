from spider_question import spider_question
from spider_index import spider_index
import requests
from bs4 import BeautifulSoup
import random
import numpy
import redis

# maxpage=29981   # real
# maxpage=2       # test purpose  
def getQuestionPage(maxpage=10):

	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	Npage=0
	for link in r.smembers('link_filter'):
		# Test limitation settings
		Npage=Npage+1
		if Npage>maxpage:
			break
		# get question
		[question, answers] = spider_question(link)
		print "\n"
		print question
		print answers
		print 'Get a new question page!'