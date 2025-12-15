---
title: Chapter 3 - Building Your First ROS2 Robot Application
sidebar_position: 3
---

# Chapter 3: Building Your First ROS2 Robot Application

## Hands-On: Creating a Simple Humanoid Robot Simulator

In this chapter, we'll build a simple humanoid robot simulator that demonstrates ROS2 concepts in action. Our robot will have basic joint control and sensor simulation - similar to what you'd find in a real humanoid robot.

## Prerequisites

Before we begin, make sure you have:
- ROS2 installed (Humble Hawksbill or newer recommended)
- Basic knowledge of C++ or Python
- A terminal/command prompt ready

## Setting Up the Workspace

First, let's create a workspace for our robot application:

```bash
mkdir -p ~/humanoid_robot_ws/src
cd ~/humanoid_robot_ws
colcon build
source install/setup.bash
```

## Creating Our First Package

Let's create a package for our simple humanoid robot:

```bash
cd ~/humanoid_robot_ws/src
ros2 pkg create --build-type ament_cmake humanoid_simple_robot --dependencies rclcpp rclpy std_msgs sensor_msgs geometry_msgs
```

## Example 1: Joint State Publisher

Let's create a simple node that simulates joint states for a humanoid robot:

**C++ Implementation (`humanoid_simple_robot/src/joint_state_publisher.cpp`)**:

```cpp
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/joint_state.hpp"
#include "std_msgs/msg/header.hpp"

class JointStatePublisher : public rclcpp::Node
{
public:
    JointStatePublisher() : Node("simple_joint_publisher")
    {
        publisher_ = this->create_publisher<sensor_msgs::msg::JointState>(
            "/joint_states", 10);

        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(50), // 20 Hz
            std::bind(&JointStatePublisher::publish_joint_states, this));
    }

private:
    void publish_joint_states()
    {
        auto msg = sensor_msgs::msg::JointState();
        msg.header.stamp = this->get_clock()->now();
        msg.name = {"left_hip", "right_hip", "left_knee", "right_knee",
                   "left_shoulder", "right_shoulder", "left_elbow", "right_elbow"};

        // Simulate simple oscillating joint positions
        double t = this->get_clock()->now().nanoseconds() / 1e9;
        msg.position = {
            0.1 * sin(t),     // left_hip
            0.1 * sin(t),     // right_hip
            0.2 * sin(t),     // left_knee
            0.2 * sin(t),     // right_knee
            0.05 * cos(t),    // left_shoulder
            0.05 * cos(t),    // right_shoulder
            0.1 * sin(t),     // left_elbow
            0.1 * sin(t)      // right_elbow
        };

        publisher_->publish(msg);
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<sensor_msgs::msg::JointState>::SharedPtr publisher_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<JointStatePublisher>());
    rclcpp::shutdown();
    return 0;
}
```

## Example 2: Balance Controller

Now let's create a simple balance controller that subscribes to joint states and IMU data:

**Python Implementation (`humanoid_simple_robot/launch/balance_controller.py`)**:

```python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState, Imu
from std_msgs.msg import Float64MultiArray
import math

class SimpleBalanceController(Node):
    def __init__(self):
        super().__init__('balance_controller')

        # Subscribe to joint states and IMU data
        self.joint_subscriber = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_callback,
            10)

        self.imu_subscriber = self.create_subscription(
            Imu,
            '/imu/data',
            self.imu_callback,
            10)

        # Publish joint commands
        self.command_publisher = self.create_publisher(
            Float64MultiArray,
            '/joint_commands',
            10)

        # Timer for control loop
        self.timer = self.create_timer(0.05, self.control_loop)  # 20 Hz

        self.current_joint_states = None
        self.current_imu_data = None
        self.get_logger().info('Simple Balance Controller initialized')

    def joint_callback(self, msg):
        self.current_joint_states = msg

    def imu_callback(self, msg):
        self.current_imu_data = msg

    def control_loop(self):
        if self.current_joint_states is None or self.current_imu_data is None:
            return

        # Simple proportional controller for balance
        # Based on IMU roll/pitch angles
        roll = math.atan2(
            2.0 * (self.current_imu_data.orientation.w * self.current_imu_data.orientation.x +
                  self.current_imu_data.orientation.y * self.current_imu_data.orientation.z),
            1.0 - 2.0 * (self.current_imu_data.orientation.x * self.current_imu_data.orientation.x +
                        self.current_imu_data.orientation.y * self.current_imu_data.orientation.y)
        )

        pitch = math.asin(
            2.0 * (self.current_imu_data.orientation.w * self.current_imu_data.orientation.y -
                  self.current_imu_data.orientation.z * self.current_imu_data.orientation.x)
        )

        # Calculate corrective joint commands
        hip_correction = -1.5 * pitch  # Correct forward/backward tilt
        ankle_correction = -1.0 * roll  # Correct side-to-side tilt

        # Create and publish commands
        cmd_msg = Float64MultiArray()
        cmd_msg.data = [
            hip_correction,    # left_hip_command
            hip_correction,    # right_hip_command
            ankle_correction,  # left_ankle_command
            ankle_correction   # right_ankle_command
        ]

        self.command_publisher.publish(cmd_msg)

def main(args=None):
    rclpy.init(args=args)
    controller = SimpleBalanceController()

    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        pass
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## Example 3: Sensor Simulator

Let's create a simulated IMU node that generates realistic sensor data:

**C++ Implementation (`humanoid_simple_robot/src/imu_simulator.cpp`)**:

```cpp
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/imu.hpp"
#include "geometry_msgs/msg/vector3.hpp"
#include "geometry_msgs/msg/quaternion.hpp"
#include <random>

