---
name: requirements-engineering
description: Elicit, analyze, document, verify, validate, and maintain requirements, including requirements scattered across conversations and assignments for coding agents.
---

# Requirements engineering

Connect stakeholder needs to requirements, development assignments, and evidence about the resulting work. Use the [user guide](references/user-guide.md) for invocation and expected results.

## Glossary

- **Stakeholder:** a party affected by the system or able to influence its requirements. Distinguish its needs, knowledge, and decision authority; an agent can also be a consumer or perform an engineering role.
- **Need:** a difficulty or desired outcome for a stakeholder.
- **Requirement:** a needed behavior, quality, or constraint serving a need. A proposed requirement retains that status until established by the applicable authority.
- **Artifact:** a work product used as evidence or to communicate engineering information, including notes, models, specifications, and code.
- **Elicitation:** obtaining requirements information from stakeholders and other sources.
- **Analysis:** interpreting requirements information, examining conflicts and gaps, and deriving consequences and candidate requirements.
- **Documentation:** recording requirements and their relevant relationships so others can use and maintain them.
- **Verification:** checking an artifact or system against its stated basis. Requirements verification checks fidelity and specification quality; system verification checks fulfillment of requirements.
- **Validation:** checking whether requirements or outcomes address stakeholders' actual needs in their context of use.
- **Source:** an original statement or observation with its context. An interpretation is a meaning derived from it.
- **Authority:** the person or mandate entitled to establish a requirement or decision. Disposition records whether content is proposed, established, unresolved, or accepted for a stated purpose.

These activities recur throughout development. An agent may perform RE and implementation in one assignment; keep their results and evidence distinguishable.

## Identify the assignment

Match the requested result and observed situation. Read the selected method and [record discipline](references/record-discipline.md) for requirements work. Load further methods when their inputs or results are needed.

| Situation | Method and result |
| --- | --- |
| A difficulty or proposed feature lacks a clear need, beneficiary, or boundary | [Problem framing](references/problem-framing.md): a grounded problem and candidate outcomes. Use [business case](references/business-case.md) when a choice needs investment justification. |
| Requirements are scattered across conversations, issues, documents, or agent summaries | [Source consolidation](references/source-consolidation.md): a usable record with source meaning, authority, and unresolved interpretations preserved. |
| A stakeholder's needs, operating conditions, or constraints are missing | [Elicitation](references/elicitation.md): findings from the relevant sources and targeted remaining questions. Use [context artifacts](references/context-artifacts.md) to discover stakeholders and relationships. |
| Notes need to become requirements, or requirements conflict or lack precision | [Analysis and specification](references/analysis-specification.md): requirements, rationale, alternatives, and explicit open choices. Use [usage and quality](references/usage-quality.md) for interaction and quality requirements. |
| A task prompt or delegated assignment needs checking against intent and available context | [Task analysis](references/task-analysis.md): a feasible assignment or concrete corrections, dependencies, and completion evidence. |
| A document may misstate requirements, or delivered work may not meet them | [Review](references/review.md): identify the object being checked, compare with its basis, and report supported findings. |
| Work is resumed, a source changes, or design evidence challenges a requirement | [Change and continuation](references/change-continuation.md): recover the work and revise affected decisions. Use [process foundations](references/foundations.md) for requirements–architecture interaction. |
| A stakeholder needs to understand technical progress or decide whether an outcome meets their need | [Translation](references/task-analysis.md#translate-between-stakeholder-and-developer): a supported account of outcomes, gaps, and choices in the recipient's vocabulary; use [validation](references/review.md#validation) to establish fit. |
| The request concerns RE terminology, process, or artifact relationships | Answer the conceptual question using this glossary, [process foundations](references/foundations.md), or the [content model](references/content-model.md). A conceptual answer need not produce project requirements. |

For “this did not work,” determine what differs from what: implementation from an established requirement, a requirement from its source, or the delivered outcome from the stakeholder's need. Inspect the available record and evidence before selecting verification, analysis, or validation. Discovering an omitted stakeholder calls for elicitation and impact analysis.

For mixed work, resolve the dependency that prevents the requested result and then resume that result. General research, explanation of an unrelated feature, and implementation with settled requirements use their applicable workflows. An RE gap within them enters the relevant method without transferring ownership of the whole task to this skill.
