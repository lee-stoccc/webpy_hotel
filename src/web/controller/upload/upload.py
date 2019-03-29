# -*- coding: UTF-8 -*-
from flask import Flask, request, make_response, send_from_directory
from flask_cors import *
import sys
import os
import datetime
import uuid
import base64

app = Flask(__name__)

baseDir = sys.path[0] + '/image/'


# 获取图片后缀名
def getSuffix(filename):
    tempArr = filename.split('.')
    suffix = tempArr[-1]
    fileType = ['jpg', 'jpeg', 'gif', 'png']
    if len(tempArr) < 2:
        return 'error name'
    elif suffix not in fileType:
        return 'error type'
    else:
        return suffix


# mkdir
@app.route('/mkdir', methods=['GET'])
def mkdir():
    time = datetime.date.today().strftime('%y%m')
    dirPath = sys.path[0] + '/image/' + str(time)
    isExist = os.path.exists(dirPath)
    if not isExist:
        os.makedirs(dirPath)
        print '创建文件夹成功'
        return dirPath
    else:
        print '文件目录已存在'
        return dirPath


# 上传图片接口   需要传入的参数如下： filePath:文件路径
@app.route('/upimg/<string:basePath>', methods=['POST'])
def upimg(basePath):
    resp = make_response()
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    image = request.files.get('image')
    try:
        filePath = base64.b64decode(basePath)
        # 如果文件存在则删除
        if isPicExist(filePath):
            os.remove(filePath)
            print '删除成功'
        timePath = datetime.date.today().strftime('%y%m')
        newFilePath = mkdir() + '/' + str(uuid.uuid1()) + image.filename
        newBasePath = base64.b64encode(newFilePath)
        image.save(newFilePath)
        resDict = {'timePath': timePath, 'filePath': newBasePath}
        return str(resDict)
    except ZeroDivisionError as e:
        print e


# 判断图片是否存在
def isPicExist(filePath):
    try:
        if os.path.exists(filePath):
            return True
        else:
            return False
    except ZeroDivisionError as e:
        print e


# 下载  需要传入文件路径：filePath
@app.route('/download/<string:basePath>', methods=['GET'])
def download(basePath):
    if request.method == "GET":
        filePath = base64.b64decode(basePath)
        index = filePath.index('image')
        resPath = filePath[index:]
        rootPath = filePath[0:index + 10]
        fileName = resPath[11:]
        if os.path.isfile(filePath):
            return send_from_directory(rootPath, fileName, as_attachment=True)
        pass


# show photo    参数：basePath
@app.route('/show/<string:basePath>', methods=['GET'])
def show_photo(basePath):
    if request.method == 'GET':
        if basePath is None:
            pass
        else:
            filePath = base64.b64decode(basePath)
            if isPicExist(filePath):
                image_data = open(filePath, "rb").read()
                response = make_response(image_data)
                response.headers['Content-Type'] = 'image/png'
                return response
            else:
                return '查无路径'
    else:
        pass


if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0', port='20010')
