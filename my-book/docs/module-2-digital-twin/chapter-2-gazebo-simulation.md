---
title: Chapter 2 - Gazebo Simulation for Robotics
sidebar_position: 2
---

# Chapter 2: Gazebo Simulation for Robotics

## Introduction to Gazebo

Gazebo is a powerful, open-source robotics simulator that provides high-fidelity physics simulation, realistic sensor models, and convenient interfaces for robotics development. It's widely used in both academic and industrial robotics research, particularly for humanoid robot development.

Gazebo operates on the concept of "worlds" - virtual environments where robots can be placed, controlled, and observed. These worlds can contain static objects, dynamic objects, and various environmental conditions.

## Why Gazebo is Perfect for Humanoid Robots

### Physics Accuracy
Gazebo uses the ODE (Open Dynamics Engine) physics engine, which is well-suited for humanoid robot simulation:
- Accurate collision detection and response
- Realistic contact physics for walking and manipulation
- Support for complex multi-body dynamics
- Proper handling of balance and stability scenarios

### Sensor Simulation
Gazebo provides realistic simulation of various robot sensors:
- **Cameras**: With distortion, noise, and resolution settings
- **LIDAR**: Accurate distance measurements with configurable parameters
- **IMU**: Inertial measurements with drift and noise characteristics
- **Force/Torque sensors**: Contact force measurements
- **GPS**: Global positioning with realistic accuracy limitations

### Integration with ROS
Gazebo has deep integration with ROS/ROS2:
- Direct publishing to ROS topics from simulated sensors
- Receiving ROS messages to control simulated actuators
- Launch file integration for easy setup
- Plugin system for custom behaviors

## Setting Up Gazebo

### Installation
Gazebo can be installed as a standalone application or as part of a ROS distribution:

```bash
# For ROS2 Humble on Ubuntu
sudo apt install ros-humble-gazebo-ros-pkgs

# Launch Gazebo standalone
gz sim
```

### Basic Gazebo Concepts

#### Worlds
World files (`.sdf` format) define the environment:
- Static and dynamic objects
- Lighting conditions
- Physics parameters
- Initial robot placements

Example world file structure:
```xml
<sdf version="1.7">
  <world name="humanoid_lab">
    <!-- Physics engine settings -->
    <physics type="ode">
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1.0</real_time_factor>
    </physics>

    <!-- Ground plane -->
    <include>
      <uri>model://ground_plane</uri>
    </include>

    <!-- Lighting -->
    <include>
      <uri>model://sun</uri>
    </include>

    <!-- Your robot model -->
    <include>
      <uri>model://simple_humanoid</uri>
      <pose>0 0 1.0 0 0 0</pose>
    </include>
  </world>
</sdf>
```

#### Models
Robot models in Gazebo are defined using SDF (Simulation Description Format) or URDF (Unified Robot Description Format):
- **Links**: Physical components with geometry and mass
- **Joints**: Connections between links with constraints
- **Sensors**: Virtual sensors attached to links
- **Plugins**: Custom behaviors and ROS interfaces

## Creating a Simple Humanoid Robot in Gazebo

### URDF to SDF Conversion
Most robots are defined in URDF format, which Gazebo can automatically convert to SDF:

```xml
<!-- Example URDF for a simple humanoid robot -->
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
    <collision>
      <geometry>
        <box size="0.3 0.2 0.5"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="5.0"/>
      <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0"/>
    </inertial>
  </link>

  <!-- Head -->
  <link name="head">
    <visual>
      <geometry>
        <sphere radius="0.1"/>
      </geometry>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.1"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="1.0"/>
      <inertia ixx="0.01" ixy="0.0" ixz="0.0" iyy="0.01" iyz="0.0" izz="0.01"/>
    </inertial>
  </link>

  <joint name="neck_joint" type="revolute">
    <parent link="base_link"/>
    <child link="head"/>
    <origin xyz="0 0 0.4"/>
    <axis xyz="0 1 0"/>
    <limit lower="-0.5" upper="0.5" effort="100" velocity="1"/>
  </joint>

  <!-- Additional joints for arms and legs would follow -->
</robot>
```

### Gazebo-Specific Extensions
You can add Gazebo-specific extensions to your URDF:

```xml
<gazebo reference="base_link">
  <material>Gazebo/Blue</material>
</gazebo>

<gazebo reference="head">
  <material>Gazebo/White</material>
</gazebo>

<!-- Add a camera sensor -->
<gazebo reference="head">
  <sensor type="camera" name="head_camera">
    <update_rate>30.0</update_rate>
    <camera name="head">
      <horizontal_fov>1.3962634</horizontal_fov>
      <image>
        <width>640</width>
        <height>480</height>
        <format>R8G8B8</format>
      </image>
      <clip>
        <near>0.1</near>
        <far>100</far>
      </clip>
    </camera>
    <plugin name="camera_controller" filename="libgazebo_ros_camera.so">
      <frame_name>head_camera_optical_frame</frame_name>
      <topic_name>/head_camera/image_raw</topic_name>
    </plugin>
  </sensor>
</gazebo>
```

