#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#

from xml.dom.minidom import *
import Adafruit_CharLCD as LCD

from Class.payload import *

DISPLAY_ROWS = 2
DISPLAY_COLS = 16

# lcd init
lcd = LCD.Adafruit_CharLCDPlate()
# create spacial char
lcd.create_char(0, [0,8,12,14,12,8,0,0])         # RIGHT Arrow
lcd.create_char(1, [0,2,6,14,6,2,0,0])           # LEFT Arrow

lcd.create_char(2, [0,0,10,21,17,10,4,0])        # HEART
lcd.create_char(3, [0,0,10,31,31,14,4,0])        # HEART BOLD

lcd.create_char(4, [0,31,17,21,17,31,0,0])       # ON
lcd.create_char(5, [0,31,17,17,17,31,0,0])       # OFF

lcd.create_char(6, [0,27,14,4,14,27,0,0])        # X
lcd.create_char(7, [0,1,3,22,28,8,0,0])          # T

lcd.set_color(0.0, 0.0, 0.0)

class Widget:
  def __init__(self, myName, myFunction):
    self.text = myName
    self.function = myFunction

class Folder:
  def __init__(self, myName, myParent):
    self.text = myName
    self.items = []
    self.parent = myParent

class CommandToRun:
  def __init__(self, myName, theCommand):
    self.text = myName
    self.commandToRun = theCommand

  def Run(self):
    self.clist = split(commands.getoutput(self.commandToRun), '\n')
    if len(self.clist) > 0:
      lcd.clear()
      lines = len(self.clist)
      btmDown = 0
      for line in range(lines):
        if btmDown == 1:
          btmDown = 0
          continue
        len_msg = len(self.clist[line]) - (15)
        for i in range(len_msg):
          lcd.clear()
          lcd.message(("%s\n" % self.commandToRun))
          lcd.message(("%s" % self.clist[line][i:i+16]))
          # stop scrolling &% go next line
          if lcd.is_pressed(LCD.DOWN):
            btmDown = 1
            break
          sleep(0.3)
    sleep(2)

class createMenu:
  def __init__(self):
    self.blink = False
    self.backlight = False

    lcd.blink(self.blink)
    lcd.set_backlight(self.backlight)

    self.menu = Folder('root','')

    # load config
    self.xmlfile = 'menu.xml'
    self.xml = self._loadConfig(self.xmlfile)

  def _loadConfig(self, var=None):
    if var is None: var = self.xmlfile
    dom = parse(var)
    xml = dom.documentElement
    self.ProcessNode(xml, self.menu)
    return xml

  def ProcessNode(self, currentNode, currentItem):
    children = currentNode.childNodes
    for child in children:
      if isinstance(child, xml.dom.minidom.Element):
        if child.tagName == 'folder':
          thisFolder = Folder(child.getAttribute('text'), currentItem)
          currentItem.items.append(thisFolder)
          self.ProcessNode(child, thisFolder)
        elif child.tagName == 'widget':
          thisWidget = Widget(child.getAttribute('text'), child.getAttribute('function'))
          currentItem.items.append(thisWidget)
        elif child.tagName == 'run':
          thisCommand = CommandToRun(child.getAttribute('text'), child.firstChild.data)
          currentItem.items.append(thisCommand)

class Display:
  def __init__(self, folder):
    self.curFolder = folder
    self.curTopItem = 0
    self.curSelectedItem = 0

  def display(self):
    if self.curTopItem > len(self.curFolder.items) - DISPLAY_ROWS:
      self.curTopItem = len(self.curFolder.items) - DISPLAY_ROWS
    if self.curTopItem < 0: self.curTopItem = 0
    str = ''
    for row in range(self.curTopItem, self.curTopItem+DISPLAY_ROWS):
      if row > self.curTopItem: str += '\n'
      if row < len(self.curFolder.items):
        if row == self.curSelectedItem:
          cmd = '\x00'+self.curFolder.items[row].text
          if len(cmd) < 16:
            for row in range(len(cmd), 16): cmd += ' '

          str += cmd
        else:
          cmd = ' ' + self.curFolder.items[row].text
          if len(cmd) < 16:
            for row in range(len(cmd), 16): cmd += ' '

          str += cmd
    lcd.home()
    lcd.message(str)

  def update(self, command):
    if command == 'u': self.up()
    elif command == 'd': self.down()
    elif command == 'r': self.right()
    elif command == 'l': self.left()
    elif command == 's': self.select()

  def up(self):
    if self.curSelectedItem == 0: return
    elif self.curSelectedItem > self.curTopItem: self.curSelectedItem -= 1
    else:
      self.curTopItem -= 1
      self.curSelectedItem -= 1

  def down(self):
    if self.curSelectedItem+1 == len(self.curFolder.items): return
    elif self.curSelectedItem < self.curTopItem+DISPLAY_ROWS-1: self.curSelectedItem += 1
    else:
      self.curTopItem += 1
      self.curSelectedItem += 1

  def left(self):
    if isinstance(self.curFolder.parent, Folder):
      # find the current in the parent
      itemno = 0
      index = 0
      for item in self.curFolder.parent.items:
        if self.curFolder == item: index = itemno
        else: itemno += 1
      if index < len(self.curFolder.parent.items):
        self.curFolder = self.curFolder.parent
        self.curTopItem = index
        self.curSelectedItem = index
      else:
        self.curFolder = self.curFolder.parent
        self.curTopItem = 0
        self.curSelectedItem = 0

  def right(self):
    if isinstance(self.curFolder.items[self.curSelectedItem], Folder):
      self.curFolder = self.curFolder.items[self.curSelectedItem]
      self.curTopItem = 0
      self.curSelectedItem = 0
    elif isinstance(self.curFolder.items[self.curSelectedItem], Widget):
      eval(self.curFolder.items[self.curSelectedItem].function + '(lcd)')
    elif isinstance(self.curFolder.items[self.curSelectedItem], CommandToRun):
      self.curFolder.items[self.curSelectedItem].Run()

  def select(self):
    if isinstance(self.curFolder.items[self.curSelectedItem], Widget):
      eval(self.curFolder.items[self.curSelectedItem].function + '(lcd)')
    elif isinstance(self.curFolder.items[self.curSelectedItem], CommandToRun):
      self.curFolder.items[self.curSelectedItem].Run()
