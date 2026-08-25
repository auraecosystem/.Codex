# Global AGENTS.md

## Identity

Primary workspace: Aura Ecosystem / QUBUHUB.

Focus on AI engineering, Web4, blockchain, backend systems, DevOps, Swift, Rust, Go, Python, TypeScript, and Solidity.

## Coding Principles

- Prefer production-ready code.
- Security first.
- Type safety over convenience.
- Keep functions modular and documented.
- Preserve existing architecture unless explicitly asked to refactor.

## Style

- Use descriptive names.
- Avoid unnecessary dependencies.
- Prefer async/await.
- Generate tests alongside new code.

## Git

- Use Conventional Commits.
- Never commit secrets or API keys.
- Respect `.gitignore`.

## Documentation

Every public module should include:

- README.md
- Usage examples.
- Configuration docs.
- API docs when applicable.

## Security

- Validate user input.
- Sanitize filesystem operations.
- Never expose tokens in logs.
- Store credentials with least privilege.

## Default Workflow

1. Understand project structure.
2. Read nearby AGENTS.md files.
3. Make minimal safe changes.
4. Run lint/tests if available.
5. Explain important architectural decisions.
