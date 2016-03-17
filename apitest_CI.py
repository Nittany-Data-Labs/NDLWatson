import json
import requests

cred = open('credentials_CI.json', 'r')
parsed = json.loads(cred.read())
cred.close()

url = parsed['credentials']['url']
usr = parsed['credentials']['username']
pwd = parsed['credentials']['password']

url_alt = ["https://gateway.watsonplatform.net/concept-insights/api/v2/accounts", 
	"https://gateway.watsonplatform.net/concept-insights/api/v2/graphs"]


# get account
r_a = requests.get(url_alt[0], auth=(usr, pwd))
data_a = json.loads(r_a.text)
account = data_a['accounts'][0]['account_id']
print account

# get graphs
r_g = requests.get(url_alt[1], auth=(usr, pwd))
data_g = json.loads(r_g.text)['graphs']
graph = []
for i in data_g:
	graph.append(i)
print graph

