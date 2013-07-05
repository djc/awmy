import simplejson as json
import os, sys

LITERALS = {'only', 'max'}

def minimize(full, year):
	
	new = {}, {}
	for rule, data in full['rules'].iteritems():
		for part in data:
			
			if part[1] not in LITERALS and int(part[1]) < year:
				continue
			if part[1] == 'only' and int(part[0]) < year:
				continue
			
			new[1].setdefault(rule, []).append(part)
	
	for zone, data in full['zones'].iteritems():
		for part in data:
			
			if part['u'] and int(part['u'][0]) < year:
				continue
			
			new[0].setdefault(zone, []).append(part)
			if part['r'] is not None and part['r'] not in new[1]:
				part['r'] = None
	
	return {'zones': new[0], 'rules': new[1]}

if __name__ == '__main__':
	
	with open(sys.argv[1]) as f:
		full = json.load(f)
	
	pruned = minimize(full, 2013)
	print json.dumps(pruned)
