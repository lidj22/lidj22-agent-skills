# Process foundations and tailoring

Use this reference to organize requirements work, choose a bounded architectural investigation, or tailor the process to the project. Use the [content model](content-model.md) to identify relevant information and dependencies.

## General process model

Organize the process around five related elements: **activities/methods, artifacts, roles, tools, and milestones**. Activity orientation emphasizes how work proceeds; artifact orientation emphasizes the results, their content and dependencies, and responsibility for them. Select activities and methods to establish the needed artifact content; artifact orientation does not prescribe one universal production order.

| Element | Decision to establish |
| --- | --- |
| Activity/method | What investigation or elaboration will resolve the current uncertainty? |
| Artifact | What information must the result contain, and what does it depend on? |
| Role | Who supplies relevant knowledge, performs the work, or decides the open choice? |
| Tool | What available source or tool can produce the needed evidence? |
| Milestone | What result or decision marks sufficient progress for the present scope? |

Use these questions to organize the work, without imposing compulsory headings. Define milestones as meaningful states, such as an established project scope or an accepted specification. Reaching a milestone does not prove that every preceding activity was completed. Preserve the owner's acceptance authority.

## Problem and solution orientation

Establish the difficulty, affected stakeholders, intended outcomes, and constraints behind a requested solution. Assess proposed remedies against this problem context: implementing a request directly can preserve an unsuitable workaround. Retain explicit authorized solution constraints; problem orientation does not permit discarding them.

Distinguish the AMDiRE **context, requirements, and system** layers. Context and requirements describe the problem space; the system specification describes the solution space. Use these related abstraction levels to keep needs and technical realizations distinguishable while investigating their interaction. They do not require three separate documents.

## Twin Peaks procedure

Apply Twin Peaks when requirements and architectural choices materially constrain one another. Alternate requirements elaboration with architectural investigation:

1. Identify the requirement, constraint, or uncertainty that makes an architectural choice consequential. State what the investigation must establish and bound it to that question.
2. Examine a requirement-informed architectural option or decision. Retain its assumptions and decision status; a candidate architecture is not an implementation commitment.
3. Refine requirements using the resulting evidence. **Refinement** adds information. Where an architectural decision establishes relevant subsystems, **decompose** requirements by distributing them across those subsystems. Added detail alone is not decomposition.
4. Examine architectural choices for the resulting subsystems against their refined requirements. Feed feasibility findings, conflicts, and newly exposed stakeholder questions back into requirements work.
5. Record the examined requirement, architectural assumption or decision, evidence learned, and resulting requirement changes or open choices. Continue the alternation only as far as the current decision requires.

Keep stakeholder requirements distinct from candidate designs throughout this procedure. If a deployment option reveals an interruption that matters to a continuity need, clarify the required behavior during that interruption; do not silently weaken the need to fit the option. Conversely, an established constraint can rule out an option without a full design exercise. Seek the appropriate stakeholder decision when the feedback exposes a tradeoff beyond the agent's authority.

## Tailor the work to its setting

Examine project constraints, team and domain knowledge, stakeholders, system characteristics, business circumstances, and legal context. Select relevant artifact content and dependencies, remove unnecessary elements, and adapt the remaining elements to the project. Choose supporting methods, templates, tools, roles, milestones, and change handling to suit that selection.

Select content because it supports the current decision or a material dependency. Reuse adequate existing records; deepen weak content where uncertainty matters. State a consequential omission and its effect when relevant. Do not claim full AMDiRE coverage from a small requirements note or force a small task through the full framework. A document template organizes presentation; it does not establish that the underlying information is sound.

## Sources and attribution

Original paraphrase and operational adaptations of Birgit Penzenstadler's 2017 CECS542 Requirements Engineering teaching material:

- **P:** [Process & Roles](https://www.slideshare.net/slideshow/requirements-engineering-process-roles/78078726), slides 7–13.
- **A:** [Artifact-oriented Requirements Engineering](https://www.slideshare.net/slideshow/requirements-engineering-artifactoriented-requirements-engineering/78078838), slides 3–16.
- **F:** [Frameworks & Standards](https://www.slideshare.net/slideshow/requirements-engineering-frameworks-standards/78078792), slides 3–7. Historical course examples, not a claim of current standards compliance.
- **R:** [Recap](https://www.slideshare.net/slideshow/requirements-engineering-recap/78079402), slides 10–13.

Penzenstadler's [course publication](https://ceur-ws.org/Vol-2857/openre1.pdf) identifies the teaching materials as [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This adapted reference is provided under that license. Wording, selection, and agent-work guidance are adaptations, not quotations or claims that the course specifies this skill's contract.
