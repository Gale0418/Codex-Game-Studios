$ErrorActionPreference = 'Stop'

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)

function Fail {
  param([string]$Message)
  Write-Error ("VALIDATION_FAIL: {0}" -f $Message)
  exit 1
}

function Resolve-PythonCommand {
  foreach ($CommandName in @('python3', 'python')) {
    $Command = Get-Command $CommandName -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($Command -and -not [string]::IsNullOrWhiteSpace($Command.Source)) {
      return $Command.Source
    }
  }
  return $null
}

$PythonCommand = Resolve-PythonCommand
if (-not $PythonCommand) {
  Fail 'python3 or python is required to validate derived docs'
}

& $PythonCommand (Join-Path $Root 'scripts\generate_dispatch_manifest.py') --root $Root --check
if ($LASTEXITCODE -ne 0) {
  Fail 'command-registry.md derived docs or workflow contracts are out of sync'
}

$RequiredFiles = @(
  'references/workflow-entry-contract.md'
  'references/command-entry-contract.md'
  'references/approval-protocol.md'
  'references/governance-map.md'
  'runtime/dispatch-manifest.md'
  'runtime/session-lifecycle.md'
  'runtime/execution-policy.md'
  'production/state-schema.md'
  'commands/index.md'
  '.claude/settings.json'
  '.claude/settings.macos.json'
  '.claude/settings.windows.json'
  '.claude/statusline.sh'
  '.claude/statusline.ps1'
  '.claude/statusline.cmd'
  '.github/workflows/validate-studio.yml'
  '.claude/docs/coordination-rules.md'
  '.claude/docs/agent-coordination-map.md'
  '.claude/docs/workflow-catalog.yaml'
  '.claude/hooks/README.md'
  '.claude/hooks/session-start.sh'
  '.claude/hooks/pre-tool-use.sh'
  '.claude/hooks/post-tool-use.sh'
  '.claude/hooks/pre-compact.sh'
  '.claude/hooks/stop.sh'
  '.claude/hooks/subagent-start.sh'
  '.claude/hooks/session-start.ps1'
  '.claude/hooks/pre-tool-use.ps1'
  '.claude/hooks/post-tool-use.ps1'
  '.claude/hooks/pre-compact.ps1'
  '.claude/hooks/stop.ps1'
  '.claude/hooks/subagent-start.ps1'
  '.claude/hooks/session-start.cmd'
  '.claude/hooks/pre-tool-use.cmd'
  '.claude/hooks/post-tool-use.cmd'
  '.claude/hooks/pre-compact.cmd'
  '.claude/hooks/stop.cmd'
  '.claude/hooks/subagent-start.cmd'
  'scripts/validate_studio.cmd'
)

foreach ($RelativePath in $RequiredFiles) {
  $File = Join-Path $Root $RelativePath
  if (-not (Test-Path $File)) {
    Fail "missing required file: $File"
  }
}

$PathRuleFiles = @(
  'references/path-rules/src.md'
  'references/path-rules/design.md'
  'references/path-rules/game-rules.md'
  'references/path-rules/ui-ux.md'
  'references/path-rules/qa-regression.md'
  'references/path-rules/tests.md'
  'references/path-rules/docs.md'
  'references/path-rules/persistence.md'
  'references/path-rules/release.md'
  'references/path-rules/runtime-production.md'
  'references/path-rules/assets.md'
)

$ClaudeRuleFiles = @(
  '.claude/rules/assets.md'
  '.claude/rules/design.md'
  '.claude/rules/docs.md'
  '.claude/rules/game-rules.md'
  '.claude/rules/persistence.md'
  '.claude/rules/qa-regression.md'
  '.claude/rules/release.md'
  '.claude/rules/runtime-production.md'
  '.claude/rules/src.md'
  '.claude/rules/tests.md'
  '.claude/rules/ui-ux.md'
)

foreach ($RelativePath in $PathRuleFiles) {
  $File = Join-Path $Root $RelativePath
  if (-not (Test-Path $File)) {
    Fail "missing path rule file: $File"
  }
}

foreach ($RelativePath in $ClaudeRuleFiles) {
  $File = Join-Path $Root $RelativePath
  if (-not (Test-Path $File)) {
    Fail "missing .claude rule file: $File"
  }
}

$LegacyFiles = @()
$LegacyFiles += Get-ChildItem -Path (Join-Path $Root 'commands'), (Join-Path $Root 'references'), (Join-Path $Root 'workflows') -Recurse -File -ErrorAction SilentlyContinue
$LegacyFiles += Get-Item -Path (Join-Path $Root 'README.md'), (Join-Path $Root 'SKILL.md')
$AgentsPath = Join-Path $Root 'AGENTS.md'
if (Test-Path $AgentsPath) {
  $LegacyFiles += Get-Item -Path $AgentsPath
}

$LegacyMatches = $LegacyFiles | Select-String -Pattern '/Volumes/MyGame/codex-game-studios/' -ErrorAction SilentlyContinue
if ($LegacyMatches) {
  $LegacyMatches | ForEach-Object { Write-Error $_.ToString() }
  Fail 'legacy absolute links found; use relative paths'
}

$TemplateFiles = @()
$TemplateFiles += Get-Item -Path (Join-Path $Root 'SKILL.md')
if (Test-Path $AgentsPath) {
  $TemplateFiles += Get-Item -Path $AgentsPath
}
$TemplateFiles += Get-ChildItem -Path (Join-Path $Root 'references'), (Join-Path $Root 'workflows'), (Join-Path $Root 'commands') -Filter *.md -Recurse -File -ErrorAction SilentlyContinue

$TemplateRefs = $TemplateFiles | Select-String -Pattern 'templates/[A-Za-z0-9._-]+' -AllMatches -ErrorAction SilentlyContinue |
  ForEach-Object { $_.Matches.Value } |
  Sort-Object -Unique

foreach ($Ref in $TemplateRefs) {
  $File = Join-Path $Root $Ref
  if (-not (Test-Path $File)) {
    Fail "missing template reference: $Ref"
  }
}

Write-Output 'VALIDATION_OK'
