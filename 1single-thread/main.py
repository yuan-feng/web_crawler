from spider_question import spider_question
from spider_index import spider_index
import requests
from bs4 import BeautifulSoup
import random
import numpy
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


maxpage=29981   # real
maxpage=3     # test purpose
for page in xrange(1,maxpage):
	url="http://stackoverflow.com/questions/tagged/c%2b%2b?page="+str(page)+"&sort=newest&pagesize=15"
	[titles, links] = spider_index(url)


for key in r.scan_iter():
    r.delete(key)

for (t,l) in zip(titles,links):
	r.set(t,l)

for key in r.scan_iter():
    [question, answers] = spider_question(r.get(key))
    print "\n"
    print question
    print answers










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