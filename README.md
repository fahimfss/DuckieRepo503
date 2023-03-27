# CMPUT 503 - Experimental Mobile Robotics - Code Repository

Hi from our Duckiebot!!
![image](https://user-images.githubusercontent.com/8725869/226133600-4b5227c4-8b41-4cc6-8096-be24fc994459.png)


This is a repository made by me (Fahim Shahriar) and my partner (Ningyuan Pei) to maintain the exercise codes required for the CMPUT 503 course. This repository will host all the codes for the six exercises of CMPUT 503. which will be published sequentially. 

CMPUT 503 is based on [Duckiebots](https://get.duckietown.com/products/duckiebot-db21), a simple jetson nano-based two-wheeled robot with a  camera. We expect to learn a lot about robotics, robot kinematics, odometry, ROS, and image processing based tasks with this robot. 

Fahim's duckie bot website can be found here: [https://sites.google.com/ualberta.ca/fahims-duckie-site](https://sites.google.com/ualberta.ca/fahims-duckie-site)  
Ningyuan's duckie bot website can be found here: [https://sites.google.com/ualberta.ca/peirobot](https://sites.google.com/ualberta.ca/peirobot)

### Exercise 1
[Exercise 1](https://github.com/fahimfss/DuckieRepo503/tree/master/exercise_one) was a solo exercise where I (Fahim) set up and tested the workability of the newly assembled DuckieBot. The DuckieBot consists of many components, so it is important to verify that everything is working correctly before using it in exercises. It is equally important to understand how to implement pre-existing code to perform simple tasks such as line following and to run custom code in DuckieBot's Jetson Nano.

### Exercise 2
[Exercise 2](https://github.com/fahimfss/DuckieRepo503/tree/master/exercise_two) is a team-based exercise where we learned how to create ROS nodes for subscribing and publishing messages, send velocity commands to the duckie-bot wheels to move the bot in specific ways, and how to use ROS bag and services. Also learned about finite state machines. 

### Exercise 3
[Exercise 3](https://github.com/fahimfss/DuckieRepo503/tree/master/exercise_three) is a team-based exercise where we need to implement the apriltag detection, lane following, and sensor fusion.

### Exercise 4
[Exercise 4](https://github.com/fahimfss/DuckieRepo503/tree/master/exercise_four) is a team-based exercise. The objective of this exercise is to implement an autonomous safe tailing behavior on the Duckiebot. It combines lane following, color detection, state machine from previous exercises with new components such as vehicle detection and distance measurement. 

#### Exercise 5
[Exercise 5](https://github.com/fahimfss/DuckieRepo503/tree/master/exercise_five) is a team-based exercise. The objective of this exercise is to use ml algorithm to implement a digit detector from your Duckiebot’s camera real-time while doing lane following. It combines lane following, color detection, apriltag detection, and state machine from previous exercises with new components such as digit detection and deep learning.