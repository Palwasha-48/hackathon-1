---
title: Chapter 1 - Introduction to ROS2 Concepts
sidebar_position: 1
---

# Chapter 1: Introduction to ROS2 Concepts

## What is ROS2?

ROS2 (Robot Operating System 2) is a flexible framework for writing robot software. Despite its name, it's not an actual operating system but rather a collection of tools, libraries, and conventions that help developers create robot applications.

Think of ROS2 as the "operating system" for robots - it handles communication between different parts of a robot, manages data flow, and provides reusable components that speed up development.

## Why ROS2 Matters for Humanoid Robots

Humanoid robots are incredibly complex systems with many interconnected components:

- **Sensors**: Cameras, LIDAR, IMUs (Inertial Measurement Units), joint encoders, force/torque sensors
- **Actuators**: Motors for joints, grippers, walking mechanisms
- **Controllers**: Balance controllers, motion planners, gait generators
- **AI systems**: Perception, planning, decision-making modules
- **Safety systems**: Emergency stops, collision avoidance

All of these components need to communicate and coordinate seamlessly. ROS2 provides the infrastructure for this communication, allowing different teams to develop individual components that can work together.

## Key Components of ROS2

### Nodes
A node is a process that performs computation. In a humanoid robot, you might have:
- `camera_node`: Processes images from head cameras
- `joint_controller`: Controls motor positions
- `balance_controller`: Maintains robot stability
- `perception_node`: Identifies objects and obstacles

Nodes are typically implemented as individual programs that can run on the same computer or distributed across multiple computers.

### Topics
Topics are named buses over which nodes exchange messages. Think of them like radio stations - publishers broadcast on specific topics, and subscribers listen to those topics.

For example, a camera node might publish images on the `/head_camera/image_raw` topic, while a perception node subscribes to this topic to detect objects.

### Messages
Messages are the data structures sent between nodes. They have a specific format defined by message definition files. Common message types include:
- `sensor_msgs/Image`: Camera images
- `sensor_msgs/JointState`: Joint angles and velocities
- `geometry_msgs/Twist`: Velocity commands
- `std_msgs/String`: Text messages

### Services
Services provide a request/reply communication pattern. A client sends a request and waits for a response from a server. For example, you might have a service to calibrate sensors or save robot configurations.

### Actions
Actions are like services but for long-running tasks with feedback. They allow clients to send goals, receive continuous feedback, and get results when tasks complete. Perfect for navigation or manipulation tasks.

## Real-World Example: Humanoid Robot Walking

Let's look at how ROS2 coordinates a humanoid robot taking a step:

1. **Sensor Node**: Publishes joint angles and IMU data to `/joint_states` and `/imu/data` topics
2. **Perception Node**: Subscribes to camera feeds, detects walkable surfaces, publishes to `/walkable_area` topic
3. **Walking Controller**: Subscribes to sensor data and walkable areas, calculates footstep plan, publishes commands to `/leg_controller/command` topic
4. **Motor Controllers**: Receive commands, drive motors, and provide feedback

All of this happens in real-time with precise timing, coordinated through ROS2's communication system.

## Advantages of Using ROS2

- **Modularity**: Components can be developed independently and integrated later
- **Reusability**: Many common robot functions are available as pre-built packages
- **Distributed Computing**: Different parts can run on different computers
- **Community Support**: Large ecosystem of tools and libraries
- **Cross-Platform**: Runs on Linux, Windows, and macOS
- **Real-Time Capabilities**: Support for time-sensitive applications

## Getting Started with ROS2

ROS2 uses a client library called RCL (ROS Client Library). The most common implementations are:
- **rclcpp**: For C++ development
- **rclpy**: For Python development

Most humanoid robot projects use a combination of both, with performance-critical components in C++ and higher-level logic in Python.

## Summary

ROS2 is the foundation that makes complex robot development manageable. For humanoid robots, it's especially crucial because of the many interconnected subsystems that need to work together. In the next chapter, we'll explore how these components actually communicate through ROS2's messaging system.