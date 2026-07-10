<#
.SYNOPSIS
    Installs the Codex Game Studios Skill and local plugin package.
#>

[CmdletBinding()]
param(
    [string]$TargetSkillsDir = "$HOME\.codex\skills\codex-game-studios",
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$codexHome = Split-Path -Parent (Split-Path -Parent $TargetSkillsDir)
$env:CODEX_HOME = $codexHome
$installer = Join-Path $PSScriptRoot "install.py"

& python $installer
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}