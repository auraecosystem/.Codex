# Repository Guidelines for Codex

## Project Architecture
- **Stack:** Node.js / TypeScript / React / Express
- **Pattern:** Layered architecture (`/src/controllers`, `/src/services`, `/src/models`)

## Coding Rules & Standards
- Enforce strict typing in TypeScript; never use `any`.
- Prefer ES Modules (`import`/`export`) over CommonJS (`require`).
- Use `async/await` for asynchronous code with explicit `try/catch` error handling.
- Avoid hardcoding secrets; access parameters via `process.env`.

## Execution Rules & Testing
- Build check command: `npm run build`
- Unit tests command: `npm test`
- Linter command: `npm run lint`
- **Constraint:** Always run `npm test` after making modifications to ensure no regression errors.
