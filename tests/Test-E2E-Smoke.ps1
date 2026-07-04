# End-to-End Integration Smoke Test for Codex Game Studios
[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$RepoRoot = Split-Path -Parent $ScriptDir

Write-Host "=== Codex Game Studios E2E Smoke Test ===" -ForegroundColor Cyan

# Check Skill and Manifest
$SkillFile = Join-Path $RepoRoot "SKILL.md"
if (-not (Test-Path $SkillFile)) {
    throw "SKILL.md missing: $SkillFile"
}

Write-Host "[1/2] Verifying Agents & Commands..." -ForegroundColor Yellow
$agentsDir = Join-Path $RepoRoot "agents"
$commandsDir = Join-Path $RepoRoot "commands"

if (-not (Test-Path $agentsDir)) {
    throw "agents/ directory missing under $RepoRoot"
}
if (-not (Test-Path $commandsDir)) {
    throw "commands/ directory missing under $RepoRoot"
}
Write-Host "  Agents & Commands Verification PASSED." -ForegroundColor Green

Write-Host "[2/2] Verifying Templates & Workflows..." -ForegroundColor Yellow
$templatesDir = Join-Path $RepoRoot "templates"
$workflowsDir = Join-Path $RepoRoot "workflows"

if (-not (Test-Path $templatesDir)) {
    throw "templates/ directory missing under $RepoRoot"
}
if (-not (Test-Path $workflowsDir)) {
    throw "workflows/ directory missing under $RepoRoot"
}
Write-Host "  Templates & Workflows Verification PASSED." -ForegroundColor Green

Write-Host "=== Game Studios E2E Smoke Test PASSED! ===" -ForegroundColor Green
