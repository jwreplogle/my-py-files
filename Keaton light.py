
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
#start programming

while 1==1:

    print('Enter 1 to turn light on')
    print('Any other key will turn it off')
    x = input()
    if x == "y":
        GPIO.output(16,GPIO.HIGH)
    else:
        GPIO.output(16,GPIO.LOW)



#end of programming