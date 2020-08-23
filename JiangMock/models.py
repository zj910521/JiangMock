from JiangMock import db

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    desc = db.Column(db.String(100),nullable=False)
    api = db.relationship('Api',backref='project')
    is_delete = db.Column(db.Boolean,default=False)


class Api(db.Model):
    __tablename__ = 'api'
    id = db.Column(db.Integer,primary_key=True)
    method = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(100), nullable=False, unique=True)
    request_url = db.Column(db.String(100),nullable=False,unique=True)
    project_id = db.Column(db.Integer,db.ForeignKey('project.id'))
    is_delete = db.Column(db.Boolean,default=False)
    search_id = db.relationship("SearchRespons", backref='api')

class SearchRespons(db.Model):
    __tablename__ = "search"
    id = db.Column(db.Integer,primary_key=True)
    # 2.请求模式（json or formdata）
    request_model = db.Column(db.String(50),nullable=False)
    request_heard = db.Column(db.String(300))
    request_data = db.Column(db.String(300),nullable=False)
    response_data = db.Column(db.TEXT,nullable=False)
    api_id = db.Column(db.Integer,db.ForeignKey('api.id'))
    all_check = db.Column(db.Boolean,default=True)
    is_delete = db.Column(db.Boolean,default=False)


