from flask import Flask
from flask_cors import CORS
from flask import jsonify, request
from kenlm_service import load_model,process_line
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/kenlm_api', methods=(['POST']))
def kenlm_api():
    data = request.get_json()  ####task_id
    lang=data['lang']
    text=data['text']
    score=process_line(load_model(lang),text)
    # 构造要返回的 JSON 数据
    response_data = {
        "status": "success",
        "message": "Received data successfully",
        "score": score  # 将请求中的 JSON 数据返回
    }

    # 返回 JSON 响应
    return jsonify(response_data)