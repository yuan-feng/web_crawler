from spider_question import spider_question
from spider_index import spider_index
import requests
from bs4 import BeautifulSoup
import random
import numpy
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

for key in r.scan_iter():
    r.delete(key)
# Test case
test_url="http://stackoverflow.com/questions/tagged/c%2b%2b?page=2&sort=newest&pagesize=15"
[titles, links] = spider_index(test_url)
[titles2, links2] = spider_index(test_url)

link_filter='myset'
for (t,l) in zip(titles,links):
	if r.sadd(link_filter,l) :	
		r.set(t,l)
		print 'Found a new question link!'
	else:
		print 'Filter out a duplicate link!'

for (t,l) in zip(titles2,links2):
	if r.sadd(link_filter,l) :	
		r.set(t,l)
		print 'Found a new question link!'
	else:
		print 'Filter out duplicate links!'