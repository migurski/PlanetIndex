#!/usr/bin/env python

from time import time
from os import stat, environ
from re import search

def nice_size(file):
    size = stat(file).st_size
    KB = 1024.
    MB = 1024. * KB
    GB = 1024. * MB
    TB = 1024. * GB
    
    if size < KB:
        size, suffix = size, ''
    elif size < MB:
        size, suffix = size/KB, 'KB'
    elif size < GB:
        size, suffix = size/MB, 'MB'
    elif size < TB:
        size, suffix = size/GB, 'GB'
    else:
        size, suffix = size/TB, 'TB'
    
    if size < 10:
        return '%.1f %s' % (size, suffix)
    else:
        return '%d %s' % (size, suffix)

def nice_time(time):
    if time < 15:
        return 'moments'
    if time < 90:
        return '%d seconds' % time
    if time < 60 * 60 * 1.5:
        return '%d minutes' % (time / 60.)
    if time < 24 * 60 * 60 * 1.5:
        return '%d hours' % (time / 3600.)
    if time < 7 * 24 * 60 * 60 * 1.5:
        return '%d days' % (time / 86400.)
    if time < 30 * 24 * 60 * 60 * 1.5:
        return '%d weeks' % (time / 604800.)

    return '%d months' % (time / 2592000.)

def file_info(file, name):
    size = nice_size(file)
    hash = search(r'\w{32}', open(file+'.md5', 'r').read()).group(0)
    date = nice_time(time() - stat(file).st_mtime)

    return '<li><b><a href="%(file)s">%(name)s</a></b><br><b>%(size)s</b>, created %(date)s ago.<br>md5: %(hash)s.</li>' % locals()

print 'Content-Type: text/html\n'
print '<img id="logo" src="logo.png">'
print '<h1>', environ.get('HTTP_HOST', 'planet.openstreetmap.org'), '</h1>'

print '<ul>'
print file_info('planet-latest.osm.bz2', 'Latest Weekly Planet File')
print file_info('changesets-latest.osm.bz2', 'Latest Weekly Changesets')
print '</ul>'

print """
<p>
The files found here are regularly-updated, complete copies of the OpenStreetMap.org
database, and are distributed under a Creative Commons Attribution-ShareAlike 2.0 license.

The complete planet is very large, so you may prefer to use one of
<a href="http://wiki.openstreetmap.org/wiki/Planet.osm#Mirrors">several periodic extracts</a>
(individual countries or states) from third parties. <a href="http://download.geofabrik.de/osm/">GeoFabrik.de</a>
and <a href="http://downloads.cloudmade.com/">Cloudmade.com</a> are two providers
of extracts with up-to-date worldwide coverage.

You can <a href="http://wiki.openstreetmap.org/wiki/Planet.osm#Processing_the_File">process the file</a>
or extracts with a variety of tools. <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>
is a general-purpose command-line tool for converting the data among different formats
and databases, and <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql">Osm2pgsql</a>
is a tool for importing the data into a Postgis database for rendering maps.
</p>

<p>
For more information about Planet.osm, <a href="http://wiki.openstreetmap.org/wiki/Planet.osm">see the project wiki</a>.
</p>

<p>
If you find data within OpenStreetMap that you believe is an infringement of someone else's copyright, then please make contact with the <a href="http://wiki.openstreetmap.org/wiki/Data_working_group">OpenStreetMap Data Working Group</a>.
</p>
"""
