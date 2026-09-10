# Professional Report Reviewer

> Make sure the report holds up before someone acts on it.

Professional Report Reviewer is an Agent Skill for consultants, researchers, analysts, strategists, and other professionals whose work is reviewed repeatedly before it goes to clients, executives, boards, investment committees, or internal decision-makers.

Give it an existing report. It checks facts, calculations, reasoning, evidence, comparisons, synthesis, recommendations, structure, and professional language. It can diagnose problems, run focused comparisons, or revise approved issues while preserving the analysis that already works.

## Why this skill

A polished report can still fail under scrutiny. Accurate facts may lead to an unsupported conclusion. A competitor section may contain good research but compare companies on different bases. A recommendation may sound sensible while solving a problem the report never established.

A generic review prompt may also rewrite too early, flatten the report's structure, remove useful examples or qualifications, and turn a complete report into an outline or review memo.

This skill treats the report as a professional work product that already contains research and judgment. It tests whether the report holds together before it changes the writing.

## How it differs from a one-shot AI review

The first column describes common behavior from a generic prompt such as “review and improve this report.” Models and tools vary.

| | Typical one-shot AI review | Professional Report Reviewer |
| --- | --- | --- |
| Main job | Improve fluency and presentation | Test whether the facts, reasoning, comparisons, and recommendations hold |
| Sequence | May rewrite immediately | Diagnoses material issues before substantive revision |
| Judgment | Often returns caveats or broad warnings | States what holds, what is overstated or invalid, why, and what conclusion the evidence supports |
| Comparisons | May summarize each company or case separately | Establishes a shared, decision-relevant basis and gives an advantage, parity, disadvantage, conditional, or unresolved verdict |
| Facts and numbers | May accept statements at face value | Checks consequential public facts, definitions, dates, scope, and key calculations when the environment allows verification |
| Preservation | May compress, reorganize, or remove detail | Preserves valid facts, cases, qualifications, narrative depth, and the author's working structure |
| Material changes | May implement them silently | Explains them and asks for confirmation before changing meaning, scope, structure, or recommendations |
| Deletions | May remove content in the name of concision | Requires approval for each substantive deletion |
| Valid outcome | Usually produces edits | Can conclude that a passage or the full report needs no change |

## What it reviews

| Area | What it checks |
| --- | --- |
| Facts and numbers | Public facts, dates, definitions, data scope, calculations, textual errors, and consistency across the report |
| Logic | Whether conclusions follow from the premises, including causal leaps, contradictions, and unsupported generalization |
| Evidence | Whether reported facts, grounded inferences, working hypotheses, and unsupported assertions receive the right treatment |
| Comparisons | Whether companies, cases, products, and data are compared on a consistent and decision-relevant basis |
| Analysis | Whether the material produces a finding, mechanism, boundary, tradeoff, or useful judgment |
| Recommendations | Whether each recommendation addresses the diagnosed problem and fits the objective, resources, economics, and timing |
| Structure and narrative | Whether sections serve the main argument and each part moves the report forward |
| Professional language | Whether the writing is clear, precise, natural, and free of generic filler or awkward translated phrasing |

## Comparison work it can handle

| Comparison task | What the reviewer does |
| --- | --- |
| Companies, products, or cases | Applies shared criteria, separates product, supplier, and infrastructure levels where relevant, and explains which differences matter to the decision |
| Data and metrics | Checks definitions, time periods, scope, units, denominators, and whether the figures are genuinely comparable |
| Claims against sources | Traces each consequential claim to supplied evidence or relevant public facts and checks whether the wording exceeds the support |
| Sections within one report | Finds inconsistent definitions, classifications, assumptions, conclusions, or recommendations |
| Original and revised drafts | Detects lost claims, examples, qualifications, recommendations, and unapproved deletions |

## Who it is for

Use it when a report must survive several rounds of review before external delivery or internal use. Typical users include:

- Consultants and advisory teams
- Market, industry, and policy researchers
- Strategy, corporate planning, and competitive-intelligence teams
- Investment, business, and financial analysts
- Professionals preparing management, board, or executive reports
- Anyone checking a revised report before it informs a decision

## Language support

| Report language | Review coverage |
| --- | --- |
| English | Full review of facts, reasoning, evidence, comparisons, recommendations, structure, clarity, precision, and professional tone |
| Chinese | The same full review, plus checks for awkward translated phrasing, mechanical report language, and natural professional Chinese |

The skill can receive instructions and return review findings in either English or Chinese. Output quality still depends on the selected model's language ability, context window, and file support.

## Compatible environments

The core skill follows the `SKILL.md` Agent Skills format. Compatibility below means that the platform officially documents a custom Skill mechanism based on that format. Each surface may use a different installation and invocation flow.

