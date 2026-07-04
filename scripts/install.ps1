<#
.SYNOPSIS
    Installs the Codex Game Studios Skill and Plugin locally.
#>

[CmdletBinding()]
param(
    [string]$TargetSkillsDir = "$HOME\.codex\skills\codex-game-studios",
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$RepoRoot = Split-Path -Parent $ScriptDir

Write-Host "Installing Codex Game Studios to: $TargetSkillsDir" -ForegroundColor Cyan

if (-not (Test-Path $TargetSkillsDir)) {
    New-Item -ItemType Directory -Path $TargetSkillsDir -Force | Out-Null
}

$ItemsToCopy = @('SKILL.md', '.codex-plugin', 'agents', 'assets', 'commands', 'examples', 'production', 'references', 'runtime', 'scripts', 'templates', 'workflows')

foreach ($item in $ItemsToCopy) {
    $source = Join-Path $RepoRoot $item
    if (Test-Path $source) {
        $destination = Join-Path $TargetSkillsDir $item
        Write-Host "  Copying $item -> $destination" -ForegroundColor Gray
        Copy-Item -Path $source -Destination $destination -Recurse -Force
    }
}

Write-Host "Codex Game Studios installed successfully!" -ForegroundColor Green
