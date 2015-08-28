#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from Class import *

run = createMenu()

display = Display(run.menu)
display.display()

while True:
  try:
    if (lcd.is_pressed(LCD.LEFT)):
      display.update('l')
      display.display()
      sleep(0.25)

    elif (lcd.is_pressed(LCD.UP)):
      display.update('u')
      display.display()
      sleep(0.25)

    elif (lcd.is_pressed(LCD.DOWN)):
      display.update('d')
      display.display()
      sleep(0.25)

    elif (lcd.is_pressed(LCD.RIGHT)):
      display.update('r')
      display.display()
      sleep(0.25)

    elif (lcd.is_pressed(LCD.SELECT)):
      display.update('s')
      display.display()
      sleep(0.25)


  except KeyboardInterrupt, SystemExit:
    lcd.clear()
    lcd.set_backlight(False)
    lcd.set_color(0,0,0)
    raise