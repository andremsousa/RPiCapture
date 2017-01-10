# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys, os
import Adafruit_CharLCD as LCD

#Definir PIN
lcd_rs	= 27
lcd_en	= 22
lcd_d4 	= 25
lcd_d5	= 24
lcd_d6	= 23
lcd_d7 	= 18
lcd_backlight = 4
#tipo de lcd
lcd_columns = 16
lcd_rows = 2

#iniciar LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
			   lcd_columns, lcd_rows, lcd_backlight)


powerbutton = 9
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(powerbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
#	GPIO.wait_for_edge(powerbutton, GPIO.FALLING)
	print "Antes do while"
	try:
	    while True:
        # this will run until button attached to 24 is pressed, then 
        # if pressed long, shut program, if pressed very long shutdown Pi
        # stop recording and shutdown gracefully
        	lcd.clear()
		msg = '*'
		print "Waiting for button press" # rising edge on port 24"
	        GPIO.wait_for_edge(powerbutton, GPIO.RISING)
        	print "Stop button pressed"
	       # stop_recording()

        # poll GPIO 24 button at 20 Hz continuously for 3 seconds
        # if at the end of that time button is still pressed, shut down
        # if it's released at all, break
        	for i in range(30):
            		if not GPIO.input(powerbutton):
                		break
	       		time.sleep(0.05)
			print "Valor do I=",i
			istring = str(i)
			lcd.clear()
			lcd.message('Vai tirar foto'+istring)
			
				
				

#  		if 25 <= i < 58:              # if released between 1.25 & 3s close prog
#           		 print "Closing program"
#			 lcd.clear()
#			 lcd.message('Closing \nprogram')			
#		         flash(0.02,50) # interval,reps
            	        #sys.exit()

	        if GPIO.input(powerbutton):
        	    if i >= 29:
 #               	shutdown()
			lcd.clear()
			lcd.blink(True)
			lcd.message('Snapshot')
			print "Snapshot?"
			time.sleep(5.0)
			lcd.blink(False)
			snapShot()	

	except KeyboardInterrupt:
		GPIO.cleanup()
		print "Done!"
	


def snapShot():
	lcd.clear()
	GPIO.cleanup()
	print "Vai tirar foto"
	os.system('cd')
	os.system('./webcam.sh')
	print "Já tirou"
	lcd.message('Done!')
if True:
	main()
