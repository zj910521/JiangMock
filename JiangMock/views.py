import json

from JiangMock import app,models
from flask import render_template,request

@app.route("/")
def index():
    return "abc"

@app.route("/<path:path>",methods=['GET', 'PUT', 'DELETE', 'POST'])
def search_request(path):
    print(path,request.path,request.method)
    m = models.Api.query.filter_by(url=request.path,method=request.method).first_or_404()
    body = json.loads(m.body)
    return body

@app.errorhandler(404)
def url_not_found(error):
    return json.dumps({
        "status": 404,
        "msg": "the request url not found,please check"
    })