## Controlling Robots in Gazebo

### Joint Control
Gazebo supports various control methods:
- **Position control**: Set desired joint angles
- **Velocity control**: Set desired joint velocities
- **Effort control**: Apply desired torques/forces
- **PID controllers**: Built-in or custom controllers

### ROS Integration
Gazebo plugins enable ROS communication:
- `libgazebo_ros_joint_state_publisher`: Publish joint states
- `libgazebo_ros_diff_drive`: Differential drive control
- `libgazebo_ros_p3d`: 3D position/velocity feedback
- Custom plugins for specialized control

Example launch file to start Gazebo with a robot:
```xml
<launch>
  <!-- Start Gazebo -->
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$(find my_robot_description)/worlds/humanoid_lab.world"/>
  </include>

  <!-- Spawn robot in Gazebo -->
  <node name="spawn_urdf" pkg="gazebo_ros" type="spawn_model"
        args="-file $(find my_robot_description)/urdf/simple_humanoid.urdf
              -urdf -model simple_humanoid -x 0 -y 0 -z 1.0"/>

  <!-- Robot state publisher -->
  <node name="robot_state_publisher" pkg="robot_state_publisher"
        type="robot_state_publisher" />
</launch>
```

## Physics Configuration for Humanoid Robots

### Time Stepping
For stable humanoid simulation:
```xml
<physics type="ode">
  <max_step_size>0.001</max_step_size>  <!-- Small steps for stability -->
  <real_time_factor>1.0</real_time_factor>  <!-- Real-time simulation -->
  <real_time_update_rate>1000</real_time_update_rate>  <!-- High update rate -->
</physics>
```

### Contact Parameters
Important for stable walking:
```xml
<ode>
  <solver>
    <type>quick</type>
    <iters>10</iters>
    <sor>1.3</sor>
  </solver>
  <constraints>
    <cfm>0.0</cfm>
    <erp>0.2</erp>
    <contact_max_correcting_vel>100.0</contact_max_correcting_vel>
    <contact_surface_layer>0.001</contact_surface_layer>
  </constraints>
</ode>
```

## Advanced Gazebo Features

### Plugins System
Gazebo's plugin system allows custom behaviors:
- **Model plugins**: Add behaviors to specific models
- **World plugins**: Add global simulation behaviors
- **Sensor plugins**: Process sensor data
- **System plugins**: Modify core simulation

### Sensors and Actuators
Gazebo provides realistic simulation of various sensors:
- **Depth cameras**: RGB-D sensors with depth information
- **3D LIDAR**: Multi-line laser range finders
- **Force sensors**: Joint force/torque measurements
- **IMU sensors**: Inertial measurement units
- **GPS sensors**: Global positioning simulation

### Environments and Scenarios
Gazebo can simulate various environments:
- **Indoor scenarios**: Rooms, corridors, furniture
- **Outdoor environments**: Terrain, weather, lighting
- **Dynamic obstacles**: Moving objects and people
- **Interactive elements**: Doors, switches, tools

## Best Practices for Humanoid Robot Simulation

### Model Accuracy
- Use realistic mass and inertial properties
- Accurate joint limits and friction parameters
- Proper collision geometry (not just visual geometry)
- Realistic actuator dynamics and limitations

### Physics Tuning
- Start with conservative parameters and tune gradually
- Use smaller time steps for stability
- Adjust contact parameters for realistic interaction
- Balance accuracy with computational performance

### Validation
- Compare simulation and real robot behavior
- Use system identification to tune models
- Test on increasingly complex scenarios
- Document the reality gap for your specific application

## Real-World Example: Gazebo in Humanoid Development

The ROSIN project (ROS-Industrial) extensively uses Gazebo for humanoid robot development:

1. **Model Development**: Teams create detailed robot models with accurate physics
2. **Controller Testing**: Walking and manipulation controllers are validated in simulation
3. **Integration Testing**: Multi-robot scenarios are tested before deployment
4. **Training**: AI systems are trained in simulation before real-world deployment

This approach has enabled faster development cycles and safer testing of complex humanoid behaviors.

## Summary

Gazebo is a powerful tool for humanoid robot development, providing realistic physics simulation and seamless ROS integration. Understanding how to properly configure and use Gazebo is essential for effective robot development. The next chapter will explore Unity as an alternative simulation platform with different strengths and capabilities.