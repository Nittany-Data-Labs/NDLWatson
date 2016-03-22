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
print cred
account = 0
graph = []

def getAccountInfo():
	global account
	r_a = requests.get(url_alt['acc'], auth=(cred['usr'], cred['pwd']))
	data_a = json.loads(r_a.text)
	account = data_a['accounts'][0]['account_id']
	print account

# get graphs
def getAvailableGraphs():
	global graph
	r_g = requests.get(url_alt['gph'], auth=(cred['usr'], cred['pwd']))
	data_g = json.loads(r_g.text)['graphs']
	for i in data_g:
		graph.append(i)
	pprint.pprint(graph)

# get available copora for account
def getAvailableCorpora():
	url_account = url_alt['crp']+'/'+str(account)
	r_c = requests.get(url_account, auth=(cred['usr'], cred['pwd']))
	data_c = json.loads(r_c.text)['corpora']
	pprint.pprint(data_c)

#insert new document into corpus
def createNewCorpus(corpus_object, corp_name):
	print 'Creating new corpus: ' + str(corp_name)
	corp_ob = open(corpus_object, 'r')
	url = str(url_alt['crp']) + '/' + str(account) +'/'+ str(corp_name)
	print 'corpus url:', url
	r = requests.put(url, data = corp_ob, auth=(cred['usr'], cred['pwd']))
	print r.status_code
	corp_ob.close()
	pprint.pprint(r.text)
	# pprint.pprint(json.loads(r.text))

def delCorpus(corp_name):
	print "Deleting Corpus " + str(corp_name)
	url = url_alt['crp'] + '/' + str(account) + '/' + str(corp_name)
	print url
	r = requests.delete(url, auth=(cred['usr'], cred['pwd']), data = str(corp_name))
	print r.status_code
	pprint.pprint(r.text)

def inputDocumentToCorpus(document_object, filename, corp_name):
	# get document obejct requirements and load into temporary variables
	doc_ob = open(document_object, 'r')
	data = open(filename, 'r')
	parsed_doc_ob = json.loads(doc_ob.read())
	doc_ob.close()

	# insert data into document object
	parsed_doc_ob['parts'][0]['data'] = data.read()
	data.close()
	
	# dump processed document object to json
	output_doc_ob = json.dumps(parsed_doc_ob)

	# send outpt docuemnt object to watson
	url = url_alt['crp'] +'/'+ str(account) +'/'+  str(corp_name)  +'/documents/'+ str(parsed_doc_ob['id'])
	print url
	r = requests.put(url, data = output_doc_ob, auth=(cred['usr'], cred['pwd']))
	print r.status_code
	pprint.pprint(r.text)

def getConcepts(raw_doc):
	global graph
	print "Getting concepts for", str(raw_doc) + "..."
	print 'using', graph[1]
	doc = open(raw_doc,'r')
	parsed = doc.read()
	doc.close()
	url = url_alt['gph'] + "/wikipedia/en-latest/annotate_text"
	headers = {'content-type': 'text/plain'}
	print url
	r = requests.post(url, data = str(parsed), auth=(cred['usr'], cred['pwd']), headers = headers)
	print r.status_code
	print r.text


print 'account:'
getAccountInfo()
print 'graphs:'
getAvailableGraphs()

# test: create new corpus
# createNewCorpus('corpus_object.json', 'test4')
# inputDocumentToCorpus('document_object.json', 'Journals/goodnight0', 'test1')

print 'corpora:'
getAvailableCorpora()

# test: get document from corporat
# corp_url = url_alt['crp'] + '/' + account + '/' + 'test1'+ '/documents/'
# r = requests.get(corp_url, auth=(cred['usr'], cred['pwd']))
# print "data from test1"
# pprint.pprint(r.text)

getConcepts('Journals/goodnight0')



