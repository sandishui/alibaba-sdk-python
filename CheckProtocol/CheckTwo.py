#coding=utf-8
import urllib2

def getHttpCode(urlpath):
    try:
        response = urllib2.urlopen(urlpath)
    except urllib2.HTTPError as e:
        #if(e.code == 400):
        #    return  400
        if(e.code == 404):
            return  404
        raise RuntimeError('HTTPError')
    except urllib2.URLError:
        raise RuntimeError('URLError')
    raise RuntimeError('HTTPError')

def checkHttpCode(code):
    if(code == 400):
        print(code)
    else:
        print("error:",code)



