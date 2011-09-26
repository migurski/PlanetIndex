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

    return '<b><a href="%(file)s">%(name)s</a></b><br><b>%(size)s</b>, created %(date)s ago.<br><small>md5: %(hash)s</small>.' % locals()

planet_link = file_info('planet-latest.osm.bz2', 'Latest Weekly Planet File')
changesets_link = file_info('changesets-latest.osm.bz2', 'Latest Weekly Changesets')

print """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /</title>
  <link href="style.css" rel="stylesheet" type="text/css">
 </head>
 <body>
<img id="logo" src="logo.png" alt="OSM logo" width="128" height="128">
<h1>Planet OSM</h1>

<p>
The files found here are regularly-updated, complete copies of the OpenStreetMap.org
database, and are distributed under a Creative Commons Attribution-ShareAlike 2.0 license.
For more information, <a href="http://wiki.openstreetmap.org/wiki/Planet.osm">see the project wiki</a>.
</p>

<table id="about">
  <tr>
    <th>
        <h2>Complete OSM Data</h2>
    </th>
    <th>
        <h2>Using The Data</h2>
    </th>
    <th>
        <h2>Extracts &amp; Mirrors</h2>
    </th>
  </tr>
  <tr>
    <td>
        <p>%(planet_link)s</p>
        <p>%(changesets_link)s</p>
        <p>
        Each week, a new and complete copy of all data in OpenStreetMap is made
        available as a compressed XML file, along with a smaller file with
        complete metadata for all changes made since the previous week.
        </p>
    </td>
    <td>
        <p>
        You are granted permission to use OpenStreetMap data by 
        <a href="http://osm.org/copyright">the OpenStreetMap License</a>, which also describes 
        your obligations.
        </p>
        <p>
        You can <a href="http://wiki.openstreetmap.org/wiki/Planet.osm#Processing_the_File">process the file</a>
        or extracts with a variety of tools. <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>
        is a general-purpose command-line tool for converting the data among different formats
        and databases, and <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql">Osm2pgsql</a>
        is a tool for importing the data into a Postgis database for rendering maps.
        </p>
        <p>
        <a href="http://wiki.openstreetmap.org/wiki/Coastline_error_checker">Processed coastline data</a>
        derived from OSM data is also needed for rendering usable maps, and can be found in a
        <a href="http://tile.openstreetmap.org/processed_p.tar.bz2">single shapefile</a> (360MB).
        </p>
    </td>
    <td>
        <p>
        The complete planet is very large, so you may prefer to use one of
        <a href="http://wiki.openstreetmap.org/wiki/Planet.osm#Mirrors">several periodic extracts</a>
        (individual countries or states) from third parties. <a href="http://download.geofabrik.de/osm/">GeoFabrik.de</a>
        and <a href="http://downloads.cloudmade.com/">Cloudmade.com</a> are two providers
        of extracts with up-to-date worldwide coverage.
        </p>
    </td>
  </tr>
</table>

<p>
If you find data within OpenStreetMap that you believe is an infringement of someone else's copyright, then please make contact with the <a href="http://wiki.openstreetmap.org/wiki/Data_working_group">OpenStreetMap Data Working Group</a>.
</p>
""" % locals()
