#Libraries
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#start programming
GPIO.setup(21,GPIO.OUT)

for i in range(10):
    GPIO.output(21,GPIO.HIGH)
    print ("LED on")
    time.sleep(1)
    GPIO.output(21,GPIO.LOW)
    print("LED off")
    time.sleep(1)
    print (i)

GPIO.cleanup()
os.system('clear')

#end of programming