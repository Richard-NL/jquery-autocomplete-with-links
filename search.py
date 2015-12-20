#!/usr/bin/env python

# enable debugging
import cgitb, os, urllib, json

cgitb.enable()

print("Content-Type: application/json \n\n")

ingredients = [
	'Apple',
	'Appricot',
	'Almond',
	'Asparagus',
	'Banana',
	'Black Berry',
	'Beer',
	'Bastard Sugar',
	'Beef',
	'Cider',
	'Cinamon',
	'Chili',
	'Curry',
    'Chicken',
	'Durian',
	'Date']

query_string = os.environ.get("QUERY_STRING", "")
query_string_parameters = urllib.parse.parse_qs(query_string)


try:
	search_string = query_string_parameters['q'][0]

except KeyError:
    search_string = ''


matches = list(filter(lambda x: x.lower().startswith(search_string), ingredients))
print(json.dumps(matches))
	

