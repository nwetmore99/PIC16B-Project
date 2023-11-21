import subprocess
import time
import pyautogui
import platform

os = platform.system()

def increase_volume():
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_SOUND_UP') # for mac
    else:
        pyautogui.press("volumeup") # for windows


def decrease_volume():
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_SOUND_DOWN') # for mac
    else:
        pyautogui.press("volumedown") # for windows


def play_pause():
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_PLAY')
    else:
        pyautogui.press("playpause")
    time.sleep(1)

def skip_track():
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_NEXT')
    else:
        pyautogui.press("nexttrack")
    time.sleep(3)

# exec(open('win_volumeup.py').read())                
# exec(open('win_volumedown.py').read())
# exec(open('win_playpause.py').read())