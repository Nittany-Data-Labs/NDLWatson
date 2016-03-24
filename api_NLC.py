import json
from get_cred import get_cred
from watson_developer_cloud import NaturalLanguageClassifierV1

cred = get_cred('NLC')

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


# createClassifier('Journals/Sentences/test_file_5.csv')
classifier_id = listClassifier(0)
checkClassifierStatus(classifier_id)
