# imports
import time
import pyautogui
import platform
import subprocess

os = platform.system()

#####
# The functions below ALL auto-detect your operating system. These are
# designed around MacOS and Windows. 
# NOTE: scrub_spotify() is NOT functional for Windows. 
#####

def increase_volume():
    """
    The increase_volume() function allows Python to increase the volume of
    your system.
    """
    # MacOS Execute
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_SOUND_UP') 
    # Windows Execute
    else:
        pyautogui.press("volumeup")

def decrease_volume():
    """
    The decrease_volume() function allows Python to decrease the volume of
    your system.
    """
    # MacOS Execute
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_SOUND_DOWN')
    # Windows Execute
    else:
        pyautogui.press("volumedown")

def play_pause():
    """
    The play_pause() function allows Python to pause or play any media on
    your system. 
    """
    # MacOS Execute
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_PLAY')
    # Windows Execute
    else:
        pyautogui.press("playpause")
    time.sleep(1)

def skip_track():
    """
    The skip_track() function allows Python to skip to the next song in a
    playlist. 
    """
    # MacOS Execute
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_NEXT')
    # Windows Execute
    else:
        pyautogui.press("nexttrack")
    time.sleep(1)

def prev_track():
    """
    The prev_track() function allows Python to go back to the previous song in
    a playlist.
    """
    # MacOS Execute
    if os == "Darwin":
        pyautogui.press(u'KEYTYPE_PREVIOUS')
    # Windows Execute
    else:
        pyautogui.press("prevtrack")
    time.sleep(1)

def is_spotify_running():
    """
    The is_spotify_running() function is used to make sure Spotify is open
    on a MacOS system.
    """
    # MacOS Execute
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
    # Skip if not MacOS. Functionality not provided in Windows.
    else:
        pass

def scrub_spotify(offset):
    """
    The scrub_spotify() function allows Python to scrub through a song or 
    podcast in Spotify of a MacOS system.
    """
    # MacOS Execute
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
    # Skip if not MacOS. Functionality not provided in Windows.
    else:
        pass
