from lcd import drivers
import time
import datetime
import threading
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 26
display = drivers.Lcd()
now = datetime.datetime.now()
discomfortIndex = ''
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
            discomfortIndex = ('%.1f*C, %.1f%%' %(temperature,humidity))
        else:
            print("read error")

        # 4초마다 센서로부터 값을 가져오도록 설정
        time.sleep(2)
t = threading.Thread(target=getDiscom)
t.start()
try:
    print('Writing to Display')
    display.lcd_display_string("Hello, World!!",1)
    while True:
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x %X").replace(" ",""),1)
        time.sleep(0.5)
        display.lcd_display_string(discomfortIndex,2)
        time.sleep(0.5)


        

    
finally:
    print("cleaning up")
    display.lcd_clear()