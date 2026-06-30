$ErrorActionPreference = "Stop"

$ExpectedRoot = "C:\Development\Workspace\DevotionalRepo\kutumba-family-program"
$NestedRoot = "C:\Development\Workspace\DevotionalRepo\kutumba-family-program\kutumba-family-program"

Write-Host "Expected canonical root: $ExpectedRoot"
Write-Host "Current nested path: $NestedRoot"

if (Test-Path -LiteralPath (Join-Path $ExpectedRoot ".git")) {
    Write-Host "Canonical root already contains .git"
    git -C $ExpectedRoot rev-parse --show-toplevel
    git -C $ExpectedRoot status --short
    exit 0
}

if (Test-Path -LiteralPath (Join-Path $NestedRoot ".git")) {
    Write-Warning "Repository is still nested. Run Prompt 00 in Cursor before continuing."
    exit 2
}

Write-Error "No Git repository found at the expected or nested path."
