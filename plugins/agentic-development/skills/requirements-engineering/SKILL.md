---
name: requirements-engineering
description: Elicit, analyze, specify, review, validate, and maintain requirements for owner-led engineering decisions.
---

# Requirements engineering

This skill uses Birgit Penzenstadler’s requirements engineering course and its AMDiRE content model to support requirements from initial context through validation and change. Its work products are decision context, candidate requirements, review findings, and maintained requirements with inspectable source relationships. The [user guide](references/user-guide.md) describes invocation, inputs, outputs, and scope.

The [course map](references/course-map.md) identifies source material, coverage, and project-specific adaptations.

## Common language

- **Artifact:** a structured work product containing related content items.
- **Content model:** the information and relationships to establish, independently of document layout.
- **Need:** a stakeholder difficulty or desired outcome.
- **Requirement:** a needed behavior, quality, or constraint serving a need.
- **Requirements record:** the issue, document, or linked artifacts holding requirements and their current disposition.
- **Source:** evidence or a stakeholder statement, including its qualifications.
- **Interpretation:** a derived meaning or assumption, distinct from its source.
- **Authority:** the person or mandate entitled to establish a requirement or decision.
- **Disposition:** proposed, established, unresolved, or explicitly accepted for a stated purpose.
- **Requirements QA:** checking requirements artifacts for quality defects.
- **Verification:** checking whether a system fulfills its requirements.
- **Validation:** checking with relevant stakeholders whether the requirements represent their needs in use.

## Identify the assignment

Match the requested result and the available artifacts to the cases below. These are entry points, not a mandatory lifecycle sequence. Read the selected reference and [record discipline](references/record-discipline.md) for requirements work; load additional methods only when the artifact needs them.

| Request or artifact condition | Assignment and reference | Work product |
|---|---|---|
| Process setup, tailoring, abstraction level, or requirements–architecture interplay needs clarification | [Course foundations](references/course-foundations.md) and [content model](references/content-model.md) | Tailored artifact scope, roles, methods, tools, and milestones |
| The justification for an undertaking or choice among alternatives is unclear | [Business case](references/business-case.md) | Business-case report with evidence, alternatives, and recommendation |
| Stakeholders, goals, domain, or shared system vision need development | [Context artifacts](references/context-artifacts.md) and [content model](references/content-model.md) | Related context artifacts and system vision |
| User interaction, quality expectations, or requirement categories need elaboration | [Usage and quality](references/usage-quality.md) | Usage model and differentiated quality, process, deployment, and system requirements |
| A difficulty, goal, or proposed feature lacks a clear need or boundary | [Problem framing](references/problem-framing.md) | Decision context and candidate outcomes |
| Needed stakeholder or domain information is missing | [Elicitation](references/elicitation.md) | Source-grounded findings and consequential open questions |
| Notes need to become requirements, or requirements conflict or lack precision | [Analysis and specification](references/analysis-specification.md) | Requirements with rationale, assumptions, and unresolved choices |
| An existing record needs checking for ambiguity, inconsistency, omissions, or unsupported claims | [Requirements QA](references/review.md#requirements-qa) | Findings tied to affected requirements and consequences |
| The question is whether proposed requirements address stakeholders' actual needs | [Validation](references/review.md#validation) | Stakeholder feedback and recorded agreement or disagreement |
| Work is resumed, a source changes, or a requirement is corrected | [Change and continuation](references/change-continuation.md) | Recovered state and affected requirements updated or flagged |

When the required content or abstraction level is unclear, use the [content model](references/content-model.md) to locate the gap before choosing a method.

For a generic “review,” use requirements QA for document defects and validation for fit to stakeholder needs; combine them when both are requested. For a mixed assignment, address the blocking artifact gap first and retain the requested result. If plausible assignments imply materially different work and context does not resolve them, ask which result is wanted.

System verification, general explanation, standalone research, and implementation with settled requirements stay with their normal task workflow. A consequential requirements gap within those tasks enters the applicable case above; it does not convert the whole assignment into RE.
