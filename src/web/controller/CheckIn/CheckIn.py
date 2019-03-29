# coding=utf-8
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import web
import json
from ..orm.Hotel import Hotel
from ..orm.CheckIn import CheckIn
from ..orm.RelationCheckIn import RelationCheckIn
from ..utils.utils import *
from sqlalchemy import *


# 时间日期
class SearchAllCheckInList(object):
    def POST(self):
        Params = web.input('nHotelDocType')
        web.input('nDocType')
        web.input('sGuestDocNameLike')
        web.input('sHotelName')
        web.input('nSex')

        Query = Hotel.session.query(Hotel)
        if Params['HotelID']:
            Query = Query.filter(Hotel.HotelID == Params['HotelID'])
        if Params['nProvinceID']:
            Query = Query.filter(Hotel.ProvinceID == Params['nProvinceID'])
        if Params['nCityID']:
            Query = Query.filter(Hotel.CityID == Params['nCityID'])
        if Params['nDistrictID']:
            Query = Query.filter(Hotel.DistrictID == Params['nDistrictID'])
        if Params['sHotelCode']:
            Query = Query.filter(Hotel.HotelCode.like("%" + Params['sHotelCode'] + "%"))
        if Params['sHotelName']:
            Query = Query.filter(Hotel.HotelName.like("%" + Params['sHotelName'] + "%"))
        if Params['sRegStartDate']:
            sRegStartDate = Utils().strDataToData(Params['sRegStartDate'])
            Query = Query.filter(Hotel.RegStartTime >= sRegStartDate)
        if Params['sRegEndDate']:
            Query = Query.filter(Hotel.RegStartTime <= Params['sRegEndDate'])
        lsQueryData = Query.limit(20).offset(0).all()
        lsDataList = []
        for objQueryData in lsQueryData:    # 统计酒店的订单数
            global objData
            objData = objQueryData.hotel_to_json()
            global lsCheckinCount
            lsCheckinCount = CheckinCount().POST(objData["HotelID"])
            if lsCheckinCount:
                CheckInCount = lsCheckinCount[1]
            else:
                CheckInCount = 0
            objData['CheckInCount'] = CheckInCount
            lsDataList.append(objData)
        # for objCheckinCount in lsCheckinCount:
        #     lsGuestCount = GuestCount().POST(objData["HotelID"])
        #     print lsGuestCount

        return json.dumps({"code": 200, "data": lsDataList})


class CheckinCount(object):
    def POST(self, HotelID):
        objQueryData = Hotel.session.query(Hotel.HotelID, func.count(Hotel.HotelID).label("count")). \
            join(CheckIn, Hotel.HotelID == CheckIn.HotelID). \
            filter(Hotel.HotelID == HotelID).group_by(Hotel.HotelID).first()
        return objQueryData


# class GuestCount(object):
#     def POST(self, CheckInID):
#         objQueryData = Hotel.session.query(func.count(Hotel.HotelID).label("count")). \
#             join(CheckIn, Hotel.HotelID == CheckIn.HotelID). \
#             jion(RelationCheckIn, Hotel.HotelID == RelationCheckIn.CheckInID). \
#             filter(Hotel.HotelID == CheckInID).group_by(Hotel.HotelID).first()
#         if objQueryData:
#             return objQueryData[0]
#         else:
#             return 0
