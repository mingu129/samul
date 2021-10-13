import time
import picamera

path = "/home/pi/src5/06_multi_media"
camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)
    camera.capture('%s/photo.jpg' % path)

finally:
    camera.stop_preview()

