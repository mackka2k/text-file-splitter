# Package the TextFileSplitter application for distribution

# Build the application in Release mode
Write-Host "Building TextFileSplitter in Release mode..."
dotnet build -c Release

# Create a distribution folder
$distributionFolder = "TextFileSplitter-Distribution"
if (Test-Path $distributionFolder) {
    Remove-Item $distributionFolder -Recurse -Force
}
New-Item -ItemType Directory -Name $distributionFolder

# Copy necessary files to the distribution folder
Copy-Item "bin\Release\net9.0-windows\*" -Destination $distributionFolder -Recurse
Copy-Item "run.bat" -Destination $distributionFolder
Copy-Item "README.md" -Destination $distributionFolder
Copy-Item "app.manifest" -Destination $distributionFolder

# Create a zip file of the distribution
$zipFile = "TextFileSplitter.zip"
if (Test-Path $zipFile) {
    Remove-Item $zipFile -Force
}
Compress-Archive -Path $distributionFolder -DestinationPath $zipFile

Write-Host "Application packaged successfully as $zipFile"