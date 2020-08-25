import json

from flask.views import MethodView

from JiangMock import app, models
from flask import render_template,request

from JiangMock.Validator import Validator
from JiangMock import session

@app.route("/")
def index():
    response_list=[]
    project = models.Project.query.filter_by(is_delete=False).all()
    for i in project:
        api_list = []
        api = models.Api.query.filter_by(project_id=i.id).all()
        print(api)
        if api:
            for j in api:
                api_dict = {
                    "api_id": j.id, "api_method": j.method, "api_name": j.name, "api_url": j.url
                }
                api_list.append(api_dict)
        response_dict = {
            "pro_id":i.id,
            "pro_name":i.name,
            "pro_desc":i.desc,
            "api_list":api_list
        }
        response_list.append(response_dict)
    print(response_list)

    return render_template("index.html",response_list=response_list)

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
            pro_dict = {"pro_id":i.id,"pro_name":i.name,"pro_desc":i.desc}
            projectList.append(pro_dict)

        return json.dumps(projectList)
    def post(self,pro_name):
        pro_name = request.form.get("pro_name")
        pro_desc = request.form.get("pro_desc")
        exist = models.Project.query.filter_by(name=pro_name).first()
        if exist:
            return "数据已存在"
        else:
            project = models.Project(name=pro_name,desc=pro_desc)
            session.add(project)
            session.commit()

        return "添加成功"


class Api(MethodView):

    def get(self,pro_id):
        print(pro_id)
        api = models.Api.query.filter_by(project_id=pro_id).all()
        api_List = []
        for i in api:
            api_dict = {"api_id":i.id,"api_method":i.method,"api_name":i.name,"api_url":i.url}
            api_List.append(api_dict)
        if len(api) == 0 :
            return "不存在接口数据"
        return json.dumps(api_List)


app.add_url_rule('/project/<string:pro_name>',view_func=Project.as_view('project'))
app.add_url_rule('/api/<string:pro_id>',view_func=Api.as_view('api'))


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