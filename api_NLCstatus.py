import json
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

natural_language_classifier = NaturalLanguageClassifier(
  username='c3d9a7ab-e9bc-4b15-b02f-0de513be0047',
  password='7snmYSBWCeEp')

classifiers = natural_language_classifier.list()
print(json.dumps(classifiers, indent=2))