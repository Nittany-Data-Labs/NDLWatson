import urllib2
from bs4 import BeautifulSoup

def URLToText(url):
	try:
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
	except Exception:
		return -1
	soup = BeautifulSoup(response, 'html.parser')
	result = soup.find('div', {'class' :'entry-content'}).text
	return result
