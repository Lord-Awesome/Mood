import pygsheets #installed using pip in cmd
#import os
import time
import numpy as np
#path = "C:\\Users\\myran\\Desktop" #change for pi
#os.chdir(path)

def plotter(people_moods):

    #people_moods = ['chris', 1, 'josh', 2, 'nicole', 3, 'nathan', 4]
    person1 = ''
    person2 = ''
    person3 = ''
    person4 = ''
    person5 = ''
    lights_array = np.zeros([16,10]) #specify size of lights grid

    for moods_index in range(0,len(people_moods),4): #iterates by 4 because every entry has name, mood, color1, color2
        person = people_moods[moods_index].lower()
        print(person)

        # Assign people to the 5 person slots
        if person1 == '' or person1 == person:
            person1 = person
            lights_array[0,0] = people_moods[moods_index+2]  #assign color 1 to the line
            lights_array[0,1] = people_moods[moods_index+3]  #assign color 2 to the line
            lights_array[0,2] = -1 #indicates a space (no light)
            #print('person1', person1)
        elif person2 == '' or person2 == person:
            person2 = person
            lights_array[1,0] = people_moods[moods_index+2]
            lights_array[1,1] = people_moods[moods_index+3]
            lights_array[1,2] = -1
            #print('person2', person2)
        elif person3 == '' or person3 == person:
            person3 = person
            lights_array[2,0] = people_moods[moods_index+2]
            lights_array[2,1] = people_moods[moods_index+3]
            lights_array[2,2] = -1
            #print('person3', person3)
        elif person4 == '' or person4 == person:
            person4 = person
            lights_array[3,0] = people_moods[moods_index+2]
            lights_array[3,1] = people_moods[moods_index+3]
            lights_array[3,2] = -1
            #print('person4', person4)
        elif person5 == '' or person5 == person:
            person5 = person
            lights_array[4,0] = people_moods[moods_index+2]
            lights_array[4,1] = people_moods[moods_index+3]
            lights_array[4,2] = -1
            #print('person5', person5)
        else:
            #print('too many people!')
            continue

        #put the moods into an array where each row is a person
        if person == person1:
            for i in range(30):
                if lights_array[0,i] == 0:
                    lights_array[0,i] = people_moods[moods_index+1]
                    break
                else:
                    continue

        elif person == person2:
            for i in range(30):
                if lights_array[1,i] == 0:
                    lights_array[1,i] = people_moods[moods_index+1]
                    break
                else:
                    continue

        elif person == person3:
            for i in range(30):
                if lights_array[2,i] == 0:
                    lights_array[2,i] = people_moods[moods_index+1]
                    break
                else:
                    continue

        elif person == person4:
            for i in range(30):
                if lights_array[3,i] == 0:
                    lights_array[3,i] = people_moods[moods_index+1]
                    break
                else:
                    continue

        elif person == person5:
            for i in range(30):
                if lights_array[4,i] == 0:
                    lights_array[4,i] = people_moods[moods_index+1]
                    break
                else:
                    continue
        else:
            continue
    
    return lights_array




    
