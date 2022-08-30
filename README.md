### RESEARCHTRACK1 ###
### INTRODUCTION ###: 
Assignment 1 in RESEARCH TRACK-1, mainly concentrates on simulating the code on the python simulator for running a specified task with the help of a self-governing robot. The robot must travel in the counter-clockwise direction by grabbing up the silver token and placing those silver token behind by turning the robot in any one direction.

## AIM ##To develop a code for a robot to complete the task within the specified environment in the Python simulator. 

To Write a python script for achieving this robot"s behaviour:
 
-In this assignment the code must be designed to run the robot without detecting the boxes around all the directions (from -180.0 degrees to 180.0 degrees)

-Constantly drive the robot around the circuit in the counter-clockwise direction

-Avoid touching the golden boxes

-When the robot is close to a silver box, it should grab it, and move it behind itself #PROCEDURE:

## LINEAR VELOCITY FOR THE ROBOT ##:
Firstly in order to move the robot forward a function called DRIVE() has been defined. 

This function has two motors to activate mo and m1. When a set of values is given to the motors, the robot moves forward if it is (+), else drives backward for (-).

## ANGULAR VELOCITY FOR THE ROBOT ##:
In addition to the linear velocity of the robot, this robot also requires an angular velocity to turn right or left. 

So, a function is determined in the program to define the angular velocity for the robot. This function "TURN" is determined to initiate the motors in the robot to give an angular velocity. 

The robot can be turned by giving different speed to the motor. i.e., motor 1 (-) & motor 2 (+). To make the robot turn left. motor 1 (+) & motor 2 (-). To make the robot turn right.


 ## RESULT ##:
-The above-mentioned procedures are used to run the robot in the specified path without disturbing the environment.

-The code for this assignment has been stored in ASSIGNMENT-1.

-We can run the ASSIGNMENT-1 code in the python simulator by using (python run.py ASSIGNMENT1.py).

