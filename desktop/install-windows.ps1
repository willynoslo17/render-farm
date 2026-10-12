# Usage: powershell -ExecutionPolicy Bypass -File install-windows.ps1 -App <opentoonz|pinta|vidcutter|olive|affine>
# Pinned official installer, SHA256-verified, then run. (winget/choco alternatives are not version+hash pinned.)
param([Parameter(Mandatory)][ValidateSet('opentoonz','pinta','vidcutter','olive','affine')][string]$App)
$ErrorActionPreference = 'Stop'
$line = Get-Content "$PSScriptRoot\apps.lock" | Where-Object { $_ -match "^$App windows " } | Select-Object -First 1
if (-not $line) { throw "no Windows build for $App" }
$p = $line -split '\s+'; $sha = $p[2]; $url = $p[3]
$out = Join-Path $env:TEMP (Split-Path $url -Leaf)
Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing
if ((Get-FileHash $out -Algorithm SHA256).Hash.ToLower() -ne $sha) { Remove-Item $out; throw "SHA256 mismatch for $App" }
Start-Process -FilePath $out -Wait
