# PIC16B-Project

## OVERVIEW: 

In this project, our aim was to create a program that could perform simple tasks such as controlling volume and media with nothing but a wave of the hand. Using Google's MediaPipe as well as a nueral network, we took location nodes of a user's hand tracked by the camera on their device and matched it with set gestures that were linked to various media control functions. The ideal intended use is for example, having Spotify and our program run in the background while working on an essay. This way, the user could just put their hand up to their computer to change volume, pause, skip, etc. However, this program also works for any media the computer is playing: Youtube, Netflix, and more.

## TO USE: 

You have already successfully downloaded the repository! All you need to do is open the terminal and navigate to the folder the repository is stored in. Then type `python gui.py` and sit back in amazement as you control your media like a wizard! 

## Gestures: 
### Pointing with your index finger
up = volume up

down = volume down

left = rewind 10 seconds (only implemented for Spotify)

right = fast forward 10 seconds (only implemented for Spotify)


### Pointing with your thumb
left = previous track

right = skip track

### Full palm facing the camera
pause/play media
