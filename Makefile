GENTOO_TZDATA = $(shell ls /usr/portage/distfiles/tzdata20* 2>/dev/null | tail -n1)
TZDATA_LATEST = $(or $(GENTOO_TZDATA),tzdata-latest.tar.gz)
TZDATA_URL = ftp://ftp.iana.org/tz/tzdata-latest.tar.gz

index.html: pruned.json index.tmpl
	@python create.py pruned.json > index.html

pruned.json: source.json prune.py
	@python prune.py source.json > pruned.json

source.json: zones.py $(TZDATA_LATEST)
	@python zones.py $(TZDATA_LATEST) > $@

tzdata-latest.tar.gz:
	@echo Downloading $(TZDATA_URL)
	@wget -q $(TZDATA_URL)

serve:
	@python serve.py

clean:
	rm -rf index.html *.json tzdata-latest.tar.gz
