# PowerShell script to zip manual_hades2_ernnr directory and create .apworld file

$workspaceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceDir = Join-Path $workspaceRoot "manual_hades2_ernnr"
$zipFile = Join-Path $workspaceRoot "manual_hades2_ernnr.zip"
$apworldFile = Join-Path $workspaceRoot "manual_hades2_ernnr.apworld"

# Check if source directory exists
if (-not (Test-Path $sourceDir)) {
    Write-Host "Error: Source directory '$sourceDir' not found." -ForegroundColor Red
    exit 1
}

# Remove existing zip file if it exists
if (Test-Path $zipFile) {
    Remove-Item $zipFile -Force
    Write-Host "Removed existing zip file."
}

# Create the zip file
Write-Host "Zipping contents of '$sourceDir'..."
Compress-Archive -Path $sourceDir -DestinationPath $zipFile -Force

# Remove existing .apworld file if it exists
if (Test-Path $apworldFile) {
    Remove-Item $apworldFile -Force
    Write-Host "Removed existing .apworld file."
}

# Rename zip to .apworld
Rename-Item -Path $zipFile -NewName (Split-Path $apworldFile -Leaf)
Write-Host "Created '$apworldFile'" -ForegroundColor Green
