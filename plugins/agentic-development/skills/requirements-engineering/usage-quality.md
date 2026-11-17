# Usage models and quality

Use this reference when a system vision needs behavioral elaboration, a quality goal lacks a satisfaction criterion, or a requirements artifact needs quality assurance. Relate the work to the [content model](content-model.md); choose the content needed for the decision rather than producing every notation.

## Usage model

A usage model describes observable system behavior from the user's perspective, at the system boundary. A use case groups scenarios serving an actor's task or objective; a scenario is one ordered interaction sequence. A functional requirement identifies a required system response within that behavior. Keep these distinct: an isolated requirement sentence does not describe the whole use case.

From the system vision and business processes, identify actors, their tasks, external systems, and the system's role. Establish which work people retain and which work the system supports. Elaborate the interactions and information crossing the boundary. Structure the usage model as an overview of use cases, descriptions of individual use cases, and scenario diagrams. Tailor the representation while preserving their relationships.

For a material use case, capture its objective, scope, abstraction level, primary actor, trigger, preconditions, successful and failed end conditions, main interaction sequence, and relevant alternatives. Walk through concrete scenarios with stakeholders; group related scenarios into the same use case and refine the use case when a scenario exposes a missing condition. Trace scenario steps to functional requirements and exchanged information to the data model. Missing decisions remain open rather than becoming invented exception behavior.

## Quality models and requirement categories

A quality model identifies quality aspects and their relationships. Use it to examine which concerns matter for the system and stakeholder; a list of abstract qualities alone does not provide measurable requirements. Select a model appropriate to the system and examine its limitations; do not use one universal quality checklist or infer standards compliance from a category name.

Classify statements labeled non-functional by the content they govern:

| Content item | Question to resolve |
|---|---|
| Process requirements | What characteristics or constraints apply to the development project or process? |
| Deployment requirements | What must hold for introduction, migration, or deployment? |
| System constraints | What system-related restrictions apply, including mandated technologies? |
| Quality requirements | What quality must the system exhibit, for whom, and under which conditions? |

Derive quality requirements from system goals through concrete scenarios. Specify the relevant behavior or property, conditions, rationale, satisfaction criterion, measurement approach, and risk if unsatisfied. Retain bounds established by sources or an authorized decision. For a missing satisfaction criterion, apply [specification for the decision](analysis-specification.md#specify-for-the-decision) to distinguish evidence gaps from criteria that can be proposed. Inspect crosscutting effects on other behavior and stakeholder concerns. A feature intended to improve usability is a possible means, not proof of the required usability.

## Quality assurance of artifacts

Distinguish an invalid requirement, which misrepresents stakeholder intention, from a valid requirement with a quality defect such as ambiguity or missing measurability. Validation checks requirement correctness against stakeholder intention; verification checks a system's fulfillment of requirements. Checking the requirements document is requirements QA or review, not evidence that a system has been verified.

Apply constructive QA while producing artifacts: consistent concepts, suitable structure, trace links, and precise formulations. Apply analytical QA through examination or inspection of the artifact. Select criteria for its intended downstream use: completeness, consistency, unambiguity, correctness, structure, traceability, changeability, understandability, and stakeholder agreement. Seek counterexamples and missing cases; a review can expose incompleteness without proving universal completeness.

Check individuals, sets, and artifacts: ambiguous terminology in one sentence; contradictory conditions across requirements; missing or inconsistent relationships between models. Report the affected content, evidence, consequence, and unresolved judgment.

## Sources and adaptation

Adapted in original prose from Birgit Penzenstadler's CECS 542 teaching materials. Selective elaboration and evidence and authority handling adapt the material to bounded agent-assisted work. These adaptations are offered under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), the course-material license stated in the author's [course publication](https://ceur-ws.org/Vol-2857/openre1.pdf). Third-party figures and example text are not reproduced.

- U: [Usage Models](https://www.slideshare.net/slideshow/requirements-engineering-usage-models/78078950), slides 3–4, 7, 10–17.
- N: [Classification of non-functional requirements](https://www.slideshare.net/slideshow/requirements-engineering-nonfunctional-requirements/78079011), slides 5, 13, 15–16, 18–20.
- Q: [Quality Models](https://www.slideshare.net/slideshow/requirements-engineering-quality-models/78079027), slides 12–17.
- A: [Quality Assurance](https://www.slideshare.net/slideshow/requirements-engineering-quality-assurance/78079094), slides 7–8, 11–21, 26–27.
