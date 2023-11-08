#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

int main(int argc, char **argv){
    ros::init(argc, argv, "control_car");
    ros::NodeHandle node_obj;
    ros::Publisher control_car_publisher=node_obj.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
    ros::Rate loop_rate(10);
    geometry_msgs::Twist msg;
    // msg.linear.x=0;
    printf("Use w,a,s,d to move the bot and press q for exit.\n");
    std::string inputString;
    while(ros::ok()){
        std::getline(std::cin, inputString);
        if(inputString.compare("w") == 0){
        msg.linear.x=msg.linear.x+0.01;
        }
        if(inputString.compare("q") == 0){
        msg.linear.x=0;
        }
        if(inputString.compare("s") == 0){
        msg.linear.x=msg.linear.x-0.01;
        }
        ROS_INFO("Publishing\n");
        control_car_publisher.publish(msg);
        loop_rate.sleep();
    }
    
    return 0;
}