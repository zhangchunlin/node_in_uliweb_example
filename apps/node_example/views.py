#coding=utf-8
from uliweb import expose, redirect
@expose('/')
def index():
    return redirect(url_for_static("node/index.html"))
