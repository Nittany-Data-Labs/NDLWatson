import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='c3d9a7ab-e9bc-4b15-b02f-0de513be0047',
  password='7snmYSBWCeEp')

with open('/Users/sahilmishra/Desktop/NDLWatson/Journals/Sentences/test_file.csv', 'rb') as training_data:
  classifier = natural_language_classifier.create(
    training_data=training_data,
    name='MyNDLClassfier',
    language='en'
  )
print(json.dumps(classifier, indent=2))