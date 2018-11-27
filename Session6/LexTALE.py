## LexTALE English
# In this experiment, people will see a number of English words, one after another. 
# Their task is to decide for each word whether it is an actual existing English word or not. 
# Reaction times and accuracy will be recorded and saved in a csv file. 

# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((1000, 800), color='teal')

# prepare text stimulus
text = visual.TextStim(win, text='0', color='white')

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
    
#present empty screen for 1 second, just for now
text.setText(' ')
text.draw()  # draw the stimulus to the back buffer
win.flip()
core.wait(1)  # wait for 1 second on a blank window

## read in stimuli from text file 

## loop over words and present them one by one until a button is pressed
# right arrow for "Yes, it's a word"
# left arrow for "No, it's not a word"

# record time of the button press relative to the picture presentation time 

# append every trial to a csv file 

# save the final csv file 

win.close()  # close the window