| Environment | Format status | Install or invoke |
| --- | --- | --- |
| [ChatGPT desktop and Codex](https://developers.openai.com/codex/skills/) | Native Agent Skills format; this package also includes `agents/openai.yaml` | Add the standalone skill in ChatGPT desktop and invoke it with `@professional-report-reviewer`. In Codex, install it as a local skill and use `$professional-report-reviewer` or `/skills`. |
| [Claude.ai](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | Compatible custom Skill format | Upload the skill folder as a ZIP through the custom Skills settings. Availability depends on the Claude plan and code-execution access. |
| [Claude Code](https://code.claude.com/docs/en/skills) | Compatible filesystem-based Skill | Copy the folder to `~/.claude/skills/professional-report-reviewer/` or `.claude/skills/professional-report-reviewer/`, then use `/professional-report-reviewer` or ask naturally. |
| [Qoder IDE and CLI](https://docs.qoder.com/extensions/skills) | Compatible `SKILL.md` Skill | Install from GitHub with Qoder's Skills CLI or copy the folder to `~/.qoder/skills/professional-report-reviewer/`. Invoke it with `/professional-report-reviewer` or ask naturally. |
| [QoderWork](https://docs.qoder.com/qoderwork/skills) | Compatible uploaded or filesystem Skill | Paste the GitHub repository link and ask QoderWork to install it, upload the package, or place it in `~/.qoderwork/skills/`. |
| Other agents that read `SKILL.md` | Expected to work at the instruction level | Point the agent to `SKILL.md`. File access, web verification, scripts, and invocation syntax depend on the host. |

The current regression suite covers skill behavior. Cross-platform results still vary by model, product surface, and host permissions.

## Install

### Ask your agent

Copy this repository's URL and tell a compatible agent:

```text
Install the Professional Report Reviewer skill from this GitHub repository.
```

### Install manually

1. Download the repository ZIP.
2. Keep `SKILL.md`, `references/`, `scripts/`, `tests/`, and `agents/` together in one `professional-report-reviewer` folder.
3. Add that folder through your product's Skills interface or place it in the documented local skills directory.
4. Start with a small, non-confidential report and confirm that the skill appears in the product's skill list.

This project does not require a separate website or document-upload service.

## Use it

Attach the complete report and ask in plain language. Invocation syntax varies by product.

### Full report review

```text
Use Professional Report Reviewer to review this report.
Start with a diagnosis and a located list of material issues.
For each issue, tell me what holds, what does not, why, and what conclusion the evidence supports.
Do not change the central argument, restructure the report, or delete substantive content before I approve the proposed changes.
```

### Competitor or case comparison

```text
Use Professional Report Reviewer to examine the comparison in this report.
Put the companies and cases on a common, decision-relevant basis.
Identify incomparable evidence, explain the differences that matter, and give a clear verdict.
```

### Compare two drafts

```text
Use Professional Report Reviewer to compare the original and revised reports.
Find any lost claims, facts, examples, qualifications, recommendations, or changes in certainty and scope.
Do not rewrite either version.
```

### Chinese language review

```text
Use Professional Report Reviewer to edit the Chinese in this report.
Keep the claims, conclusions, structure, examples, and all substantive content.
Remove awkward translated phrasing and make the language natural and professional.
Flag factual or logical problems separately.
```

## Review workflow

`Diagnosis → Located issues → Professional verdicts → Approval of material changes → Revision → Final verification`

The workflow scales with the task. A focused language edit does not need a full review package. A sound report can pass without unnecessary rewriting.

## Editing boundaries

Language and formatting edits can be applied directly when they preserve meaning. Changes to claims, certainty, scope, recommendations, taxonomy, or structure require confirmation.

Every proposed deletion of substantive content must identify:

- The exact location
- What would disappear
- Why removal is recommended
- What the report would lose or gain
- A less destructive alternative, when one exists

The final revision is checked against the source for meaning, scope, evidence, examples, recommendations, continuity, and numbering.

## Repository structure

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Core workflow, decision rules, and editing boundaries |
| `references/review-criteria.md` | Detailed checks for facts, numbers, logic, comparisons, recommendations, and professional Chinese |
| `references/analytical-contribution-gate.md` | Tests whether a section contributes analysis instead of filler |
| `references/output-formats.md` | Output shapes for review-only, revision, and focused-edit tasks |
| `references/behavioral-regression.md` | Maintenance and regression guidance |
| `scripts/` | Deterministic checks for selected clean-draft issues |
| `tests/` | Behavioral cases used to test the review rules |
| `agents/openai.yaml` | Optional display metadata for ChatGPT and Codex |

## Project status

This project is in beta. Its rules come from recurring failures in professional report review and are backed by deterministic checks and behavioral regression cases.

Results vary by model, context length, file-handling support, tool access, and subject matter. Keep a qualified human reviewer in the loop when a report will influence an important external or internal decision.

## Privacy

This project does not run an independent document-upload service. Your report is handled by the AI environment you choose, subject to that product's privacy policy and your organization's information-security requirements.

Do not post confidential reports, client names, unpublished data, or personal information in public issues. A short, anonymized example is usually enough to reproduce a problem.

## Feedback

Useful issue reports include:

- A valid inference was dismissed as unsupported
- A material logic error was missed
- Incomparable evidence received only a vague warning
- A rewrite removed facts, examples, qualifications, or judgments
- The revised language became generic, awkward, or less natural
- The same case produced materially different behavior across models

When possible, include an anonymized source passage, the actual review output, and the result you expected.

## License

Licensed under the [PolyForm Perimeter License 1.0.1](https://polyformproject.org/licenses/perimeter/1.0.1).

You may use, modify, and share the project for permitted purposes, including personal work, internal company work, and paid professional work. You may not use it to provide others with a product that competes with this software. The project is source-available and does not use the MIT License. See `LICENSE` for the exact terms.

## Maintainer

Created and maintained by [AliciaLiu0526](https://github.com/AliciaLiu0526).
