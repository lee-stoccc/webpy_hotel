# coding: utf-8
import web
import os, sys
from web.controller.login.login import Login
from web.controller.index.index import Index
from web.controller.Jsons.jsonEx import JsonEx
from web.controller.user.user import AddUser, DelUser, SearchUser, SearchUserRole
from web.controller.Hotel.hotel import SearchHotel


# render = web.template.render('templates/second')


def customhook():
    web.header('Access-Control-Allow-Origin', '*')
    web.header('Access-Control-Allow-Headers',
               'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
    web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')


# from libs import web
urls = (
    '/index', Index,
    "/login", Login,
    '/jsons', JsonEx,
    '/adduser', AddUser,
    "/deluser", DelUser,
    "/user/searchuser", SearchUser,
    "/user/SearchUserRole", SearchUserRole,
    "/hotel/searchhotel", SearchHotel
)
app = web.application(urls, globals())


def aa():
    print "dsafjalsdf"


if __name__ == "__main__":
    app.add_processor(web.loadhook(customhook))
    app.run()

    # web.httpserver.runsimple(app.wsgifunc(), ('10.3.15.79', 8001))
    # WSGIServer(('0.0.0.0', 8000), app.wsgifunc()).serve_forever()
#
