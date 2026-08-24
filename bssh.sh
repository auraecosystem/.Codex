# 1. Interactive TUI Mode
codex

# 2. Direct Prompt (Interactive)
codex "explain this codebase to me"

# 3. Full-Auto Mode (Sandboxed write access, auto-approves until failure)
codex --full-auto "create a todo app in React"

# 4. Non-Interactive / CI Pipeline Execution
codex exec "npm test && fix lint errors"
