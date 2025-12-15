# Content Data Model: Physical AI & Humanoid Robotics Educational Book

**Date**: 2025-12-06
**Feature**: 001-book-content
**Status**: Complete

## Overview

This document defines the data model for the educational book content, including the structure of modules, chapters, quizzes, and their relationships. The model ensures consistent organization and progression of educational content from basic to advanced concepts.

## Core Entities

### Book
- **name**: Physical AI & Humanoid Robotics – From Basics to Advanced
- **description**: Comprehensive educational book covering Physical AI and Humanoid Robotics
- **target_audience**: Beginners, students, curious individuals
- **prerequisites**: None (designed for beginners)
- **learning_path**: Sequential modules from Basic → Intermediate → Intermediate → Advanced
- **total_modules**: 4
- **chapters_per_module**: 3
- **assessments_per_module**: 1 quiz

### Module
- **id**: module_{number}_{level}_{descriptor}
- **title**: Descriptive title of the module content
- **level**: basic | intermediate | advanced
- **position**: 1-4 (defines sequence)
- **learning_objectives**: List of what reader will learn
- **prerequisites**: Previous modules/chapters required
- **estimated_duration_hours**: 3-5 hours
- **chapters**: [Chapter IDs]
- **quiz**: Quiz ID
- **success_criteria**: Measurable outcomes for module completion

### Chapter
- **id**: chapter_{module_number}_{chapter_number}_{topic}
- **title**: Specific topic within the module
- **module_id**: Reference to parent module
- **position_in_module**: 1-3 (defines sequence within module)
- **learning_objective**: Specific concept or skill to be learned
- **content_type**: concept | application | case_study | practical
- **key_terms**: List of technical terms defined in chapter
- **examples**: List of real-world examples included
- **prerequisite_knowledge**: Concepts reader should understand
- **followup_chapter**: Next chapter in sequence

### Quiz
- **id**: quiz_{module_number}
- **module_id**: Reference to associated module
- **questions**: List of Question objects
- **passing_score**: 80% (12 out of 15 questions)
- **question_count**: 15 questions per quiz
- **difficulty_level**: Matches associated module level
- **assessment_type**: comprehension | application | analysis

### Question
- **id**: q_{quiz_id}_{number}
- **quiz_id**: Reference to parent quiz
- **question_text**: Clear, unambiguous question
- **question_type**: multiple_choice | true_false | short_answer
- **difficulty**: basic | intermediate | advanced
- **associated_concept**: Which chapter/module concept this tests
- **options**: [Multiple choice options if applicable]
- **correct_answer**: The correct response
- **explanation**: Why the answer is correct

### Technical Term
- **term**: The technical term being defined
- **definition**: Clear, simple explanation
- **chapter_introduced**: Where this term is first defined
- **related_terms**: Associated concepts or terminology
- **examples**: Practical examples of the term in use
- **importance_level**: High | Medium | Low (for emphasis in text)

### Real-World Example
- **id**: example_{module}_{number}
- **title**: Descriptive title of the example
- **module_id**: Which module this example supports
- **chapter_id**: Which chapter this example supports
- **description**: Detailed explanation of the example
- **relevance**: How this connects to the concept being taught
- **complexity_level**: Matches associated content level
- **visual_elements**: Associated diagrams or images

## Content Relationships

### Module → Chapter (One-to-Many)
- Each module contains exactly 3 chapters
- Chapters must be completed in sequence within a module
- Each chapter builds on previous chapter knowledge within the module

### Module → Quiz (One-to-One)
- Each module has exactly one associated quiz
- Quiz tests concepts from all chapters in the module
- Module completion requires passing the associated quiz

### Chapter → Technical Terms (One-to-Many)
- Each chapter may introduce multiple technical terms
- Terms are defined when first introduced
- Later chapters may reference previously defined terms

### Chapter → Real-World Examples (One-to-Many)
- Each chapter should include 2-3 real-world examples
- Examples illustrate the concepts being taught
- Examples are relevant to the target audience level

### Book → Modules (One-to-Many)
- Book contains exactly 4 modules
- Modules must be completed in sequence
- Each module builds on knowledge from previous modules

## Validation Rules

### Module Validation
- Module level must match position (1=Basic, 2-3=Intermediate, 4=Advanced)
- Module must have exactly 3 chapters
- Module must have exactly 1 quiz
- Module estimated duration must be 3-5 hours
- Module learning objectives must align with level

### Chapter Validation
- Chapter position in module must be 1, 2, or 3
- Chapter must belong to exactly one module
- Chapter learning objective must be specific and measurable
- Chapter must not introduce concepts from later chapters
- Chapter must include at least 2 real-world examples

### Quiz Validation
- Quiz must have 15 questions
- Quiz difficulty must match associated module level
- Quiz must test concepts from all 3 chapters in the module
- Quiz passing score must be 80% (12/15)
- Questions must be unambiguous and clear

### Technical Term Validation
- Term must be defined when first introduced
- Term definition must be appropriate for target audience
- Term must be used consistently throughout the book
- Term must be relevant to the chapter content

## State Transitions

### Content Development States
- **Draft**: Initial content creation
- **Reviewed**: Peer review completed
- **Fact-Checked**: Technical accuracy verified
- **Formatted**: Visual design applied
- **Approved**: Ready for publication
- **Published**: Available to readers

### Learning Progression States
- **Not Started**: Module/chapter not yet accessed
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
- Each chapter requires previous chapter in same module
- Technical terms require understanding of foundational concepts

### Cross-Reference Guidelines
- Later modules may reference concepts from earlier modules
- Cross-references must be clear and helpful
- No circular dependencies between chapters/modules
- Prerequisite knowledge clearly stated at chapter beginning