# User guide

Use requirements-engineering to establish what an effort must achieve, make assignments usable, inspect whether work meets requirements, and maintain meaning as evidence changes. The same agent can perform RE and development; each activity retains its own purpose and evidence.

## Requests and results

| Request | Useful result |
| --- | --- |
| “Work out what needs to change.” | Problem context, affected stakeholders, candidate requirements, and consequential choices. |
| “Recover the requirements from these conversations and issues.” | A consolidated record with material source relationships, authority, and unresolved interpretations. |
| “Check this task before I give it to an agent.” | Concrete prompt corrections, missing inputs or dependencies, and evidence needed for completion. |
| “This does not do what we agreed.” | A comparison of the requirement and actual behavior, identifying whether the gap concerns implementation, specification, or the underlying need. |
| “Explain what the implementation accomplishes.” | A stakeholder-readable account of outcomes supported by the implementation evidence and the remaining gaps. |
| “Continue this work with the new stakeholder message.” | Recovered decisions and records, affected requirements and assignments updated or flagged. |

Supply existing sources and artifacts when available. State the intended decision or deliverable when known. Missing information is part of the work: the agent retrieves accessible evidence and distinguishes investigable questions from stakeholder choices.

Outputs use the project's existing artifact structure. A useful requirements record connects needs to required behavior and qualities, source meaning, constraints, decisions, and unresolved matters. Its location and significant dependencies support continuation by another consumer.

## Decisions and boundaries

Editing, publication, implementation, and acceptance follow the applicable project rules and existing authorization. Stakeholder feedback has scope and authority; a completed draft or agent review does not create acceptance. Already-settled decisions remain settled unless relevant evidence or authorized direction changes them.

The skill supplies requirements methods and the requirements side of development handoffs. Development and orchestration workflows supply implementation, test execution, model selection, and runtime control. RE may reveal a missing requirement inside those workflows without taking over the entire assignment.

## Further guidance

The [entry point](../SKILL.md) routes assignments to methods. [Process foundations](foundations.md) supports tailoring and requirements–architecture investigation; the [content model](content-model.md) relates information across artifacts. Source material, terminology provenance, and adaptation notices are available in [sources](sources.md).
