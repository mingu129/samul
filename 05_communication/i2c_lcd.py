from lcd import drivers
import time
display = drivers.Lcd()


i = 0
try:
    print('Writing to Display')
    display.lcd_display_string("Hello, World!!",1)
    while True:
        display.lcd_display_string("** WELCOME **",2)
        time.sleep(0.002)
        display.lcd_display_string("   WELCOME   ",2)
        time.sleep(0.002)

        

    
finally:
    print("cleaning up")
    display.lcd_clear()