$saat= New-ScheduledTaskTrigger -AtLogOn
$uygulama    = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument 'C:\websiteBlocker.pyw'
$ayar = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType "S4U" -RunLevel Highest
Register-ScheduledTask -TaskName "websiteBlocker" -Action $uygulama -Trigger $saat -Principal $ayar -Force
