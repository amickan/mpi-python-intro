# LexTALE English
# In this experiment, people will see a number of English words, one after another. 
# Their task is to decide for each word whether it is an actual existing English word or not. 
# Reaction times and accuracy will be recorded and saved in a csv file. 

# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event, gui
import pandas as pd
import numpy as np
import os
import time
import sys

## prepare stimuli and window 
# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((1000, 800), color='grey')
# prepare text stimulus
text = visual.TextStim(win, text='0', color='white', wrapWidth=800, height = 24, units = 'pix')
stim = visual.TextStim(win, text='0', color='white', wrapWidth=800, height = 30, units = 'pix')
# load trial dataframe 
items = pd.read_table('testlist.txt')

# ask for participant number
gui = gui.Dlg()
gui.addField("Pp-nr:")
gui.show()
ppnr = gui.data[0]

# set file name including the pnumber, and check whether the file exists already
filename = ppnr + "_data_LexTALE.csv"
if os.path.exists(filename):
    text.setText("This participant number has already been used! Use a different number.")
    text.draw()
    win.flip()
    core.wait(2)
    win.close()
    sys.exit("Stopped execution because file " + filename + " already exists!")
dataFile = open(filename, 'w') 
dataFile.write("{}, {}, {}, {}, {}, {}\n".format("trial_nr", "word", "wordstatus", "response", "rt", "error"))

# show instructions
text.setText("""This test consists of 60 trials, in each of which you will see a string of letters.

Your task is to decide whether the letter string is an existing English word or not. 
If you think it is an existing English word, you click on the RIGHT arrow key, 
and if you think it is not an existing English word, you click on the LEFT arrow key.

You have as much time as you like for each decision.

If you wish to stop the experiment, press ESCAPE at any time. 

If everything is clear, press SPACE to start the experiment.""")
text.draw()  # draw the stimulus to the back buffer
win.flip()

# wait for PP to press space to continue
keys = event.waitKeys(keyList=["space"])

# run experiment 
trialnr = 0
for word in items.word:
    trialnr += 1
    # start each trial with a fixation cross of 500 ms
    stim.setText('+')
    stim.draw()  # draw the stimulus to the back buffer
    win.flip()
    core.wait(0.5)
    # then show the word 
    stim.setText(word)
    stim.draw()
    win.flip()
    t0 = time.clock()
    # and wait for a button press, no time limit
    answer = event.waitKeys(keyList=["right", "left", "escape"])
    t1 = time.clock()
    rt = t1-t0 # get reaction time
    
    if answer[0]=="escape":
        break
    
    # convert answer code to a number
    if answer[0] == "right":
        response = 1
    else:
        response = 0
     
    # check answer for correctness
    if response == items.wordstatus[trialnr-1]:
        errorcode = 0
    else:
        errorcode = 1
         
    dataFile.write("{}, {}, {}, {}, {}, {}\n".format(trialnr, word, items.wordstatus[trialnr-1], response, rt, errorcode))

# show a finished message
stim.setText('You are done! :-) ')
stim.draw()
win.flip()
core.wait(1)

win.close()  # close the window
