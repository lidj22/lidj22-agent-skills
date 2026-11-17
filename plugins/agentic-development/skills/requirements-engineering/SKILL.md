---
name: requirements-engineering
description: "Perform requirements engineering (RE) related tasks. Description TBD. See README.md."
---

# Requirements Engineering (RE)

## Definitions

- Artifact: any documentation, can be note, code piece, powerpoint slide, napkin note

Processes

- Elicitation: process of finding what the requirements are
- Analysis: identify inconsistencies and contradictions within existing requirements
- Documentation: writing the stakeholder requirements down
- Verification: did i correctly write down what these people say/am i building the system right
- Validation: (to stakeholders) is this what you really need/am i building the right system

Requirement types:

- Quality requirement
- Non-functional requirement

Techniques for developing requirements:

- natural language requirements
- modeled requirements
  - graphs (e.g. UML/mermaid)
  - formulas (math representation)
  - code (pseudocode, prototype)
- artifact-based RE
  - goals
  - stakeholders
  - constraints

## Processes

> TODO: this should be a conditional path.

Process (software engineering); state diagram omitted:

1. requirements engineering
2. design
3. implementation
4. testing
5. deployment/installation
6. maintenance/evolution

And during the process, many stages loop all the way back.

The RE Process itself is broken to 4 parts:

1. req. elicitation: reach out to stakeholders (wishes, constraints, needs)
2. analysis
3. documentation
4. verification + validation

Subsystems and Twin Peaks

Q: What happens when going back from design to RE?

1. RE of a system
2. design of system (have subsystems)
3. RE of a subsystem
4. ... (repeat)
