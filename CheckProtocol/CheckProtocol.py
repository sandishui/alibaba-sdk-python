#coding=utf-8

import sys

'''
说明：
    返回 400  正常
    返回 -1   为其他httpcode
    返回 -2   url错误
    
'''
if __name__ == '__main__':
    url = "https://huodong.aliyuncs.com"

    # 获取版本信息 print(sys.version_info.major) # minor
    info = sys.version_info
    # print(info.major)
    # 判断版本
    if(2 == info.major):
        import CheckTwo
        code = CheckTwo.getHttpCode(url)
        CheckTwo.checkHttpCode(code)
    elif(3 == info.major):
        import CheckThree
        code = CheckThree.getHttpCode(url)
        CheckThree.checkHttpCode(code)
