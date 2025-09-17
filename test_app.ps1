# Test script for TextFileSplitter application

# Create test input file
$testContent = @"
# This is a comment
example1.com
example2.com
example3.com
# Another comment
example4.com
example5.com
example6.com
example7.com
example8.com
example9.com
example10.com
"@

$testInputFile = "test_input.txt"
$testContent | Out-File -FilePath $testInputFile -Encoding UTF8

Write-Host "Test input file created: $testInputFile"

# Run the application with a small chunk size for testing
Write-Host "Running TextFileSplitter..."
dotnet bin\Release\net9.0-windows\TextFileSplitter.dll

Write-Host "Test completed."