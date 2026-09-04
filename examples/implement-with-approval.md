# Approved implementation example

## Request

```text
Adopt candidate 1, the standard-library validation adaptation, and explicitly authorize implementation. Change only the files you listed, run focused tests, and report the pre-state, post-state, untouched files, and exact rollback procedure.
```

## Expected behavior

The agent should inspect the worktree before editing, use the appropriate Git or non-Git checkpoint policy, make the smallest compatible change, validate it, and report what changed. It should not create commits, archives, manifests, or broad refactors unless the user separately asks for them.
