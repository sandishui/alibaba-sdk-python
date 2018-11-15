#coding=utf-8
import urllib2

def getHttpCode(urlpath):
    try:
        response = urllib2.urlopen(urlpath)
    except urllib2.HTTPError as e:
        if(e.code == 400):
            return  400
        return -1
    except urllib2.URLError:
        return -2

def checkHttpCode(code):
    if(code == 400):
        print(code)
    else:
        print("error:",code)



