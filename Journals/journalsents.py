import os
import unicodedata

#f = open('journals.txt', 'w')

entry_file = open('../Sentences/zombieprincess.txt', 'w')

for i, journal_entry in enumerate(os.listdir(os.getcwd())):
	if journal_entry.endswith('.py') or journal_entry.endswith('s'):
		continue
	with open(journal_entry) as f:
		for line in f:
			entry_file.write(str(journal_entry) + ',' + str(line))
	'''
	entry_file = open('./sentences.txt', 'w')
	entry_file.write(
			entry_file.write(unicodedata.normalize('NFKD', sentence).encode('utf8', 'ignore'))
			entry_file.write('\n')
	entry_file.close()
	'''


