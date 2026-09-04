# remix-me in 60 seconds

This tiny example shows the safety boundary: analysis is automatic; edits wait for a concrete choice and explicit authorization.

## 1. Give a reference and a local repo

```text
Use $remix-me with this reference:
https://github.com/Unclecheng-li/AI_Animation

Look at the current repository too. Infer what the project is mainly trying to achieve,
then stop before changing files.
```

## 2. Review the recommendation

```text
Project goal: produce reliable, auditable data transformations.

Useful idea: the reference's gallery-style, example-first presentation could make
the pipeline's results easier to discover.

Fit: medium (helps communication, not the data path)
Effort: low (README demo and one rendered flow)
Risk: low if kept documentation-only; do not copy source assets without checking terms

No files changed. Choose: adopt, pilot, defer, or do not integrate.
```

## 3. Choose, then authorize

```text
Adopt the documentation-only idea and authorize implementation. Keep it under
demo/, add a short README link, run the package validator, and report the checkpoint.
```

The agent now makes only that focused change, runs the requested checks, and reports what changed and how to roll it back. If you stop after step 2, the repository remains untouched.

## Try the real skill

Install the pinned release, then paste the prompts above in Codex or Claude Code. Replace the reference with a paper, web page, code sample, design, or several sources; the comparison and authorization boundary stays the same.
