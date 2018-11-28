
import ssl
from urllib import request
from urllib import error

# ssl._create_default_https_context = ssl._create_unverified_context


def getHttpCode(urlpath):
    try:

        req = request.Request(urlpath)
        response = request.urlopen(req) 
    except error.HTTPError as e:
        if(e.code == 400):
           return  400
        #if(e.code == 404):
        #    return  404
        raise RuntimeError('HTTPError')
    except error.URLError:
        raise RuntimeError('URLError')
    raise RuntimeError('HTTPError')

def checkHttpCode(code):
    if(code == 400):
        print(code)
    else:
        print("error:",code)

