from flask import request

def getHeaderValue(name):
    ret = request.headers.get(name)
    if (ret)