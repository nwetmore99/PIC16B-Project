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
layout = [
          # Introduction Section #
          [sg.Text('Hand Gesture Inputs', font=('Arial', 30))],
          [sg.Text(intro)],
          [sg.HSep()],
          
          # Enable Camera #
          [sg.Text('Enable Camera', font=('Arial', 20))],
          [sg.Button('Turn on camera')],
          [sg.HSep()],
          
          # Settings Tab #
          [sg.Text('Settings',font=('Arial',20))],
          [sg.Text('Input Sensitivity')],
          [sg.Slider([90,99], orientation='h', s=(10,15), 
                     key='-PER-', default_value = 95)],
          # Testing button.
          # [sg.Button('Check')],
          [sg.HSep()],
          
          # Gestures List #
          [sg.Text('List of Recognized Gestures', font=('Arial', 20))],
          [sg.Table([['Point Up','Volume Up'],
                     ['Point Down','Volume Down'],
                     ['Open Hand','Pause/Play'],
                     ['Thumb Left','Previous Song'],
                     ['Thumb Right','Skip Song'],
                     ['Point Left','Scrub Back'],
                     ['Point Right','Scrub Forward']],
                     ['Recognized Gesture','Output'], 
                     num_rows=3
                     )],
          [sg.HSep()],
          
          # Useful Inputs #
          [sg.Text('Necessary Hotkeys:', font=('Arial', 20))],
          [sg.Frame('Keyboard Inputs', [[
              sg.Text('Q: Quit Camera')
              ]])],
          [sg.Quit()]
          ]      

window = sg.Window('Hand Gesture Inputs', layout, size = (800,600)) 

# Everything runs in the loop here.
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    
    # Testing button.
    # if event =='Check':
    #     print("Confidence: ", values['-PER-']/100)
        
    if event == 'Turn on camera':
        exec(open('camera.py').read())
    
    if event == '-PER-':
        window['-PER-'].update(values['-PER-'][:-1])
        confidence_threshold = values['-PER-']/100
    

    
window.close()


## Note from Josh: To bypass camera perms, launch program through terminal. ##