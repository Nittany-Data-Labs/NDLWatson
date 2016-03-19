import urllib2
from bs4 import BeautifulSoup

def URLToText(url):
	response = urllib2.urlopen(url)
	soup = BeautifulSoup(response, 'html.parser')
	result = soup.find('div', {'class' :'entry-content'}).text
	return result
