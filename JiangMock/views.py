import json

from flask.views import MethodView

from JiangMock import app, models
from flask import render_template,request

from JiangMock.Validator import Validator


@app.route("/")
def index():
    return render_template("index.html")

class Project(MethodView):

    def get(self,pro_name):
        print("1234")
        if pro_name != "all":
            project = models.Project.query.filter_by(name=pro_name,is_delete=False).first_or_404()
            print(project)
        else:
            project = models.Project.query.filter_by(is_delete=False).all()
        projectList = []
        for i in project:
            pro_dict = {"pro_name":i.name,"pro_desc":i.desc}
            projectList.append(pro_dict)

        return json.dumps(projectList)
    def post(self):
        pass

app.add_url_rule('/project/<string:pro_name>',view_func=Project.as_view('project'))


@app.route("/<path:path>",methods=['GET', 'PUT', 'DELETE', 'POST'])
def search_request(path):
    print(path,request.path,request.method,request.base_url)
    m = models.Api.query.filter_by(request_url=request.base_url,method=request.method,is_delete=False).first_or_404()
    model = ""
    if m.method == "POST":
        if len(request.form) == 0 :
            model = "JSON"
            data = json.loads(request.get_data(as_text=True))
        else:
            model = "FORM"
            data = request.form
    print(data)
    search = models.SearchRespons.query.filter_by(api_id=m.id,request_model=model).all()
    print(search)
    response = Validator.check_data(search,data)

    return response



@app.errorhandler(404)
def url_not_found(error):
    return json.dumps({
        "status": 404,
        "msg": "the request url not found,please check"
    })