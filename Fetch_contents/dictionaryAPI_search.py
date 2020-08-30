import urllib
import urllib.request
import json

def json_definition(word, ref='collegiate', key='dce9abaf-3300-4320-a6ad-f2350a6d5918'):
	'''
	Grab a definition of a word in JSON format.
	Return the definition.
	'''
	uri = 'https://dictionaryapi.com/api/v3/references/'+ ref + '/json/' + word+ "?key="+key
	response = urllib.request.urlopen(uri)
	str_response = response.read().decode('utf-8')
	obj = json.loads(str_response)[0]	# dictionary is nested in a list
	
	print('=======\nSource: Merriam-Webster Dictionary - https://dictionaryapi.com/\n')
	
	#print(obj.keys())
	print(f'=======\nDefinition for "{word}":')
	return obj['shortdef'][0].capitalize()	# return the key storing the definition as string
	

if __name__ == '__main__':
	topic = input('>> topic input: ')
	print(json_definition(topic))
