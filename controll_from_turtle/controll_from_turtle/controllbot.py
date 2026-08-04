import rclpy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped

msg = None

def callTime():
    global pub
    global msg
    global node

    if msg is None:
        return

    controller_rep = Twist()
    controller_stamped = TwistStamped()

    controller_rep.linear.x = float(msg.axes[1])*0.22
    controller_rep.linear.y = 0.0
    controller_rep.linear.z = 0.0
    controller_rep.angular.x = 0.0
    controller_rep.angular.y = 0.0
    controller_rep.angular.z = float(msg.axes[0])*2.84


    #controller_stamped.header.frame_id = ''
    controller_stamped.header.stamp = node.get_clock().now().to_msg()
    controller_stamped.twist = controller_rep

    pub.publish(controller_stamped)

def callback(msg_joy:Joy):
    global msg
    msg = msg_joy


def main():
    #globla variables
    global pub
    global node

    #init ros2
    rclpy.init()

    #create a node  
    node = rclpy.create_node("controller")

    #create a subscriber for Joy
    sub = node.create_subscription(Joy,"/joy",callback,1)

    #create a publisher for /cmd_vel
    pub = node.create_publisher(TwistStamped,"/cmd_vel",1)

    #create a timer
    node.create_timer(0.01,callTime)

    #keep alive the program
    rclpy.spin(node)

    #shutdown the program
    rclpy.shutdown()
    node.destroy_node()


if __name__ == "__main__":
    main()