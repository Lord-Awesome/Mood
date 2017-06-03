import pygsheets #installed using pip in cmd
#import os
import time
import numpy as np
#path = "C:\\Users\\myran\\Desktop" #change for pi
#os.chdir(path)


def mood_data_analytics(lights_array):


    for person in range(0,4):
        for mood_index in range(3,9):
            if lights_array[person,mood_index] != 0:
                try:
                    mood_value = lights_array[person, mood_index]
                    plotting_row = 16 - mood_value
                    plotting_row = int(plotting_row)
                    if lights_array[plotting_row, mood_index] == 0:
                        lights_array[plotting_row,mood_index] = person+1
                    else:
                        lights_array[plotting_row,mood_index] = int(lights_array[plotting_row,mood_index]*10)+person+1
                except:
                    print("Plotting Failed")
                    continue
                #print(lights_array)

    return lights_array
