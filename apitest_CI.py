# Testing Concept Insights API
# Version: 1.0
# Author:  Myron Leung

import json
from get_cred import get_cred
import requests
import pprint

# base urls for accounts (acc), graphs (gph), corpora (crp)
url_alt = {'acc':"https://gateway.watsonplatform.net/concept-insights/api/v2/accounts", 
	'gph': "https://gateway.watsonplatform.net/concept-insights/api/v2/graphs", 
	'crp': "https://gateway.watsonplatform.net/concept-insights/api/v2/corpora"}

cred = get_cred('CI')
account = 0
# get account
def getAccountInfo():
	global account
	r_a = requests.get(url_alt['acc'], auth=(cred['usr'], cred['pwd']))
	data_a = json.loads(r_a.text)
	account = data_a['accounts'][0]['account_id']
	print account


# get graphs
def getAvailableGraphs():
	r_g = requests.get(url_alt['gph'], auth=(cred['usr'], cred['pwd']))
	data_g = json.loads(r_g.text)['graphs']
	graph = []
	for i in data_g:
		graph.append(i)
	print graph

# get available copora for account
def getAvailableCorpora():
	url_account = url_alt['crp']+'/'+str(account)
	r_c = requests.get(url_account, auth=(cred['usr'], cred['pwd']))
	data_c = json.loads(r_c.text)['corpora']
	print data_c

#insert new document into corpus
def createNewCorpus(data, name):
	url = str(url_alt['crp']) + '/' + str(account) +'/'+ str(name)
	r = requests.put(url, data = data, auth=(cred['usr'], cred['pwd']))
	print r.status_code
	pprint.pprint(json.loads(r.text))

print 'account: ', getAccountInfo()
print 'graphs: ', getAvailableGraphs()
print 'creating new corpus...'
raw_file = open('corpora_setup.json', 'r')
data = json.loads(raw_file.read())
raw_file.close()

pprint.pprint(data)

createNewCorpus(data, 'test_corpus_name')
print 'exiting...'


