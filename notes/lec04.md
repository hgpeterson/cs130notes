# AI Coding Tools

Uses:
- auto-generate/complete code
- generate comments
- generate tests
- summarize code for humans/commit messages
- provide code-review and suggestions
- perform refactoring
- find bugs

*Major struggle:* considering all files in project.
This contradicts the **High Cohesion, Low Coupling** principle:
- Everything in a module/class/etc should be hyper-focused on the relevant task -> High Cohesion
- Better to have each piece be as independent as possible -> Low Coupling

Another struggle: *diagnoseable tests*, i.e. tests that do one thing at a time so that they have a clear meaning if they fail. But they do well if you nudge them.