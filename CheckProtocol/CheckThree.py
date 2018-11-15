
import ssl
from urllib import request
from urllib import error

# ssl._create_default_https_context = ssl._create_unverified_context


def getHttpCode(urlpath):
    try:

        context = ssl._create_unverified_context()
        req = request.Request(urlpath)
        response = request.urlopen(req, context=context)
    except error.HTTPError as e:
        if(e.code == 400):
            return  400
        return -1
    except error.URLError:
        return -2

def checkHttpCode(code):
    if(code == 400):
        print(code)
    else:
        print("error:",code)

