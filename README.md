# Circuit-Python

## Table of Contents 
* [Classes and Modules]()
* [Fun with RGB]()

## Classes and Modules

Main Code:

import time
import board
from RGB import LED   # import the LED class from the RGB module

blueLEDPin = board.D10
redLEDPin = board.D8
greenLEDPin = board.D9

myBlueLED = LED(blueLEDPin)
myRedLED = LED(redLEDPin)
myGreenLED = LED(greenLEDPin)

while True:
    myBlueLED.fade()
    time.sleep(1)
    myGreenLED.fade()
    time.sleep(1)
    myRedLED.fade()
    time.sleep(1) 
    myYellowLED.fade()
    time.sleep(1)
    myCyanLED.fade()
    time.sleep(1)
    myMagentaLED.fade()
    time.sleep(1) 


Class Code:

import time
import board
import pwmio
import digitalio

lightBulb = digitalio.DigitalInOut(board.D13)       # I moved my RGBLED power wire from 5v
lightBulb.direction = digitalio.Direction.OUTPUT    # and plugged it into D13.  I'll explain later.

class LED:      # It's propper coding to always write a line explaining a class
                # with a "docstring."   Like this:
    '''LED is a class designed for a single color LED to fade in and out'''

    def __init__(self, ledpin, name):
        # init is like void Setup() from arduino.  Initialize your pins here
        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)
        self.name = name

    def fadedown(self): # Fades LED from bright to dim
        for i in range(255):
            if i < (255/2):
                self.led.duty_cycle = int(i * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def fadeup(self):  # Fades LED from dim to bright
        for i in range(255):
            if i > (255/2):
                self.led.duty_cycle = 65535 - int((i - (255/2)) * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def on(self, brightness=65535):  # Remember "on" means duty cycles < 65535
        self.led.duty_cycle = 65535 - brightness
        lightBulb.value = 65535


    def off(self): # "off" means the duty cycle should be full.
        self.led.duty_cycle = 65535



class RGB:
    '''this class should implement all 3 pins together to control an RGB LED'''
    from RGB import LED
        # Let's take a second to appreciate that we're using a class to call a class!
        # Let LED do all the nitty-gritty work, this RGB class will be the "manager"


    def __init__(self, redPin, greenPin, bluePin):
        # To initialize an RGB LED, we need to initialize 3 LED pins.
        self.myRedLED = LED(redPin, "red")
        self.myBlueLED = LED(bluePin, "blue")
        self.myGreenLED = LED(greenPin, "green")

    def blue(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.off()
        
    def red(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.on(brightness)

    def green(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.off()
        self.myGreenLED.on(brightness)
        self.myRedLED.off()

    def yellow(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.off()
        self.myGreenLED.on(brightness)
        self.myRedLED.on(brightness)


    def cyan(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.on(brightness)
        self.myRedLED.off()

    def magenta(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.on(brightness)

    def off(self):
        # This turns off all 3 LEDs, but my LEDs were still glowing a tiny bit.
        # To fix this, I took the RGB power wire out of 5V and plugged it into D13.
        # Now when I want the LED to be off, it's truly off!
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.off()
        lightBulb.value = 0


# Overview of assignment
The goal of this assignment is to get an RGB led to fade using classes. Overall I think the assignment was easy once I got the hang of it. I had a few problems with the code. Lines of code wouldn't correspond with the class.py or the main.py and the fade function never worked. In order to solve this problem, I asked around for help until Miriam helped solve the problem. 












## Fun with RGB

Main Code:

import time
import board
from rgb import RGB

r1 = board.D8
b1 = board.D9
g1 = board.D10
r2 = board.D4
b2 = board.D5
g2 = board.D7  # D6 uses the same timer as D8,9,10.  Avoid!

full = 65535  # Max Brightness
half = int(65535 / 2)  # Half Brightness

myRGBled1 = RGB(r1, g1, b1)  # create a new RGB object, using pins 8, 9, & 10
myRGBled2 = RGB(r2, g2, b2)  # create a new RGB object, using pins 4, 5, & 7


while True:

    #myRGBled1.Alternate(.2, 20000)
    #myRGBled2.Alternate(.2, 20000)
    #time.sleep(1)

    myRGBled1.Blinky(.2, 20000)
    myRGBled2.Blinky(.2, 20000)
    time.sleep(1)

    myRGBled1.blue(half)
    myRGBled2.yellow(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.red()
    myRGBled2.cyan()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.green()
    myRGBled2.magenta()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(1)

    myRGBled1.white(half)
    time.sleep(1)
    myRGBled1.off(half)
    time.sleep(1)

   
   
Class Code:   

import time
import board
import pwmio
import digitalio

lightBulb = digitalio.DigitalInOut(board.D13)       # I moved my RGBLED power wire from 5v
lightBulb.direction = digitalio.Direction.OUTPUT    # and plugged it into D13.  I'll explain later.

class LED:      # It's propper coding to always write a line explaining a class
                # with a "docstring."   Like this:
    '''LED is a class designed for a single color LED to fade in and out'''

    def __init__(self, ledpin, name):
        # init is like void Setup() from arduino.  Initialize your pins here
        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)
        self.name = name

    def fadedown(self): # Fades LED from bright to dim
        for i in range(255):
            if i < (255/2):
                self.led.duty_cycle = int(i * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def fadeup(self):  # Fades LED from dim to bright
        for i in range(255):
            if i > (255/2):
                self.led.duty_cycle = 65535 - int((i - (255/2)) * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def on(self, brightness=65535):  # Remember "on" means duty cycles < 65535
        self.led.duty_cycle = 65535 - brightness
        lightBulb.value = 65535


    def off(self): # "off" means the duty cycle should be full.
        self.led.duty_cycle = 65535



class RGB:
    '''this class should implement all 3 pins together to control an RGB LED'''
    from RGB import LED
        # Let's take a second to appreciate that we're using a class to call a class!
        # Let LED do all the nitty-gritty work, this RGB class will be the "manager"


    def fadeup(self):  # Fades LED from dim to bright
        for i in range(255):
            if i > (255/2):
                self.led.duty_cycle = 65535 - int((i - (255/2)) * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def __init__(self, redPin, greenPin, bluePin):
        # To initialize an RGB LED, we need to initialize 3 LED pins.
        self.myRedLED = LED(redPin, "red")
        self.myBlueLED = LED(bluePin, "blue")
        self.myGreenLED = LED(greenPin, "green")


    def blue(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.off()

    def red(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.on(brightness)

    def green(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.off()
        self.myGreenLED.on(brightness)
        self.myRedLED.off()

    def yellow(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.off()
        self.myGreenLED.on(brightness)
        self.myRedLED.on(brightness)


    def cyan(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.on(brightness)
        self.myRedLED.off()

    def magenta(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.on(brightness)

    def white(self, brightness=65535):
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.on(brightness)
        self.myRedLED.on(brightness)


    def Blinky(self, rate, brightness = 65535):
        for i in range(20):
          self.red(brightness)
          time.sleep(rate)
          self.off()
          time.sleep(rate)
          self.white(brightness)
          time.sleep(rate)
          self.off
          time.sleep(rate)
          self.yellow(brightness)
          time.sleep(rate)
          self.off()
          time.sleep(rate)
          self.white(brightness)
          time.sleep(rate)
          self.off
          time.sleep(rate)
          self.green(brightness)
          time.sleep(rate)
          self.off()
          time.sleep(rate)
          self.white(brightness)
          time.sleep(rate)
          self.off
          time.sleep(rate)
          self.cyan(brightness)
          time.sleep(rate)
          self.off()
          time.sleep(rate)
          self.white(brightness)
          time.sleep(rate)
          self.off
          time.sleep(rate)
          self.blue(brightness)
          time.sleep(rate)
          self.off()
          time.sleep(rate)
          self.white(brightness)
          time.sleep(rate)
          self.off
          time.sleep(rate)
          self.magenta(brightness)
          time.sleep(rate)
          self.off()
          time.sleep(rate)
          self.white(brightness)
          time.sleep(rate)
          self.off
          time.sleep(rate)

    def Alternate(self, rate, brightness = 65535):
       for i in range(10):
         self.red(brightness)
         self.green(brightness)
         self.blue(brightness)
         self.yellow(brightness)
         self.cyan(brightness)
         self.magenta(brightness)
         time.sleep(rate)
         time.sleep(rate)
         self.off




    def off(self):
        # This turns off all 3 LEDs, but my LEDs were still glowing a tiny bit.
        # To fix this, I took the RGB power wire out of 5V and plugged it into D13.
        # Now when I want the LED to be off, it's truly off!
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.off()
        lightBulb.value = 0

# Overview of assignment
The goal of this assignment is to get an RGB led to work with class modules. This assignment was easy as well since basically all we needed to do was copy and paste code. Although we need to create our own functions. I created the function Blinky and Alternate. Alternate never worked for some reason. I soon came to realize that the RGB LEDs were alternating without the alternate function, which is why I commented it out in the main. I think my code is broken because it still works even though I didn't call it


## Evidence
![Wiring](https://github.com/hgeorge82/Circuit-Python2/blob/main/rgb%20wiring.png)
![Gif of Blinky and "Alternate"](https://github.com/hgeorge82/Circuit-Python2/blob/main/rgb%20led%20gif.gif)