class ImuSimulator : public rclcpp::Node
{
public:
    ImuSimulator() : Node("imu_simulator")
    {
        publisher_ = this->create_publisher<sensor_msgs::msg::Imu>("/imu/data", 10);

        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(10), // 100 Hz
            std::bind(&ImuSimulator::publish_imu_data, this));

        // Initialize random number generator
        random_engine_.seed(std::chrono::system_clock::now().time_since_epoch().count());
    }

private:
    void publish_imu_data()
    {
        auto msg = sensor_msgs::msg::Imu();
        msg.header.stamp = this->get_clock()->now();
        msg.header.frame_id = "imu_link";

        // Simulate slight orientation variations around upright position
        double t = this->get_clock()->now().nanoseconds() / 1e9;

        // Add small oscillations to simulate walking dynamics
        double roll = 0.02 * sin(0.5 * t) + 0.01 * (distribution_(random_engine_) - 0.5);
        double pitch = 0.03 * cos(0.7 * t) + 0.01 * (distribution_(random_engine_) - 0.5);
        double yaw = 0.01 * sin(0.3 * t) + 0.005 * (distribution_(random_engine_) - 0.5);

        // Convert Euler angles to quaternion
        double cy = cos(yaw * 0.5);
        double sy = sin(yaw * 0.5);
        double cp = cos(pitch * 0.5);
        double sp = sin(pitch * 0.5);
        double cr = cos(roll * 0.5);
        double sr = sin(roll * 0.5);

        msg.orientation.w = cr * cp * cy + sr * sp * sy;
        msg.orientation.x = sr * cp * cy - cr * sp * sy;
        msg.orientation.y = cr * sp * cy + sr * cp * sy;
        msg.orientation.z = cr * cp * sy - sr * sp * cy;

        // Simulate angular velocity (derivative of orientation)
        msg.angular_velocity.x = 0.02 * 0.5 * cos(0.5 * t);
        msg.angular_velocity.y = -0.03 * 0.7 * sin(0.7 * t);
        msg.angular_velocity.z = 0.01 * 0.3 * cos(0.3 * t);

        // Simulate linear acceleration (gravity + small variations)
        msg.linear_acceleration.x = 9.81 * sin(pitch);
        msg.linear_acceleration.y = -9.81 * sin(roll);
        msg.linear_acceleration.z = 9.81 * cos(roll) * cos(pitch);

        publisher_->publish(msg);
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<sensor_msgs::msg::Imu>::SharedPtr publisher_;
    std::mt19937 random_engine_;
    std::uniform_real_distribution<double> distribution_{-1.0, 1.0};
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<ImuSimulator>());
    rclcpp::shutdown();
    return 0;
}
```

## Launching the System

Create a launch file to bring up all nodes together:

**Launch File (`humanoid_simple_robot/launch/simple_humanoid.launch.py`)**:

```python
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    return LaunchDescription([
        # Joint state publisher
        Node(
            package='humanoid_simple_robot',
            executable='joint_state_publisher',
            name='joint_publisher',
            output='screen'
        ),

        # IMU simulator
        Node(
            package='humanoid_simple_robot',
            executable='imu_simulator',
            name='imu_sim',
            output='screen'
        ),

        # Balance controller
        Node(
            package='humanoid_simple_robot',
            executable='balance_controller',
            name='balance_ctrl',
            output='screen'
        )
    ])
```

## Running the Example

To run this system:

1. Build your workspace:
```bash
cd ~/humanoid_robot_ws
colcon build --packages-select humanoid_simple_robot
source install/setup.bash
```

2. Launch the system:
```bash
ros2 launch humanoid_simple_robot simple_humanoid.launch.py
```

3. Monitor the topics:
```bash
# View joint states
ros2 topic echo /joint_states

# View IMU data
ros2 topic echo /imu/data

# View commands
ros2 topic echo /joint_commands
```

## Visualization with RViz

You can visualize your robot in RViz by creating a URDF (Unified Robot Description Format) file and using the Robot State Publisher:

**URDF Snippet (`humanoid_simple_robot/urdf/simple_humanoid.urdf`)**:

```xml
<?xml version="1.0"?>
<robot name="simple_humanoid">
  <!-- Base link -->
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.3 0.2 0.5"/>
      </geometry>
      <material name="blue">
        <color rgba="0 0 1 1"/>
      </material>
    </visual>
  </link>

  <!-- Head -->
  <link name="head">
    <visual>
      <geometry>
        <sphere radius="0.1"/>
      </geometry>
      <material name="white">
        <color rgba="1 1 1 1"/>
      </material>
    </visual>
  </link>

  <joint name="neck_joint" type="revolute">
    <parent link="base_link"/>
    <child link="head"/>
    <origin xyz="0 0 0.3"/>
    <axis xyz="0 1 0"/>
    <limit lower="-0.5" upper="0.5" effort="100" velocity="1"/>
  </joint>

  <!-- Additional links for arms and legs would follow the same pattern -->
</robot>
```

## Real-World Applications

This simple example demonstrates the core concepts used in real humanoid robots:

1. **Modular Design**: Each component (joints, sensors, controllers) runs as a separate node
2. **Real-time Communication**: High-frequency sensor and command updates
3. **Distributed Processing**: Different nodes can run on different computers
4. **Standard Message Types**: Using common ROS2 message formats for interoperability

## Summary

In this chapter, we built a complete ROS2 application that demonstrates how different components of a humanoid robot communicate. We created nodes for joint state publishing, IMU simulation, and balance control, showing how ROS2's communication patterns enable complex robot behaviors. This foundation will serve you well as we move to more advanced topics in subsequent modules.