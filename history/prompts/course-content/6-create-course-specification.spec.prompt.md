---
id: 6
title: create-course-specification
stage: spec
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: course-content
branch: 001-course-content
user: Claude Code
command: /sp.specify
labels: ["specification","educational-content","robotics-course"]
links:
  spec: specs/001-course-content/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-course-content/spec.md
 - specs/001-course-content/checklists/requirements.md
tests:
 - none
---

## Prompt

```text
i also want updation in specify file. Define the content:
- Course intro
- Module 1: ROS2 (nodes, topics, Python agents, URDF)
- Module 2: Gazebo/Unity (physics, collisions, sensors)
- Module 3: Isaac Sim (VSLAM, nav, synthetic data, Nav2)
- Module 4: VLA (Whisper, GPT commands, task→actions)
Audience: beginners. Outcome: structured course.
```

## Response snapshot

Created comprehensive specification for Physical AI & Humanoid Robotics course with 4 technology-focused modules: ROS2 basics, Digital Twin simulation, Isaac Sim integration, and Vision-Language-Action systems. Defined 5 learning objectives with proper progression from course introduction through advanced AI integration. Specified educational requirements matching user's technology requirements and success criteria for beginner-appropriate learning outcomes.

## Outcome

- ✅ Impact: Complete course content specification with technology-focused modules
- 🧪 Tests: none
- 📁 Files: spec.md and requirements checklist created
- 🔁 Next prompts: /sp.plan to create implementation plan
- 🧠 Reflection: Specification successfully structured for technology-focused robotics course

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create implementation plan for course development