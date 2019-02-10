#Tina Guo and Amma Agyei
#Bubble Level

import microbit
import math

def calculate_angle(x,y,z):
        a1 = math.atan2(x,math.sqrt((y ** 2) + (z ** 2)))
        print(math.degrees(a1))
        return math.degrees(a1)

def bubble_display(x_angle, y_angle):
    if(x_angle > -10 and x_angle < 10):
        if(y_angle > -10 and y_angle < 10):
            microbit.display.show(microbit.Image.HEART)
        elif(y_angle < 0 and y_angle > -90):
            microbit.display.show(microbit.Image.ARROW_S)
        elif(y_angle < 90 and y_angle > 0):
            microbit.display.show(microbit.Image.ARROW_N)
    elif(x_angle < 90):
        if(x_angle > 10):
            if(y_angle < 10 and y_angle > -90):
                microbit.display.show(microbit.Image.ARROW_SW)
            if(y_angle < 90 and y_angle > 0):
                microbit.display.show(microbit.Image.ARROW_NW)
            if(y_angle < 10 and y_angle > 0):
                microbit.display.show(microbit.Image.ARROW_W)
        elif(x_angle < 0 and x_angle > -90):
            if(y_angle < 10 and y_angle > -10):
                microbit.display.show(microbit.Image.ARROW_E)
            elif(y_angle < 10):
                microbit.display.show(microbit.Image.ARROW_SE)
            elif(y_angle > 10):
                microbit.display.show(microbit.Image.ARROW_NE)



while True:
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()

    x_angle = calculate_angle(x,y,z)
    y_angle = calculate_angle(y,x,z)
    print((x_angle,y_angle))
    bubble_display(x_angle,y_angle)
    microbit.sleep(400)

#if xtilt > 170
    #if ytilt > 190
      #  arrow_NW
    #elif if ytilt < 170
     #   arrow_SW
    #else
     #   arrow_W
#elif xtilt < 170


    #def bubble_display(x_angle,y_angle):
     #   if (x_angle <= math.degrees(10.0) and y_angle <= math.degrees(10.0)):
      #      microbit.display.show(microbit.Image.HEART)
       # if (y_angle > 10.0):
        #    microbit.display.show(microbit.Image.ARROW_N)
        #elif (x_angle < 0):
         #   microbit.display.show(microbit.Image.ARROW_W)

