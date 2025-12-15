---
description: Execute a skill from the .claude/skills library
usage: /run <skill-name> [instructions]
---

## STRICT EXECUTION RULES

> [!CAUTION]
> You MUST follow the steps in the SKILL.md file **exactly**. Do NOT improvise, skip steps, or write code unless a step explicitly tells you to.

1. Find the skill file at `.claude/skills/$ARGUMENTS[0]/SKILL.md`.
2. If it does not exist, STOP and report the error to the user.
3. Read the file and **adopt the Role**.
4. Execute ONLY the steps listed in "Process" or "Action", in order.
5. **NEVER write code directly** unless a step says "Generate code for X".
6. If a step says "Run `/sp.specify`", you MUST run that command and WAIT for approval.
7. After completing all steps, STOP. Do not add extra features or run tests.

## User Instructions

{$ARGUMENTS[1...]}
