param(
    [string]$OutputPath = (Join-Path $PSScriptRoot "..\assets\social-preview.png")
)

Add-Type -AssemblyName System.Drawing

$width = 1280
$height = 640
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputPath)
$outputDirectory = [System.IO.Path]::GetDirectoryName($resolvedOutput)
[System.IO.Directory]::CreateDirectory($outputDirectory) | Out-Null

$bitmap = New-Object System.Drawing.Bitmap($width, $height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

$background = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
    (New-Object System.Drawing.Rectangle(0, 0, $width, $height)),
    ([System.Drawing.Color]::FromArgb(10, 18, 38)),
    ([System.Drawing.Color]::FromArgb(24, 72, 130)),
    25
)
$graphics.FillRectangle($background, 0, 0, $width, $height)

$accentBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(56, 189, 248))
$mutedBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(191, 219, 254))
$whiteBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
$cardBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(42, 255, 255, 255))
$borderPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(110, 147, 197, 253), 2)

$graphics.FillEllipse($accentBrush, 76, 82, 22, 22)
$graphics.DrawLine((New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(125, 211, 252), 4)), 87, 105, 87, 535)

$labelFont = New-Object System.Drawing.Font("Segoe UI Semibold", 22, [System.Drawing.FontStyle]::Bold)
$titleFont = New-Object System.Drawing.Font("Segoe UI", 54, [System.Drawing.FontStyle]::Bold)
$subtitleFont = New-Object System.Drawing.Font("Segoe UI", 25, [System.Drawing.FontStyle]::Regular)
$metricFont = New-Object System.Drawing.Font("Segoe UI", 26, [System.Drawing.FontStyle]::Bold)
$smallFont = New-Object System.Drawing.Font("Segoe UI", 18, [System.Drawing.FontStyle]::Regular)

$graphics.DrawString("OPEN-SOURCE DISCOVERY & DOWNLOAD HUB", $labelFont, $accentBrush, 125, 72)
$graphics.DrawString("32 Math Modeling", $titleFont, $whiteBrush, 120, 145)
$graphics.DrawString("Agents & Skills", $titleFont, $whiteBrush, 120, 215)
$graphics.DrawString("Curated  |  Classified  |  Commit-pinned  |  Download-verified", $subtitleFont, $mutedBrush, 125, 310)

$cards = @(
    @{ X = 125; Width = 250; Main = "32 / 32"; Sub = "valid archives" },
    @{ X = 395; Width = 250; Main = "6 groups"; Sub = "task-oriented catalog" },
    @{ X = 665; Width = 250; Main = "SHA-256"; Sub = "verification records" }
)

foreach ($card in $cards) {
    $rect = New-Object System.Drawing.Rectangle($card.X, 395, $card.Width, 112)
    $graphics.FillRectangle($cardBrush, $rect)
    $graphics.DrawRectangle($borderPen, $rect)
    $graphics.DrawString($card.Main, $metricFont, $whiteBrush, $card.X + 20, 410)
    $graphics.DrawString($card.Sub, $smallFont, $mutedBrush, $card.X + 20, 458)
}

$graphics.DrawString("github.com/caojian1134/mathmodel-agent-resources", $smallFont, $mutedBrush, 125, 555)

$bitmap.Save($resolvedOutput, [System.Drawing.Imaging.ImageFormat]::Png)

$background.Dispose()
$accentBrush.Dispose()
$mutedBrush.Dispose()
$whiteBrush.Dispose()
$cardBrush.Dispose()
$borderPen.Dispose()
$labelFont.Dispose()
$titleFont.Dispose()
$subtitleFont.Dispose()
$metricFont.Dispose()
$smallFont.Dispose()
$graphics.Dispose()
$bitmap.Dispose()

Write-Output $resolvedOutput
