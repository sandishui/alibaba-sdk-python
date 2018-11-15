#!/usr/bin/python
#coding=utf-8
import sys

'''
说明：
    返回 400  正常
    返回 其他 抛出异常
    
'''
if __name__ == '__main__':
    url = "https://huodong.aliyuncs.com"
    #url = "http://www.baidu.com"
    # 获取版本信息 print(sys.version_info.major) # minor
    info = sys.version_info[0]
    # print(info.major)
    # 判断版本
    if(2 == info):
        import CheckTwo
        code = CheckTwo.getHttpCode(url)
        CheckTwo.checkHttpCode(code)
    elif(3 == info):
        import CheckThree
        code = CheckThree.getHttpCode(url)
        CheckThree.checkHttpCode(code)

