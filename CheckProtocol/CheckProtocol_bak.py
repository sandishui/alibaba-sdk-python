#coding=utf-8

import requests

def getHttpCode(url):
    try:
        # request url
        html = requests.get(url)
    except requests.exceptions.ConnectionError, e:
        print(url,": ConnectionError: ",e.message)
        return -1

    # get statusCode
    code = html.status_code

    return code

def checkHttpCode(code):
    if(code == -1):
        print("error")
    else:
        print(code)


if __name__ == '__main__':
    url = "https://huodong.aliyuncs.com"
    code = getHttpCode(url)
    checkHttpCode(code)