# Testing Concept Insights API
# Version: 1.0
# Author:  Myron Leung

import json
from get_cred import get_cred
import requests
import pprint

class ConceptInsights:

	def __init__(self):
		# base urls for accounts (acc), graphs (gph), corpora (crp)
		self.url_alt = {'acc':"https://gateway.watsonplatform.net/concept-insights/api/v2/accounts", 
			'gph': "https://gateway.watsonplatform.net/concept-insights/api/v2/graphs", 
			'crp': "https://gateway.watsonplatform.net/concept-insights/api/v2/corpora"}

		self.cred = get_cred('CI')
		print self.cred
		self.account = 0
		self.graph = []

	def getAccountInfo(self):
		url_alt = self.url_alt
		cred = self.cred
		r_a = requests.get(url_alt['acc'], auth=(cred['usr'], cred['pwd']))
		data_a = json.loads(r_a.text)
		self.account = data_a['accounts'][0]['account_id']
		print self.account

	# get graphs
	def getAvailableGraphs(self):
		graph = self.graph
		cred = self.cred
		url_alt = self.url_alt
		r_g = requests.get(url_alt['gph'], auth=(cred['usr'], cred['pwd']))
		data_g = json.loads(r_g.text)['graphs']
		for i in data_g:
			graph.append(i)
		pprint.pprint(graph)

	# get available copora for account
	def getAvailableCorpora(self):
		cred = self.cred
		account = self.account
		url_alt = self.url_alt
		url_account = url_alt['crp']+'/'+str(account)
		r_c = requests.get(url_account, auth=(cred['usr'], cred['pwd']))
		data_c = json.loads(r_c.text)['corpora']
		pprint.pprint(data_c)

	#insert new document into corpus
	def createNewCorpus(self, corpus_object, corp_name):
		cred = self.cred
		account = self.account
		url_alt = self.url_alt
		print 'Creating new corpus: ' + str(corp_name)
		print 'using account:', account
		corp_ob = open(corpus_object, 'r')
		url = str(url_alt['crp']) + '/' + str(account) +'/'+ str(corp_name)
		print 'corpus url:', url
		r = requests.put(url, data = corp_ob, auth=(cred['usr'], cred['pwd']))
		print r.status_code
		corp_ob.close()
		pprint.pprint(r.text)
		# pprint.pprint(json.loads(r.text))

	def delCorpus(self, corp_name):
		cred = self.cred
		account = self.account
		url_alt = self.url_alt
		print "Deleting Corpus " + str(corp_name)
		url = url_alt['crp'] + '/' + str(account) + '/' + str(corp_name)
		print url
		r = requests.delete(url, auth=(cred['usr'], cred['pwd']), data = str(corp_name))
		print r.status_code
		pprint.pprint(r.text)

	def inputDocumentToCorpus(self, document_object, filename, corp_name):
		print "inputing document:", filename
		cred = self.cred
		account = self.account
		url_alt = self.url_alt
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

	def getConcepts(self, raw_doc):
		cred = self.cred
		graph = self.graph
		account = self.account
		url_alt = self.url_alt
		print "Getting concepts for", str(raw_doc) + "..."
		print 'using', graph[1]
		doc = open(raw_doc,'r')
		parsed = doc.read()
		doc.close()
		# set request settings
		url = url_alt['gph'] + "/wikipedia/en-latest/annotate_text"
		print url
		headers = {'content-type': 'text/plain'}
		r = requests.post(url, data = str(parsed), auth=(cred['usr'], cred['pwd']), headers = headers)
		print r.status_code
		# print r.text
		data_a = json.loads(r.text)['annotations']
		# pprint.pprint(data_a)
		for i in data_a:
			print str(i['concept']['label']) +': '+ str(i['score'])

		return data_a

	# incomplete
	def getRelatedConcepts(self, raw_doc):
		cred = self.cred
		graph = self.graph
		account = self.account
		url_alt = self.url_alt
		concepts = getConcepts(raw_doc)
		url = url_alt['gph'] + "/wikipedia/en-latest/related_concepts"
		headers = {'content-type': 'text/plain'}
		r = requests.get(url, data = concepts, auth=(cred['usr'], cred['pwd']), headers = headers)
		print r.status_code

	def getAllDocument(self, corp_name, index):
		cred = self.cred
		account = self.account
		url_alt = self.url_alt
		print 'getting', str(corp_name), "documents..."
		url = url_alt['crp'] + '/' + account + '/' + str(corp_name) + '/documents'
		r = requests.get(url, auth=(cred['usr'], cred['pwd']))
		document = json.loads(r.text)['documents']
		print r.status_code
		print document
		return document

	def getDocument(self, corp_name, doc_name):
		cred = self.cred
		account = self.account
		url_alt = self.url_alt
		print 'getting', str(doc_name) + "..."
		url = url_alt['crp'] + '/' + str(account) + '/' + str(corp_name) + '/documents/' + str(doc_name)
		r = requests.get(url, auth=(cred['usr'], cred['pwd']))
		document = json.loads(r.text)
		print r.status_code
		print document
		return document

	def getDocAnnotations(self, corp_name):
		cred = self.cred
		url_alt = self.url_alt
		account = self.account
		getDocument(corp_name, 0)
		url = url_alt['crp'] + '/' + account + '/' + str(corp_name)  + '/documents/' +  + '/annotations'



if __name__ == "__main__":
	ci = ConceptInsights()
	print 'account:'
	ci.getAccountInfo()
	print 'graphs:'
	ci.getAvailableGraphs()

	# ci.createNewCorpus('corpus_object.json', 'test1')
	# ci.inputDocumentToCorpus('document_object.json', 'Journals/goodnight0', 'doc1')

	print 'corpora:'
	ci.getAvailableCorpora()

	# getConcepts('Journals/goodnight0')
	ci.getDocument('test1', 'test1')
	# getDocAnnotations('test1')



