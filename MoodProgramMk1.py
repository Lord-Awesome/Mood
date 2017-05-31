import pygsheets #installed using pip in cmd
import os
import time
import numpy as np
path = "C:\\Users\\myran\\Desktop" #change for pi
os.chdir(path)
from plotter import plotter #user defined so it must be in path


gc = pygsheets.authorize(service_file='PiFormTest-41b3b63c1dc8.json')  #This is the only copy of the security file from google
sh = gc.open('LightsTestingSheet') #This sheet is shared with the account chrisnathanlights@piformtest.iam.gserviceaccount.com
# ^creates an object of class spreadsheet
sh.link(gc) #Links to the cloud for constant updating
wks = sh.sheet1 #Creates an object of class worksheet using the built-in sheet1
wks.resize(2,5) #all of the header information and the start line


num_rows = 2
people_moods = []
os.system('cls')

while 1:
    try:
        people_moods.append(wks.get_value((num_rows+1,3))) #Store the person
        mood = wks.get_value((num_rows+1,2))
        if mood == 'Happy':
            mood = 1
        elif mood == 'Grumpy':
            mood = 2
        elif mood == 'Sleepy':
            mood = 3
        elif mood == 'Dopey':
            mood = 4
        elif mood == 'Bashful':
            mood = 5
        elif mood == 'Sneezy':
            mood = 6
        elif mood == 'Doc':
            mood = 7
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
        output = plotter(people_moods)
        os.system('cls')
        print(output)
        #flattened_output = output.ravel()   # We can flatten the array for easy display on LEDs
        #print(flattened_output)

    except:
        #print('no change')
        time.sleep(1)
        continue
