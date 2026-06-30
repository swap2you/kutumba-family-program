param(
    [string]$RepoRoot = "C:\Development\Workspace\DevotionalRepo\kutumba-family-program"
)

$ErrorActionPreference = "Stop"

$Sources = @(
    [pscustomobject]@{ Name = "CurrentKutumba"; Path = "C:\Users\swap2\Downloads\Personal\0. KUTUMBA SANGA"; Mode = "CopyCurrent" },
    [pscustomobject]@{ Name = "LegacyBhaktivriksha"; Path = "C:\Users\swap2\Downloads\Personal\5. Devotional\1. Baktivriksha"; Mode = "IndexOnly" },
    [pscustomobject]@{ Name = "Granth"; Path = "C:\Users\swap2\Downloads\Personal\5. Devotional\Granth"; Mode = "IndexOnly" },
    [pscustomobject]@{ Name = "JayapatakaSwamiBV"; Path = "C:\Users\swap2\Downloads\Personal\5. Devotional\1. Baktivriksha\BV Material"; Mode = "IndexOnly" }
)

$Output = Join-Path $RepoRoot "build-evidence\preflight-source-inventory.csv"
New-Item -ItemType Directory -Force (Split-Path $Output) | Out-Null

$rows = foreach ($source in $Sources) {
    if (-not (Test-Path -LiteralPath $source.Path)) {
        [pscustomobject]@{
            Source = $source.Name
            Mode = $source.Mode
            FullName = $source.Path
            RelativePath = ""
            Extension = ""
            Length = 0
            LastWriteTime = ""
            Status = "SOURCE_PATH_MISSING"
        }
        continue
    }

    Get-ChildItem -LiteralPath $source.Path -Recurse -File -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -notlike '~$*' } |
        ForEach-Object {
            [pscustomobject]@{
                Source = $source.Name
                Mode = $source.Mode
                FullName = $_.FullName
                RelativePath = $_.FullName.Substring($source.Path.Length).TrimStart('\')
                Extension = $_.Extension
                Length = $_.Length
                LastWriteTime = $_.LastWriteTime.ToString("s")
                Status = "FOUND"
            }
        }
}

$rows | Export-Csv -LiteralPath $Output -NoTypeInformation -Encoding UTF8
Write-Host "Wrote $Output"
