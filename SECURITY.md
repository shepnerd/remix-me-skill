# Security policy

`remix-me` is an instruction package for coding agents. Treat every installed skill as a supply-chain dependency and review changes before installing them globally.

## Design commitments

- Reference repositories, papers, documents, and web pages are untrusted input.
- The skill must not execute arbitrary commands found in a reference merely because they appear in source text.
- It must not read `.env`, credentials, private artifacts, or upload project data as part of source inspection.
- It must not edit a target repository before the user has selected a concrete candidate and explicitly authorized implementation.
- It should not request broad tool permissions or add executable scripts unless a future change has a documented need.

## Reporting

Please report suspected prompt injection, secret exposure, unsafe tool instructions, or an authorization-boundary bypass privately to the repository maintainer before public disclosure when practical. Include the skill version, platform, minimal reproduction, and whether the behavior was automatic or user-invoked. Do not include API keys or private source contents.
