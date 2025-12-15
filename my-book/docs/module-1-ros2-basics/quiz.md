---
title: Module 1 Quiz - ROS2 Basics
sidebar_position: 4
---

# Module 1 Quiz: ROS2 Basics

Test your understanding of ROS2 fundamentals with this quiz. Each question has one correct answer unless specified otherwise.

## Question 1: What is ROS2?
A) A real-time operating system for robots
B) A flexible framework for writing robot software
C) A programming language for robotics
D) A hardware platform for robot development

<details>
<summary>Click to reveal answer</summary>

**Answer: B) A flexible framework for writing robot software**

ROS2 is not an operating system but a collection of tools, libraries, and conventions that help developers create robot applications. It provides communication infrastructure, development tools, and reusable components.

</details>

## Question 2: Which communication pattern is best for streaming sensor data?
A) Services
B) Actions
C) Topics (Publish/Subscribe)
D) Parameters

<details>
<summary>Click to reveal answer</summary>

**Answer: C) Topics (Publish/Subscribe)**

Topics are ideal for streaming data like sensor readings because they're asynchronous, allow multiple subscribers, and provide low-latency communication. Sensors continuously publish data that multiple nodes might need simultaneously.

</details>

## Question 3: What are the main components of a ROS2 system? (Select all that apply)
A) Nodes
B) Topics
C) Messages
D) Services
E) All of the above

<details>
<summary>Click to reveal answer</summary>

**Answer: E) All of the above**

ROS2 systems consist of nodes (processes that perform computation), topics (named buses for message exchange), messages (data structures), and services (request/reply communication), along with actions and parameters.

</details>

## Question 4: True or False: In ROS2, publishers know which subscribers are listening to their topics.
A) True
B) False

<details>
<summary>Click to reveal answer</summary>

**Answer: B) False**

In the publish/subscribe pattern, publishers send messages to topics without knowing who receives them, and subscribers receive messages without knowing who sent them. This decoupling is a key advantage of this pattern.

</details>

## Question 5: Which communication pattern would be best for commanding a robot to navigate to a specific location?
A) Topic
B) Service
C) Action
D) Parameter

<details>
<summary>Click to reveal answer</summary>

**Answer: C) Action**

Actions are perfect for long-running tasks like navigation that require feedback during execution (e.g., "30% to destination") and the ability to cancel the operation. Navigation typically takes time and needs to report progress.

</details>

## Question 6: What is the primary purpose of Quality of Service (QoS) settings in ROS2?
A) To limit the number of nodes that can run
B) To control message delivery behavior and performance characteristics
C) To encrypt ROS2 communications
D) To automatically generate documentation

<details>
<summary>Click to reveal answer</summary>

**Answer: B) To control message delivery behavior and performance characteristics**

QoS settings allow you to configure reliability (best effort vs. reliable), durability (volatile vs. transient), history (how many messages to keep), and other parameters that affect how messages are delivered in the system.

</details>

## Question 7: Which ROS2 client libraries are commonly used? (Select all that apply)
A) rclcpp (for C++)
B) rclpy (for Python)
C) rcljava (for Java)
D) All of the above

<details>
<summary>Click to reveal answer</summary>

**Answer: D) All of the above**

ROS2 supports multiple client libraries including rclcpp for C++, rclpy for Python, rcljava for Java, and others. This allows developers to use their preferred programming language while maintaining ROS2 communication capabilities.

</details>

## Question 8: In the context of humanoid robots, what role does ROS2 typically play?
A) Providing the operating system for the robot's computer
B) Serving as the "nervous system" that connects different robot components
C) Controlling the robot's physical movements directly
D) Storing the robot's learned behaviors

<details>
<summary>Click to reveal answer</summary>

**Answer: B) Serving as the "nervous system" that connects different robot components**

ROS2 handles communication between different parts of a humanoid robot - sensors, actuators, controllers, AI systems - allowing them to work together seamlessly. It's the middleware that enables distributed robot software development.

</details>

## Question 9: Which command would you use to see all available ROS2 topics?
A) ros2 show topics
B) ros2 list topics
C) ros2 topic list
D) ros2 topic show

<details>
<summary>Click to reveal answer</summary>

**Answer: C) ros2 topic list**

The `ros2 topic list` command displays all currently available topics in the ROS2 system. You can also use `ros2 topic list -t` to see topic types as well.

</details>

## Question 10: What is the purpose of the ROS2 parameter system?
A) To store configuration values for nodes
B) To send messages between nodes
C) To control robot hardware directly
D) To visualize robot data

<details>
<summary>Click to reveal answer</summary>

**Answer: A) To store configuration values for nodes**

Parameters are key-value pairs that represent configuration settings for nodes. They're used for values that don't change frequently but may need to be adjusted, like controller gains or sensor thresholds.

</details>

## Scoring

- 9-10 correct: Excellent! You have a solid understanding of ROS2 fundamentals.
- 7-8 correct: Good job! You understand the core concepts with room for deeper exploration.
- 5-6 correct: You have a basic understanding but should review the material.
- Below 5: Consider reviewing the module content before proceeding to the next module.

## Next Steps

Once you've completed this quiz and feel confident about ROS2 concepts, proceed to Module 2: Digital Twin Technologies (Gazebo/Unity) where you'll learn how to simulate and test your robot systems in virtual environments.