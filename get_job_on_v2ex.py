# -*- coding: utf-8 -*-
import requests
from BeautifulSoup import BeautifulSoup
class JobInfo(object):
	"""docstring for JobInfo"""
	def __init__(self, arg):
		super(JobInfo, self).__init__()
		self.url = arg
	
	def scrapyInfoFromV2ex(self):
		url = self.url
		r = requests.get(url = url)
		# print "v2ex response " + r.content
		return r.content
		
	
	def getPostList(self, content):
		""" content 为 scrapyInfoFromV2ex 的返回值"""
		soup = BeautifulSoup(content)
		x = 5
		postList = []
		while x < 82:
			title = soup.find("div", {"id": "Main"}).contents[3].contents[x].contents[2].find("span").contents[0].string
			url = soup.find("div", {"id": "Main"}).contents[3].contents[x].contents[2].find("span").contents[0]['href']
			post = {"url":url, "title":title}
			if u"实习" in post["title"]:
				postList.append(post)
			x = x + 2
		for post in postList:
			print "found jobs ==>" + str(postList) + "\n"
		return postList

	def getPostContent(self, url):
		""" url 为 v2ex url"""
		r = requests.get(url = "http://v2ex.com" + url)
		soup = BeautifulSoup(r.content)
		res = (soup.find("div", {"class": "topic_content"}))
		res = str(res).replace('<br />', '\n')
		res = res.replace('<div class="topic_content">', "")
		res = res.replace('</div>', "")
		print res
		return res






