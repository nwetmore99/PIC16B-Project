#need to run `pip install pycaw` first
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
    
current = volume.GetMasterVolumeLevelScalar()
if current==1.0:
    print("Volume Already at Maximum!")
    exit()
if (current>=0) & (current<=0.9):
    volume.SetMasterVolumeLevelScalar(current+0.1, None)
    exit()
if (current>0.9):
    volume.SetMasterVolumeLevelScalar(1.0, None)
