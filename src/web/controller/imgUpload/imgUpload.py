import web
import json
from ..utils.utils import *
import sys
import os
import datetime
import uuid
import base64

baseDir = sys.path[0] + '/image/'


def out(func):
    def inner(*k, **ks):
        res = func(*k, **ks)
        print k
        print ks
        print 'do someting with logging this way'
        return res
    return inner

class Upload(object):
    @out
    def POST(self):
        Params = web.input('basePath')
        image = web.input(image={})
        if Params['basePath'] != '':
            return 11
            # filePath = base64.b64decode(Params['basePath'])
            # if isPicExist(filePath):
            #     os.remove(filePath)
            #     print 1
        else:
            timePath = datetime.date.today().strftime('%y%m')
            newFilePath = mkdir() + '/' + str(uuid.uuid1()) + image.image.filename
            newBasePath = base64.b64encode(newFilePath)
            fout = open(newFilePath, 'w')
            # fout.write(image.myfile.file.read())
            # image.write(newFilePath)
            resDict = {'timePath': timePath, 'filePath': newBasePath}
            return str(resDict)
        print baseDir
        return 1




def isPicExist(filePath):
    try:
        if os.path.exists(filePath):
            return True
        else:
            return False
    except ZeroDivisionError as e:
        print e


def mkdir():
    time = datetime.date.today().strftime('%y%m')
    dirPath = sys.path[0] + '/image/' + str(time)
    isExist = os.path.exists(dirPath)
    if not isExist:
        os.makedirs(dirPath)
        return dirPath
    else:
        return dirPath
