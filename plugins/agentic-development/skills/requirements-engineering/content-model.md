# Artifact and content model

Read this reference when deciding what a requirements record needs to contain, tracing a changed premise, or checking whether a draft covers the relevant abstraction levels. Use [process foundations](foundations.md) for process choices and tailoring.

## Content is not a document outline

An **artifact** is a work result with structure, content, and a representation; an **artifact model** relates artifacts and their dependencies. A structure model arranges documents, packages, or sections. A content model identifies the information and concepts that must relate meaningfully. Representation is how that information is expressed, such as prose or a diagram. The reference model and a project's actual artifact instances are distinct.

An issue, decision note, model, or specification may hold relevant content. One document can contain several kinds of content, and one logical artifact can span several records. Choose a readable representation; a populated template is not proof of adequate content.

## Three layers and three specification artifacts

Apply the **three-layer AMDiRE model** to distinguish context, requirements, and system content. Select the content needed for the current decision; the layers do not prescribe a document hierarchy or require every item on every project.

| Layer / artifact | Purpose | Content areas |
| --- | --- | --- |
| Context / Context Specification | Explain the setting, problem, motivations, and boundaries. | Project scope; constraints and rules; business case; stakeholder model; objectives and goals; domain model; glossary. |
| Requirements / Requirements Specification | Describe the system's required contribution and externally relevant properties. | System vision; usage and service models; functional hierarchy; data model; system constraints; quality requirements; process requirements; deployment requirements; risk list; glossary. |
| System / System Specification | Describe a technical realization sufficiently to relate design decisions to the requirements. | Architecture overview; function model; component model; data model; behaviour model; glossary. |

Context and requirements form the model's problem space; system specification forms its solution space. **System vision belongs to the requirements layer** in this model. A data model can occur at different abstraction levels: avoid treating a domain concept, required information, and a technical data representation as interchangeable merely because all concern data.

## Maintain relationships that support a decision

Inspect the relationships relevant to the current decision:

| Relationship | What to establish or inspect |
| --- | --- |
| Stakeholders, goals, business case, and scope | Whose difficulty matters, what outcome is sought, why addressing it is worthwhile, and what is inside the effort's boundary? Keep unsupported benefit claims visible as assumptions. |
| Domain, rules, and requirements | What existing concepts, practices, interfaces, or constraints shape the required behavior? Distinguish an external rule from a proposed internal design. |
| System vision and usage | What contribution should the system make, and what user interaction demonstrates that contribution? Usage models refine the vision through black-box behavior. |
| Goals, usage, and quality | Under which conditions must the behavior be sufficiently good, for whom, and with what observable consequence? Do not invent target values to fill a quality field. |
| Requirements and system design | Which design decision realizes or constrains which requirement? What feasibility finding requires returning to the requirements? Keep the intended outcome distinguishable from the selected mechanism. |
| Changed content and dependent content | If a goal, rule, scenario, or design assumption changes, which related requirements and decisions need reconsideration? Inspect relevant dependencies rather than merely replacing the original sentence. |

A business case concerns the reason to undertake the effort; a goal expresses a desired outcome; a system vision describes the intended system contribution; a usage model describes externally visible interaction. Collapsing them into a feature list loses different questions the model is intended to preserve.

## Choose the next useful elaboration

Locate the current uncertainty in these relationships. If the beneficiary or intended outcome is unclear, deepen context. If the outcome is understood but behavior is ambiguous, examine usage and the relevant requirements. If feasibility depends on a technical choice, investigate the corresponding system-level question and feed the result back into requirements.

These are decision cues, not a fixed progression. Work can begin from an existing design, a stakeholder account, or an incomplete specification. Preserve adequate existing content and make only the relevant missing relationships explicit. Owner acceptance remains the acceptance decision; this model supplies material for that decision rather than an automatic completeness score.

## Sources and attribution

- **A:** Birgit Penzenstadler, [Requirements Engineering — Artifact-oriented Requirements Engineering](https://www.slideshare.net/slideshow/requirements-engineering-artifactoriented-requirements-engineering/78078838), 2017, slides 3–6, 12–16, 21. Layer membership follows the individual layer diagrams on slides 14–16.
- **R:** Birgit Penzenstadler, [Requirements Engineering — Recap](https://www.slideshare.net/slideshow/requirements-engineering-recap/78079402), 2017, slide 3.

Original paraphrase and adaptations of the course material. Penzenstadler's [course publication](https://ceur-ws.org/Vol-2857/openre1.pdf) identifies the teaching materials as [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This adapted reference is provided under that license. Operational questions and bounded agent-work guidance above are adaptations, not claims that the course prescribes this skill's workflow.
