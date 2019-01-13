# coding=utf-8
# !/usr/bin/python
# -*- coding: UTF-8 -*-
from ..orm.user import User
from ..orm.UserDataRole import UserDataRole
import web
import json
from sqlalchemy import *


class AddUser(object):
    def POST(self):
        Params = web.input('name')
        web.input("id")
        session = User.DBSession()
        new_user = User(UserCode=Params['UserCode'], UserName=Params['UserName'], UserID=Params["UserID"])
        session.add(new_user)
        session.commit()
        session.close()
        return json.dumps({"code": 200})


class DelUser(object):
    def POST(self):
        session = User.DBSession()
        target = session.query(User).filter(User.UserID >= 1).all()
        for v in target:
            session.delete(v)
            session.commit()
            session.close()


#  多表联查，join on，多表json序列化
class  SearchUserRole(object):
    def POST(self):
        # session = User.DBSession()
        dtParams = web.input("UserID")
        web.input("UserDataRoleID")
        strQuery = User.session.query(User, UserDataRole).join(UserDataRole,
                                                                              User.UserID == UserDataRole.UserID)
        if dtParams['UserCode']:
            strQuery = strQuery.filter(User.UserCode.like("%" + dtParams['UserCode'] + "%"))
        if dtParams['UserName']:
            strQuery = strQuery.filter(User.UserName.like("%" + dtParams['UserName'] + "%"))
        if dtParams['Remark']:
            strQuery = strQuery.filter(UserDataRole.Remark.like("%" + dtParams['Remark'] + "%"))
        lsDataSet = strQuery.limit(20).offset(0).all()
        lsDataList = []
        for objDataSet in lsDataSet:
            objData={}
            objUser = objDataSet[0].user_to_json()
            objUserDataRole = objDataSet[1].user_to_json()
            objData['User'] = objUser
            objData['UserDataRole'] = objUserDataRole
            lsDataList.append(objData)
        Data ={}
        Data['DataSet'] = lsDataList
        Data['PageNum'] = len(lsDataList)
        return json.dumps(Data)

# 分页、不定参数、模糊查询、序列化、单页查询
class SearchUser(object):
    def POST(self):
        # session = User.DBSession()
        dtParams = web.input("UserID")
        web.input("UserCode")
        web.input("UserName")
        strQuery = User.session.query(User)
        if dtParams['UserID']:
            strQuery = strQuery.filter(User.UserID == dtParams['UserID'])
        if dtParams['UserCode']:
            strQuery = strQuery.filter(User.UserCode.like("%" + dtParams['UserCode'] + "%"))
        if dtParams['UserName']:
            strQuery = strQuery.filter(User.UserName.like("%" + dtParams['UserName'] + "%"))
        lsDataSet = strQuery.limit(20).offset(1).all()
        lsDataList = []
        for objDataSet in lsDataSet:
            lsDataList.append(objDataSet.user_to_json())
        return json.dumps(lsDataList)

# 此种方法不能自动判断前端传空值
# lsDataSet = User.session.query(User).filter(
#         #     and_(
#         #         User.UserID == dtParams['UserID'],
#         #         User.UserCode.like("%"+dtParams['UserCode']+"%"),
#         #         User.UserName.like("%"+dtParams['UserName']+"%")
#         #     )
#         # ).limit(10).offset(2).all()
