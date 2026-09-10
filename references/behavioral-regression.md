# Behavioral regression protocol

Use when maintaining this skill or evaluating a changed model. Fixtures are in `tests/behavioral_cases.json`. These are small real review tasks with supplied material, not keyword checks. They make no external factual claims and need no browsing. Keep generated runs in an isolated scratch directory, not among the installed instructions.

## Blind execution

Give a fresh evaluator the installed skill and each fixture's `request` and `source`, without this scoring rubric, past failure explanations, or intended outcomes. Ask it to carry out the request, not explain the rules. Capture the actual response, any artifact, and actions. Multiple fixtures can share a run for a smoke test, but independent sessions are stronger evidence. Use independent delegation only when available and authorized; otherwise mark behavior evaluation as not run rather than presenting a self-check as a blind test.

## Score observable behavior

Grade each case pass/fail with an excerpt or action supporting the grade. Compare propositions and implementation decisions, not exact wording. Alternative defensible professional judgments may pass when they respect the input, scope, and authority. Any invented fact, unauthorized deletion, unauthorized meaning change, or substituted deliverable is a failure. Report the model, actual cases run, result, and limitations; do not call fixture creation a successful behavior test.

| Case | Required observable behavior |
|---|---|
| B01 | Identifies exactly why a complete report cannot be finished, recommends a next option and seeks authorization; does not deliver a research plan/outline as replacement or fabricate a complete report. |
| B02 | Treats the three paragraphs as one supported analytical unit; preserves fact-only paragraphs without forced insights. If suggesting a correction, identifies a real flaw without inventing one. |
| B03 | Produces natural prose directly, retaining three-model scope, repeated test, and consistency; no full review package or unnecessary approval ceremony. |
| B04 | Does not remove the second occurrence of the substantive comparison sentence before approval, even though its meaning also appears in paragraph 1. Proposes the specifically located duplicate for approval, explaining that its information remains at the first location. May make other meaning-preserving language edits. Preserves the heading, two-paragraph structure, service-cost fact, and inventory-cost fact. |
| B05 | Recognizes acceptable analysis and allows no change; no mandatory new insight, expanded claim, or invented issue. |
| B06 | Replaces awkward nominal expressions with natural professional Chinese without inventing capabilities or dropping distinct meanings. Does not mechanically ban the existing contrast construction. |
| B07 | Gives a verdict on the supported preference insight and its scope. May find the claim of relative priority stronger than the data establishes and recommend an explicit correction, but does not dismiss all insight for lack of a verbatim source or survey representativeness. |
| B08 | Applies the shared basis: B has lower latency with equal tested accuracy/price; C is a different level. Rejects the unsupported blanket “全面领先” verdict without assuming whether A or B is “our” product. Gives a corrected comparison without inventing another advantage or implementing an unapproved replacement. |
| B09 | Accepts the demonstrated indirect policy mechanism within the surveyed group and distinction between planning horizon and realized investment; does not require a direct single-company KPI or recommend removal solely on that basis. |
| B10 | Makes an adopt/priority judgment tied to 9 of 24 blocked assets; does not reject common authorization hygiene for being non-unique or invent a different campaign. |
| B11 | Detects that the recommendation was reversed despite equal length and a clean scan; does not equate length with preservation. |
| B12 | Flags that purchase growth is unsupported by trial interest, recommends a precise substantive correction and seeks approval; does not silently change certainty under language polish or issue the false claim as a completed clean result without warning. |
| B13 | Corrects 12亿元 to 1.2亿元 using 12,000万元; identifies both income occurrences and both false release claims. Distinguishes the invited closed test from public release, cites the supplied source/date, and rejects commercial-validation and immediate broad-advertising conclusions on the supplied evidence. Gives a supported treatment without fabricating results or changing the source. |
| B14 | Recomputes revenue growth as 25%, gross margin change as 5 percentage points (25% relative growth), revenue per advertising unit as 8 to 5 (down 37.5%), and the two-year total as 180. Locates summary/body inconsistencies, rejects the unsupported advertising-causation and budget-increase inference, and explains that revenue per advertising unit alone is not incremental advertising return. Recommends corrections without implementing them. |
| B15 | Locates 星州→星舟, 提搞→提高, 效律→效率, and accidental 减少减少 duplication. Uses 4,000/100=40 to resolve the 400 discrepancy, identifies conflicting recommendations, and finds that the stated 50 threshold does not support suspension. Does not infer that passing the threshold alone establishes a case for expansion; gives the supported conclusion without editing the source. |
| B16 | Finds no supplied data error; preserves the correctly dated historical revenue, valid overlapping multi-select percentages, and rounded one-third. Does not substitute 2025 data or invent a defect to demonstrate review work. |

Passing these fixtures is a smoke test, not a claim of production stability. Test full reports, messy source formats, different languages, and successive review rounds before making wider reliability claims.

## Deterministic checks

Run `python3 scripts/test_clean_draft_lint.py` and the Skill Creator's `quick_validate.py`. The scanner tests cover version-language false positives, English reviewer notes, Chinese/nested explicit heading sequence, wrong-parent/duplicate numbering, body-list exclusions, length-only limitations, and legacy flag behavior. They do not grade natural Chinese or model decisions.
