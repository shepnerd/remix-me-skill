# Comparison schema

Use this schema when the analysis has multiple candidate items or when the user needs an auditable decision record. Keep evidence links or repository-relative paths next to claims.

## Source card

```yaml
source_id: short-stable-id
locator: URL, repository, paper identifier, or local path
kind: repo | paper | docs | webpage | ui | other
revision_or_date: known revision/date or unknown
license_or_reuse: observed terms or unknown
problem: one sentence
project_goal_relevance: goals advanced, blocked, or unaffected
items:
  - id: source-item-id
    name: method/component/pattern
    summary: what it does
    inputs_outputs: interfaces and assumptions
    evidence:
      - kind: claim | experiment | implementation | test | benchmark | anecdote
        ref: URL or path/section
        strength: high | medium | low
    prerequisites: []
    style_or_layout: optional content/design observations
    uncertainties: []
```

## Candidate comparison

Use one row per independently selectable item. Scores are qualitative; explain the reason instead of presenting false precision.

| Field | Meaning |
|---|---|
| Candidate | Stable name and source-item ID |
| Source evidence | Exact section, symbol, test, figure, or URL supporting it |
| Local analogue | Existing module, API, document, or UI surface |
| Goal alignment | Which stated project goal this advances and how |
| Delta | What would actually change locally |
| Fit | high / medium / low, with compatibility reason |
| Benefit | User or system outcome expected |
| Trade-offs | Correctness, performance, UX, complexity, or scope costs |
| Maturity | demonstrated / partial / conceptual |
| Risks | technical, dependency, security/privacy, legal, operational, maintenance |
| Effort | small / medium / large, with major work packages |
| Opportunity cost | What current goal, reliability, time, or budget could be displaced |
| Validation | Focused tests, benchmark, review, or user acceptance evidence |
| Recommendation | integrate / pilot / defer / do not integrate |

## Evidence labels

- **Observed:** directly supported by fetched source content or local repository inspection.
- **Inferred:** a reasoned connection; include the premise and uncertainty.
- **Recommended:** a proposed action or judgment, not a source claim.

Do not aggregate the dimensions into a single numeric score unless the user asks for one and the weighting is stated.
