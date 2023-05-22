"""
Features:
    1] App consists of a canvas and two buttons.
    2] First button: When clicked, a random geometric image from the open source repository 
    (https://github.com/hfg-gmuend/openmoji/tree/master/src/symbols/geometric) is downloaded and 
    rendered at random location on the canvas. It's selectable' and movable. 
    An image appears whenever this button is clicked, without removing/overwriting the previous images.
    3] Second button: This button will be used for grouping multiple images as a single object. 
        Select multiple images and click the button. Those images will move as a single object thereafter.
    4] The image size is displayed whenever a new image is rendered on the canvas.
    5] The location & size of the selected image is displayed.
"""


# Importing required libraries
import sys
from PyQt6.QtWidgets import QApplication
from windowsPg import WindowP

if __name__ == '__main__':
    
    # Opens a canvas
    app = QApplication(sys.argv)
    window = WindowP()
    window.show()
    sys.exit(app.exec())
