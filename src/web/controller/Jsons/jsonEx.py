import json
import web
from ..orm.user import User

# urls = ()
app = web.application()


class JsonEx(object):
    def POST(self):
        datas = web.input()
        py_name = datas['name']
        py_pass = datas['pass']
        session = User.DBSession()
        new_user = User(id='6', name=py_name)
        # new_user = User(name=py_name, password=py_pass)
        session.add(new_user)
        session.commit()
        session.close()
        # # py_json = {'py_name': py_name, 'py_pass': py_pass}
        web.header('Content-type', 'text/json')
        web.header('Access-Control-Allow-Origin', '*')
        # print py_pass, py_name
        return json.dumps({"code":200})

# jsons = web.application(urls, globals())
