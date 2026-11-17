Requirements engineering development notes, guideline, philosophy. This branch is for demonstration purposes only, and does not claim to implement a complete requirements engineering skill; do not merge the skill.

These are my notes not part of the skill. Read how this works, how commits are intentionally prepared in their chronological and motivating order.

The purpose of this skill has already been outlined under https://github.com/lidj22/lidj22-agent-skills/issues/1. The ongoing attempt is in https://github.com/lidj22/lidj22-agent-skills/pull/7 and motivates this branch's creation to demonstrate how things should be done.

Penzenstadler's course material forms a progressive outline of what the skill should look like, where terminology should be inherited.

It is not supposed to be a faithful 1-1 copy of every sentence. It is a primary material with which supplementary experience, interpretations, assignments are anchored onto. Note also how even though I'm writing based on lecture videos, I'm also drawing on agent development and SDD concepts.

To copy/paste the full structure 1-1 and do nothing further, or in any way perform no transformative change such that the skill inherits copyright licenses, confidently disqualifies any PR opened against this repository.

## Glossary

- Ordinary path: a path loaded into frequently by agent across most tasks. Can be further specified by "ordinary context path", "ordinary task path", etc. Otherwise, it's a "conditional" path (subject to conditions) or "exceptional" path (a rare condition).
    - SKILL.md is part of ordinary path, because it's loaded by all consumers.
    - README.md is part of conditional path, because skill consumers are not expected to read it unless they are supposed to develop an equivalent skill.

Ordinary path files should carry universal or high-frequency concepts, while deferring non-essential details to conditional paths for clarification.

- "We define X here. For Lean formalization, refer to [Y](Y) instead."

Citations, provenance, history, belong either in an exceptional path, or do not belong in source at all. See https://github.com/lidj22/lidj22-agent-skills/issues/5.

## Methodology

When populating the skill with concepts/methods, frequently reflect on:

- are these ordinary path, or conditional path?
- what tasks does course or other material formalize for common agentic development tasks?

The course discusses "learning goals"; our skill must transform learning goals into application and reliable execution.

## Evaluation

> Outline the tasks and sub-tasks that an RE is expected to identify and perform.

For this section, we refer to an RE (requirements engineer) as an agent subject to RE assignments, and may/may not have loaded an RE skill. The skill does not need to be this skill; it simply needs to implement RE framework.

### Conceptual Question/Answering

Most basic: an RE is expected to know what requirements engineering is, and answer conceptual questions under the framework as outlined by the course.

- What is elicitation?
- What is the difference between quality requirement and non-functional requirement (NFR)?

Knowing what "elicitation" is, however, does not translate to "performing effective, high quality elicitation."

- When does this skill apply? Process (lecture 2) covers software development vs. requirements engineering.
    - "This isn't doing what we said it would"
    - "This didn't work as expected" -> "fix design"
    - "I forgot to talk to this team about the feature" -> stakeholder

Verification vs. validation: come up with some real world tasks that force distinction between the two.

### Agentic Development

The core purpose of RE is arguably, to ensure and automate the transformation of stakeholder requirements to an implementation or product, which/whose properties can conversely be verified against the stakeholder's requirements.

- Documentation. User requirements are all over the place, and in agent development usually in transcripts; how do we consolidate, categorize, assign provenance/authority/role, endorse/invalidate/question/arrange various requirements?
- Task prompt review (requirements analysis). How well can an agent execute a given task under a certain context? Applicable to long-context and horizon tasks, such as `/goal`, Claude `/loop`, workflow orchestration, scheduled jobs, etc.
- Translate between stakeholder and developers (in agentic development, this could mean translate between the user and a `/goal` executor, for example).
    - agent -> user translation: what has the agent performed technically, and how does it relate to stakeholder specified requirements?
    - more broadly, this is to translate between non-technical (stakeholder) language and technical (developer) language.

This does not necessarily mean the RE communicates with separate agents or groups; sometimes, it may perform the role of the technical staff in addition to RE. For example:

- user <-> agent (RE + developer)
- other developers and stakeholders <-> user <-> agent (RE) <-> other developers and stakeholders
- user <-> orchestrator (RE) <-> development workflow

Orchestration hygiene:

- Which part of the RE process necessitates independent subagent?
