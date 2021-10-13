import time
import picamera

path = "/home/pi/src5/06_multi_media"
camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)
    while True:
        s = int(input("photo: 1, video: 2, exit: 9"))
        now_str = time.strftime("%Y%m%d_%H%M%S")
        if s == 1:
            camera.capture('%s/%s.jpg' % (path, now_str))
        elif s == 2:
            camera.start_recording('%s/%s.h264' % (path, now_str))
            s = input("press enter to stop")
            camera.stop_recording
        elif s == 9:
            break
        else:
            print("wrong command")  

    

finally:
    camera.stop_preview()

