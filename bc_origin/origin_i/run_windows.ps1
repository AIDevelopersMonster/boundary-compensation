# BC-Origin Windows run helper
# Runs BC-Origin visual pipeline using a real Python 3 interpreter.
# If Windows prints only "Python" for `python --version`, it is usually a Store alias, not a usable interpreter.

Set-Location (Resolve-Path "$PSScriptRoot\..\..")

Write-Host "BC-Origin: starting Windows execution pipeline"

function Test-PythonCommand {
    param(
        [string]$Cmd,
        [string[]]$Args
    )
    try {
        $out = & $Cmd @Args --version 2>&1
        if ($LASTEXITCODE -ne 0) { return $false }
        $text = ($out | Out-String).Trim()
        return ($text -match '^Python\s+3\.[0-9]+\.[0-9]+')
    } catch {
        return $false
    }
}

$python = $null
$argsBase = @()

if (Test-PythonCommand -Cmd "py" -Args @("-3")) {
    $python = "py"
    $argsBase = @("-3")
} elseif (Test-PythonCommand -Cmd "python" -Args @()) {
    $python = "python"
    $argsBase = @()
} else {
    Write-Host "No real Python 3 interpreter was found." -ForegroundColor Red
    Write-Host "Observed symptom: python --version prints only 'Python' or opens the Microsoft Store alias." -ForegroundColor Yellow
    Write-Host "Install Python 3 from https://www.python.org/downloads/windows/ and enable 'Add python.exe to PATH'." -ForegroundColor Yellow
    Write-Host "Then open a NEW PowerShell window and run:" -ForegroundColor Yellow
    Write-Host "  python --version" -ForegroundColor Cyan
    Write-Host "  .\bc_origin\lab\run_windows.ps1" -ForegroundColor Cyan
    exit 1
}

Write-Host "Using Python command: $python $($argsBase -join ' ')"

Write-Host "Installing dependencies..."
& $python @argsBase -m pip install -r bc_origin\lab\requirements.txt
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Running visual generator..."
& $python @argsBase bc_origin\lab\python\generate_visuals.py --out bc_origin\lab\outputs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Done. Outputs:"
Get-ChildItem bc_origin\lab\outputs
