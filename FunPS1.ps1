for ($i = 1; $i -lt 4; $i++) {
    Start-Sleep(0);
    Write-Host "shutdown in " $i
    Start-Process -FilePath "C:\ProgramData\chocolatey\lib\mpv.install\tools\mpv.exe" -ArgumentList .\pipes.mp3
}
write-Host "shutdown"
#shutdown /s