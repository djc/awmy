import json

if __name__ == '__main__':
	
	with open('pruned.json') as f:
		data = json.load(f)
	
	with open('index.tmpl') as f:
		tmpl = f.read()
	
	for k, v in data.items():
		tmpl = tmpl.replace('{{ %s }}' % k, json.dumps(v))
	
	print(tmpl)
