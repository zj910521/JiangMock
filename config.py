USERNAME = 'root'
PASSWORD = '****'
HOST = '123.207.29.73'
DB = 'JiangMock'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://%s:%s@%s/%s' % (USERNAME, PASSWORD, HOST, DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
