function niceTime(msec)
{
    if(msec < 15*1000) {
        return 'moments';

    } else if(msec < 90*1000) {
        return (msec / 1000).toFixed(0) + ' seconds';

    } else if(msec < 60*60*1000 * 1.5) {
        return (msec / (60 * 1000)).toFixed(0) + ' minutes';

    } else if(msec < 24*60*60*1000 * 1.5) {
        return (msec / (3600 * 1000)).toFixed(0) + ' hours';

    } else if(msec < 7*24*60*60*1000 * 1.5) {
        return (msec / (86400 * 1000)).toFixed(0) + ' days';

    } else if(msec < 30*24*60*60*1000 * 1.5) {
        return (msec / (604800 * 1000)).toFixed(0) + ' weeks';

    } else {
        return (msec / (2592000 * 1000)).toFixed(0) + ' months';
    }
}

function niceSize(bytes)
{
    var KB = 1024,
        MB = 1024 * KB,
        GB = 1024 * MB;
    
    if(bytes < KB) {
        var size = bytes, suffix = 'B';
    
    } else if(bytes < MB) {
        var size = bytes / KB, suffix = 'KB';
    
    } else if(bytes < GB) {
        var size = bytes / MB, suffix = 'MB';
    
    } else {
        var size = bytes / GB, suffix = 'GB';
    }
    
    if(size < 10) {
        return size.toFixed(1) + ' ' + suffix;
    
    } else {
        return size.toFixed(0) + ' ' + suffix;
    }
}

function sizeAgeHTML(file)
{
    if(XMLHttpRequest != undefined)
    {
        var xhr = new XMLHttpRequest();
        xhr.open('HEAD', file, false);
        xhr.send();
        
        var modified = xhr.getResponseHeader('Last-Modified'),
            length = parseInt(xhr.getResponseHeader('Content-Length')),
            age = niceTime((new Date()).getTime() - Date.parse(modified)),
            size = niceSize(length);
        
        console.log([modified, age]);
        console.log([length, size]);
        
        return '<br><b>'+size+'</b>, created '+age+' ago.';
    }
    
    return '';
}

function hashHTML(file)
{
    if(XMLHttpRequest != undefined)
    {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', file, false);
        xhr.send();
        
        var hash = xhr.responseText.match(/\w{32}/)[0];
        
        return '<br><small>md5: '+hash+'</small>.';
    }
    
    return '';
}
