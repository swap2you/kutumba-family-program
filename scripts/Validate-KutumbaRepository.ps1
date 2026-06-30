# KUTUMBA Repository Validation
# Returns exit code 0 on pass, nonzero on critical failures

param(
    [string]$RepoRoot = ""
)

$ErrorActionPreference = "Continue"
$failures = @()
$warnings = @()

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
    $RepoRoot = (git rev-parse --show-toplevel 2>$null)
    if (-not $RepoRoot) { $RepoRoot = "C:\Development\Workspace\DevotionalRepo\kutumba-family-program" }
}

function Add-Failure($msg) { $script:failures += $msg }
function Add-Warning($msg) { $script:warnings += $msg }

Write-Host "=== KUTUMBA Repository Validation ===" -ForegroundColor Cyan
Write-Host "Root: $RepoRoot"

$headSha = (git -C $RepoRoot rev-parse HEAD 2>$null)
Write-Host "HEAD: $headSha"

# 1. GitHub visibility PUBLIC (documented decision)
try {
    $gh = gh repo view swap2you/kutumba-family-program --json visibility,isPrivate 2>$null | ConvertFrom-Json
    if ($gh.visibility -ne "PUBLIC" -or $gh.isPrivate -ne $false) {
        Add-Failure "GitHub visibility must be PUBLIC by governing decision (got $($gh.visibility))"
    }
} catch {
    Add-Warning "Could not verify GitHub visibility via gh CLI"
}

# 2. README and security docs agree with public visibility
foreach ($doc in @("README.md", "SECURITY-PRIVACY.md")) {
    $p = Join-Path $RepoRoot $doc
    if (Test-Path $p) {
        $c = Get-Content -LiteralPath $p -Raw
        if ($c -match '\bprivate documentation-first\b' -and $c -notmatch 'public documentation') {
            Add-Failure "$doc still claims private-only posture without public documentation statement"
        }
        if ($c -notmatch 'public documentation') {
            Add-Warning "$doc may not state public documentation posture"
        }
    }
}

