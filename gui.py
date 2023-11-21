#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 01:52:31 2023

@author: josh
"""

### GUI Design for Camera App ###

# Package for GUI #
import PySimpleGUI as sg

## Stored Text ##
intro = "This program enables hand gestures to interact with your computer."

## Creating GUI ##
sg.theme("DarkBlue14")
layout = [[sg.Text('Hand Gesture Inputs', font=('Arial', 20))],
          [sg.Text(intro)],
          [sg.HSep()],
          [sg.Text('Enable Camera:', font=('Arial', 15)), sg.Button('Turn on camera')],
          [sg.HSep()],
          [sg.Text('List of Recognized Gestures', font=('Arial', 15))],
          [sg.Table([['Point Up',''],
                     ['Point Down',''],
                     ['Thumbs Up',''],
                     ['Open Hand',''],
                     ['Gesture 6','']],
                     ['Recognized Gesture','Output'], 
                     num_rows=3,
                     )],
          [sg.HSep()],
          [sg.Text('Necessary Hotkeys:', font=('Arial', 15))],
          [sg.Frame('Keyboard Inputs', [[
              sg.Text('Q: Quit Camera'),
              sg.Text('P: Detect Gesture')
              ]])],
          [sg.Quit()]]      

window = sg.Window('Hand Gesture Inputs', layout, size = (500,400)) 

# Everything runs in the loop here.
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
        
    if event == 'Turn on camera':
        exec(open('camera.py').read())
    
window.close()


## Note from Josh: To bypass camera perms, launch program through terminal. ##