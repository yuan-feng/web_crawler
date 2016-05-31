from spider_question import spider_question
from spider_index import spider_index
import requests
from bs4 import BeautifulSoup
import random
import numpy
import redis

# maxpage=29981   # real
# maxpage=2       # test purpose  
def getIndexPage(maxpage=2):

	
	r = redis.StrictRedis(host='localhost', port=6379, db=0)

	maxpage=2    
	for page in xrange(1,maxpage+1):
		url="http://stackoverflow.com/questions/tagged/c%2b%2b?page="+str(page)+"&sort=newest&pagesize=15"
		[titles, links] = spider_index(url)


	link_filter='link_filter'
	for (t,l) in zip(titles,links):
		if r.sadd(link_filter,l) :	
			r.set(t,l)
			print 'Found a new question link!'
		else:
			print 'Filter out a duplicate link!'