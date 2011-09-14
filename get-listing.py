from httplib import HTTPConnection
from time import strptime, mktime
from os.path import splitext
from urllib import urlopen
from re import findall
from os import utime, mkdir

base = 'http://planet.openstreetmap.org/'
html = urlopen(base).read()

for match in findall(r'<a href="(.+)">(.+)</a>  +(\S.+\S)  +(\S+)', html):
    href, name, date, size = list(match)
    
    if splitext(name)[1] in ('.bz2', '.md5', '.gz'):
        time = mktime(strptime(date, '%d-%b-%Y %H:%M'))
        
        print >> open(name, 'w'), 'Hello World.'
        utime(name, (time, time))
        
        #print name, date, time
    elif name.endswith('/'):
        time = mktime(strptime(date, '%d-%b-%Y %H:%M'))
        
        mkdir(name)
        utime(name, (time, time))
        
        print name, date, time
