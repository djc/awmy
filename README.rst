arewemeetingyet.com
===================

A single-page web thingy that helps communicate (recurring) meeting times
to globally distributed (and therefore timezone-challenged) participants.

Requirements
------------

* A tzdata tarball (as distributed by IANA)
* Python (tested with 2.7)

How to install
--------------

Simply run ``make``, which will retrieve the latest timezone information and
build the templates. On gentoo, it will use the latest installed timezone data
from ``/usr/portage/distfiles/tzdata20*``, on other systems it will download the
latest timezone information from ftp.iana.org. If you are not on gentoo, you
have to manually delete tzdata-latest.tar.gz and re-run ``make`` to update
timezones.

The JavaScript code currently assumes installation at a host root and
redirection of all requests for that host to ``index.html``. On Apache, this
can be achieved by employing the ``FallbackResource`` directive (consider
also enabling ``AllowEncodedSlashes`` for your virtual host).

To test locally, run ``make serve`` to spin up a simple http server on port 8000.
