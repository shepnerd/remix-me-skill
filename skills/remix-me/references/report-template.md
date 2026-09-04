# Reference integration report

## 1. Scope and decision status

- User objective:
- Sources in scope (identity, revision/date, access status):
- Target repository and revision:
- Project primary goal, users, and current success criteria:
- Provisional problem brief (when inferred from the repository):
- Evidence and confidence for that brief:
- User confirmation/correction: **pending / confirmed / corrected**
- Goal-related constraints and opportunity costs:
- Out of scope / unavailable inputs:
- Mode: **analyze / recommend / implement**
- Adoption choice: **not applicable / pending / decided**
- Implementation authorization: **not applicable / pending / decided**

## 2. Source cards

For each source, summarize the problem, independently selectable items, interfaces/assumptions, evidence, style/layout observations, license/provenance, and uncertainties. Label claims observed/inferred/recommended.

## 3. Target-repository map

Summarize the project’s primary goal first, then relevant architecture, existing capabilities, extension points, contracts, dependencies, runtime constraints, tests, docs/UI conventions, and limitations. Cite repository-relative paths.

## 4. Comparison matrix

Use one row per candidate and include source evidence, local analogue, project-goal alignment, delta, fit, benefits, trade-offs, maturity, risks, opportunity cost, effort, validation, and recommendation. Include explicit “do not integrate” rows where useful.

## 5. Recommendation and choices

Prioritize candidates and explain the reasoning. Call out evidence gaps, incompatible assumptions, and license/security concerns. If the problem brief was inferred, confirm it before treating the recommendations as final. In recommend or implement mode, ask the user to choose candidates, then to authorize implementation, unless the user has already made either decision unambiguously. In analyze mode, do not ask for implementation authorization.

## 6. If approved: delivery plan

- Scope and non-goals:
- Ordered, reversible changes:
- Acceptance criteria:
- Tests/benchmarks/review evidence:
- Documentation, attribution, and migration notes:
- Rollback or disable path:

## 7. Checkpoint record (implementation mode)

- Pre-state reference (normally Git `HEAD`, or a user-approved backup):
- State before editing: **clean / pre-existing changes / non-Git**
- Backup: **not needed / not created / created at:**
- Post-state identifier or manifest path:
- Changed paths:
- Intentionally untouched paths:
- Validation performed:
- Exact rollback procedure and limitations:
