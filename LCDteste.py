
#!/bin/python
# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh

import RPi.GPIO as GPIO
import time
import os
import Adafruit_CharLCD as LCD


lcd_rs = 27
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows)


# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Our function on what to do when the button is pressed
GPIO.add_event_detect(4,GPIO.BOTH)


while True:      
	time.sleep(1)






