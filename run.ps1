$scriptDirectory = $PSScriptRoot
Push-Location $scriptDirectory

# Define the paths to Python scripts
$aScript = ".\input\diarization.py"
$bScript = ".\input\video_creator.py"
# 
Start-Process -FilePath "python" -ArgumentList "$aScript" -Wait
Start-Process -FilePath "python" -ArgumentList "$bScript" -Wait
# 
# Remove the tmp folder
$folderPath = ".\tmp"
if (Test-Path -Path $folderPath -PathType Container) {
    Remove-Item -Path $folderPath -Force -Recurse
} else {
    Write-Host "The folder $folderPath does not exist."
}

Pop-Location