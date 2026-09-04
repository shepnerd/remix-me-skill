# Contributing to remix-me

## Before changing the skill

- Keep the core workflow platform-neutral and in one `skills/remix-me/SKILL.md`.
- Put substantial conditional guidance in `references/` rather than making the entrypoint longer.
- Preserve the two explicit decisions before mutation: what to adopt and whether to authorize implementation.
- Do not turn a single observed failure into a broad rule unless the rule improves the general workflow.
- Never add secrets, private project artifacts, copied proprietary text, or unreviewed executable source.

## Validation

Run:

```bash
python3 scripts/validate_skill_package.py
```

For behavioral changes, add a concise fixture or evaluation note under `evals/` and explain the expected safety boundary. Do not require API keys for structural checks.

## Pull requests

Describe the user problem, the affected platform(s), the files changed, and the evidence that the behavior improved. If a change affects Codex metadata, keep `agents/openai.yaml` consistent with the skill name and description. Avoid unrelated formatting churn.
