### Exercise two website
[https://sites.google.com/ualberta.ca/fahims-duckie-site/exercises/exercise-2](https://sites.google.com/ualberta.ca/fahims-duckie-site/exercises/exercise-2)
    

### Exercise two file descriptions

**[bagprocess.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/bagprocess.py)**   
A simple python file to verify the contents of the ros bag file, created by [duckie_mover.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/duckie_mover.py)

**[duckie_mover.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/duckie_mover.py)**   
This is the primary file for exercise two. It contains code for moving/rotating the robot based on the given tasks and sending the led commands to the led server

**[image_sub_pub.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/image_sub_pub.py)**   
This file contains the code for subscribing to the duckie-bot camera topic, printing the image size, and re-publishing the image data

**[image_subscriber.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/image_subscriber.py)**   
This file contains a simple subscriber node that subscribe to the custom message published by the `my_subscriber_publisher_node` node in
[image_sub_pub.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/image_sub_pub.py) file

**[led_service.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/led_service.py)**   
This file receives and carries out led light changing instructions sent by the `my_mover_node` in [duckie_mover.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/duckie_mover.py)

**[my_publisher_node.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/my_publisher_node.py)**   
ROS publisher and subscriber demo file 

**[run.bag](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/run.bag)**   
This bag file captures the odometry information written by the `my_mover_node` in [duckie_mover.py](https://github.com/fahimfss/DuckieRepo503/blob/master/exercise_two/duckie_mover.py), for exercise two part two
