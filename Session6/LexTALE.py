## LexTALE English
# In this experiment, people will see a number of English words, one after another. 
# Their task is to decide for each word whether it is an actual existing English word or not. 
# Reaction times and accuracy will be recorded and saved in a csv file. 

# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event
import pandas as pd
import numpy as np
import psychopy.gui
import os
import time

# ask for participant number
gui = psychopy.gui.Dlg()
gui.addField("Pp-nr:")
gui.show()
ppnr = gui.data[0]

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((1000, 800), color='teal')

# prepare text stimulus
text = visual.TextStim(win, text='0', color='white', wrapWidth=150)

# show instructions
text.setText("""This test consists of about 60 trials, in each of which you will see a string of letters. 
Your task is to decide whether this is an existing English word or not. 
If you think it is an existing English word, you click on the RIGHT arrow key, 
and if you think it is not an existing English word, you click on the LEFT arrow key.

You have as much time as you like for each decision. This part of the experiment will take about 5 minutes.

If everything is clear, press SPACE to start the experiment.""")
text.draw()  # draw the stimulus to the back buffer
win.flip()

# check for key presses
keys = event.waitKeys(keyList=["space"])

# load trial dataframe 
items = pd.read_table('testlist.txt')

# inititate a data frame
data = []

# set file name including the pnumber, and check whether the file exists already
filename = ppnr + "_data_LexTALE.csv"
if os.path.exists(filename):
    sys.exit("File: " + filename + " already exists!")
dataFile = open(filename, 'w') 
dataFile.write("#{}, {}, {}\n".format("word", "response", "rt"))

# start experiment 
for word in items.word:
    # start each trial with a fixation cross of 500 ms
    text.setText('+')
    text.draw()  # draw the stimulus to the back buffer
    win.flip()
    core.wait(0.5)
    # then show the word 
    text.setText(word)
    text.draw()
    win.flip()
    t0 = time.clock()
    # and wait for a button press, no time limit
    answer = event.waitKeys(keyList=["right", "left"])
    t1 = time.clock()
    rt = t1-t0
    dataFile.write("{}, {}, {}\n".format(word, answer[0], rt))

win.close()  # close the window
