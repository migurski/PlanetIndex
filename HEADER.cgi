#!/usr/bin/env python

from time import strftime, localtime
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

def file_info(file, name):
    size = nice_size(file)
    hash = search(r'\w{32}', open(file+'.md5', 'r').read()).group(0)
    date = strftime('%a, %b %d %Y, %I:%M%p', localtime(stat(file).st_mtime))

    return '<li><b><a href="%(file)s">%(name)s</a></b><br><b>%(size)s</b>, created %(date)s.<br>md5: %(hash)s.</li>' % locals()

print 'Content-Type: text/plain\n'
print '<img src="logo.png">'
print '<h1>', environ.get('HTTP_HOST', 'planet.openstreetmap.org'), '</h1>'

print '<ul>'
print file_info('planet-latest.osm.bz2', 'Latest Weekly Planet')
print file_info('changesets-latest.osm.bz2', 'Latest Weekly Changeset')
print '</ul>'

print '<p>If you find data within OpenStreetMap that you believe is an infringement of someone else\'s copyright, then please make contact with the <a href="http://wiki.openstreetmap.org/wiki/Data_working_group">OpenStreetMap Data Working Group</a>.</p>'