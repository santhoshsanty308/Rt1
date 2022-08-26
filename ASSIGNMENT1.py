from __future__ import print_function

import time
from sr.robot import *

d_thr=0.4 ## DISTANCE TO GRAB THE TOKEN ##
d_thr2=0.6 ## THE ROBOT IS CLOSE ENOUGH TO THE SILVER TOKEN ##
d_front_thr=1.6 ## THE ROBOT CLOSE ENOUGH TO THE GOLDEN TOKEN ##
angle_thr=1.0 ## ANGLE THRESHOLD TO GRAB THE TOKEN ##

R=Robot() ## Instance of the class Robot ##

def drive(speed, seconds): ## function for setting a linear velocity ##
    R.motors[0].m0.power = speed 
    R.motors[0].m1.power = speed
    time.sleep(seconds) 
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds): ## function for setting an angular velocity ##
    
    R.motors[0].m0.power = speed ## speed of the wheel##
    R.motors[0].m1.power = -speed
    time.sleep(seconds) 
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token(): ## function to find the siver token ## 
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist = token.dist
            rot_y = token.rot_y
    if dist==100:
        return -1,-1
    else:
        return dist,rot_y 
def find_golden_token(): ## function to find the golden token ##
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist
            rot_y=token.rot_y
    if dist==100:
        return -1,-1
    else:
        return dist,rot_y
    
def find_front_golden_token(): ## function to find the front golden token ##
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and -20 < token.rot_y and token.rot_y <20:
            dist=token.dist
            rot_y=token.rot_y
    if dist==100:
        return -1,-1
    else:
        return dist,rot_y
def find_right_golden_token(): ## function to find the right golden token ##
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and 60< token.rot_y and token.rot_y < 100:
            dist=token.dist
            rot_y=token.rot_y
    if dist==100:
        return -1,-1
    else:
        return dist,rot_y
def find_left_golden_token(): ## function to find the left golden token ##
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and -100 < token.rot_y and token.rot_y < -60:
            dist=token.dist
            rot_y=token.rot_y
    if dist==100:
        return -1,-1
    else:
        return dist, rot_y
def choose_turn(): ## function to choose which side the robot should turn##
    d_left  = find_left_golden_token()
    d_right = find_right_golden_token()
    if d_right < d_left: 
        return 1
    else:
        return 0
    
while 1:
    drive(50,0.1)
    print("driving")
    d_silver_token, angle_silver_token = find_silver_token() ## passing parameters to the function to find the silver token##
    if d_silver_token < d_thr and abs(angle_silver_token) < angle_thr:
        print("grab silver token")
        R.grab()
        print("turning to grab")
        turn(30,2)
        R.release()
        turn(-30,2)
    elif d_silver_token < d_thr2:
        if angle_silver_token > angle_thr:
            print("alligning left")
            turn(2,0.5)
        elif angle_silver_token < -angle_thr:
            print("allingning right")
            turn(-2,0.5)
        else:
            print("no silver token found keep driving !")
            drive(50,0.5)
    else:   
        d_front_golden_token, angle_f_gold_token = find_front_golden_token()   ## passing parameters to function to find the golden token in front## 
        if d_front_golden_token < d_front_thr:
            print(" golden tokens ")
            anti_clockwise = choose_turn() 
            if anti_clockwise: ## if the choose_turn() function returns 1 ##
                print("turning left")
                turn(-20,0.5)
            else: ## if return 0 ##
                print("turning right")
                turn(20,0.5)
            
        
        
        

            

