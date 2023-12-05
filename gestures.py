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
    # AppleScript to check if Spotify is running
    applescript = '''
        tell application "System Events"
            set isRunning to (count of (every process whose name is "Spotify")) > 0
        end tell
        return isRunning
    '''

    # Execute the AppleScript using osascript and capture the result
    result = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)
    
    # Convert the result to a boolean
    return result.stdout.strip() == 'true'

def scrub_spotify(offset):
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
        print("Spotify is not running.") 