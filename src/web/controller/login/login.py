import web

urls = ()
r = web.template.render("templates/loign")


class Login(object):
    def GET(self):
        return r.login()


login = web.application(urls, locals())
