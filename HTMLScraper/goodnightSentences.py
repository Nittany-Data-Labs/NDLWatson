import urlcall
import unicodedata
from parse import *

#f = open('journals.txt', 'w')

with open('nightlyurls.txt') as f:
    for i, line in enumerate(f):
		entry_file = open('./Journals/goodnight' + str(i), 'w')
		current_entry = soup.URLToText(line)
		sents = nltk.sent_tokenize(current_entry) 
		for sentence in sents:
				entry_file.write(unicodedata.normalize('NFKD', sentence).encode('utf8', 'ignore'))
				entry_file.write('\n')
		entry_file.close()

'''
journal_entry = soup.URLToText("https://www.goodnightjournal.com/2016/03/so-i-quit-my-job-today/")
sents = nltk.sent_tokenize(journal_entry) 
for sentence in sents:
		f.write(unicodedata.normalize('NFKD', sentence).encode('utf8', 'ignore'))
		f.write('\n')
f.close()
'''
