# Course foundations and process choices

Read this reference when choosing how to organize requirements work, deciding whether architectural exploration is appropriate, or distinguishing the course vocabulary from an ordinary document outline. Use [content-model.md](content-model.md) to identify relevant information and dependencies.

## A process has more than activities

Penzenstadler's general process model relates five elements: **activities/methods, artifacts, roles, tools, and milestones**. Activity orientation emphasizes how work proceeds; artifact orientation emphasizes the results, their content and dependencies, and responsibility for them. Artifact orientation still needs methods and activities; it does not prescribe one universal order for producing the results. [P, slides 7–10]

For this skill, use those elements to make the current work concrete:

| Element | Operational question — adaptation for agent work |
| --- | --- |
| Activity/method | What investigation or elaboration will resolve the current uncertainty? |
| Artifact | What information must the result contain, and what does it depend on? |
| Role | Who supplies relevant knowledge, performs the work, or decides the open choice? |
| Tool | What available source or tool can produce the needed evidence? |
| Milestone | What result or decision marks sufficient progress for the present scope? |

Do not turn these questions into compulsory headings. A milestone is a meaningful state of the work, not evidence that every preceding activity has been completed. The course illustrates milestones such as defining project scope or accepting a specification; the owner retains acceptance authority in this skill. [A, slide 10; operational adaptation]

## Problem and solution orientation

A requested solution can conceal the problem it is supposed to address. The course illustrates how implementing that request directly can preserve an unsuitable workaround. Establish the difficulty, affected stakeholders, intended outcomes, and constraints so proposed remedies can be assessed against them. An explicit authorized solution constraint remains a constraint; problem orientation is not permission to discard it. [P, slides 11–13; last sentence is operational adaptation]

The course's AMDiRE model distinguishes **context, requirements, and system** layers. Context and requirements describe the problem space; the system specification describes the solution space. These are related abstraction levels, not a prohibition on discussing solutions while learning about the problem. They also are not three documents that every task must create. [A, slides 9, 12–16]

## Twin Peaks, refinement, and decomposition

The course's Twin Peaks recipe alternates requirements and architecture: make a requirement-informed architectural decision, decompose and refine requirements in light of that decision, then examine architectural decisions for the resulting subsystems. **Refinement** adds information; **decomposition** distributes requirements across subsystems. Adding detail does not necessarily decompose anything. [R, slides 12–13]

Operational adaptation: use a bounded architectural question when its answer could change a material requirement or establish feasibility. Record the requirement or uncertainty being examined, the architectural assumption, what was learned, and the resulting requirement change. A possible design is evidence for deliberation, not automatically an implementation commitment. Keep candidate architecture and stakeholder requirements distinguishable when recording the feedback.

For example, a candidate deployment architecture may reveal an interruption that matters to a stakeholder's continuity need. Investigate the interruption and clarify the required behavior during it; do not silently weaken the need to fit the candidate design. Conversely, an agreed constraint can rule out an architectural option without requiring a full design exercise.

## Tailor the work to its setting

The course connects tailoring to project constraints, team and domain knowledge, stakeholders, system characteristics, business circumstances, and legal context. Its recipe examines the artifact model, removes unnecessary elements, adapts relevant ones, and selects supporting templates, tools, roles, milestones, and change handling. [R, slides 10–11]

Operational adaptation: select content because it supports the current decision or a material dependency. Reuse adequate existing records; deepen weak content where uncertainty matters. State a consequential omission and its effect when relevant. Do not claim full AMDiRE coverage from a small requirements note or force a small task through a full framework. A document template organizes presentation; it does not establish that the underlying information is sound. [A, slides 3–6; F, slides 3–7]

## Sources and attribution

Original paraphrase and operational adaptations of Birgit Penzenstadler's 2017 CECS542 Requirements Engineering teaching material:

- **P:** [Process & Roles](https://www.slideshare.net/slideshow/requirements-engineering-process-roles/78078726), slides 7–13.
- **A:** [Artifact-oriented Requirements Engineering](https://www.slideshare.net/slideshow/requirements-engineering-artifactoriented-requirements-engineering/78078838), slides 3–16.
- **F:** [Frameworks & Standards](https://www.slideshare.net/slideshow/requirements-engineering-frameworks-standards/78078792), slides 3–7. Historical course examples, not a claim of current standards compliance.
- **R:** [Recap](https://www.slideshare.net/slideshow/requirements-engineering-recap/78079402), slides 10–13.

Penzenstadler's [course publication](https://ceur-ws.org/Vol-2857/openre1.pdf) identifies the teaching materials as [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This adapted reference is provided under that license. Wording, selection, and agent-work guidance are adaptations, not quotations or claims that the course specifies this skill's contract.
