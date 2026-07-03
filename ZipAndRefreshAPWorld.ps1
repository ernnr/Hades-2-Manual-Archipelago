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

# Copy the .apworld file to the Archipelago custom worlds folder if it exists
$customWorldsDir = 'C:\ProgramData\Archipelago\custom_worlds'
if (Test-Path $customWorldsDir -PathType Container) {
    $destinationPath = Join-Path $customWorldsDir (Split-Path $apworldFile -Leaf)
    Copy-Item -Path $apworldFile -Destination $destinationPath -Force
    Write-Host "Copied '$apworldFile' to '$destinationPath'" -ForegroundColor Green
}
else {
    Write-Host "Skipping copy to '$customWorldsDir' because it does not exist." -ForegroundColor Yellow
}

# Restart the Archipelago launcher if it is currently running
$launcherProcess = Get-Process -Name ArchipelagoLauncher -ErrorAction SilentlyContinue | Select-Object -First 1
if ($launcherProcess) {
    $launcherPath = $launcherProcess.MainModule.FileName
    Stop-Process -Id $launcherProcess.Id -Force
    Start-Sleep -Seconds 2

    if ($launcherPath -and (Test-Path $launcherPath)) {
        Start-Process -FilePath $launcherPath
        Write-Host "Restarted ArchipelagoLauncher from '$launcherPath'" -ForegroundColor Green
    }
    else {
        Write-Host "ArchipelagoLauncher was running, but its executable path could not be determined." -ForegroundColor Yellow
    }
}
else {
    Write-Host "ArchipelagoLauncher is not running; no restart needed." -ForegroundColor Yellow
}
