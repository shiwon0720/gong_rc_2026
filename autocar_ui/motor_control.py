"""
오토카 모터 제어 모듈.

아직 모터/모터드라이버 종류가 정해지지 않아서, 지금은 동작을 print로만
표시하는 '스텁(stub)' 상태입니다. UI ↔ 서버 연결 흐름만 먼저 확인하고,
나중에 실제 하드웨어가 정해지면 아래 forward/backward/left/right/stop
함수 내부만 채우면 됩니다.

예) RPi.GPIO + L298N 같은 모터드라이버를 쓰는 경우 대략적인 형태
(참고용이며, 핀 번호/배선에 따라 달라집니다):

    import RPi.GPIO as GPIO

    IN1, IN2, IN3, IN4, ENA, ENB = 17, 18, 27, 22, 23, 24

    GPIO.setmode(GPIO.BCM)
    for pin in (IN1, IN2, IN3, IN4, ENA, ENB):
        GPIO.setup(pin, GPIO.OUT)

    def forward():
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)

    def backward():
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)

    def stop():
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)

지금 단계에서는 이런 부분을 신경 쓰지 않아도 됩니다.
"""

import time

_last_direction = None
_last_time = 0.0


def execute(direction: str) -> None:
    """app.py가 호출하는 진입점. direction: forward/backward/left/right/stop"""
    global _last_direction, _last_time
    _last_direction = direction
    _last_time = time.time()

    # TODO: 하드웨어가 정해지면 이 부분을 실제 모터 제어 코드로 교체
    label = {
        "forward": "전진",
        "backward": "후진",
        "left": "좌회전",
        "right": "우회전",
        "stop": "정지",
    }.get(direction, direction)
    print(f"[motor] {label}")


def status() -> dict:
    return {"last_direction": _last_direction, "last_time": _last_time}