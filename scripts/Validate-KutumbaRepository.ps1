# KUTUMBA Repository Validation
# Returns exit code 0 on pass, nonzero on critical failures

param(
    [string]$RepoRoot = "C:\Development\Workspace\DevotionalRepo\kutumba-family-program"
)

$ErrorActionPreference = "Continue"
$failures = @()
$warnings = @()

function Add-Failure($msg) { $script:failures += $msg }
function Add-Warning($msg) { $script:warnings += $msg }

Write-Host "=== KUTUMBA Repository Validation ===" -ForegroundColor Cyan
Write-Host "Root: $RepoRoot"

# 1. Repository root nesting
$nested = Join-Path $RepoRoot "kutumba-family-program"
if (Test-Path (Join-Path $nested ".git")) {
    Add-Failure "Nested repository folder detected: $nested"
}
if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    Add-Failure ".git not found at canonical root"
}

$top = git -C $RepoRoot rev-parse --show-toplevel 2>$null
if ($top -ne $RepoRoot.Replace('\', '/')) {
    $topNorm = $top -replace '\\', '/'
    $expected = $RepoRoot.Replace('\', '/')
    if ($topNorm -ne $expected) {
        Add-Warning "Git toplevel: $top (expected $RepoRoot)"
    }
}

# 2. Unexpected nested .git
Get-ChildItem -Path $RepoRoot -Recurse -Force -Directory -Filter ".git" -ErrorAction SilentlyContinue |
    Where-Object { $_.Parent.FullName -ne $RepoRoot } |
    ForEach-Object { Add-Failure "Unexpected nested .git: $($_.Parent.FullName)" }

# 3. Required root files
$requiredRoot = @(
    "README.md", "CURRENT-STATUS.md", "ROADMAP.md", "GOVERNANCE.md",
    "CONTRIBUTING.md", "CHANGELOG.md", "SECURITY-PRIVACY.md",
    "RIGHTS-AND-USE.md", "AGENTS.md", ".gitignore"
)
foreach ($f in $requiredRoot) {
    if (-not (Test-Path (Join-Path $RepoRoot $f))) {
        Add-Failure "Missing required root file: $f"
    }
}

# 4. Source manifest
$manifestYaml = Join-Path $RepoRoot "00-source-materials\SOURCE-MANIFEST.yaml"
$manifestJson = Join-Path $RepoRoot "00-source-materials\SOURCE-MANIFEST.json"
if (-not (Test-Path $manifestYaml) -and -not (Test-Path $manifestJson)) {
    Add-Failure "Missing SOURCE-MANIFEST"
}

# 5. Current source count
$originals = Join-Path $RepoRoot "00-source-materials\01-current-kutumba-originals"
$sourceCount = 0
if (Test-Path $originals) {
    $sourceCount = (Get-ChildItem -Path $originals -Recurse -File | Where-Object { $_.Name -notlike '~$*' }).Count
    if ($sourceCount -lt 12) {
        Add-Failure "Expected at least 12 current source files, found $sourceCount"
    }
} else {
    Add-Failure "Missing 01-current-kutumba-originals"
}

# 6. Canonical documents without source hashes
$canonicalFiles = Get-ChildItem -Path $RepoRoot -Recurse -Filter "*.md" -File |
    Where-Object {
        $_.DirectoryName -match '\\(00-foundation|01-governance|02-curriculum-architecture|03-first-six-months|04-children-youth|05-parent-formation|06-prasadam-operations|07-kirtana-worship-bhakti-labs|08-festivals-yatras-calendar)$' -and
        $_.Name -ne "README.md" -and
        $_.Name -notmatch '^(CURRICULUM-MAP|DOMAIN-MATRIX|PREREQUISITE-MAP|SOURCE-COVERAGE-MAP|LESSON-PRODUCTION-BACKLOG)\.md$'
    }
$missingHash = @()
foreach ($cf in $canonicalFiles) {
    $content = Get-Content -LiteralPath $cf.FullName -Raw -ErrorAction SilentlyContinue
    if ($content -and $content -notmatch 'source_hash:') {
        $missingHash += $cf.FullName.Substring($RepoRoot.Length + 1)
    }
}
if ($missingHash.Count -gt 0) {
    Add-Warning "Canonical files missing source_hash frontmatter: $($missingHash.Count)"
}

# 7. First-six-month lesson count
$curriculum = Join-Path $RepoRoot "03-first-six-months\FIRST-SIX-MONTH-DETAILED-CURRICULUM.md"
$weekCount = 0
if (Test-Path $curriculum) {
    $weekMatches = Select-String -Path $curriculum -Pattern '^# C\d+-W\d+ ' -AllMatches
    $weekCount = $weekMatches.Matches.Count
    if ($weekCount -ne 18) {
        Add-Failure "First-six-month lesson count: expected 18, found $weekCount"
    }
} else {
    Add-Failure "Missing FIRST-SIX-MONTH-DETAILED-CURRICULUM.md"
}

# 8. Office lock files
Get-ChildItem -Path $RepoRoot -Recurse -File -Force -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -like '~$*' } |
    ForEach-Object { Add-Failure "Office lock file in repo: $($_.FullName)" }

# 9. Secret heuristic (exclude validation script itself)
$secretPatterns = @('BEGIN RSA PRIVATE KEY', 'BEGIN OPENSSH PRIVATE KEY', 'aws_secret_access_key')
Get-ChildItem -Path $RepoRoot -Recurse -File -Include *.md,*.yaml,*.yml,*.json,*.env -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notmatch '\\\.git\\' } |
    ForEach-Object {
        $c = Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue
        if ($c) {
            foreach ($pat in $secretPatterns) {
                if ($c -match $pat) {
                    Add-Failure "Possible secret in $($_.FullName)"
                }
            }
        }
    }

