# 1. Interactive TUI Mode
codex

# 2. Direct Prompt (Interactive)
codex "explain this codebase to me"

# 3. Full-Auto Mode (Sandboxed write access, auto-approves until failure)
codex --full-auto "create a todo app in React"

# 4. Non-Interactive / CI Pipeline Execution
codex exec "npm test && fix lint errors"

[shell_environment_policy]
# inherit can be "core" (default), "all", or "none"
inherit = "core"
# set to true to *skip* the filter for `"*KEY*"` and `"*TOKEN*"`
ignore_default_excludes = false
# exclude patterns (case-insensitive globs)
exclude = ["AWS_*", "AZURE_*"]
# force-set / override values
set = { CI = "1" }
# if provided, *only* vars matching these patterns are kept
include_only = ["PATH", "HOME"]
