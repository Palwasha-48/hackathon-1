---

description: "Task list template for educational book content creation"
---

# Tasks: [BOOK CONTENT FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for learning objectives), research.md, data-model.md, contracts/

**Assessments**: The examples below include quiz and assessment tasks. These are REQUIRED for educational content - each module must include quizzes for validation.

**Organization**: Tasks are grouped by learning objective/module to enable independent creation and validation of each educational component.

## Format: `[ID] [P?] [Module] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Module]**: Which module/learning objective this task belongs to (e.g., M1, M2, M3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!-- 
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.
  
  The /sp.tasks command MUST replace these with actual tasks based on:
  - Learning objectives from spec.md (with their priorities P1, P2, P3...)
  - Educational requirements from plan.md
  - Content elements from data-model.md
  - Assessment criteria from contracts/

  Tasks MUST be organized by learning objective/module so each can be:
  - Created independently
  - Validated independently
  - Delivered as an educational increment
  
  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan
- [ ] T002 Initialize [language] project with [framework] dependencies
- [ ] T003 [P] Configure linting and formatting tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY module can be created

**⚠️ CRITICAL**: No module work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T004 Setup database schema and migrations framework
- [ ] T005 [P] Implement authentication/authorization framework
- [ ] T006 [P] Setup API routing and middleware structure
- [ ] T007 Create base models/entities that all stories depend on
- [ ] T008 Configure error handling and logging infrastructure
- [ ] T009 Setup environment configuration management

**Checkpoint**: Foundation ready - module creation can now begin in parallel

---

## Phase 3: Module 1 - [Title] (Priority: P1) 🎯 MVP

**Goal**: [Brief description of what readers will learn in this module]

**Independent Validation**: [How to verify this module is complete and educational objectives are met]

### Assessments for Module 1 (REQUIRED for educational content)

> **NOTE: Write these assessments FIRST, ensure they properly validate learning objectives**

- [ ] T010 [P] [M1] Create quiz questions for Module 1 concepts in assessments/module1-quiz.md
- [ ] T011 [P] [M1] Develop practical exercises for Module 1 in exercises/module1-exercises.md

### Content Creation for Module 1

- [ ] T012 [P] [M1] Create Chapter 1 content in content/module1/chapter1.md
- [ ] T013 [P] [M1] Create Chapter 2 content in content/module1/chapter2.md
- [ ] T014 [M1] Create Chapter 3 content in content/module1/chapter3.md (depends on T012, T013)
- [ ] T015 [M1] Add Module 1 introduction and learning objectives to content/module1/intro.md
- [ ] T016 [M1] Add visual elements and formatting for Module 1 content
- [ ] T017 [M1] Add Module 1 summary and transition to Module 2

**Checkpoint**: At this point, Module 1 should be fully complete and educationally validated

---

## Phase 4: Module 2 - [Title] (Priority: P2)

**Goal**: [Brief description of what readers will learn in this module]

**Independent Validation**: [How to verify this module is complete and educational objectives are met]

### Assessments for Module 2 (REQUIRED for educational content)

- [ ] T018 [P] [M2] Create quiz questions for Module 2 concepts in assessments/module2-quiz.md
- [ ] T019 [P] [M2] Develop practical exercises for Module 2 in exercises/module2-exercises.md

### Content Creation for Module 2

- [ ] T020 [P] [M2] Create Chapter 1 content in content/module2/chapter1.md
- [ ] T021 [M2] Implement [content] in content/module2/[topic].md
- [ ] T022 [M2] Implement [content] in content/module2/[topic].md
- [ ] T023 [M2] Integrate with Module 1 concepts (if needed)

**Checkpoint**: At this point, Modules 1 AND 2 should both be complete and educationally sound

---

## Phase 5: Module 3 - [Title] (Priority: P3)

**Goal**: [Brief description of what readers will learn in this module]

**Independent Validation**: [How to verify this module is complete and educational objectives are met]

### Assessments for Module 3 (REQUIRED for educational content)

- [ ] T024 [P] [M3] Create quiz questions for Module 3 concepts in assessments/module3-quiz.md
- [ ] T025 [P] [M3] Develop practical exercises for Module 3 in exercises/module3-exercises.md

### Content Creation for Module 3

- [ ] T026 [P] [M3] Create [content] in content/module3/[topic].md
- [ ] T027 [M3] Implement [content] in content/module3/[topic].md
- [ ] T028 [M3] Implement [content] in content/module3/[topic].md

**Checkpoint**: All modules should now be educationally complete

---

[Add more module phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] TXXX [P] Documentation updates in docs/
- [ ] TXXX Code cleanup and refactoring
- [ ] TXXX Performance optimization across all stories
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [ ] TXXX Security hardening
- [ ] TXXX Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all modules
- **Modules (Phase 3+)**: All depend on Foundational phase completion
  - Modules can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired modules being complete

### Module Dependencies

- **Module 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other modules
- **Module 2 (P2)**: Can start after Foundational (Phase 2) - May build on Module 1 concepts but should be educationally self-contained
- **Module 3 (P3)**: Can start after Foundational (Phase 2) - May build on Module 1/2 concepts but should be educationally self-contained

### Within Each Module

- Assessments (required) MUST be designed to validate learning objectives
- Introductory content before detailed concepts
- Concepts before practical applications
- Core content before advanced topics
- Module complete when all chapters and assessments are ready

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all modules can start in parallel (if team capacity allows)
- All assessments for a module marked [P] can be designed in parallel
- Chapters within a module marked [P] can be written in parallel
- Different modules can be worked on in parallel by different team members

---

## Parallel Example: Module 1

```bash
# Launch all assessments for Module 1 together:
Task: "Create quiz questions for Module 1 concepts in assessments/module1-quiz.md"
Task: "Develop practical exercises for Module 1 in exercises/module1-exercises.md"

# Launch all chapters for Module 1 together:
Task: "Create Chapter 1 content in content/module1/chapter1.md"
Task: "Create Chapter 2 content in content/module1/chapter2.md"
```

---

## Content Creation Strategy

### MVP First (Module 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all modules)
3. Complete Phase 3: Module 1
4. **STOP and VALIDATE**: Validate Module 1 educational objectives independently
5. Review/publish if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add Module 1 → Validate independently → Review/Publish (MVP!)
3. Add Module 2 → Validate independently → Review/Publish
4. Add Module 3 → Validate independently → Review/Publish
5. Each module adds educational value while maintaining progression

### Parallel Team Strategy

With multiple content creators:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Creator A: Module 1
   - Creator B: Module 2
   - Creator C: Module 3
3. Modules complete and maintain educational coherence

---

## Notes

- [P] tasks = different files, no dependencies
- [Module] label maps task to specific module/learning objective for traceability
- Each module should be independently completable and educationally validated
- Ensure assessments properly validate learning objectives
- Commit after each task or logical group
- Stop at any checkpoint to validate module educational completeness
- Avoid: vague tasks, same file conflicts, cross-module dependencies that break educational progression
