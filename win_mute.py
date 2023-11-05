#need to run `pip install pycaw` first
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#get current mute status, 0 means unmuted 1 means muted
current=volume.GetMute()

#if system is not muted, mute
if current==0:
    volume.SetMute(1, None)
    
#if system is muted, unmute    
if current==1:
    volume.SetMute(0, None)
    
print(volume.GetMute())
