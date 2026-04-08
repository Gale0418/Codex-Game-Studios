$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$StageFile = Join-Path $Root 'production\stage.txt'
$ActiveFile = Join-Path $Root 'production\active.md'

$Stage = 'unknown'
$Lane = 'unknown'

if (Test-Path $StageFile) {
  $Stage = (Get-Content -Path $StageFile | Select-Object -First 1).Trim()
}

if (Test-Path $ActiveFile) {
  $LaneLine = Get-Content -Path $ActiveFile | Select-String -Pattern '^-\s*`lane`:' | Select-Object -First 1
  if ($LaneLine) {
    $Lane = ($LaneLine.Line -replace '^-\s*`lane`:\s*', '').Trim()
  }
}

Write-Output ("stage={0} lane={1}" -f $Stage, $Lane)
