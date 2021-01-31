from gpiozero import Button
from gpiozero import LED 
from picamera import PiCamera
from datetime import datetime
from signal import pause
from time import sleep

button1 = Button(2)
button2 = Button(3)
led = LED(14)
camera = PiCamera()

# the following function flashes an LED and takes a picture
def picture():
    timestamp = datetime.now().isoformat()
    print("Picture")
    led.on()
    camera.capture('/home/pi/Documents/Programs/Lab 6/%s.jpg' % timestamp)
    led.off()#set tje GPIO 17 to low
    sleep(1)
        

#button1.when_pressed = picture
button1.when_pressed = picture
#led.on() #set the GPIO 17 to high

#the following function Records a video, the LED will turn on and stay on until the recording ends
def video():
    timestamp = datetime.now().isoformat()
    camera.resolution = (640,480)
    print("Video")
    led.on()
    camera.start_recording('/home/pi/Documents/Programs/Lab 6/%s.h264' % timestamp)
    camera.wait_recording(5)
    camera.stop_recording()
    led.off()#set tje GPIO 17 to low
    sleep(1)
        
    
    ##print("recording stopped")
    
    
#button2.when_pressed = video

button2.when_pressed = video


pause()

# camera.start_preview()
# sleep(5)
# camera.capture('/home/pi/Desktop/image.jpg')
# camera.stop_preview()