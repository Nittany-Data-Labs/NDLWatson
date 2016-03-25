import os
import unicodedata

#f = open('journals.txt', 'w')

entry_file = open('./Sentences2/' + str(os.getcwd().rpartition('/')[2]), 'w')

#print os.getcwd().rpartition('/')[2]

for directory in os.listdir(os.getcwd()):
	if directory.endswith('.py') or directory.startswith('.'):
		continue
	for i, journal_entry in enumerate(os.listdir(directory)):
		if journal_entry.endswith('.py') or journal_entry.endswith('s'):
			continue
		with open(os.getcwd() + '/' + str(directory) + '/' + str(journal_entry)) as f:
			entry_file = open('./Sentences2/' + str(directory).rpartition('/')[2], 'w')
			for line in f:
#				entry_file.write(unicodedata.normalize('NFKD',(journal_entry + ',' + line).decode('utf):).encode('utf8', 'ignore'))
				entry_file.write(str(journal_entry) + ',' + str(line))
		


'''
	entry_file = open('./sentences.txt', 'w')
	entry_file.write(
			entry_file.write(unicodedata.normalize('NFKD', sentence).encode('utf8', 'ignore'))
			entry_file.write('\n')
	entry_file.close()
'''

