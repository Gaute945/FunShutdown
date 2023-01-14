import os
import win10toast

from win10toast import ToastNotifier
from preferredsoundplayer import playsound

sound = "C:/Users/MrBoobi/OneDrive - Vestland fylkeskommune/Konsept utv & prog/Prog/Root/FunShutdown/pipes.mp3"
noti = ToastNotifier()

noti.show_toast(
    "På tide og sova",
    "3",
    duration=1,
)
playsound(sound)

noti.show_toast(
    "På tide og sova",
    "2",
    duration=1,
)
playsound(sound)

noti.show_toast(
    "På tide og sova",
    "1",
    duration=1,
)
playsound(sound)

noti.show_toast(
    "På tide og sova",
    "0",
    duration=1,
)
playsound(sound)

os.system("shutdown /s /t 1")