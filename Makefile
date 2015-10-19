
index.html: pruned.json index.tmpl
	@python create.py pruned.json > index.html

pruned.json: source.json prune.py
	@python prune.py source.json > pruned.json

source.json: zones.py
	@python zones.py $(shell ls /usr/portage/distfiles/tzdata20* | tail -n1) > $@

clean:
	rm -rf index.html *.json
