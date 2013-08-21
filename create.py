import json
import jinja2

if __name__ == '__main__':
	
	data = {}
	with open('pruned.json') as f:
		data['zones'] = json.load(f)
	
	env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
	env.filters['json'] = lambda x: json.dumps(x)
	print env.get_template('index.tmpl').render(**data)
