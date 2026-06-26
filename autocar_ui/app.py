"""
AutoCar 웹 컨트롤러 (Flask)

오토카(라즈베리파이) 위에서 이 파일을 실행하면 웹서버가 뜨고,
같은 네트워크의 PC/휴대폰 브라우저로 접속해 방향키 UI로 조작할 수 있습니다.

실행:
    pip install -r requirements.txt
    python app.py

접속:
    http://<오토카의 IP>:5000
    (오토카에서 `hostname -I` 로 IP 확인)

파일 구성 (모두 같은 폴더에 두면 됩니다):
    app.py
    motor_control.py
    index.html
    requirements.txt
"""

import os
from flask import Flask, render_template, jsonify
import motor_control

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# index.html을 app.py와 같은 폴더에 두기 위해 template_folder를 현재 폴더로 지정
app = Flask(__name__, template_folder=BASE_DIR)

VALID_DIRECTIONS = {"forward", "backward", "left", "right", "stop"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/move/<direction>", methods=["POST"])
def move(direction):
    if direction not in VALID_DIRECTIONS:
        return jsonify(status="error", message=f"unknown direction: {direction}"), 400

    motor_control.execute(direction)
    return jsonify(status="ok", direction=direction)


@app.route("/health")
def health():
    return jsonify(status="ok", **motor_control.status())


if __name__ == "__main__":
    # host="0.0.0.0" 이어야 다른 기기(PC 등)에서 접속 가능
    app.run(host="0.0.0.0", port=5000, debug=True)