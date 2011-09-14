#!/usr/bin/env python

from os import stat

print 'Content-Type: text/plain\n'
print 'yes.'

print stat('planet-latest.osm.bz2').st_size
print open('planet-latest.osm.bz2.md5', 'r').read()
