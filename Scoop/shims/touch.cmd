@rem C:\workspace\Scoop\apps\touch\current\touch.ps1
@echo off
where /q pwsh.exe
if %errorlevel% equ 0 (
    pwsh -noprofile -ex unrestricted -file "C:\workspace\Scoop\apps\touch\current\touch.ps1"  %*
) else (
    powershell -noprofile -ex unrestricted -file "C:\workspace\Scoop\apps\touch\current\touch.ps1"  %*
)
