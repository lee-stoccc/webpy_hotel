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
class SearchHotel(object):
    def POST(self):
        Params = web.input()
        Query = Hotel.session.query(Hotel)
        if self.verify('HotelID', Params):
            Query = Query.filter(Hotel.HotelID == Params['HotelID'])
        if self.verify('nProvinceID', Params):
            Query = Query.filter(Hotel.ProvinceID == Params['nProvinceID'])
        if self.verify('nCityID', Params):
            Query = Query.filter(Hotel.CityID == Params['nCityID'])
        if self.verify('nDistrictID', Params):
            Query = Query.filter(Hotel.DistrictID == Params['nDistrictID'])
        if self.verify('sHotelCode', Params):
            Query = Query.filter(Hotel.HotelCode.like("%" + Params['sHotelCode'] + "%"))
        if self.verify('sHotelName', Params):
            Query = Query.filter(Hotel.HotelName.like("%" + Params['sHotelName'] + "%"))
        if self.verify('sRegStartDate', Params):
            sRegStartDate = Utils().strDataToData(Params['sRegStartDate'])
            Query = Query.filter(Hotel.RegStartTime >= sRegStartDate)
        if self.verify('sRegEndDate', Params):
            Query = Query.filter(Hotel.RegStartTime <= Params['sRegEndDate'])
        lsQueryData = Query.limit(20).offset(0).all()
        lsDataList = []
        for objQueryData in lsQueryData:  # 统计酒店的订单数
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

    def verify(self, key, Params):
        if key in Params and Params.get(key) != '':
            return true


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
