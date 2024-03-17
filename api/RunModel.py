from flask import Blueprint,jsonify,request,session
from flask_cors import CORS
from functools import wraps

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


def check_outputs(*required_params):
    def decorator(func):
        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)

            # 检查结果是否为字典类型
            if not isinstance(result, dict):
                return jsonify({'error': '返回结果类型错误'}), 500

            # 检查结果中是否包含必需的字段
            required_fields = required_params  # 请根据实际情况修改字段列表
            missing_fields = [field for field in required_fields if field not in result]
            if missing_fields:
                return jsonify({'error': f'缺少{"、".join(missing_fields)}字段'}), 500

            # 其他的出参检查逻辑...
            result.update({'message':'参数检测通过'})
            return jsonify(result)

        return wrapper

    return decorator


@runmodel.route('/run', methods=['GET', 'POST'])
@check_params('email', 'name', 'age')  # 添加这个装饰器来检查入参
@check_outputs('result', 'time')  # 添加这个装饰器来检查出参
def run():
    # 如果所有参数都存在，你的逻辑代码将在这里执行
    result = {'result':'300','time':'2'}
    return result
