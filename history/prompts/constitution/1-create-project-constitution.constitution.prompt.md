---
id: 1
title: create-project-constitution
stage: constitution
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: Claude Code
command: /sp.constitution
labels: ["constitution","project-setup","spec-driven-development"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - none
---

## Prompt

```text
Project Name: Physical AI & Humanoid Robotics – From Basics to Advanced
Purpose:
Create a fully structured educational book that teaches Physical AI and Humanoid Robotics in simple, clear, and engaging language. The book must guide readers from foundational concepts to advanced systems using an easy, approachable writing style.
Project Principles:
The book must be divided into 4 modules, each containing 3 chapters, followed by 1 quiz per module.
The book must start with a detailed introduction explaining what Physical AI is, what Humanoid Robotics is, what the reader will learn, and how the book is structured.
Module progression must follow this order:
Module 1 → Basic
Module 2 → Intermediate
Module 3 → Intermediate
Module 4 → Advanced
All writing must use simple, clear, human-friendly language that even beginners can understand.
Visual feel must be strong:
Clean fonts
Pleasant color themes (described textually)
Easy-to-read formatting
The book content must maintain conceptual depth without overwhelming the reader.
The structure should always remain:
Book Introduction → 4 Modules → (Each with 3 Chapters + Quiz)
Technical accuracy, clarity, and educational usefulness must be maintained throughout.
Additional helpful or valuable topics may be added when beneficial.
The tone must stay encouraging, friendly, and motivating.
```

## Response snapshot

Updated the project constitution and aligned templates for the Physical AI & Humanoid Robotics educational book project. Created a new constitution with 6 core principles: Educational Structure and Progression, Accessibility and Clarity, Visual Design Excellence, Sequential Learning Path, Content Quality and Accuracy, and Comprehensive Coverage. Updated dependent templates to align with educational book requirements: plan-template.md now includes educational constitution checks, spec-template.md updated with learning objectives instead of user stories, and tasks-template.md adapted for module-based content creation with assessments.

## Outcome

- ✅ Impact: Created new project constitution and updated templates for educational book project
- 🧪 Tests: none
- 📁 Files: 4 files updated (constitution + 3 templates)
- 🔁 Next prompts: /sp.specify to create feature specification
- 🧠 Reflection: Templates successfully adapted from software development to educational content creation context

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create feature specification for first module