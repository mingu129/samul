import RPi.GPIO as GPIO
import time
# 온습도 센서 사용을 위해 import
import Adafruit_DHT

# 쓰레드 사용을 위해 import
import threading

# 4-digit의 핀번호
SEGMENT_PINS = [3, 21, 8, 6, 5, 2, 9] #2,3,4,5,6,7,8
DIGIT_PINS = [4, 16, 20, 10] #4,11,12,13

# LED의 핀번호
LIGHT_PINS = [13, 19, 26]
t = None
sensor = Adafruit_DHT.DHT11
DHT_PIN = 17

# 불쾌지수 값 초기화
discomfortIndex = "00"
GPIO.setmode(GPIO.BCM)

for light in LIGHT_PINS:
    GPIO.setup(light, GPIO.OUT)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)


for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)
    

data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

# 온습도 센서로부터 온도와 습도를 읽어오고 그 값을 통해 불쾌지수를 discomfortIndex 에 저장하는 함수
def getDiscom():

    # discomfortIndex(불쾌지수 변수)
    global discomfortIndex

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor,DHT_PIN)
        if humidity is not None and temperature is not None:

            # 1.8 × 온도 - 0.55 (1 - 습도) (1.8 × 온도 - 26) + 32 = 불쾌지수
            T = temperature
            R = humidity * 0.01
            
            # 구한 불쾌지수를 변수에 저장
            discomfortIndex = str(9/5 * T - 0.55 * (1 - R) * ( 9/5 * T - 26 ) + 32)
        else:
            print("read error")

        # 4초마다 센서로부터 값을 가져오도록 설정
        time.sleep(4)

# 불쾌지수에 따라 다른 LED가 켜지도록 하는 함수
def ledByDiscom():  
    global discomfortIndex
   
    while True:
        # 불쾌지수는 소수점을 제외한 값만으로 계산
        discomIndex2 = int(discomfortIndex[0:2])
        print("현재 불쾌지수 : " + str(discomIndex2))

        # 불쾌지수가 80 이상일시 빨간색 LED에 불이 켜지게 함
        if discomIndex2 >= 80:
            GPIO.output(LIGHT_PINS[0], GPIO.LOW)
            GPIO.output(LIGHT_PINS[1], GPIO.LOW)
            GPIO.output(LIGHT_PINS[2], GPIO.HIGH)

        # 불쾌지수가 80 미만, 68 이상 일시 노란색 LED에 불이 켜지게 함
        elif discomIndex2 < 80 and discomIndex2 >= 68:
            GPIO.output(LIGHT_PINS[0], GPIO.LOW)
            GPIO.output(LIGHT_PINS[1], GPIO.HIGH)
            GPIO.output(LIGHT_PINS[2], GPIO.LOW)
        
        # 불쾌지수가 68 미만 일시 파란색 LED에 불이 켜지게 함
        else:
            GPIO.output(LIGHT_PINS[0], GPIO.HIGH)
            GPIO.output(LIGHT_PINS[1], GPIO.LOW)
            GPIO.output(LIGHT_PINS[2], GPIO.LOW)

        # 4초마다 이 과정을 수행하게 함
        time.sleep(4)
    
        
# 4-digit에 숫자를 디스플레이하게 하는 함수
def display(digit, number): 
    for i in range(4):
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)
    for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.001)
        
    

# 불쾌지수를 저장하는 getDiscom 함수를 실행하는 쓰레드 생성, start
t = threading.Thread(target=getDiscom)
t.start()

# 불쾌지수의 값에 따라 다른 LED의 불이 켜지게하는 ledByDiscom 함수를 실행하는 쓰레드 생성, start
t2 = threading.Thread(target=ledByDiscom)
t2.start()

try:
    # 무한반복하며 불쾌지수를 4-digit에 디스플레이 한다.
    while True:
        display(1,int(discomfortIndex[0]))
        display(2,int(discomfortIndex[1:2]))
        
# 최종적으로 cleanup 함수를 실행후 bye 출력
finally:
    GPIO.cleanup()
    print('bye')

