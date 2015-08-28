Raspberry Pi Lcd Menu
==============

เนื่องจาก LIB ที่หาได้ทั้งหลาย ยังไม่ค่อยโดนใจ

- ตัว `Adafruit_Python_CharLCD` สร้าง menu ยากมากกกกก

- ตัว `adafruit_lcd_plate_menu` เขียนดี
แต่ เมนูออกแบบให้ซับซ้อนๆ ยาก .. คนเอาไปใช้ต้องรู้ python พอสมควร
(.. ยิ่งวาด menu เยอะ ยิ่งเมนูซับซ้อน ยิ่งออกแบบลำบาก)

- ตัว `RaspberryPiLcdMenu` เขียนเรียบง่ายดี
โครงสร้างเป็น XML ทำให้ คนนำไปใช้ไม่ต้องรู้ code เยอะ
ก็สร้าง menu ใช้เองได้ ... แต่ดันไม่ update ใช้กับ LCD ที่มีไม่ได้
(ของผมไม่ได้ใช้ MCP230XX)

สรุปก็เลยต้องโมเอง แต่คิดว่า ใช้งานง่ายขึ้นเยอะ
แยกเป็น playload ให้ เขียนค่อยอดได้ง่ายขึ้น
(ตัวแปร LCD กะ lcd จะ base on Adafruit_CharLCDPlate)


base on
=====
- `https://github.com/aufder/RaspberryPiLcdMenu`
- `https://github.com/rodrigodiez/adafruit_lcd_plate_menu`
- `https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code`
- `https://github.com/adafruit/Adafruit_Python_CharLCD`

Vdo ตัวอย่าง
========
- `https://www.youtube.com/watch?v=oN0il4XK2gQ`