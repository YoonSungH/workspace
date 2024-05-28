# C:\workspace\Scoop\apps\touch\current\touch.ps1
$path = Join-Path $PSScriptRoot "..\apps\touch\current\touch.ps1"
if ($MyInvocation.ExpectingInput) { $input | & $path  @args } else { & $path  @args }
exit $LASTEXITCODE
