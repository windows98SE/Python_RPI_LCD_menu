#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
import os
import psutil
import commands
from string import split
from datetime import datetime, timedelta
from time import sleep, strftime, localtime

import Adafruit_CharLCD as LCD

# payload
def showDateTime(lcd):
  lcd.clear()
  while not(lcd.is_pressed(LCD.LEFT)):
    sleep(0.25)
    lcd.home()
    lcd.message(strftime('%a %b %d %Y\n%I:%M:%S %p', localtime()))
  lcd.clear()

def showRam(lcd):
  lcd.clear()
  values = psutil.virtual_memory()

  total = values.total >> 20
  free = values.free >> 20

  lcd.message("Total:%sMB\nFree: %sMB" % (total, free))
  sleep(3)

def showVersion(lcd):
  lcd.clear()
  logo = '[ StepHack.C\x02m ]'
  version = 'V.1.0.0'
  lcd.message(("%s\n%s" % (logo, version.rjust(16))))
  sleep(3)

def showDescription(lcd):
  title = "License :"
  msg = "The GNU General Public License is a free, copyleft license for software and other kinds of works."
  scroll_msg(lcd, title, msg)

def LcdRed(lcd):
  lcd.set_color(1,0,0)

def LcdBlue(lcd):
  lcd.set_color(0,1,0)

def LcdGreen(lcd):
  lcd.set_color(0,0,1)

def LcdOff(lcd):
  lcd.set_color(0,0,0)

def DoShutdown(lcd):
  DoQuit(lcd, "sudo shutdown -h now")

def DoReboot(lcd):
  DoQuit(lcd, "sudo reboot")

def DoQuit(lcd, cmd=None):
  lcd.clear()
  lcd.message("Are you sure?\nPress Sel for Y")
  while 1:
    if lcd.is_pressed(LCD.LEFT):
      break
    if lcd.is_pressed(LCD.SELECT):
      lcd.clear()
      lcd.set_backlight(False)
      lcd.set_color(0,0,0)
      if cmd is not None: commands.getoutput(cmd)
      quit()
    sleep(0.25)

def scroll_msg(lcd, title, msg):
  len_msg = len(msg) - (15)
  for i in range(len_msg):
    if lcd.is_pressed(LCD.LEFT):
      break
    lcd.clear()
    lcd.message(("%s\n" % title))
    lcd.message(("%s" % msg[i:i+16]))
    sleep(0.3)
