# imports
import time
import pyautogui
import platform
import subprocess

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
    time.sleep(1)

def prev_track():
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_PREVIOUS')
    else:
        pyautogui.press("prevtrack")
    time.sleep(1)

def is_spotify_running():
    if os == 'Darwin':
        # AppleScript to check if Spotify is running
        applescript = '''
            tell application "System Events"
                set isRunning to (count of (every process whose name is "Spotify")) > 0
            end tell
            return isRunning
        '''

        # Execute AppleScript with osascript and capture the result
        result = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)

        # Convert the result to a boolean
        return result.stdout.strip() == 'true'
    else:
        pass
def scrub_spotify(offset):
    if os == 'Darwin':
        if is_spotify_running():
            # AppleScript to scrub Spotify
            applescript = f'''
                tell application "Spotify"
                    set currentTrack to the current track
                    set currentPosition to player position
                    set player position to currentPosition + {offset} # Scrub forward by (typically) 10 seconds, adjust as needed
                end tell
            '''

            # Execute the AppleScript using osascript
            subprocess.run(['osascript', '-e', applescript])
    else:
        pass
