from spider_question import spider_question
from spider_index import spider_index
import requests
from bs4 import BeautifulSoup
import random
import numpy
import redis

# r = redis.StrictRedis(host='localhost', port=6379, db=0)



def getIndexPage():
	flag=1
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	
	page_number= r.lpop('wait_index_list')

	if not page_number:
		print "All index page are done!"
		flag=0
	else:

		url="http://stackoverflow.com/questions/tagged/c%2b%2b?page="+str(page_number)+"&sort=newest&pagesize=15"
		[titles, links] = spider_index(url)

		for (t,l) in zip(titles,links):
			if r.sadd('link_filter',l) :	
				r.rpush('wait_link_list',l)
				r.hset(l,'1',t)
				print 'Found a new question link!'
			else:
				print 'Filter out a duplicate link!'

	return flag

# a=r.lpop('wait_link_list')

# r.llen('wait_link_list')

# for i in range(100000):
# 	r.rpush('wait_link_list',i)

# for i in range(100000):
# 	r.lpop('wait_link_list')