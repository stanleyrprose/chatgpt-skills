# Security Policy

## Scope

Security reports are welcome for issues that could cause unintended code execution, credential exposure, permission expansion, unsafe tool use, or misleading security guarantees in this repository's Skills, validators, scripts, or CI configuration.

This repository contains instruction text and validation tooling. A Skill is **not** an authority grant: it cannot expand Tool/MCP permissions, bypass platform safety controls, or create capabilities that the runtime does not already authorize.

## Reporting a vulnerability

Do **not** include secrets, exploit payloads, private credentials, or sensitive reproduction details in a public GitHub issue.

Preferred reporting path:

1. Use GitHub private vulnerability reporting / Security Advisories if the repository exposes that option.
2. If private reporting is not available, contact the repository maintainer privately through the maintainer's GitHub profile before sending sensitive details.

A public issue is appropriate only for non-sensitive hardening suggestions that do not disclose an exploitable path.

## High-priority findings

Examples include:

- remote content executed directly by a shell;
- credential or keychain access not required by the Skill's purpose;
- environment enumeration combined with outbound network access;
- instructions that claim to bypass permission or authorization boundaries;
- CI or validator gaps that allow unsafe Skill content to pass while appearing verified;
- routing behavior that turns a user-invoked Skill into an automatic permission-expanding path.

## Validation boundary

The repository's static security gate is intentionally conservative and pattern-based. A clean scan is necessary evidence, not proof that a Skill or script is secure.

Security claims should distinguish:

- what was statically checked;
- what was executed or tested;
- what remains outside the evidence boundary.

## Supported version

Security fixes target the current `main` branch. Historical branches are retained as repository history and are not independently supported unless explicitly stated.
