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

Refer to the ``Makefile`` for further instructions. The ``source.json``
``Makefile`` target is currently Gentoo-specific; you can trivially generate
``source.json`` by passing an explicit path to the tzdata tarball to
``zones.py``.

The JavaScript code currently assumes installation at a host root and
redirection of all requests for that host to ``index.html``. On Apache, this
can be achieved by employing the ``FallbackResource`` directive (consider
also enabling ``AllowEncodedSlashes`` for your virtual host).
