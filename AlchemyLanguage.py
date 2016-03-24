import json
import requests
import pprint
import csv
from get_cred import get_cred
from watson_developer_cloud import AlchemyLanguageV1

url = 'http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment'

length = 0
def getPayload(filename):
    global length
    output = []
    with open(str(filename)) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            output.append(row['Sentence'])
            length += 1
    return output



# Getting credentials
print 'getting credentials...'
filename = 'credentials.json'
print "importing from:", filename
cred = open(filename, 'r')
parsed = json.loads(cred.read())
cred.close()
cred = {'url': parsed['AL']['url'],'apikey': parsed['AL']['apikey']}

payload = getPayload('Journals/Sentences/test_file.csv')

print "running request..."

c = 0
# for i in payload:
#     c += 1
#     print str(c) + ": "
#     try:
#         alchemy_language = AlchemyLanguageV1(api_key=cred['apikey'])
#         output = json.dumps(alchemy_language.sentiment(text=i))
#         pprint.pprint(json.loads(output))
#     except:
#         print "coding error"

with open(str('Journals/Sentences/test_file_sentiment.csv'), 'w') as csvfile:
    fieldnames = ['Sentence', 'Score', 'Type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in range(1, length):
        try:
            print c+1
            alchemy_language = AlchemyLanguageV1(api_key=cred['apikey'])
            output = json.dumps(alchemy_language.sentiment(text=payload[c]))
            writer.writerow({'Sentence': payload[c], 'Score': json.loads(output)['docSentiment']['score'], 'Type': json.loads(output)['docSentiment']['type']})
        except:
            print "coding error"
        c += 1
