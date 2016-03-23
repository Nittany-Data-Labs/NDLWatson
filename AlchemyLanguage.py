import json
import requests
import pprint
from get_cred import get_cred
from watson_developer_cloud import AlchemyLanguageV1

url = 'http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment'

# Getting credentials
print 'getting credentials...'
filename = 'credentials.json'
print "importing from:", filename
cred = open(filename, 'r')
parsed = json.loads(cred.read())
cred.close()
cred = {'url': parsed['AL']['url'],'apikey': parsed['AL']['apikey']}

payload = 'Yesterday my autistic grandson left his favorite jacket on the bus, and he had a meltdown.'

print "running request..."
alchemy_language = AlchemyLanguageV1(api_key=cred['apikey'])
output = json.dumps(alchemy_language.sentiment(text=payload))
pprint.pprint(json.loads(output))
