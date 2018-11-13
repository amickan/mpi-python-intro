# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event
import os
os.chdir("./PicturesRotation")

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600), color='teal')
pic = visual.ImageStim(win = win, image = None)
win.flip()

count = 0 
speed = 1 # to control rotation speed

# use a while loop to show a rotating hat
while True:
    
    if count > 359:
        count = 0
    if count < 0:
        count = 359
    
    keyPress = event.getKeys(keyList=['space', 'up', 'down', 'return', 'right', 'left'])
    if 'space' in keyPress: #stop the presentation with spacebar
        break
    if 'up' in keyPress: # speed up
        speed += 1
    if 'down' in keyPress: # slow down
        speed -= 1
    if 'return' in keyPress: # pause and continue
        event.waitKeys(keyList = 'return')
    if 'right' in keyPress: # clockwise
        speed = speed*(-1)
    if 'left' in keyPress: # counterclockwise
        speed = speed*(-1)
        
    pic.setImage(f'hat{count}.png')
    pic.draw()
    win.flip()
        
    #increment the file counter
    count += speed
        

win.close()  # close the window

