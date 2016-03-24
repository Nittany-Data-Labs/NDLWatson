import json
import pprint
import csv
from get_cred import get_cred
from watson_developer_cloud import NaturalLanguageClassifierV1
from watson_developer_cloud import AlchemyLanguageV1

cred = get_cred('NLC')

# Alchemy Language credentials
url = 'http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment'
print 'getting credentials...'
filename = 'credentials.json'
print "importing from:", filename
creds = open(filename, 'r')
parsed = json.loads(creds.read())
creds.close()
creds = {'url': parsed['AL']['url'],'apikey': parsed['AL']['apikey']}
alchemy_language = AlchemyLanguageV1(api_key=creds['apikey'])

# Natural Language Classifier information credentials
natural_language_classifier = NaturalLanguageClassifierV1(
  username=cred['usr'],
  password=cred['pwd'])

def createClassifier(filename):
    print 'creating classfier...'
    with open(filename, 'rb') as training_data:
        classifier = natural_language_classifier.create(
            training_data=training_data,
            name='NDL_Classfier',
            language='en'
        )
    print(json.dumps(classifier, indent=2))

def listClassifier(classifier_index):
    print 'listing classfiers...'
    classifiers = natural_language_classifier.list()
    output = json.dumps(classifiers, indent=2)
    print json.dumps(classifiers, indent=2)
    output = json.loads(output)
    print output['classifiers'][classifier_index]['classifier_id']
    return output['classifiers'][classifier_index]['classifier_id']

def checkClassifierStatus(classifier_id):
    print 'check classifier status...'
    status = natural_language_classifier.status(classifier_id)
    print (json.dumps(status, indent=2))

def classifySentence(sentence, classifier_id):
    classes = natural_language_classifier.classify(classifier_id, sentence)
    return [json.loads(json.dumps(classes, indent=2))['classes'][0]['class_name'], json.loads(json.dumps(classes, indent=2))['classes'][0]['confidence']]

def classifyJournal(filename, classifier_id):
    journal = open(filename, 'r')
    with open(str(filename)+'_classed.csv', 'w') as csvfile:
        fieldnames = ['Sentence', 'Class', 'Confidence', 'Sentiment', 'Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
        classed = []
        for i in journal:
            c += 1
            try:
                classed = classifySentence(str(i), classifier_id)
                output = json.dumps(alchemy_language.sentiment(text=i))

                writer.writerow({'Sentence': i, 'Class': classed[0], 'Confidence': classed[1], 'Sentiment': json.loads(output)['docSentiment']['type'], 'Score': json.loads(output)['docSentiment']['score']})

                print str(i) + ':', classed[0]
            except:
                print 'error'
    journal.close()
# createClassifier('Journals/Sentences/test_file_5.csv')
classifier_id = listClassifier(0)
# checkClassifierStatus(classifier_id)
# pprint.pprint(classifySentence('Kind of feel little uncomfortable here.', classifier_id))

classifyJournal('Journals/goodnight365', classifier_id)
