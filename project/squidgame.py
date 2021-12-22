
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import threading
import pyaudio
import wave
import board
import sys
import os
import digitalio
import psutil
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


current_system_pid = os.getpid()

servoPin = 4   # 서보 핀
switch_pin = 21


isPlaying = False
isWatching = False
alive = True
isMoving = 0
RED = 20
YELLOW = 16

# 남은시간 설정값
timeLeft = 30


def servo(pin, degree, t):
    GPIO.setmode(GPIO.BCM)  # 핀의 번호를 보드 기준으로 설정, BCM은 GPIO 번호로 호출함
    GPIO.setup(servoPin, GPIO.OUT)  # GPIO 통신할 핀 설정
    pwm = GPIO.PWM(servoPin, 50)  # 서보모터는 PWM을 이용해야됨. 16번핀을 50Hz 주기로 설정

    pwm.start(4.5)  # 초기 시작값, 반드시 입력해야됨

    pwm.ChangeDutyCycle(degree)
    time.sleep(t)

    # 아래 두줄로 깨끗하게 정리해줘야 다음번 실행할때 런타임 에러가 안남
    pwm.stop()
    GPIO.cleanup(pin)


def play(name: str):
    CHUNK = 1024
    wf = wave.open(name, 'rb')
    p = pyaudio.PyAudio()

    # 음성데이터 스트림 열기
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    # 음성데이터를 입력받아 출력
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

# 스위치의 입력을 체크하여 스위치 입력시 win() 함수 실행


def switch():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    val = 0
    try:
        while 1:
            val = GPIO.input(switch_pin)
            if(val == 1):
                win()
                break

    finally:
        GPIO.cleanup()


# 사망시 실행되는 함수, dead.wav를 재생하고 종료
def dead():
    global asd
    asd = 0
    play('dead.wav')
    ThisSystem = psutil.Process(current_system_pid)
    ThisSystem.terminate()

# 우승시 실행되는 함수, win.wav를 재생하고 종료


def win():
    global asd
    asd = 0
    play('win.wav')
    ThisSystem = psutil.Process(current_system_pid)
    ThisSystem.terminate()

# 음악을 재생후 고개를 돌리는 함수, 움직일 경우 dead() 함수를 통해 사망처리


def playAndTurn(name):
    global isPlaying, isWatching, alive

    if(alive == True):

        play(name)
        servo(servoPin, 4.5, 0.5)

        led(RED, YELLOW)
        time.sleep(2)
        isWatching = True
        # 고개를 돌리고 2초후 움직임 감지시 isMoving의 값에 따라 dead() 함수 실행
        if isMoving == 1:
            dead()
        time.sleep(1.3)

        servo(servoPin, 12.5, 0.5)

        led(YELLOW, RED)
        isWatching = False

        isPlaying = False
    else:
        dead()


thresh = 50
max_diff = 5
a, b, c = None, None, None

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)


# 움직임을 감시하는 함수, 프레임의 비교를 통해 움직임을 감지한다.
def motionThread():
    global isMoving
    if cap.isOpened():
        ret, a = cap.read()
        ret, b = cap.read()
        while ret:
            ret, c = cap.read()
            draw = c.copy()
            if not ret:
                break

            a_gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
            b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
            c_gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)

            diff1 = cv2.absdiff(a_gray, b_gray)
            diff2 = cv2.absdiff(b_gray, c_gray)

            ret, diff1_t = cv2.threshold(diff1, thresh, 255, cv2.THRESH_BINARY)
            ret, diff2_t = cv2.threshold(diff2, thresh, 255, cv2.THRESH_BINARY)

            diff = cv2.bitwise_and(diff1_t, diff2_t)

            k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
            diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

            diff_cnt = cv2.countNonZero(diff)
            if diff_cnt > max_diff:
                nzero = np.nonzero(diff)
                cv2.rectangle(draw, (min(nzero[1]), min(nzero[0])),
                              (max(nzero[1]), max(nzero[0])), (0, 255, 0), 2)

                isMoving = 1

            else:
                isMoving = 0
            stacked = np.hstack((draw, cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)))
            cv2.imshow('motion', stacked)

            a = b
            b = c

            if cv2.waitKey(1) & 0xFF == 27:
                break


bw = False

# LED를 제어하는 함수, led(킬 전등, 끌 전등)


def led(pin, pin2):
    GPIO.cleanup(pin)
    GPIO.cleanup(pin2)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)

    GPIO.output(pin2, False)
    GPIO.output(pin, True)


# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c, reset=RESET_PIN)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 45)


# 남은 시간을 OLED에 표시해주는 함수
def timer():
    global timeLeft, alive
    while True:
        if(timeLeft == -1):
            alive = False
            break
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        if(timeLeft < 10):
            ti = '00:0' + str(timeLeft)
        else:
            ti = '00:' + str(timeLeft)
        draw.text((0, 0), ti, font=font, fill=255)
        time.sleep(1)
        timeLeft -= 1
        oled.image(image)
        oled.show()


# 게임 실행의 흐름을 제어하는 함수
def mugung():
    while True:
        playAndTurn('mugung.wav')


time.sleep(2)
# 고개를 뒤로 돌린체 시작한다.
servo(servoPin, 12.5, 0.5)

# 쓰레드 시작
t1 = threading.Thread(target=timer)
t4 = threading.Thread(target=switch)
t2 = threading.Thread(target=motionThread)
t3 = threading.Thread(target=mugung)

t1.start()
t4.start()
t2.start()
t3.start()
