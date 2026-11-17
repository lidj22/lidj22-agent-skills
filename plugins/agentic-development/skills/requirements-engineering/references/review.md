# Requirements review

A review produces evidence-backed findings about an artifact or outcome. Establish the object being checked and its basis before choosing the method.

| Question | Object and basis | Result |
| --- | --- | --- |
| Does this record faithfully and adequately express the requirements? | Requirements against source meaning and specification criteria | Requirements verification / QA |
| Does the implementation fulfill the requirement? | System behavior against the established requirement | System verification evidence or an identified evidence gap |
| Do these requirements or outcomes address the actual need? | Proposed or delivered outcomes in stakeholder context | Validation feedback and its scope |

## Requirements QA

Identify the relevant original sources, the artifact's intended use, and the claims to check. Establish the source's consequential conditions and obligations before relying on the candidate's paraphrase of them. If the candidate is already familiar, reconstruct those conditions from the originals and retain the basis for disputed readings. An author's comparison document is also an artifact to verify.

Apply the [source comparison](source-consolidation.md#preserve-the-meaning) to consequential restatements. For derived requirements, examine whether the stated need, rationale, assumptions, and decision authority support the derivation. Keep a supported proposal distinguishable from a claimed source obligation.

Inspect contradictions, omissions, ambiguity, and inadequate satisfaction criteria within and across requirements. Use [usage and quality](usage-quality.md#quality-assurance-of-artifacts) when detailed specification-quality criteria are needed, and the [content model](content-model.md) when the finding concerns relationships across artifacts.

For a suspected defect, show the source, affected statement, and a situation where the difference changes the result. Check for an applicable exception or explicit authorization that would make the candidate correct. A reviewer should be able to explain why the faithful counterpart is acceptable, not merely detect suspicious wording.

If review is delegated, provide original evidence and the review question directly. Keep the author's synthesis distinguishable from those sources. Review agreement without an inspectable source comparison does not establish fidelity.

Return findings with their consequences and evidence, distinguishing supported corrections from stakeholder choices. State coverage and unavailable evidence. Apply corrections within the existing authorization.

## System verification

Identify the requirement, its operating conditions and criterion, and the implementation evidence available. Inspect relevant tests, behavior, records, or technical findings through the applicable development workflow. Compare the observation with the requirement; a claim that a test passed is insufficient when the test checks a different condition.

Report what is supported, contradicted, or untested. An implementation defect goes to implementation work. An ambiguous requirement goes to analysis; a technical constraint that makes the requirement infeasible enters requirements–architecture investigation. A successful implementation of an unsuitable requirement calls for validation.

## Validation

Identify whose need or decision is represented and what the stakeholder can establish. Present concrete outcomes, scenarios, alternatives, and tradeoffs in their vocabulary. Reuse applicable existing stakeholder decisions rather than requesting confirmation of settled meaning.

Record feedback with its source, scope, and authority. Trace disagreement or changed understanding to affected requirements. Keep unconfirmed interpretations proposed. If the required stakeholder evidence is unavailable, provide the useful analysis and precise unresolved question; agent simulation supplies no stakeholder agreement.

Validation establishes fit within the scope of the evidence and stakeholder authority. Acceptance follows the applicable decision process and existing grants; neither task completion nor review agreement creates it.

## Source

The course QA terminology is recorded in [sources](sources.md#terminology-boundary); the [usage and quality adaptation notice](sources.md#usage-qualitymd) accompanies its specification-quality guidance.
