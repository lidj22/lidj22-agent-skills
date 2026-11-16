---
name: requirements-engineering
description: Establish, review, or resume requirements for a bounded owner-led engineering decision. Use when requirements engineering is requested, requirements must be defined for design, or consequential ambiguity affects required behavior, scope, or decision authority. Do not invoke for general research, explanation, or routine implementation with clear requirements.
---

# Requirements engineering

Produce or maintain a requirements record that preserves the owner's intended result and supports the decision at hand. Work at the level of detail that decision needs. Research and design exploration may inform requirements; they do not establish the owner's intent or authorize implementation.

## Establish the working boundary

Identify the assignment, intended use of the requirements, relevant stakeholders, system boundary, and constraints from available sources. A complete problem statement is not a prerequisite: distinguish established context from proposed interpretations and gaps.

Read the relevant source passages, existing requirements, project rules, and authorization before asking for information. Retrieve accessible missing context. When establishing or reconsidering requirements, read [Problem framing and requirements derivation](references/problem-framing.md) to connect stakeholder difficulties to required outcomes and resolve consequential interpretation gaps.

Distinguish facts you can investigate, choices requiring the owner's judgment, and provisional assumptions that let useful work continue. Ask now when unresolved alternatives materially affect the decision at hand and the available evidence cannot resolve them. Explain the consequence of the choice; keep downstream detail open until it matters. A provisional assumption supports a proposal, not an established requirement or authority to act.

Use an established authoritative issue, document, or linked artifacts as the requirements record where possible. If authority is not established, propose the existing or new artifact to maintain; do not promote a working draft to authority merely by selecting it. Identify its location and status for continuation. Maintain one operative account; use source control or the appropriate change record for history. Keep private session identifiers and incidental conversation details out of reusable requirements.

## Preserve meaning and authority

Keep these distinctions inspectable wherever they affect a decision:

- **Source:** the statement or evidence and enough context to recover its intended meaning. A link alone may be insufficient.
- **Requirement:** a needed behavior, quality, or constraint connected to the need it serves.
- **Interpretation:** a conclusion drawn from sources. Give the basis for material derivations; identify assumptions and alternatives that change the result.
- **Authority:** the person or mandate that can establish the requirement or make the decision. Authorship and confidence are not authority.
- **Disposition:** whether a statement is proposed, established by an applicable instruction or authorized decision, unresolved, or explicitly accepted for its stated purpose.

Use the project's vocabulary consistently. Preserve qualifications, boundaries, and exceptions when translating a source into requirements. Do not turn an illustrative example into an exhaustive rule or an agent recommendation into an owner requirement. Make legitimate derived requirements available as proposals. Preserve the criterion attached to a delegated decision: permission to choose does not supply evidence that an option meets it. Investigate missing evidence where possible; otherwise expose the dependency or propose a provisional choice with its basis. Record explicit adoption or acceptance only when supported by evidence.

## Deliver the assigned work product

**Establish:** Produce a requirements record adequate for the bounded decision. Include the relevant decision context, required behavior and qualities, material source and authority relationships, open matters and their consequences, and current disposition. Use whatever structure makes those relationships easy to inspect; do not impose headings or a schema when existing artifacts suffice.

**Review:** Inspect the record against its intended use and source meaning. Identify consequential omissions, contradictions, unsupported interpretations, ambiguity, and authority gaps. Attach each finding to the affected statement or relationship, explain its consequence, and distinguish a correction supported by evidence from a proposed choice. State what the record currently supports. Review findings do not automatically amend or establish requirements.

**Resume or correct:** Recover the authoritative record, relevant sources, current requirements, and outstanding work. Do not infer acceptance from missing history. Trace corrections through dependent requirements, interpretations, examples, and readiness claims. Apply changes within the existing grant; present changes requiring additional authority separately. Flag affected dependencies that cannot yet be resolved rather than leaving them apparently settled.

Keep open matters connected to the decisions they affect. Separate an unknown fact that can be investigated from a choice requiring the owner's judgment. Reuse shared provenance where it remains clear; avoid repeating metadata for its own sake. State the overall draft disposition once and add local qualifications only where their omission would change a decision.

## Bound completion and acceptance

Complete the assigned work when its work product is available, material relationships can be inspected, and its disposition accurately reflects the evidence. An explicitly requested draft can be complete as a draft. If a dependency prevents completion, deliver useful partial work and identify the dependency, consequence, and remaining work; do not claim the blocked assignment is complete.

Report the record's location, supported next decision, and consequential unresolved matters so a successor can continue. Keep required outcomes separate from proposed designs. Design discoveries may reopen requirements without turning RE into an implementation or runtime-control system.

The owner accepts by inspection and an explicit decision. Agent review and task completion do not substitute for acceptance. This skill grants no permission to edit, publish, implement, or accept beyond the user's existing authorization. Do not create evaluation infrastructure, scoring, benchmarks, or an additional acceptance gate as a prerequisite to this work.
