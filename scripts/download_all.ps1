param(
    [string]$Destination = (Join-Path (Split-Path -Parent $PSScriptRoot) 'project-archives'),
    [ValidateRange(1, 8)]
    [int]$Workers = 4,
    [ValidateRange(1, 10)]
    [int]$Retries = 4
)

$ErrorActionPreference = 'Stop'
$script = Join-Path $PSScriptRoot 'download_all.py'
python $script --destination $Destination --workers $Workers --retries $Retries
if ($LASTEXITCODE -ne 0) {
    throw "One or more downloads failed. See download-report.csv in $Destination"
}
