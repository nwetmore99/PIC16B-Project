import subprocess
import time
import pyautogui

def increase_volume():
    pyautogui.press(u'KEYTYPE_SOUND_UP')


def decrease_volume():
    pyautogui.press(u'KEYTYPE_SOUND_DOWN')

def skip_track():
    pyautogui.press(u'KEYTYPE_NEXT')
    time.sleep(3)

def play_pause():
    pyautogui.press(u'KEYTYPE_PLAY')
    time.sleep(1)

# exec(open('win_volumeup.py').read())                
# exec(open('win_volumedown.py').read())
# exec(open('win_playpause.py').read())