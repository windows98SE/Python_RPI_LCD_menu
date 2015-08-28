#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 
import os
import psutil
import commands
from time import sleep, strftime, localtime

import Adafruit_CharLCD as LCD

DEBUG = 1

# payload 
def showDateTime(lcd):
  if DEBUG:
    print('in showDateTime')
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
  if DEBUG:
    print('in showVersion')
  lcd.clear()
  logo = '[ StepHack.C\x02m ]'
  version = 'V.1.0.0'
  lcd.message(("%s\n%s" % (logo, version.rjust(16))))
  sleep(3)

def showDescription(lcd):
  if DEBUG:
    print('in showDescription')

  title = 'License :'
  License = 'The GNU General Public License is a free, copyleft license for software and other kinds of works.'
  len_msg = len(License) - (15)
  for i in range(len_msg):
    if lcd.is_pressed(LCD.LEFT):
      break
    lcd.clear()
    lcd.message(("%s\n" % title))
    lcd.message(("%s" % License[i:i+16]))
    sleep(0.3)

def LcdRed(lcd):
  lcd.set_color(1,0,0)

def LcdBlue(lcd):
  lcd.set_color(0,1,0)

def LcdGreen(lcd):
  lcd.set_color(0,0,1)

def LcdOff(lcd):
  lcd.set_color(0,0,0)

def DoShutdown(lcd):
  lcd.clear()
  lcd.message('Are you sure?\nPress Sel for Y')
  while 1:
    if lcd.is_pressed(LCD.LEFT):
      break
    if lcd.is_pressed(LCD.SELECT):
      lcd.clear()
      lcd.set_backlight(False)
      lcd.set_color(0,0,0)
      commands.getoutput("sudo shutdown -h now")
      quit()
    sleep(0.25)

def DoReboot(lcd):
  lcd.clear()
  lcd.message('Are you sure?\nPress Sel for Y')
  while 1:
    if lcd.is_pressed(LCD.LEFT):
      break
    if lcd.is_pressed(LCD.SELECT):
      lcd.clear()
      lcd.set_backlight(False)
      lcd.set_color(0,0,0)
      commands.getoutput("sudo reboot")
      quit()
    sleep(0.25)

def DoQuit(lcd):
  lcd.clear()
  lcd.message('Are you sure?\nPress Sel for Y')
  while 1:
    if lcd.is_pressed(LCD.LEFT):
      break
    if lcd.is_pressed(LCD.SELECT):
      lcd.clear()
      lcd.set_backlight(False)
      lcd.set_color(0,0,0)
      quit()
    sleep(0.25)
