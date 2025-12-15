# Content Data Model: Physical AI & Humanoid Robotics Course

**Date**: 2025-12-06
**Feature**: 001-course-content
**Status**: Complete

## Overview

This document defines the data model for the educational course content, including the structure of modules, lessons, quizzes, and their relationships. The model ensures consistent organization and progression of educational content from ROS2 basics to Vision-Language-Action systems.

## Core Entities

### Course
- **name**: Physical AI & Humanoid Robotics Course
- **description**: Comprehensive course covering ROS2, Digital Twin simulation, Isaac Sim, and Vision-Language-Action systems
- **target_audience**: Beginners with minimal programming experience
- **prerequisites**: Basic computer literacy
- **learning_path**: Sequential modules from ROS2 basics to VLA systems
- **total_modules**: 4
- **lessons_per_module**: 3
- **assessments_per_module**: 1 quiz

### Module
- **id**: module_{number}_{descriptor}
- **title**: Descriptive title of the module content
- **position**: 1-4 (defines sequence: ROS2 → Digital Twin → Isaac → VLA)
- **learning_objectives**: List of what learner will learn
- **prerequisites**: Previous modules/lessons required
- **estimated_duration_hours**: 4-6 hours
- **lessons**: [Lesson IDs]
- **quiz**: Quiz ID
- **success_criteria**: Measurable outcomes for module completion

### Lesson
- **id**: lesson_{module_number}_{lesson_number}_{topic}
- **title**: Specific topic within the module
- **module_id**: Reference to parent module
- **position_in_module**: 1-3 (defines sequence within module)
- **learning_objective**: Specific concept or skill to be learned
- **content_type**: concept | application | practical | example
- **key_terms**: List of technical terms defined in lesson
- **examples**: List of practical robotics examples included
- **prerequisite_knowledge**: Concepts learner should understand
- **followup_lesson**: Next lesson in sequence

### Quiz
- **id**: quiz_{module_number}
- **module_id**: Reference to associated module
- **questions**: List of Question objects
- **passing_score**: 80% (typically 12 out of 15 questions)
- **question_count**: 15 questions per quiz
- **difficulty_level**: Matches associated module level
- **assessment_type**: comprehension | application | practical

### Question
- **id**: q_{quiz_id}_{number}
- **quiz_id**: Reference to parent quiz
- **question_text**: Clear, unambiguous question
- **question_type**: multiple_choice | true_false | practical_scenario
- **difficulty**: beginner | intermediate | advanced
- **associated_concept**: Which lesson/module concept this tests
- **options**: [Multiple choice options if applicable]
- **correct_answer**: The correct response
- **explanation**: Why the answer is correct

### Technical Term
- **term**: The technical term being defined
- **definition**: Clear, simple explanation appropriate for beginners
- **lesson_introduced**: Where this term is first defined
- **related_terms**: Associated concepts or terminology
- **examples**: Practical examples of the term in use
- **importance_level**: High | Medium | Low (for emphasis in text)

### Practical Example
- **id**: example_{module}_{number}
- **title**: Descriptive title of the example
- **module_id**: Which module this example supports
- **lesson_id**: Which lesson this example supports
- **description**: Detailed explanation of the example
- **relevance**: How this connects to the concept being taught
- **complexity_level**: Matches associated content level
- **visual_elements**: Associated diagrams or code examples

## Content Relationships

### Module → Lesson (One-to-Many)
- Each module contains exactly 3 lessons
- Lessons must be completed in sequence within a module
- Each lesson builds on previous lesson knowledge within the module

### Module → Quiz (One-to-One)
- Each module has exactly one associated quiz
- Quiz tests concepts from all lessons in the module
- Module completion requires passing the associated quiz

### Lesson → Technical Terms (One-to-Many)
- Each lesson may introduce multiple technical terms
- Terms are defined when first introduced
- Later lessons may reference previously defined terms

### Lesson → Practical Examples (One-to-Many)
- Each lesson should include 2-3 practical robotics examples
- Examples illustrate the concepts being taught
- Examples are relevant to the target audience level

### Course → Modules (One-to-Many)
- Course contains exactly 4 modules
- Modules must be completed in sequence
- Each module builds on knowledge from previous modules

## Validation Rules

### Module Validation
- Module position must be 1, 2, 3, or 4
- Module must have exactly 3 lessons
- Module must have exactly 1 quiz
- Module estimated duration must be 4-6 hours
- Module learning objectives must align with technology focus

### Lesson Validation
- Lesson position in module must be 1, 2, or 3
- Lesson must belong to exactly one module
- Lesson learning objective must be specific and measurable
- Lesson must not introduce concepts from later lessons
- Lesson must include at least 2 practical robotics examples

### Quiz Validation
- Quiz must have 15 questions
- Quiz difficulty must match associated module level
- Quiz must test concepts from all 3 lessons in the module
- Quiz passing score must be 80%
- Questions must be unambiguous and clear

### Technical Term Validation
- Term must be defined when first introduced
- Term definition must be appropriate for beginner audience
- Term must be used consistently throughout the course
- Term must be relevant to the lesson content

## State Transitions

### Content Development States
- **Draft**: Initial content creation
- **Reviewed**: Peer review completed
- **Fact-Checked**: Technical accuracy verified
- **Formatted**: Visual design applied
- **Approved**: Ready for publication
- **Published**: Available to learners

### Learning Progression States
- **Not Started**: Module/lesson not yet accessed
- **In Progress**: Currently being studied
- **Completed**: Content finished but quiz not taken
- **Assessed**: Quiz completed
- **Mastered**: Quiz passed (80%+)
- **Advanced**: Ready for next module

## Content Dependencies

### Prerequisites Structure
- Module 2 requires Module 1 completion
- Module 3 requires Module 2 completion
- Module 4 requires Module 3 completion
- Each lesson requires previous lesson in same module
- Technical terms require understanding of foundational concepts

### Cross-Reference Guidelines
- Later modules may reference concepts from earlier modules
- Cross-references must be clear and helpful
- No circular dependencies between lessons/modules
- Prerequisite knowledge clearly stated at lesson beginning
- Practical examples should build on previous examples when possible