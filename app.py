from flask import Flask,render_template,request
from flask_cors import CORS
from .api.RunModel import runmodel
# from api.account import account
# from api.article import article
# import config
# from models import mail,db

app = Flask(__name__)
# #绑定配置文件
# app.config.from_object('config.Dev')
app.register_blueprint(runmodel)
# app.register_blueprint(article)
# db.init_app(app)
# mail.init_app(app)

CORS(app,cors_allowed_origins="*")
@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)

