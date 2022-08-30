### RESEARCHTRACK1 
### INTRODUCTION: 
Assignment 1 in RESEARCH TRACK-1, mainly concentrates on simulating the code on the python simulator for running a specified task with the help of a self-governing robot. The robot must travel in the counter-clockwise direction by grabbing up the silver token and placing those silver token behind by turning the robot in any one direction.

## AIM-To develop a code for a robot to complete the task within the specified environment in the Python simulator: 

To Write a python script for achieving this robot"s behaviour:
 
-In this assignment the code must be designed to run the robot without detecting the boxes around all the directions (from -180.0 degrees to 180.0 degrees)

-Constantly drive the robot around the circuit in the counter-clockwise direction

-Avoid touching the golden boxes

-When the robot is close to a silver box, it should grab it, and move it behind itself #PROCEDURE:

## LINEAR VELOCITY FOR THE ROBOT:
Firstly in order to move the robot forward a function called DRIVE() has been defined. 

This function has two motors to activate mo and m1. When a set of values is given to the motors, the robot moves forward if it is (+), else drives backward for (-).

## ANGULAR VELOCITY FOR THE ROBOT:
In addition to the linear velocity of the robot, this robot also requires an angular velocity to turn right or left. 

So, a function is determined in the program to define the angular velocity for the robot. This function "TURN" is determined to initiate the motors in the robot to give an angular velocity. 

The robot can be turned by giving different speed to the motor. i.e., motor 1 (-) & motor 2 (+). To make the robot turn left. motor 1 (+) & motor 2 (-). To make the robot turn right.

## PREDEFINED FUNCTOINS & CLASS, CREATED BY (PROFESSOR-CARMINE RECCHIUTO):
 The R is a robot () - Class robot is created. 
 
 R.grab() - To grab the silver box whenever the robot is near to silver token.
 
 R.release() - To release the grabbed silver token.
 
 R.see() - To see the robot
 
 def drive (speed, seconds): Function to initiate the linear velocity for the robot.
 
 def turn (speed, seconds): Function to initiate the angular velocity for the robot.

## RECOGNITION OF TOKEN:
## SILVER TOKEN : 
find_silver_token() - find the closest silver token. 

A function find_silver_token is created with variables, d_silver_token = distance from the silver token to robot, angle_silver_token = postion of the silver token oriented with respect to the robot. 

If the token.dist returns d_silver_token and token.rot_y returns angle_silver_token then the token is silver. if the d_silver_token less than threshold distance(minimum distance assigned for the robot grab silver token) and absolute angle of angle_silver_token less than angle_thr (angle to allign the robot with the silver token to grab) is both satisfied the robot will grab the silver token, turn and place it behind itself and turns again.

A second threshold distance is created to allign the robot with the silver token. If Second threshold distance (d_thr2) is greater than d_silver_token then it allign itself with silver token respect to the angle_silver_token and angle_thr condtions.

## GOLDEN TOKEN: 
find_gold_token() - find closest gold token.

In addition to silver token, As the robot should avoid the golden token, four functions are created naming find_left_golden_token(), find_right_golden_token(), find_front_golden_token() and find_golden_token() . These functions are created with respective parameters such as : distance of the robot from the respective golden token(front, left and right) and angle fo the robot with respect to the respective golden token (front, left, right).

If the distance from the front golden token is lesser than the d_front_thr ( minimum distance from which the robot should avoid the golden tokens), robot should prioritise which side it should turn.For that decision making, a fucntion chosse_turn() is called.

If distance from robot to right golden token is lesser than distance from robot to left golden token, then the robot should turn left or else turn right.

In front, left, right golden token functions respective range of angles are given for orientation of the robot to visualise the golden token and avoid them.

 ## RESULT ##:
-The above-mentioned procedures are used to run the robot in the specified path without disturbing the environment.

-The code for this assignment has been stored in ASSIGNMENT-1.

-We can run the ASSIGNMENT-1 code in the python simulator by using (python run.py ASSIGNMENT1.py).

