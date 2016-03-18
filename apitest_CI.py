# Testing Concept Insights API
# Version: 1.0
# Author:  Myron Leung

import json
from get_cred import get_cred
import requests

# base urls for accounts (acc), graphs (gph), corpora (crp)
url_alt = {'acc':"https://gateway.watsonplatform.net/concept-insights/api/v2/accounts", 
	'gph': "https://gateway.watsonplatform.net/concept-insights/api/v2/graphs", 
	'crp': "https://gateway.watsonplatform.net/concept-insights/api/v2/corpora"}

cred = get_cred('CI')

# get account
r_a = requests.get(url_alt['acc'], auth=(cred['usr'], cred['pwd']))
data_a = json.loads(r_a.text)
account = data_a['accounts'][0]['account_id']
print account

# get graphs
r_g = requests.get(url_alt['gph'], auth=(cred['usr'], cred['pwd']))
data_g = json.loads(r_g.text)['graphs']
graph = []
for i in data_g:
	graph.append(i)
print graph

# get copora
r_c = requests.get(url_alt['crp'], auth=(cred['usr'], cred['pwd']))
data_c = json.loads(r_c.text)['corpora']
corpora = []
for i in data_c:
	corpora.append(i)
# print corpora
