# Use your turtlebot3 with xbox Controller

##Demo
> In the demo we going to execute many terminals through SSh and our PC

### Step 1

Create a terminal and change the **ROS_DOMAIN_ID** to a unique ID

    export ROS_DOMAIN_ID=15

connect your Xbox controller to the pc and execute

    ros2 launch joy joy_node.launch.py

We can verify the node's operation by pressing the buttons on our controller and executing in another terminal whit **ROS_DOMAIN_ID=15**

    ros2 topic echo /joy

### Step 2

Connect your turtlebot with SSH

      ssh turtlecitoqturtlecito-1.local 
      
Change **ROS_FOMAIN_ID**

      export ROS_DOMAIN_ID=15
      
Started your turtlebot

      ros2 launch turtlebot3_bringhup robot.launch.py

And finaly ejecute the controller node

    ros2 run controll_from_turtle controllbot.py

    

