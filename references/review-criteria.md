# Review criteria

Use criteria relevant to the task. A checklist is a diagnostic aid, not a requirement to discover an issue in every category. The evidence-status taxonomy and editing authority in `SKILL.md` are authoritative.

## Objective, synthesis, and hierarchy

Identify the question, audience, intended decision or interpretation, and governing conclusion. Check whether each section plays a useful role in that argument. Topic headings may be appropriate for reference or technical material; conclusion-led headings help when readers need executive takeaways. Do not force identical section shapes, a fixed number of findings, or MECE for its own sake.

Flag material accumulation when serial descriptions obscure relationships, mechanisms, tradeoffs, or implications. Group analytically related facts and clarify their synthesis within the existing architecture first. Facts and cases may precede or follow a shared conclusion; they do not each need a miniature insight. Read [analytical-contribution-gate.md](analytical-contribution-gate.md) for these contextual tests.

Check peer-level categories and parent-child relationships. Distinguish companies, actions, outcomes, and criteria where mixing them distorts the analysis. A tidy table does not fix a conceptual mismatch. Major restructuring requires a demonstrated problem and approved old-to-new map.

## Facts, calculations, text, and document consistency

These checks, together with logic below, are baseline work in a full review. Identify actual defects; do not manufacture a finding for every category.

- **Facts and source data:** Check names, entities and relationships, dates, product status, policy descriptions, and consequential numerical claims. Consult the original cited material and relevant public authoritative sources when tools and scope permit. Compare the same period, population, geography, definition, unit, currency, and version; distinguish actuals from estimates and forecasts. A newer number does not make an accurately dated historical number wrong. Attribute company statements appropriately. If sources conflict, resolve differences in scope, timing, or authority where possible; state exactly what remains unresolved when they cannot be reconciled.
- **Calculations:** Recompute key totals, shares, growth rates, margins, ratios, and unit conversions from the available inputs. Check denominators, formulas, percentage change versus percentage-point change, and whether table/chart results follow from the data. Allow stated rounding; overlapping categories need not sum to 100%. A discrepancy is not automatically an arithmetic error if the inputs use different definitions.
- **Textual errors:** Check typos, wrong or missing characters, accidental duplicated words, punctuation that changes meaning, inconsistent proper names or abbreviations, and unclear referents. Check misplaced negation carefully. Correct an unambiguous typo within authorized language editing; if the intended factual claim is uncertain, identify the ambiguity without guessing.
- **Document consistency:** Cross-check the same facts, metrics, dates, names, assumptions, and conclusions in the summary, headings, body, tables, charts, captions, notes, and references. Check chart labels, units, axes, and series against the underlying data where available. Trace a confirmed error to other occurrences and dependent conclusions; do not repair only the first visible instance. If a source, formula, or chart is inaccessible, identify that specific verification limit rather than claiming it passed.

For each confirmed error, give the location, original wording/value, correct wording/value, verification basis (source and relevant date or reproducible calculation), and consequence for the report. Include downstream occurrences and recommendations when affected. Minor typos may be grouped, with no invented strategic consequence. A false statement, an unverified statement, and a defensible inference require different verdicts. Recommend the appropriate correction decisively; apply `SKILL.md`'s authority gates before changing substantive content. Do not silently delete an erroneous passage or weaken an entire analysis in place of correcting its premise and assessing what follows.

## Logic and evidence

For consequential claims, trace support and reasoning, considering alternative explanations and material boundary conditions. Flag internal contradictions, shifting definitions or comparison bases, circular reasoning, conclusions that do not follow from the premises, correlation presented as causation, one example generalized to an entire market, absence of evidence treated as evidence of absence, and vendor claims promoted to independent results. Identify the failed reasoning step and state the strongest conclusion that the corrected premises support; do not stop at “逻辑不清.”

Use the four evidence statuses from `SKILL.md`: reported fact, grounded inference, working hypothesis, unsupported assertion. Recommendations/judgments are roles whose premises and fit must be assessed, not a competing status category. Check source date, scope, attribution, and comparability. Do not invent citations or require a source to state the report's inference verbatim.

