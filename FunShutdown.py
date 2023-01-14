import os
import win10toast

from win10toast import ToastNotifier
from preferredsoundplayer import playsound

noti = ToastNotifier()

noti.show_toast(
    "På tide og sova",
    "3",
    duration=1,
)
playsound("FunShutdown/pipes.mp3")

noti.show_toast(
    "På tide og sova",
    "2",
    duration=1,
)
playsound("FunShutdown/pipes.mp3")

noti.show_toast(
    "På tide og sova",
    "1",
    duration=1,
)
playsound("FunShutdown/pipes.mp3")

noti.show_toast(
    "På tide og sova",
    "0",
    duration=1,
)
playsound("FunShutdown/pipes.mp3")

#os.system("shutdown /s /t 1")