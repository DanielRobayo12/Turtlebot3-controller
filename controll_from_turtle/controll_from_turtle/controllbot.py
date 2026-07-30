import rclpy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def callTime(msg:Joy):
    global pub

    controller_rep = Twist

    controller_rep._linear.x = msg._axes[1]
    controller_rep._angular.z = msg._axes[0]

    pub.publish(controller_rep)


def main():
    #globla variables
    global pub

    #init ros2
    rclpy.init()

    #create a node
    node = rclpy.create_node("controller")

    #create a subscriber for Joy
    sub = node.create_subscription(Joy,"/joy",callTime,1)

    #create a publisher for /cmd_vel
    pub = node.create_publisher(Twist,"/cmd_vel")

    #create a timer
    node.create_timer(0.01,callTime)

    #keep alive the program
    rclpy.spin(node)

    #shutdown the program
    rclpy.shutdown()
    node.destroy_node()


if __name__ == "__main__":
    main()