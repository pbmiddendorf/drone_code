import pigpio #allows nice PWM output on almost any pin, incl hardware pwm if necessary
from time import sleep
testPWMPin = 4 #this is physical pin 7, gpio pins are designated by their BCM number
outputPulseWidth = 1000 #1000 is the minimum, ie not moving
pi = pigpio.pi() #opens the local pi 
pi.set_mode(testPWMPin, pigpio.OUTPUT) #each pin has to be explicitly set to the right mode
pi.set_servo_pulsewidth(testPWMPin, outputPulseWidth) #sends the command to the esc over the designated pin

for i in range(1, 200):
    outputPulseWidth = outputPulseWidth + 1
    pi.set_servo_pulsewidth(testPWMPin, outputPulseWidth)
    sleep(0.1)

for i in range(1, 200):
    outputPulseWidth = outputPulseWidth - 1
    pi.set_servo_pulsewidth(testPWMPin, outputPulseWidth)
    sleep(0.1)

pi.stop()
