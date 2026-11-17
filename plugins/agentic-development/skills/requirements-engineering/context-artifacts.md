# Context artifacts

Use the artifact whose missing content obstructs the current decision. Maintain the relationships between relevant artifacts without requiring every artifact to be completed. Keep existing project vocabulary, and apply [record discipline](record-discipline.md) to assumptions, disagreements, sources, and authority.

## Stakeholder model

A stakeholder can influence requirements or be affected by the system; having an interest does not imply supporting the project. Distinguish the person's role with the system from their role and decision competence in the project organization.

1. Discover candidate roles from lifecycle phases, operational and business context, and goals. Check outward from the product through its containing systems to the wider environment; include maintenance/support, passive affected parties, and regulators where relevant.
2. Record each relevant role's concerns and expectations, knowledge or contribution, influence, relationships, availability, and actual decision authority. A compact matrix or role diagram is sufficient; do not infer authority from influence.
3. Identify whose viewpoint informs each disputed need. Preserve incompatible accounts until clarified or resolved by the appropriate stakeholders. Arrange the necessary two-way information exchange: who needs what information, why, how, and when.

**Output:** a stakeholder model that identifies sources for elicitation, authority for decisions, and missing viewpoints. Use it to ground goals, domain concepts, vision, and later usage descriptions.

## Goals and their relationships

1. Extract intended outcomes and their stakeholders. When given a concrete feature or design, ask what outcome it serves; retain the proposal's status while recovering its rationale.
2. Distinguish business goals (strategic/project impact), usage goals (user/context outcomes), and system goals (system characteristics). Refine only enough to support the current decision, linking subgoals to their parents and identifying support and conflict relationships.
3. Describe what satisfying each relevant goal would mean. Record supplied measures or thresholds and their basis. Where none is established, expose the question; do not turn an invented number into a requirement. Identify obstacles or anti-goals when they explain why an intended outcome may fail.
4. Where decomposition is useful, distinguish what the system must ensure from what the surrounding context must provide. In the goal-tree technique, these are requirement leaves and expectation leaves respectively; record dependencies between them. This distinction is a modeling technique, not a universal naming rule.
5. Make conflicting goals comparable enough for a stakeholder decision. Propose alternatives or priorities with consequences; do not silently settle a conflict through the selected design.

**Output:** a goal model with rationale, refinement/dependency relationships, responsibility, and unresolved conflicts or satisfaction conditions. Use it to explain requirements and investigate alternatives without prematurely fixing architecture.

## Domain model and glossary

Start with the business case, stakeholder knowledge, goals, and relevant domain research. Identify candidate concepts from nouns in this material; distinguish conceptual business objects, real-world things, and events from software classes. Describe each important concept, then add necessary associations. Decide whether a candidate is a concept in its own right or an attribute of another. Add role names, multiplicities, and static rules only where established and useful; leave disputed or unknown cardinalities open.

Begin with a sketch or concept table and refine to a class diagram when relationships need that precision. Check coverage of important concepts, attributes, and associations, and maintain a glossary using the same meanings. A static domain model supports later behavioral views; it does not prescribe a database schema.

**Output:** conceptual structure and vocabulary usable by both stakeholders and the agent. Develop it iteratively with the system vision; use it to support usage modeling.

## System vision

Combine the business case, stakeholder model, goals, and domain model into an abstract picture of the proposed system. Show the boundary, neighboring systems, major features or usage, business and operational context, relevant stakeholders, and their concerns. Include enough structure and process to make those concerns intelligible. A rich picture, sketch, or concise textual view can support discussion; implementation detail is not needed merely to make the picture look concrete.

Review the picture with the relevant stakeholders for a clear boundary, comprehensibility, and sufficient coverage. Establish a shared vision through agreement among active stakeholders. Label an unreviewed or contested version as a proposed vision and retain disagreements. An agent's synthesis does not establish agreement.

**Output:** a communicable vision and its agreement status, plus implications for the usage model, quality requirements, and risk list. Feed newly discovered concepts back into the domain model and missing viewpoints back into stakeholder work.

## Sources and attribution

- [Stakeholders](https://www.slideshare.net/slideshow/requirements-engineering-stakeholders/78078882), slides 4–6, 8–12, 16–18.
- [Goals](https://www.slideshare.net/slideshow/requirements-engineering-goals/78078900), slides 6–7, 11–17, 20, 23–28, 31, 38–41.
- [Domain Models](https://www.slideshare.net/slideshow/requirements-engineering-domain-models/78078947), slides 3–7, 12, 15, 17–18.
- [System Vision](https://www.slideshare.net/slideshow/requirements-engineering-system-vision/78078930), slides 5, 9, 11, 20, 26–29.

Original paraphrase adapted from Birgit Penzenstadler's linked Requirements Engineering decks. Course artifact content and relationships are retained; selective elaboration, explicit unresolved evidence, and authority handling adapt them to agent work. The author's [course publication](https://ceur-ws.org/Vol-2857/openre1.pdf) identifies the teaching materials as CC BY-SA 4.0. This adaptation is provided under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). No third-party diagrams or student examples are reproduced.
