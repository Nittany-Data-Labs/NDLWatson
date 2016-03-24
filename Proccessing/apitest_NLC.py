# Testing Natural Langauge Processor API
# Version: 1.0
# Author:  Myron Leung

import json
import requests
from get_cred import get_cred
from watson_developer_cloud import NaturalLanguageClassifierV1 as nlc

cred = get_cred('NLC')

natural_language_classifier = nlc(
  username=cred['usr'],
  password=cred['pwd'])

