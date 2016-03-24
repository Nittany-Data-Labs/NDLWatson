import json
from get_cred import get_cred
from watson_developer_cloud import NaturalLanguageClassifierV1

cred = get_cred('NLC')

natural_language_classifier = NaturalLanguageClassifierV1(
  username=cred['usr'],
  password=cred['pwd'])

def createClassifier():
    with open('Journals/Sentences/test_file_5.csv', 'rb') as training_data:
        classifier = natural_language_classifier.create(
            training_data=training_data,
            name='NDL_Classfier',
            language='en'
        )
    print(json.dumps(classifier, indent=2))
def listClassifier():
    classifiers = natural_language_classifier.list()
    print(json.dumps(classifiers, indent=2))

createClassifier()
listClassifier()
