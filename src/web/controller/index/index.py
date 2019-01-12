import web
import os,sys
import json

# import MySQL as db

render = web.template.render('templates/second')
# db = web.database(dbn='mysql', host='127.0.0.1', post=3308, db='user', user='root', pw='911789')
urls = (
    # '/index', 'Index',
)


class Index(object):
    def GET(self):
        # names = os.getcwd()
        # name = sys.path.append(names)
        # name = sys.path
        name = 'Web.py'
        # name =1
        # list = db.select('user')
        dict1 = '{"age": "12"}'
        json_info = json.loads(dict1)
        print json_info['age']
        print 111111
        return render.index(name)


index = web.application(urls, locals())
# if __name__ == "__main__":
#     app = web.application(urls, globals())
#     app.run()
#     # web.httpserver.runsimple(app.wsgifunc(), ('10.3.15.79', 8001))
#     # WSGIServer(('0.0.0.0', 8000), app.wsgifunc()).serve_forever()
