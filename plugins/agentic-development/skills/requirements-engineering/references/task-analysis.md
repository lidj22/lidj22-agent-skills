# Task analysis and translation

Use this method when a task prompt must carry stakeholder intent into engineering work, or when technical results must be explained in terms of that intent. It applies to a human developer, a coding agent, or an orchestrated workflow.

## Analyze an assignment

Recover the requested outcome, applicable requirements, existing decisions, and the intended recipient's available context. Distinguish the immediate deliverable from the larger project goal. A request to investigate, propose, implement, or verify can concern the same feature while authorizing different work.

Examine whether the assignment provides or makes discoverable:

| Relationship | Question to resolve |
| --- | --- |
| Outcome and need | What useful result must the recipient produce, and whose need does it serve? |
| Scope and authority | What may be changed or decided, and what established constraints apply? |
| Inputs and dependencies | Which sources, artifacts, tools, access, or upstream decisions does the work need? |
| Required behavior and evidence | How can the recipient demonstrate the requested result, including consequential exceptions and quality requirements? |
| Continuation | Where does the result belong, and what unresolved dependency or next decision must another consumer inherit? |

Inspect the actual inputs and access where available. Separate a missing fact the recipient can investigate from an unavailable prerequisite or a stakeholder choice. Identify contradictory instructions and assumptions that would change the result. Use [source consolidation](source-consolidation.md) when the assignment relies on scattered or interpreted requirements.

Propose the smallest correction that makes the assignment usable: supply a source reference, clarify the expected result, preserve a condition, expose a dependency, or separate tasks with different outputs or authority. Decompose when the work has independently inspectable results or a dependency prevents coherent execution. Existing authorization applies; decomposition introduces no new permission gate.

For delegated work, preserve the requirement and its qualifications across the handoff. Give the recipient the relevant sources and the basis for consequential choices. Select models, schedule work, and manage runtime resources through the applicable orchestration workflow; this method supplies its requirements and dependencies.

## Return the assessment

Provide the corrected assignment when editing is authorized; otherwise provide a separate proposed correction. Explain each material defect through its execution consequence and source basis. State which work can proceed and which dependency actually blocks it. Assess the assignment against its intended recipient without claiming to know that recipient's capability from a prompt inspection alone.

An assignment is usable when its outcome, relevant constraints, inputs, and evidence are sufficiently clear for the requested work. A feasible prompt does not establish that its execution will succeed.

## Translate between stakeholder and developer

From stakeholder to developer, express needs as observable outcomes, operating conditions, constraints, and choices. Preserve the user's vocabulary through a glossary or explicit mapping when technical terminology differs. Distinguish a requested outcome from a suggested mechanism and retain mandated mechanisms as constraints.

From developer to stakeholder, inspect the actual artifact or execution evidence and connect it to the requested outcome. Explain what is implemented, what has been checked, what remains unknown, and what decision follows. A completed activity is evidence of the activity; demonstrating a requirement needs evidence about that requirement. Keep recommendations separate from established decisions.

Choose examples and consequences that make a technical distinction meaningful to the recipient. For “does this solve the problem?”, distinguish conformity to the agreed requirement from fit to the original need. Use [review](review.md) for the evidence comparison and stakeholder validation. Retain links to detailed evidence so a concise explanation remains inspectable.
