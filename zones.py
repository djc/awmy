#!/usr/bin/env python
import sys, os, re, tarfile, json

FILES = {
	'africa', 'antarctica', 'asia', 'australasia',
	'europe', 'northamerica', 'southamerica',
}

WS_SPLIT = re.compile("[ \t]+")

def lines(fn):
	
	with tarfile.open(fn, 'r:*') as tar:
		for info in tar:
			
			if not info.isfile() or info.name not in FILES:
				continue
			
			f = tar.extractfile(info)
			for ln in f:
				ln = ln.decode('iso-8859-1')
				ln = ln.rstrip()
				ln = ln.split('#', 1)[0]
				ln = ln.rstrip(' \t')
				if ln:
					yield ln
			
			f.close()

def offset(s):
	
	if s in {'-', '0'}:
		return 0
    
	dir, s = (-1, s[1:]) if s[0] == '-' else (1, s)
	words = [int(n) for n in s.split(':')]
	assert 1 <= len(words) < 4, words
	words = words + [0] * (3 - len(words))
	
	assert 0 <= words[0] < 24, words
	assert 0 <= words[1] < 60, words
	assert 0 <= words[2] < 60, words
	return dir * sum((i * num) for (i, num) in zip(words, (3600, 60, 1)))

def zoneline(ls):
	ls[1] = None if ls[1] == '-' else ls[1]
	tmp = offset(ls[0]), ls[1], ls[2], ls[3:]
	return {k: v for (k, v) in zip('orfu', tmp)}

def parse(fn):
	
	zones, rules, zone = {}, {}, None
	for ln in lines(fn):
		
		# see zic(8) for documentation
		words = WS_SPLIT.split(ln)
		if words[0] == 'Zone':
			assert words[1] not in zones, words[1]
			zone = []
			zone.append(zoneline(words[2:]))
			if '/' in words[1]:
				zones[words[1]] = zone
		
		elif words[0] == '':
			assert zone is not None
			zone.append(zoneline(words[1:]))
			
		elif words[0] == 'Rule':
			zone = None
			words[8] = offset(words[8])
			rule = rules.setdefault(words[1], [])
			rule.append(words[2:])
			
		elif words[0] == 'Link':
			zone = None # ignore
		else:
			assert False, ln
	
	return {'zones': zones, 'rules': rules}

if __name__ == '__main__':
	
	path = sys.argv[1]
	version = re.match('tzdata(.*)\.tar\.gz$', os.path.basename(path))
	if version is None:
		raise StandardError('argument must be tzdata archive')
	
	print(json.dumps(parse(path)))
