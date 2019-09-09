 #import
import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk


GPIO.setwarnings(False) 
# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
LED_ON = 15
 
# Define some device constants
LCD_WIDTH = 20    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7
GPIO.setup(LED_ON, GPIO.OUT) # Backlight enable


 
def lcd_init():
  # Initialise display
    lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
    lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
    time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
    GPIO.output(LCD_RS, mode) # RS

    # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x10==0x10:
        GPIO.output(LCD_D4, True)
    if bits&0x20==0x20:
        GPIO.output(LCD_D5, True)
    if bits&0x40==0x40:
        GPIO.output(LCD_D6, True)
    if bits&0x80==0x80:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    lcd_toggle_enable()

    # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x01==0x01:
        GPIO.output(LCD_D4, True)
    if bits&0x02==0x02:
        GPIO.output(LCD_D5, True)
    if bits&0x04==0x04:
        GPIO.output(LCD_D6, True)
    if bits&0x08==0x08:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)
 
def lcd_string(message,line,style):
  # Send string to display
  # style=1 Left justified
  # style=2 Centred
  # style=3 Right justified
 
    if style==1:
        message = message.ljust(LCD_WIDTH," ")
    elif style==2:
        message = message.center(LCD_WIDTH," ")
    elif style==3:
        message = message.rjust(LCD_WIDTH," ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)
 
def lcd_backlight(flag):
  # Toggle backlight on-off-on
    GPIO.output(LED_ON, flag)


def main():
  # Initialise display
    lcd_init()
 
  # Toggle backlight on-off-on
    lcd_backlight(True)
    time.sleep(0.5)
    lcd_backlight(False)
    time.sleep(0.5)
    lcd_backlight(True)
    time.sleep(0.5)
# tkinter entry
    master = tk.Tk()
#set c1-c4 to string variables
    c1=StringVar()
    c2=StringVar()
    c3=StringVar()
    c4=StringVar()
# set the default values of c1-c4 to 1 from the drop down list
    c1.set(1)
    c2.set(1)
    c3.set(1)
    c4.set(1)
#cdata is the data that is listed in the combo box drop down
    cdata=("1", "2", "3")

    master.title("Text for 4 x 20")
    tk.Label(master, text="Enter Text To Display on LED; 1-Left 2-Center 3-Right", fg='red').grid(row=0)
#ComboBox 4 each    
    cb1=ttk.Combobox(master, textvariable=c1, values=cdata, width=3).grid(row=1, column=0)
    cb2=ttk.Combobox(master, textvariable=c2, values=cdata, width=3).grid(row=2, column=0)
    cb3=ttk.Combobox(master, textvariable=c3, values=cdata, width=3).grid(row=3, column=0)
    cb4=ttk.Combobox(master, textvariable=c4, values=cdata, width=3).grid(row=4, column=0)
#Labels 4 each   
    tk.Label(master, text="Display Line 1", width=15).grid(row=1, column=1)
    tk.Label(master, text="Display Line 2", width=15).grid(row=2, column=1)
    tk.Label(master, text="Display Line 3", width=15).grid(row=3, column=1)
    tk.Label(master, text="Display Line 4", width=15).grid(row=4, column=1)
#data entry for 4 lines
    e1 = tk.Entry(master, width=20)
    e2 = tk.Entry(master, width=20)
    e3 = tk.Entry(master, width=20)
    e4 = tk.Entry(master, width=20)
#setting the locations of data entry
    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    e3.grid(row=3, column=2)
    e4.grid(row=4, column=2)
    
#function to close the master window    
    def clall():
        master.destroy()
#function to set dtrings and intergers, print them to console, and push string to display
    def stext():
        line1 = str(e1.get())
        line2 = str(e2.get())
        line3 = str(e3.get())
        line4 = str(e4.get())
        cc1 = int(c1.get())
        cc2 = int(c2.get())
        cc3 = int(c3.get())
        cc4 = int(c4.get())
        print("cb1= ", cc1)
        print("cb2= ", cc2)
        print("cb3= ", cc3)
        print("cb4= ", cc4)
        print ("Line 1 = ", line1)
        print ("Line 2 = ", line2)
        print ("Line 3 = ", line3)
        print ("Line 4 = ", line4)
    # Send text to display
        lcd_string(line1,LCD_LINE_1,cc1)
        lcd_string(line2,LCD_LINE_2,cc2)
        lcd_string(line3,LCD_LINE_3,cc3)
        lcd_string(line4,LCD_LINE_4,cc4)
#commands to either kill the window or goto stext function
    tk.Button(master, text='Quit', command=clall).grid(row=5, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Show', command=stext).grid(row=5, column=2, sticky=tk.W, pady=4)

    tk.mainloop()


if __name__ == '__main__':
 
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)
        lcd_string("Goodbye!",LCD_LINE_1,2)
        GPIO.cleanup()
