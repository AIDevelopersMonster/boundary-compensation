# BC-Origin Windows run helper
# Runs BC-Origin visual pipeline using Python launcher (py) or python fallback

Set-Location (Resolve-Path "$PSScriptRoot\..\..")

Write-Host "BC-Origin: starting Windows execution pipeline"

$python = $null
$argsBase = @()

try {
    py -3 --version | Out-Null
    $python = "py"
    $argsBase = @("-3")
} catch {
    try {
        python --version | Out-Null
        $python = "python"
        $argsBase = @()
    } catch {
        Write-Error "Python not found. Install Python 3 or enable py launcher."
        exit 1
    }
}

Write-Host "Using Python command: $python"

Write-Host "Installing dependencies..."
& $python @argsBase -m pip install -r bc_origin\lab\requirements.txt

Write-Host "Running visual generator..."
& $python @argsBase bc_origin\lab\python\generate_visuals.py --out bc_origin\lab\outputs

Write-Host "Done. Outputs:"
Get-ChildItem bc_origin\lab\outputs
