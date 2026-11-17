# Analysis and specification

The work product is a requirements record suitable for its intended decision. Its structure follows the project artifacts rather than a mandatory template.

For artifact selection and dependencies, read [content model](content-model.md). Use [usage and quality](usage-quality.md) for interaction models and requirement categories, and [process foundations](foundations.md) for refinement, decomposition, or Twin Peaks.

## Analyze the material

Connect candidate requirements to needs and sources using the problem-framing reference when that relationship is unresolved. Separate behavior, qualities, constraints, assumptions, and design proposals. Preserve mandated solution constraints as constraints.

Use a representation only when it resolves a material question: a scenario for competing interpretations; a state model for permitted transitions; a decision table for interacting rules; a context model for system boundary and external responsibilities. Keep relevant normal, alternative, and failure situations consistent with the record.

Analyze a claimed conflict in a situation where the rules apply together: identify the statements, conditions, affected stakeholders, and incompatible outcomes. Evaluate the conditions, exceptions, and existing grants against that situation before declaring an unresolved conflict. Apply an exception or grant within its stated scope; do not require it to be granted again unless an applicable source requires that further decision. Added restrictions, approval steps, and blockers need a warrant just as expanded permissions do. A stricter outcome is not inherently a more faithful interpretation. A qualification of one obligation does not automatically qualify a related obligation. Check whether a consequential change follows from the source or is only a preferred reconciliation using the [source-warrant comparison](review.md#compare-source-and-candidate-meaning). Where no authorized source supersedes an obligation, preserve compatible obligations. Treat a reconciliation that changes their meaning as a proposed policy choice rather than a necessary consequence of the source. Resolve actual conflicts using established authority and evidence, and expose unresolved policy or priority choices with their consequences. Preserve viable alternatives until the decision criterion and supporting evidence distinguish them.

## Specify for the decision

Apply bidirectional traceability to preserve meaning through derivation and revision. For each resulting obligation or permission, identify its source and the inference that warrants it. For each material source obligation affected by the work, account for whether it is preserved, qualified, superseded by an authorized statement, or unresolved. A single passage can establish several independent obligations; preserving its main topic does not preserve them all. Carry actors, objects, conditions, exceptions, and bounds through the transformation.

For a material derivation or revision, establish its relationship to the source through [comparative requirements QA](review.md#requirements-qa). Keep proposed policy choices and uncertain interpretations distinguishable at the decisions they affect. A draft label does not establish the source warrant for a change or suspend checking its independently specified aspects.

State the observable behavior or quality needed for the decision. Retain supplied or agreed bounds with their conditions. Where a satisfaction criterion is missing, distinguish an unknown fact from a choice to be proposed: construct a candidate criterion tied to the stated need, separating the observation that supports it from the proposed value judgment or tradeoff. Leave its approval explicit. A qualitative criterion must identify an observable outcome and how satisfaction would be judged, not merely call it acceptable. Leave a parameter unresolved when neither evidence nor a defensible proposal supplies it.

Keep scope, rationale, source relationships, assumptions, and unresolved decisions inspectable. Prioritization follows stakeholder goals and constraints; agent recommendations retain their proposed status. A requirement's source can be shared with related requirements when the relationship remains clear.

## Check contract sufficiency

For a contract intended to guide implementation or independent consumers, check whether two conforming consumers could make materially incompatible decisions from the same relevant inputs where shared behavior is required. Specify the observable behavior and information semantics needed to prevent that divergence, including consequential combinations, changes, and unresolved states. Distinguish those semantic obligations from representation and implementation choices that may remain free.

Where sources do not fix a contract decision, propose a reasoned choice with its basis, or identify the unresolved dependency and the work it actually blocks. Do not defer the behavior the contract is meant to determine merely by assigning it to implementation. Walk through a consequential downstream use of the record: if the consumer must invent that behavior, the contract still needs elaboration.

Internal quality checking uses [requirements QA](review.md#requirements-qa); confirming fit to stakeholder needs uses validation. Neither requires implementation or a formal skill evaluation.
