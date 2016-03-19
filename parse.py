from __future__ import division  # Only if using Python 2, changes / operator to true division, not floor division  
#nltk: Natural language toolkit.  See http://www.nltk.org/
import nltk, re, pprint
from nltk import word_tokenize
import urllib2

#url = "https://www.goodnightjournal.com/2016/03/irrational-phobias/"
#response = urllib2.urlopen(url)

#raw = response.read().decode('utf8')

#Put filename in here
fh = open('./2554.txt')

raw = fh.read().decode('utf8')

sents = nltk.sent_tokenize(raw)

#print sents[10]

#sents[0] = ''.join([x if ord(x) < 128 else ' ' for x in sents[0]])

#print sents[10]

#print sents[10:20]

modified_sents = []

for i in range(0,len(sents)):
	current_sentence = sents[i]
	current_sentence = current_sentence.replace('\n', ' ')
	current_sentence = current_sentence.replace('\r', ' ')
	current_sentence = re.sub(' +',' ', current_sentence)
	modified_sents.append(current_sentence)
	


print modified_sents[10:20]
#pprint.pprint(sents[10:20])



