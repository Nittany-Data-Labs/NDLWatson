import json
import requests
import commands
from watson_developer_cloud import NaturalLanguageClassifierV1 as nlc

def get_cred(APIname):
	print 'getting credentials...'
	filename = 'journal_app/static/cred.json'
	print "importing from:", filename
	cred = open(filename, 'r')
	parsed = json.loads(cred.read())
	cred.close()

	# output = [url, usr, pwd]
	return {'url': parsed[APIname]['url'],
		'usr': parsed[APIname]['username'],
		'pwd': parsed[APIname]['password']}
