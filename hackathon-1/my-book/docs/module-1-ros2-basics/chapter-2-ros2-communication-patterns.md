---
title: Chapter 2 - ROS2 Communication Patterns
sidebar_position: 2
---

# Chapter 2: ROS2 Communication Patterns

## Overview of Communication Patterns

In ROS2, there are four main communication patterns that allow nodes to exchange information: **Publish/Subscribe (Topics)**, **Request/Reply (Services)**, **Action-based Communication**, and **Parameters**. Each pattern serves different purposes in robot systems.

## 1. Publish/Subscribe (Topics) - The Most Common Pattern

The publish/subscribe pattern is asynchronous communication where publishers send messages to topics without knowing who receives them, and subscribers receive messages without knowing who sent them.

### How It Works
- Publishers send data to named topics
- Subscribers listen to specific topics
- The ROS2 middleware handles message routing
- Multiple publishers can send to the same topic
- Multiple subscribers can listen to the same topic

### Example: Sensor Data Distribution
```
Camera Node → /camera/image_raw → Perception Node
              /camera/image_raw → Recording Node
              /camera/image_raw → GUI Display Node

IMU Node → /imu/data → Balance Controller
          /imu/data → State Estimation Node
```

### When to Use Topics
- **Streaming data**: Sensor readings, camera images, joint states
- **Broadcasting**: Information that multiple nodes need
- **Real-time systems**: Where low latency is important
- **One-to-many communication**: One source, multiple consumers

### Quality of Service (QoS) Settings
ROS2 provides QoS settings to control message delivery behavior:
- **Reliability**: Best effort vs. reliable delivery
- **Durability**: Volatile vs. transient local (for late-joining subscribers)
- **History**: Keep last N messages vs. keep all messages
- **Depth**: How many messages to queue

For humanoid robots, QoS settings are crucial. For example, joint commands need reliable delivery, while some sensor data might use best-effort to avoid delays.

## 2. Request/Reply (Services) - Synchronous Communication

Services provide synchronous request/reply communication. A client sends a request and waits for a response from a server.

### How It Works
- Client sends a request to a service
- Server processes the request and sends back a response
- Client waits for the response (blocking)
- One-to-one communication

### Example: Robot Services
```
Client: "Please calibrate the IMU"
Server: "Calibration complete" or "Calibration failed"

Client: "Save current joint positions as home pose"
Server: "Home pose saved successfully"
```

### When to Use Services
- **One-time operations**: Calibration, configuration, saving data
- **Querying information**: Getting robot status, current configuration
- **Operations with clear start/end**: Loading/unloading, starting/stopping processes

## 3. Action-based Communication - Long-Running Tasks

Actions are perfect for long-running tasks that require feedback during execution and a final result.

### How It Works
- Client sends a goal to an action server
- Server provides continuous feedback during execution
- Client can monitor progress and cancel if needed
- Server sends final result when complete

### Example: Humanoid Robot Actions
```
Action: /walk_to_location
Goal: Move to coordinates (x=5.0, y=3.0)
Feedback: "Progress: 30% - Current position (x=1.5, y=0.9)"
Result: "Success - Reached destination" or "Failed - Obstacle detected"
```

### When to Use Actions
- **Navigation**: Moving to locations
- **Manipulation**: Grasping objects
- **Complex behaviors**: Walking, dancing, performing tasks
- **Tasks with feedback needs**: Progress monitoring, cancelation

## 4. Parameters - Configuration Values

Parameters are key-value pairs that represent configuration settings for nodes.

### How It Works
- Nodes declare parameters they can accept
- Parameters can be set at startup or changed at runtime
- Useful for configuration values that don't change frequently

### Example: Robot Parameters
```
/joint_controller: max_velocity=2.0
/joint_controller: acceleration_limit=1.0
/perception_node: detection_threshold=0.7
```

## Practical Example: Humanoid Robot Balance System

Let's see how these patterns work together in a humanoid robot's balance system:

### Topics (Publish/Subscribe)
- `/joint_states` - Current joint positions and velocities (published by joint controllers)
- `/imu/data` - Inertial measurement data (published by IMU driver)
- `/center_of_mass` - Estimated center of mass (published by state estimator)

### Services (Request/Reply)
- `/calibrate_sensors` - Calibrate all balance-related sensors
- `/save_home_position` - Save current pose as default standing position

### Actions (Action-based)
- `/balance_adjustment` - Perform complex balance recovery sequence
- `/step_execution` - Execute a single walking step with feedback

### Parameters
- `balance_gain_p` - Proportional gain for balance controller
- `max_tilt_angle` - Maximum acceptable tilt before recovery
- `step_height` - Height of foot during walking steps

## Design Patterns in ROS2

### The Publisher-Subscriber Pattern
Most sensor data flows through topics using this pattern. Multiple nodes can subscribe to the same sensor data without affecting the publisher.

### The Client-Server Pattern
Configuration and one-time operations use services. For example, multiple nodes might need to request robot calibration.

### The Action Server Pattern
Complex behaviors like walking, grasping, or navigation use actions for their progress feedback and cancelation capabilities.

## Best Practices for Communication Design

1. **Choose the right pattern**: Use topics for streaming data, services for one-time operations, actions for long-running tasks
2. **Design clear topic names**: Use descriptive, hierarchical names like `/robot_name/sensor_type/data_type`
3. **Consider message frequency**: Balance between having current data and system load
4. **Use appropriate QoS settings**: Critical control messages need reliable delivery
5. **Plan for system integration**: Consider how different nodes will need to communicate

## Summary

Understanding ROS2 communication patterns is crucial for building effective robot systems. Each pattern serves specific purposes and choosing the right one for each interaction is key to creating robust, efficient humanoid robot applications. In the next chapter, we'll build a simple ROS2 robot application to practice these concepts.