import pygsheets #installed using pip in cmd
import os
import time
import numpy as np
path = "C:\\Users\\myran\\Desktop" #change for pi
os.chdir(path)
from plotter import plotter #user defined so it must be in path
from mood_data_analytics import mood_data_analytics
from mood_array_to_lights import mood_array_to_lights

import Adafruit_WS2801
import ADAfruit_GPIO.SPI as SPI
PIXEL_COUNT = 160
PIXEL_CLOCK = 11
PIXEL_DOUT = 10
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
pixels.clear()


gc = pygsheets.authorize(service_file='PiFormTest-41b3b63c1dc8.json')  #This is the only copy of the security file from google
sh = gc.open('LightsTestingSheet') #This sheet is shared with the account chrisnathanlights@piformtest.iam.gserviceaccount.com
# ^creates an object of class spreadsheet
sh.link(gc) #Links to the cloud for constant updating
wks = sh.sheet1 #Creates an object of class worksheet using the built-in sheet1
#wks.resize(2,5) #all of the header information and the start line


num_rows = 2
people_moods = []
os.system('cls')

while 1:
    try:
        people_moods.append(wks.get_value((num_rows+1,3))) #Store the person
        mood = wks.get_value((num_rows+1,2))
        if mood == '1':
            mood = 1
        elif mood == '2':
            mood = 2
        elif mood == '3':
            mood = 3
        elif mood == '4':
            mood = 4
        elif mood == '5':
            mood = 5
        elif mood == '6':
            mood = 6
        elif mood == '7':
            mood = 7
        elif mood == '8':
            mood = 8
        elif mood == '9':
            mood = 9
        elif mood == '10':
            mood = 10
        people_moods.append(mood) #Store the mood

        color1 = wks.get_value((num_rows+1,4))
        if color1 == 'Red':
            color1 =1
        elif color1 == 'Orange':
            color1 = 2
        elif color1 == 'Yellow':
            color1 = 3
        elif color1 == 'Green':
            color1 = 4
        elif color1 == 'Blue':
            color1 = 5
        elif color1 == 'Purple':
            color1 = 6
        people_moods.append(color1) #store color 1

        color2 = wks.get_value((num_rows+1,5))
        if color2 == 'Red':
            color2 =1
        elif color2 == 'Orange':
            color2 = 2
        elif color2 == 'Yellow':
            color2 = 3
        elif color2 == 'Green':
            color2 = 4
        elif color2 == 'Blue':
            color2 = 5
        elif color2 == 'Purple':
            color2 = 6
        people_moods.append(color2) #store color 2
            
        num_rows = num_rows+1
        
        #print(people_moods)
        lights_array = plotter(people_moods)
        print(lights_array)
        lights_array = mood_data_analytics(lights_array)
        print(lights_array)
        lights_array = mood_array_to_lights(lights_array)
        pixels.show()
        #os.system('cls')
        #flattened_output = output.ravel()   # We can flatten the array for easy display on LEDs
        #print(flattened_output)

    except:
        #print('no change')
        time.sleep(1)
        continue
