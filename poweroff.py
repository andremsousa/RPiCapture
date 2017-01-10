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

def update_progress(progress):
    barLength = 16 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    textlcd = "A desligar\n{0}".format ( "#"*block + " "*(barLength-block))
    lcd.message(textlcd)
    sys.stdout.write(text)
    sys.stdout.flush()	

def main():
#	GPIO.wait_for_edge(powerbutton, GPIO.FALLING)
	print "Antes do while"
	
	try:
	    while True:
        # this will run until button attached to 24 is pressed, then 
        # if pressed long, shut program, if pressed very long shutdown Pi
        # stop recording and shutdown gracefully
        	
		
		
		lcd.clear()
		print "Waiting for button press" # rising edge on port 24"
	        GPIO.wait_for_edge(powerbutton, GPIO.RISING)
        	print "Stop button pressed"
	       # stop_recording()

        # poll GPIO 24 button at 20 Hz continuously for 3 seconds
        # if at the end of that time button is still pressed, shut down
        # if it's released at all, break
		print ""
		print "progress : 0->1"
        	for i in range(21):
            		if not GPIO.input(powerbutton):
                		break
	       		time.sleep(0.1)
			update_progress(i/20.0)
			
#			string = str(i)
#			lcd.message('Vai desligar')			
				
				

#  		if 25 <= i < 58:              # if released between 1.25 & 3s close prog
#           		 print "Closing program"
#			 lcd.clear()
#			 lcd.message('Closing \nprogram')			
#		         flash(0.02,50) # interval,reps
            	        #sys.exit()

	        if GPIO.input(powerbutton):
        	    if i >= 19 :
                        lcd.clear()
			lcd.blink(True)
			lcd.message('Vai desligar')
			print "Vai desligar"
			time.sleep(5.0)
			lcd.blink(False)
			shutdown()	

	except KeyboardInterrupt:
		lcd.message('Cleaning LCD')
		time.sleep(2.0)
		lcd.clear()
		GPIO.cleanup()
		print "Done!"
	


def shutdown():
	lcd.clear()
	lcd.message('A desligar')
	GPIO.cleanup()
	print "A desligar"
	os.system('sudo shutdown -h now')
	lcd.message('Done!')
if True:
	main()
