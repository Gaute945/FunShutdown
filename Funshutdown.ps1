for ($i = 1; $i -lt 4; $i++) {
    Start-Sleep(3);
    Write-Host "shutdown in " $i
    Start-Process -FilePath "C:\ProgramData\chocolatey\lib\mpv.install\tools\mpv.exe" -ArgumentList "C:\Users\MrBoobi\OneDrive - Vestland fylkeskommune\Konsept utv & prog\Prog\Root\FunShutdown\pipes.mp3"
    Start-Sleep(1);
}
shutdown /s