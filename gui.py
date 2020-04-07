from tkinter import *
import RPi.GPIO as GPIO

# setup
GPIO.setmode(GPIO.BCM)

redLed = 10
blueLed = 3
greenLed = 26

GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(blueLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)


GPIO.output(redLed, GPIO.LOW)
GPIO.output(blueLed, GPIO.LOW)
GPIO.output(greenLed, GPIO.LOW)

# GUI definitions
win = Tk()
win.title("LED Toggler")

# event function
def red():
    GPIO.output(redLed, GPIO.HIGH)
    GPIO.output(blueLed, GPIO.LOW)
    GPIO.output(greenLed, GPIO.LOW)

def blue():
    GPIO.output(redLed, GPIO.LOW)
    GPIO.output(blueLed, GPIO.HIGH)
    GPIO.output(greenLed, GPIO.LOW)
    
def green():
    GPIO.output(redLed, GPIO.LOW)
    GPIO.output(blueLed, GPIO.LOW)
    GPIO.output(greenLed, GPIO.HIGH)
    
def close():
    win.destroy()
    GPIO.cleanup()

# Widgets
redButton = Radiobutton(win, text = "Toggle red", command = red)
redButton.grid(row = 0, column = 0)

blueButton = Radiobutton(win, text = "Toggle blue", command = blue)
blueButton.grid(row = 2, column = 0)

greenButton = Radiobutton(win, text = "Toggle green", command = green)
greenButton.grid(row = 4, column = 0)

exitButton = Button(win, text = "Exit", command = close)
exitButton.grid(row = 6, column = 0)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()