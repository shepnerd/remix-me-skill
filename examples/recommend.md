# Recommendation example

## Request

```text
Compare these two repositories and this blog post with my project. Recommend at most three ideas worth adapting. Include local analogues, risks, opportunity cost, effort, and what should not be integrated. Do not edit anything.
```

## Expected behavior

The agent should preserve source provenance, deduplicate overlapping ideas, apply the project’s primary goal as a hard filter, and present selectable integrate/pilot/defer/do-not-integrate options. It should leave the repository unchanged.
