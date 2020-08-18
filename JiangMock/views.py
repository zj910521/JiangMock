import json

from JiangMock import app,models
from flask import render_template,request

@app.route("/")
def index():
    return "abc"

@app.route("/<path:path>",methods=['GET', 'PUT', 'DELETE', 'POST'])
def search_request(path):
    print(path,request.path,request.method,request.base_url)
    m = models.Api.query.filter_by(request_url=request.base_url,method=request.method).first_or_404()
    model = ""
    if m.method == "POST":
        if len(request.form) == 0 :
            model = "JSON"
            data = json.loads(request.get_data(as_text=True))
        else:
            model = "FORM"
            data = request.form

    search = models.SearchRespons.query.filter_by(api_id=m.id,request_model=model).all()
    check = ""
    for i in search:
        check = True
        for j in data:
            try:
                if j not in i.request_data or data.get(j) != json.loads(i.request_data)[j]:
                    check = False
            except KeyError:
                check = False
        if check == True:
            return i.response_data
    if check == False:
        return "找不到相关返回配置"


@app.errorhandler(404)
def url_not_found(error):
    return json.dumps({
        "status": 404,
        "msg": "the request url not found,please check"
    })