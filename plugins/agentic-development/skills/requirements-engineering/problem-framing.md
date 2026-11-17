# Problem framing and requirements derivation

Use these relationships to improve the requirements record. Include the reasoning that changes a decision; do not reproduce every relationship as a section or questionnaire.

## From a difficulty to a requirement

Connect the stakeholder's difficulty to the outcome they need and the conditions in which it matters. A requested feature is evidence of a proposed remedy; identify its intended benefit before treating the remedy as necessary. Preserve an explicitly mandated solution constraint when one exists.

Check the explanation against available accounts of actual work: who encounters the difficulty, at what point, and what happens as a result? Distinguish an observed failure from a suspected cause. If the cause is unknown, identify the evidence needed rather than declaring that a favored intervention will solve it.

Derive candidate requirements that describe the required observable behavior or quality in those conditions. Explain how each material derivation serves the outcome and which assumptions it depends on. Avoid importing a particular implementation unless evidence or an authorized constraint requires it. Do not invent numerical targets to make a statement appear precise.

## Resolve differences that matter

When two plausible interpretations imply different requirements, use a concrete distinguishing scenario: a situation where one interpretation yields a different result from the other. State the resulting choice and its consequence. Do not ask the owner to restate an abstract ambiguity when the scenario makes the decision intelligible.

Seek the answer in existing evidence first. An operational fact may be established by records or people who perform the work. A preference or tradeoff may require the responsible stakeholder. A reversible interpretation may be carried as a visible assumption in a draft when it does not conceal a material commitment. Reversibility alone does not authorize a decision.

Prioritize gaps by their effect on the present decision. A detail needed to implement a later design need not block a useful requirements draft. Conversely, a missing distinction that changes who benefits, required behavior, or an important constraint belongs in the current account even if it is inconvenient to resolve.

## Preserve the reason for a choice

Connect a proposed choice to its decision criterion and supporting evidence. Authority, confidence, and familiarity are not substitutes for that evidence. Where alternatives remain viable, identify what would distinguish them rather than treating the easiest-to-describe option as selected.

When new evidence changes a premise, inspect affected requirements, assumptions, examples, and readiness claims. Revise the dependent meaning, not merely the wording of the original statement. Keep unaffected requirements intact and identify unavailable dependencies that still need inspection.

## Example: warehouse receiving discrepancies

A warehouse manager requests barcode scanners because receiving staff spend too long reconciling deliveries. Receiving notes show that several suppliers use a single package label for cartons containing different products. Other discrepancies have no recorded explanation.

The evidence supports a problem identifying mixed contents for some deliveries; it does not establish manual transcription as the cause of every discrepancy. The needed outcome includes reducing reconciliation time or effort; the acceptable improvement and current baseline remain to be established. A candidate functional requirement is that receiving staff can reconcile the products actually received with the expected delivery, including mixed cartons. That capability alone is insufficient if the resulting workflow makes reconciliation slower. Scanning is one possible mechanism, subject to what the labels identify and what supporting records are available.

A distinguishing scenario is a carton whose outer label matches the delivery record but whose contents differ. Recording that carton as received and confirming its contents have different consequences. Supplier packing records and the existing inspection practice may resolve factual questions; any unresolved choice about the assurance needed before accepting a delivery belongs to the responsible stakeholder. A scanner product need not be selected to make that requirement clearer.

If the manager delegates identification-method selection based on supplier coverage, that coverage must be investigated. Permission to choose a method does not justify assuming that every supplier labels individual products. The draft can preserve the needed outcome and record method selection as unresolved while other requirements proceed.
