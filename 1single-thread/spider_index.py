#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
# url="http://stackoverflow.com"

def spider_index(url, verbose =1):
	r = requests.get(url)
	mainurl="http://stackoverflow.com"

	soup = BeautifulSoup(r.content, 'html.parser')

	main_data = soup.find_all("div",{"class":"summary"})

	# The votes_data and view_data will be added and optimized later.
	votes_data = soup.find_all("div",{"class":"votes"})
	view_data = soup.find_all("div",{"class":"views"})

	# find all the titles and link
	question_titles=[]
	question_links=[]
	for item in main_data:
		try:
			question_titles.append(item.contents[1].text)
			question_links.append(mainurl+item.contents[1].find_all("a",{"class":"question-hyperlink"})[0].get("href") )
			if verbose:
				print question_titles
				print question_links
		except: 
			pass

	return [question_titles,question_links]