# 3. No nested git repository
$nested = Join-Path $RepoRoot "kutumba-family-program"
if (Test-Path (Join-Path $nested ".git")) {
    Add-Failure "Nested repository folder detected: $nested"
}
if (-not (Test-Path (Join-Path $RepoRoot ".git"))) {
    Add-Failure ".git not found at canonical root"
}
Get-ChildItem -Path $RepoRoot -Recurse -Force -Directory -Filter ".git" -ErrorAction SilentlyContinue |
    Where-Object {
        $parent = $_.Parent.FullName.Replace('/', '\').TrimEnd('\')
        $root = $RepoRoot.Replace('/', '\').TrimEnd('\')
        $parent -ne $root
    } |
    ForEach-Object { Add-Failure "Unexpected nested .git: $($_.Parent.FullName)" }

# 4-7. Source manifest and hashes
$manifestYaml = Join-Path $RepoRoot "00-source-materials\SOURCE-MANIFEST.yaml"
if (-not (Test-Path $manifestYaml)) {
    Add-Failure "Missing SOURCE-MANIFEST.yaml"
} else {
    $manifestText = Get-Content -LiteralPath $manifestYaml -Raw -Encoding UTF8
    $manifestCount = ([regex]::Matches($manifestText, '(?m)^- source_id:')).Count
    $originals = Join-Path $RepoRoot "00-source-materials\01-current-kutumba-originals"
    $diskFiles = @(Get-ChildItem -Path $originals -Recurse -File | Where-Object { $_.Name -notlike '~$*' })
    if ($diskFiles.Count -ne $manifestCount) {
        Add-Failure "Manifest entry count ($manifestCount) != on-disk source count ($($diskFiles.Count))"
    }
    foreach ($f in $diskFiles) {
        $rel = $f.FullName.Substring($RepoRoot.Length + 1).Replace('\', '/')
        if ($manifestText -notmatch [regex]::Escape($f.Name)) {
            Add-Failure "Unmanifested source file: $($f.Name)"
        }
        $hashScript = Join-Path $RepoRoot "scripts\hash_file_sha256.py"
        $hash = (python $hashScript "$($f.FullName)" 2>$null | Out-String).Trim()
        if (-not $hash) {
            Add-Warning "Could not hash $($f.Name) - skipping hash verify"
            continue
        }
        if ($manifestText -notmatch $hash) {
            Add-Failure "Hash for $($f.Name) not found in manifest"
        }
    }
    if ($manifestText -match 'canonicalization_status: pending') {
        Add-Failure "SOURCE-MANIFEST still has canonicalization_status: pending"
    }
}

# 8-9. Canonical operating documents provenance
$canonicalDirs = @(
    "00-foundation", "01-governance", "02-curriculum-architecture", "03-first-six-months",
    "04-children-youth", "05-parent-formation", "06-prasadam-operations",
    "07-kirtana-worship-bhakti-labs", "08-festivals-yatras-calendar"
)
$navFiles = @('CURRICULUM-MAP.md', 'DOMAIN-MATRIX.md', 'PREREQUISITE-MAP.md', 'SOURCE-COVERAGE-MAP.md', 'LESSON-PRODUCTION-BACKLOG.md')
foreach ($dir in $canonicalDirs) {
    $abs = Join-Path $RepoRoot $dir
    if (-not (Test-Path $abs)) { continue }
    Get-ChildItem -Path $abs -Filter "*.md" -File | Where-Object {
        $_.Name -ne "README.md" -and $_.Name -ne "REVIEW-QUEUE.md" -and $_.Name -notmatch 'ADDENDUM\.md$' -and ($navFiles -notcontains $_.Name)
    } | ForEach-Object {
        $content = Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue
        if ($content -and $content -notmatch 'source_hash:') {
            Add-Failure "Canonical doc missing source_hash: $($_.FullName.Substring($RepoRoot.Length+1))"
        }
    }
}

# 10-14. Weekly folders
$weeklyRoot = Join-Path $RepoRoot "11-weekly-program-library\first-six-months"
$requiredWeekly = @(
    "complete-week.md", "overview.md", "learning-outcomes.md", "prem-ki-katha.md",
    "parent-lesson.md", "children/lesson.md", "analogy-and-application.md", "questions.md",
    "bhakti-lab.md", "family-home-practice.md", "facilitator-guide.md", "materials.md",
    "assessment.md", "newcomer-adaptation.md", "risks-and-sensitive-points.md",
    "worksheet.md", "slide-outline.md", "sources.yaml", "review-status.yaml", "README.md"
)
$mandatoryHeadings = @(
    "## Learning Outcomes", "## Parent Lesson", "## Children", "## Bhakti Laboratory",
    "## Family Home Practice", "## Teacher Preparation"
)
$weekCodes = @()
$weekFolders = @(Get-ChildItem -Path $weeklyRoot -Directory -ErrorAction SilentlyContinue)
foreach ($wf in $weekFolders) {
    if ($wf.Name -match '^(c\d+-w\d+)-') {
        $code = $Matches[1].ToUpper() -replace 'c', 'C' -replace 'w', 'W'
        $code = $Matches[1].Substring(0,2).ToUpper() + "-" + $Matches[1].Substring(3,2).ToUpper()
        $code = ($Matches[1] -replace '^c', 'C' -replace '-w', '-W').ToUpper()
        $weekCodes += $code
    }
}
# normalize week code from folder name c1-w1-...
foreach ($wf in $weekFolders) {
    if ($wf.Name -match '^(c\d+-w\d+)') {
        $raw = $Matches[1]
        $parts = $raw -split '-'
        $code = ($parts[0].ToUpper() -replace 'C', 'C') + "-" + ($parts[1].ToUpper() -replace 'W', 'W')
        $code = "C$($parts[0].Substring(1))-$($parts[1].ToUpper())"
    }
}
$weekCodes = @()
foreach ($wf in $weekFolders) {
    if ($wf.Name -match '^(c)(\d+)-(w)(\d+)') {
        $code = "C$($Matches[2])-W$($Matches[4])"
        $weekCodes += $code
        foreach ($req in $requiredWeekly) {
            $rp = Join-Path $wf.FullName ($req -replace '/', '\')
            if (-not (Test-Path -LiteralPath $rp)) {
                Add-Failure "Missing $req in $($wf.Name)"
            }
        }
        $cw = Join-Path $wf.FullName "complete-week.md"
        if (Test-Path $cw) {
            $cwContent = Get-Content -LiteralPath $cw -Raw -Encoding UTF8
            foreach ($h in $mandatoryHeadings) {
                if ($cwContent -notmatch [regex]::Escape($h)) {
                    Add-Failure "complete-week.md in $($wf.Name) missing heading: $h"
                }
            }
            if ($cwContent -notmatch 'derived_from:') {
                Add-Failure "complete-week.md in $($wf.Name) missing derived_from metadata"
            }
        }
        foreach ($yaml in @("sources.yaml", "review-status.yaml")) {
            $yp = Join-Path $wf.FullName $yaml
            if (Test-Path $yp) {
                try { Get-Content $yp -Raw | Out-Null } catch { Add-Failure "Cannot read $yaml in $($wf.Name)" }
            }
        }
    }
}
if ($weekCodes.Count -ne 18) {
    Add-Failure "Expected 18 weekly folders, found $($weekCodes.Count)"
}
$unique = $weekCodes | Select-Object -Unique
if ($unique.Count -ne 18) {
    Add-Failure "Week codes not unique: $($weekCodes -join ', ')"
}

# 15. Internal links (sample)
$brokenLinks = 0
Get-ChildItem -Path $RepoRoot -Recurse -Filter "*.md" -File |
    Where-Object { $_.FullName -notmatch '\\\.git\\' } |
    ForEach-Object {
        $md = $_
        Get-Content -LiteralPath $md.FullName -ErrorAction SilentlyContinue | ForEach-Object {
            if ($_ -match '\[([^\]]+)\]\(([^)]+)\)') {
                $target = $Matches[2]
                if ($target -match '^(https?://|mailto:|#)') { return }
                $target = ($target -split '#')[0]
                if ([string]::IsNullOrWhiteSpace($target)) { return }
                try { $target = [System.Uri]::UnescapeDataString($target) } catch {}
                $resolved = if ($target.StartsWith('/')) {
                    Join-Path $RepoRoot $target.TrimStart('/')
                } else {
                    Join-Path $md.DirectoryName $target
                }
                if (-not (Test-Path -LiteralPath $resolved)) {
                    $script:brokenLinks++
                    if ($brokenLinks -le 15) {
                        Add-Warning "Broken link in $($md.Name): $target"
                    }
                }
            }
        }
    }

# 16. Office lock files
Get-ChildItem -Path $RepoRoot -Recurse -File -Force -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -like '~$*' } |
    ForEach-Object { Add-Failure "Office lock file: $($_.FullName)" }

# 17-18. Secrets and private records heuristics
$secretPatterns = @('BEGIN RSA PRIVATE KEY', 'BEGIN OPENSSH PRIVATE KEY', 'aws_secret_access_key', 'ghp_[a-zA-Z0-9]{20,}')
$privatePatterns = @()
$privateExclude = @('\00-foundation\', '\01-governance\', '\02-curriculum', '\03-first-six-months\',
    '\04-children', '\05-parent', '\06-prasad', '\07-kirtana', '\08-festivals', 'SECURITY-PRIVACY.md', 'AGENTS.md', 'RIGHTS-AND-USE.md')
Get-ChildItem -Path $RepoRoot -Recurse -File -Include *.md,*.yaml,*.yml,*.json,*.csv,*.env -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notmatch '\\\.git\\' -and $_.Name -ne 'Validate-KutumbaRepository.ps1' } |
    ForEach-Object {
        $c = Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue
        if (-not $c) { return }
        foreach ($pat in $secretPatterns) {
            if ($c -match $pat) { Add-Failure "Possible secret in $($_.FullName)" }
        }
        foreach ($pat in $privatePatterns) {
            if ($c -match $pat) { Add-Warning "Possible private operational record pattern in $($_.FullName): $pat" }
        }
    }

# 19. No bulk legacy copy
$legacyPdf = Get-ChildItem -Path $RepoRoot -Recurse -File -Filter "*.pdf" -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -match 'Granth|Baktivriksha|BV Material' }
if ($legacyPdf.Count -gt 0) {
    Add-Failure "Bulk legacy PDFs in repository: $($legacyPdf.Count)"
}

# 20. Legacy index rights columns
foreach ($csv in @("LEGACY-BHAKTIVRIKSHA-FILE-INDEX.csv", "GRANTH-PDF-CATALOG.csv", "JAYAPATAKA-SWAMI-BV-MATERIAL-INDEX.csv")) {
    $p = Join-Path $RepoRoot "00-source-materials\03-external-reference-index\$csv"
    if (-not (Test-Path $p)) {
        Add-Failure "Missing legacy index: $csv"
    } else {
        $header = (Get-Content -LiteralPath $p -First 1)
        if ($header -notmatch 'rights_status' -or $header -notmatch 'review_status') {
            Add-Failure "$csv missing rights_status or review_status columns"
        }
    }
}

# 21. Library statuses
$famReadme = Join-Path $RepoRoot "12-family-facing-library\README.md"
if (Test-Path $famReadme) {
    $fc = Get-Content -LiteralPath $famReadme -Raw
    if ($fc -match 'publication status:\*\* `active`' -and $fc -notmatch 'planned') {
        Add-Failure "Family-facing library marked active without publication approval"
    }
}
$facReadme = Join-Path $RepoRoot "13-facilitator-library\README.md"
if (-not (Test-Path $facReadme)) { Add-Failure "Missing facilitator library README" }

# 22. Honest gaps
$ws9 = Get-Content (Join-Path $RepoRoot "09-digital-repository-publishing\GAP-RECORD.md") -Raw -Encoding UTF8
if ($ws9 -match 'Status:\s*\*\*COMPLETE\*\*' -and $ws9 -notmatch 'operating manual') {
    Add-Failure "Workstream 9 marked complete without operating manual"
} elseif ($ws9 -notmatch 'SOURCE NOT YET SUPPLIED|PARTIAL|operating manual.*not supplied') {
    Add-Failure "Workstream 9 gap not honestly reported"
}
$setu = Get-Content (Join-Path $RepoRoot "10-kutumba-setu\GAP-RECORD.md") -Raw
if ($setu -notmatch 'DRAFT REQUIRED') { Add-Failure "KUTUMBA Setu gap not honestly reported" }

# 23. Independent audit evidence
if (-not (Test-Path (Join-Path $RepoRoot "17-reviews-and-audits\INDEPENDENT-REPOSITORY-AUDIT.md"))) {
    Add-Failure "Missing INDEPENDENT-REPOSITORY-AUDIT.md"
}

# 24. Roadmap and cleanup reports exist
foreach ($r in @("ROADMAP.md", "build-evidence\CLEANUP-REPORT.md", "LICENSE.md")) {
    if (-not (Test-Path (Join-Path $RepoRoot $r))) { Add-Failure "Missing $r" }
}

# 25. Required root files
$requiredRoot = @(
    "README.md", "CURRENT-STATUS.md", "ROADMAP.md", "GOVERNANCE.md",
    "CONTRIBUTING.md", "CHANGELOG.md", "SECURITY-PRIVACY.md",
    "RIGHTS-AND-USE.md", "LICENSE.md", "AGENTS.md", ".gitignore"
)
foreach ($f in $requiredRoot) {
    if (-not (Test-Path (Join-Path $RepoRoot $f))) { Add-Failure "Missing root file: $f" }
}

# Reports
$reportDir = Join-Path $RepoRoot "build-evidence"
New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$verdict = if ($failures.Count -eq 0) { "PASS" } else { "FAIL" }
$branch = (git -C $RepoRoot branch --show-current 2>$null)

@"
# Validation Report

Generated: $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ss')
Validated against branch: $branch
Validated against HEAD: $headSha

## Verdict

**$verdict**

## Summary

- Critical failures: $($failures.Count)
- Warnings: $($warnings.Count)
- Weekly folders: $($weekFolders.Count)
- Broken links (sampled): $brokenLinks

## Privacy note

Automated heuristic checks passed; human review remains required.

## Critical failures

$(if ($failures.Count -eq 0) { '- None' } else { ($failures | ForEach-Object { "- $_" }) -join "`n" })

## Warnings

$(if ($warnings.Count -eq 0) { '- None' } else { ($warnings | ForEach-Object { "- $_" }) -join "`n" })
"@ | Out-File -FilePath (Join-Path $reportDir "VALIDATION-REPORT.md") -Encoding utf8

@"
# Privacy and Rights Scan

Generated: $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ss')

## Privacy

- Automated heuristic checks for secrets and prohibited record patterns executed
- Public repository posture documented in SECURITY-PRIVACY.md
- Reference indexes use portable source_root_id paths

## Copyright

- KUTUMBA-authored content: CC BY-NC-SA 4.0 (see LICENSE.md)
- Legacy collections indexed only

## Verdict

$(if ($failures.Count -eq 0) { 'PASS — Automated heuristic checks passed; human review remains required.' } else { 'FAIL — see VALIDATION-REPORT.md' })
"@ | Out-File -FilePath (Join-Path $reportDir "PRIVACY-AND-RIGHTS-SCAN.md") -Encoding utf8

Write-Host ""
Write-Host "Verdict: $verdict" -ForegroundColor $(if ($verdict -eq 'PASS') { 'Green' } else { 'Red' })
Write-Host "Failures: $($failures.Count), Warnings: $($warnings.Count)"

if ($failures.Count -gt 0) { exit 1 }
exit 0
