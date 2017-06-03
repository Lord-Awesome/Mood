import pygsheets #installed using pip in cmd
#import os
import time
import numpy as np
import Adafruit_WS2801
import ADAfruit_GPIO.SPI as SPI
import random
PIXEL_COUNT = 160
PIXEL_CLOCK = 11
PIXEL_DOUT = 10
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
#path = "C:\\Users\\myran\\Desktop" #change for pi
#os.chdir(path)

def mood_array_to_lights(lights_array):
##    lights_vector_upper_half = []
##    lights_vector_lower_half = []
##    lights_codes_upper_half = []
##    lights_codes_lower_half = [] 
    person_colors = []
    
    color_red = Adafruit_WS2801.RGB_to_color(244,66,66)
    color_orange = Adafruit_WS2801.RGB_to_color(244,137,66)
    color_yellow = Adafruit_WS2801.RGB_to_color(244,229,66)
    color_green = Adafruit_WS2801.RGB_to_color(66,244,72)
    color_blue = Adafruit_WS2801.RGB_to_color(66,226,244)
    color_purple = Adafruit_WS2801.RGB_to_color(197,66,244)
    colors = [color_red, color_orange, color_yellow, color_green, color_blue, color_purple]
    
    mood_color_0 = Adafruit_WS2801.RGB_to_color(229,24,0)
    mood_color_1 = Adafruit_WS2801.RGB_to_color(225,0,73)
    mood_color_2 = Adafruit_WS2801.RGB_to_color(221,0,167)
    mood_color_3 = Adafruit_WS2801.RGB_to_color(176,0,217)
    mood_color_4 = Adafruit_WS2801.RGB_to_color(81,0,213)
    mood_color_5 = Adafruit_WS2801.RGB_to_color(0,10,210)
    mood_color_6 = Adafruit_WS2801.RGB_to_color(0,99,206)
    mood_color_7 = Adafruit_WS2801.RGB_to_color(0,185,202)
    mood_color_8 = Adafruit_WS2801.RGB_to_color(0,198,129)
    mood_color_9 = Adafruit_WS2801.RGB_to_color(0,194,43)
    mood_colors = [mood_color_0, mood_color_1, mood_color_2, mood_color_3, mood_color_4, mood_color_5, mood_color_6, mood_color_7, mood_color_8, mood_color_9]

    for i in range(5): #adds lights to list by row
        for j in range(10):
##            lights_vector_upper_half.append(int(lights_array[i,j])) 
           if int(lights_array[i,j]) != 0 and item != -1:
                pixels.set_pixel((i*10)+j, mood_colors[int(lights_array[i,j])-1])

    for i in range(5, 16):
        for j in range(10):
##            lights_vector_lower_half.append(int(lights_array[i,j])
            if item != 0 and item < 10:
                plotting_color = colors[int(lights_array[int(item)-1,0])-1]
                if plotting_color in person_colors:
                    plotting_color2 = colors[int(lights_array[int(item)-1,1])-1]
                    if plotting_color2 in person_colors:
##                        lights_codes_lower_half.append(colors[int(item)]) 
                        pixels.set_pixel_rgb((i*10)+j, colors[int(item)])
                    else:
##                        lights_codes_lower_half.append(plotting_color2) 
                        pixels.set_pixel_rgb((i*10)+j, plotting_color2)
                        person_colors.append(plotting_color2)
                else:
##                    lights_codes_lower_half.append(plotting_color) 
                    pixels.set_pixel_rgb((i*10)+j, plotting_color)
                    person_colors.append(plotting_color)
            if item > 10: #if two people want to plot on the same LED
                item = str(item)
                pixels.set_pixel_rg((i*10)+j, colors[int(item[random.randint(0,len(item))])]) #pick a random color out of the possible ones
                
                

            
##    for item in lights_vector_upper_half:
##        if item != 0 and item != -1:
##            lights_codes_upper_half.append(mood_colors[item-1])
##        if item == 0:
##            lights_codes_upper_half.append(0)
##        if item == -1:
##            lights_codes_upper_half.append(0)

##    for item in lights_vector_lower_half:
##        if item == 0:
##            lights_codes_lower_half.append(0)
##        if item != 0 and item < 10:
##            plotting_color = colors[int(lights_array[int(item)-1,0])-1]
##            if plotting_color in person_colors:
##                plotting_color2 = colors[int(lights_array[int(item)-1,1])-1]
##                if plotting_color2 in person_colors:
##                    lights_codes_lower_half.append(colors[int(item)])
##                else:
##                    lights_codes_lower_half.append(plotting_color2)
##                    person_colors.append(plotting_color2)
##            else:
##                lights_codes_lower_half.append(plotting_color)
##                person_colors.append(plotting_color)
##        else:
##            lights_codes_lower_half.append(item) 
           
            
    #lights_vector = [lights_codes_upper_half, lights_codes_lower_half]

    return lights_array
