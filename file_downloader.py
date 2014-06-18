# coding: utf-8

import ui
import sys
import clipboard
import os
import urllib
import console
# import custom view for progressbar
from progressBarView import progressBarView

# callback function for urllib with the download status
def dlProgress(count, blockSize, totalSize):
	global pBar # import progressbar object from the main thread
	# if count = 0 the download is just started then set the file size
	if (count==0):
		pBar.setMaxValue(totalSize)
	else: # else set the current downloaded value (# of downloaded blocks * block size)
		pBar.setCurrentValue(count*blockSize)

# function called when 'open_in' button is pressed
def button_tapped(sender):
	# import variabile from main thread
	global openFile
	global view
	# set to true because the button was pressed
	openFile = True 
	# close the view to open the file
	view.close()

# load view from pyui file
view = ui.load_view('file_downloader')

# get object references from the view
openButton = view['openButton']
label1= view['label1']
label2= view['label2']
pBar = view['pBar']

# disable the button until the download is completed
openButton.enabled = False 
openButton.border_color = 0.7
#boolean to test in this thread if the botton has been pressed
openFile = False

# present the view to the user
view.present('sheet')
# get download link from clipboard OR sys.argv
fileUrl = clipboard.get() 
if len(sys.argv)>1:
	fileUrl = sys.argv[1]

# download file in /Downloads folder with original file name
fileName="Downloads/"+os.path.basename(fileUrl)

# display filename to the user
label1.text = "Downloading "+os.path.basename(fileUrl)+"..."

# download the file and call dlProgress for each block downloaded
urllib.urlretrieve(fileUrl, fileName, reporthook=dlProgress)

# tell the user that the download is completed and enabled button(s)
label2.text = "Dowload completed!"
openButton.enabled = True 
openButton.border_color = openButton.tint_color

# wait for the user to perform an action
view.wait_modal()

# if the user has cloased the view with "open in..." than open the file 
# in another app and remove it 
if(openFile):
	console.open_in(fileName)
	os.remove(fileName)
