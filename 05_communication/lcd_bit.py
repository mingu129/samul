from requests.api import patch
from lcd import drivers
import time
import requests
from bs4 import BeautifulSoup
import threading
import json
display = drivers.Lcd()
sisae= ""
url = "https://crix-api-endpoint.upbit.com/v1/crix/candles/days/?code=CRIX.UPBIT.KRW-BTC"

def getBit():
    global sisae
    while True:
        response = requests.get(url)
        html = response.text
        ht = html[1:len(html)-1]
        result = json.loads(ht)
        sisae = str(format(int(result["tradePrice"]), ',')) + "W"
        time.sleep(0.5)


        

t = threading.Thread(target=getBit)
t.start()

try:
    display.lcd_display_string("Bitcoin Price",1)
    while True:      
        display.lcd_display_string(sisae,2)
        time.sleep(0.5)

        

    
finally:
    print("cleaning up")
    display.lcd_clear()