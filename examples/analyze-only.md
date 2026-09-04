# Analyze-only example

## Request

```text
Use remix-me. Here are a paper and its released repository: ...
Do not modify my project. First infer what problem my repository is actually trying to solve and identify which claims are directly supported by the sources.
```

## Expected behavior

The agent should inspect the target project and sources, produce a provisional brief with evidence and confidence, separate observed facts from inferences, and ask the user to confirm or correct the brief. It should not ask for implementation authorization in an explicitly analysis-only request or modify files.
