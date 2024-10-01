import ctypes
import random

def russian_roulette():
    random_number = random.randint(1,6)
    if random_number == 6:
        ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    print(random_number)

russian_roulette()