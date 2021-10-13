import time


sensor = Adafruit_DHT.DHT11
DHT_PIN = 17

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor,DHT_PIN)
        if humidity is not None and temperature is not None:
            # 1.8 × 온도 - 0.55 (1 - 습도) (1.8 × 온도 - 26) + 32
            print('Temperature=%.1f* Humidity=%.1f%%' %(temperature,humidity))
            T = temperature
            R = humidity * 0.01

            a = 9/5 * T - 0.55 * (1 - R) * ( 9/5 * T - 26 ) + 32
            print("%.1f" % a)
        else:
            print('Read Error')
finally:
    print('bye') 