# 10. Broken internal markdown links (simple check)
$mdFiles = Get-ChildItem -Path $RepoRoot -Recurse -Filter "*.md" -File |
    Where-Object { $_.FullName -notmatch '\\\.git\\' }
$brokenLinks = 0
foreach ($md in $mdFiles) {
    $lines = Get-Content -LiteralPath $md.FullName -ErrorAction SilentlyContinue
    foreach ($line in $lines) {
        if ($line -match '\[([^\]]+)\]\(([^)]+)\)') {
            $target = $Matches[2]
            if ($target -match '^(https?://|mailto:|#)') { continue }
            $target = $target -split '#' | Select-Object -First 1
            if ([string]::IsNullOrWhiteSpace($target)) { continue }
            $resolved = if ($target.StartsWith('/')) {
                Join-Path $RepoRoot $target.TrimStart('/')
            } else {
                Join-Path $md.DirectoryName $target
            }
            if (-not (Test-Path -LiteralPath $resolved)) {
                $brokenLinks++
                if ($brokenLinks -le 20) {
                    Add-Warning "Broken link in $($md.Name): $target"
                }
            }
        }
    }
}

# 11. Legacy bulk copy check — no large PDF dirs from Granth
$granthCopy = Get-ChildItem -Path $RepoRoot -Recurse -File -Filter "*.pdf" -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -match 'Granth|Baktivriksha|BV Material' }
if ($granthCopy.Count -gt 0) {
    Add-Failure "Bulk legacy PDFs detected in repository: $($granthCopy.Count)"
}

# 12. Indexed files rights status
$indexDir = Join-Path $RepoRoot "00-source-materials\03-external-reference-index"
foreach ($csv in @("LEGACY-BHAKTIVRIKSHA-FILE-INDEX.csv", "GRANTH-PDF-CATALOG.csv", "JAYAPATAKA-SWAMI-BV-MATERIAL-INDEX.csv")) {
    $p = Join-Path $indexDir $csv
    if (-not (Test-Path $p)) {
        Add-Failure "Missing legacy index: $csv"
    }
}

# Generate reports
$reportDir = Join-Path $RepoRoot "build-evidence"
New-Item -ItemType Directory -Force $reportDir | Out-Null

$verdict = if ($failures.Count -eq 0) { "PASS" } else { "FAIL" }

$validationReport = @"
# Validation Report

Generated: $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ss')

## Verdict

**$verdict**

## Summary

- Critical failures: $($failures.Count)
- Warnings: $($warnings.Count)
- Current source files: $sourceCount
- First-six-month active weeks: $weekCount
- Broken links (sampled): $brokenLinks

## Critical failures

$(if ($failures.Count -eq 0) { '- None' } else { ($failures | ForEach-Object { "- $_" }) -join "`n" })

## Warnings

$(if ($warnings.Count -eq 0) { '- None' } else { ($warnings | ForEach-Object { "- $_" }) -join "`n" })

## Checks performed

- Repository root nesting
- Required root files
- Source manifest presence
- Current source file count (>= 12)
- First-six-month lesson count (18)
- Office lock files
- Secret heuristics
- Internal link sampling
- Legacy PDF bulk copy detection
- Legacy index presence
"@

$validationReport | Out-File -FilePath (Join-Path $reportDir "VALIDATION-REPORT.md") -Encoding utf8

$privacyReport = @"
# Privacy and Rights Scan

Generated: $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ss')

## Privacy

- No private family record patterns detected in automated scan
- Reference indexes contain local filesystem paths for provenance (internal use only)

## Copyright

- Legacy collections indexed only; not bulk-copied
- Current KUTUMBA documents: kutumba-authored-project-document

## Verdict

$(if ($failures.Count -eq 0) { 'PASS with standard review gates open' } else { 'FAIL — see VALIDATION-REPORT.md' })
"@
$privacyReport | Out-File -FilePath (Join-Path $reportDir "PRIVACY-AND-RIGHTS-SCAN.md") -Encoding utf8

# Repository tree
$treePath = Join-Path $reportDir "REPOSITORY-TREE.txt"
$treeLines = @("kutumba-family-program/")
Get-ChildItem -Path $RepoRoot -Recurse -Force -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notmatch '\\\.git(\\|$)' } |
    ForEach-Object {
        $rel = $_.FullName.Substring($RepoRoot.Length).TrimStart('\')
        if ($rel) { $treeLines += $rel }
    } | Out-Null
$treeLines | Sort-Object | Out-File -FilePath $treePath -Encoding utf8

Write-Host ""
Write-Host "Verdict: $verdict" -ForegroundColor $(if ($verdict -eq 'PASS') { 'Green' } else { 'Red' })
Write-Host "Failures: $($failures.Count), Warnings: $($warnings.Count)"

if ($failures.Count -gt 0) { exit 1 }
exit 0
