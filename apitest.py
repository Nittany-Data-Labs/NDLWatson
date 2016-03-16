import json
import requests
from watson_developer_cloud import NaturalLanguageClassifierV1 as nlc

cred = open('credentials.json', 'r')
parsed = json.loads(cred.read())
cred.close()

url = parsed['credentials']['url']
usr = parsed['credentials']['username']
pwd = parsed['credentials']['password']

natural_language_classifier = nlc(
  username=usr,
  password=pwd)