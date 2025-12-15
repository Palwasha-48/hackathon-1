import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Manual sidebar for the Physical AI & Humanoid Robotics book
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Introduction',
      items: ['course-introduction/index'],
      collapsed: false
    },
    {
      type: 'category',
      label: 'Module 1: ROS2 Basics',
      items: [
        'module-1-ros2-basics/index',
        'module-1-ros2-basics/chapter-1-intro-to-ros2-concepts',
        'module-1-ros2-basics/chapter-2-ros2-communication-patterns',
        'module-1-ros2-basics/chapter-3-building-first-ros2-application',
        'module-1-ros2-basics/quiz'
      ],
      collapsed: false
    },
    {
      type: 'category',
      label: 'Module 2: Digital Twin Technologies (Gazebo/Unity)',
      items: [
        'module-2-digital-twin/index',
        'module-2-digital-twin/chapter-1-intro-to-digital-twins',
        'module-2-digital-twin/chapter-2-gazebo-simulation',
        'module-2-digital-twin/chapter-3-unity-for-robot-simulation',
        'module-2-digital-twin/quiz'
      ],
      collapsed: false
    },
    {
      type: 'category',
      label: 'Module 3: Isaac Sim',
      items: [
        'module-3-isaac-sim/index',
        'module-3-isaac-sim/chapter-1-intro-to-isaac-sim',
        'module-3-isaac-sim/chapter-2-robot-simulation-control',
        'module-3-isaac-sim/chapter-3-ai-training-computer-vision',
        'module-3-isaac-sim/quiz'
      ],
      collapsed: false
    },
    {
      type: 'category',
      label: 'Module 4: VLA Systems',
      items: [
        'module-4-vla-systems/index',
        'module-4-vla-systems/chapter-1-intro-to-vla-systems',
        'module-4-vla-systems/chapter-2-vla-architecture-implementation',
        'module-4-vla-systems/chapter-3-vla-applications-future',
        'module-4-vla-systems/quiz'
      ],
      collapsed: false
    }
  ],
};

export default sidebars;