Separate the supported core from an unsupported extension and give a verdict on each. Clarify an implicit but defensible bridge. Recommend approval of a narrower claim when scope or certainty must change; do not silently perform a substantive change under “language correction.” A request for more evidence is useful only alongside the best current judgment and when the missing information could materially change it.

## Insight and recommendations

A useful insight is grounded and explains a pattern, mechanism, distinction, condition, tradeoff, or implication. It need not be unprecedented or favorable. Reject pseudo-insight that merely restates facts with “this shows” or generic importance language. Equally, do not turn every definition, method, and fact paragraph into an insight requirement.

For material recommendations, judge fit with the diagnosed problem, user, brand, economics, resources, and timing. State whether to adopt, reject, narrow, deprioritize, or make conditional. Explain the mechanism and relevant tradeoff; “high risk” alone is not a verdict. Apply comparable criteria yourself where the material permits it. An alternative should repair the same objective within scope; a new strategy needs explicit approval.

## Repetition and content economy

Distinguish literal repetition, semantic repetition, summary/body repetition, and circular recaps. Summaries and orientation may deliberately repeat core findings. Do not flag necessary repetition simply because wording overlaps.

Prefer meaning-preserving language tightening. Combining clauses without removing a substantive occurrence is ordinary editing; removing a whole repeated sentence, paragraph, case, or row requires explicit deletion approval even if its meaning remains elsewhere. Any loss of evidence, nuance, a recommendation, or other distinct meaning also requires deletion approval. A shorter sentence can preserve all content; equal word count can erase the argument. No numeric retention target proves preservation.

## Natural professional Chinese

Write as a professional explaining a concrete judgment to another professional. Prefer an identifiable actor, ordinary verb, and precise object. Use established technical terminology where it adds precision; explain an unfamiliar term when needed. Do not convert a report into casual conversation or literary prose.

Check collocation and intelligibility in context, not just sentence length. Ask whether a Chinese-speaking reader can understand who does what, under which condition, without mentally translating back into English. Replace invented nominal labels, unnecessary noun chains, and hollow verbs such as “实现…的兑现” when a direct expression preserves the intended proposition. If the underlying meaning is unclear, do not invent one to make the sentence smooth.

Context-dependent examples, not universal word bans:

| Awkward expression | Natural alternative when this is the intended meaning |
|---|---|
| “推动用户能动性的兑现” | “让玩家的选择真正影响剧情” |
| “实现关系状态的连续性” | “让角色记住此前的交流，并在后续对话中作出一致回应” |
| “构建用户与内容之间的价值交换” | “玩家为持续更新的故事付费” **only if this is the stated business mechanism**; otherwise recover the actual meaning before rewriting |
| “为用户提供对迁移成本的降低” | “降低用户的迁移成本” |
| “该能力形成差异化抓手并承接增长转化” | Name the already-supported distinction and action, e.g. “更短的响应时间有助于减少玩家在对话中退出”; do not add that mechanism unless supported |

The first two alternatives apply only when the passage already means those specific things; neither licenses adding memory functions or branching-story claims. Common professional terms such as “价值交换” may be correct in their own conceptual context. Preserve precision instead of blacklisting vocabulary.

Use natural clause order and clear referents. Vary sentence shape where repetitive templates impede reading. A logical transition must express a real relationship; adding “因此” does not repair a missing inference. Colons, dashes, and “不是……而是……” are allowed when useful. Do not import a prose-writing skill's blanket punctuation or sentence bans into professional reports.

For slides, concise titles and bullets should convey a claim with support; do not create cryptic noun fragments merely to look like PPT language. For reports, preserve connected explanatory prose. Tables are useful for comparison or lookup, not as boxes for every paragraph.

## Review completeness and stop condition

Each critical or major issue should have an exact location, verdict, consequence, and proposed treatment. Consolidate related minor instances; no minimum issue count applies. Distinguish mandatory corrections from optional preferences.

For an authorized revision, verify source meaning and approved changes, coherent argument, natural expression, format, and standalone report language. Necessary subject-matter limitations are allowed; editor instructions and evidence-collection requests belong outside the clean draft. Check numbering and layout separately from semantic review. A limited script scan does not certify professional quality.

If these checks find no consequential defect, retain the content and finish. Do not repeat review until every sentence has been changed.
