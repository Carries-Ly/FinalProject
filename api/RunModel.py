from flask import Blueprint,jsonify,request,session
from flask_cors import CORS

runmodel = Blueprint('runmodel',__name__,url_prefix='/runmodel')
CORS(runmodel, cors_allowed_origins="*")


def check_params(*required_params):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 对于GET请求，使用request.args
            if request.method == 'GET':
                data = request.args
            # 对于POST请求，假设使用的是JSON格式
            else:
                # data = request.args
                data = request.json or {}
                print(data)

            missing_params = [param for param in required_params if param not in data]
            if missing_params:
                return jsonify({'error': f'缺少{"、".join(missing_params)}参数'}), 400

            return func(*args, **kwargs)

        return wrapper

    return decorator
@runmodel.route('/run', methods=['GET', 'POST'])
@check_params('email', 'name', 'age')  # 添加这个装饰器来检查参数
def run():
    # 如果所有参数都存在，你的逻辑代码将在这里执行
    return jsonify({'message': '参数检查通过，你的逻辑已执行'})
