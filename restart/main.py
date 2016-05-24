from spider_question import spider_question
from spider_index import spider_index
import requests
from bs4 import BeautifulSoup


url="http://stackoverflow.com"
[titles, links] = spider_index(url)







url="http://stackoverflow.com/questions/37210656/fragment-is-in-backstack"
[question, answers] = spider_question(url)