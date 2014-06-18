# USAGE:
# Import this class in your python script: 'from progressBarView import progressBarView'
# If you use the UI Designer you have just to add a 'Custom View' to your main view,
# resize it like you want, than 'edit attributes' and set 'progressBarView' in 'Custom View Class'.
# You can choose color, background, border size and color directly from the UI Designer in 'edit attributes'.
# If you don't use the UI Designer just inizialize the view like any other custom view and set the proprieties.
# Once you have setup the view you have to call the method 'setMaxValue(value)' to set
# the value that the script have to reach, than 'setCurrentValue(value)' sets the value
# currently reached.
# If you want to use this progressbar to display the status of a download take
# a look at 'file_downloader.py'

import ui

class progressBarView (ui.View):

    def draw(self):
        # This will be called whenever the view's content needs to be drawn.
        if hasattr(self, 'maxValue') and hasattr(self, 'currentValue'):
            lenght=int((self.width*self.currentValue)/self.maxValue)
        else:
            lenght=0
        rect = ui.Path.rect(0, 0, lenght, self.height)
        ui.set_color(self.tint_color)
        rect.fill()

    def setMaxValue(self,max):
        self.maxValue=max

    def setCurrentValue(self,current):
        if(current>self.maxValue):
            self.currentValue=self.maxValue
        else:
            self.currentValue=current
        self.set_needs_display()

