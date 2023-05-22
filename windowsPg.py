# Importing required libraries

import random
import requests
import urllib.request
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QWidget
from PyQt6.QtSvg import *
import urllib.request

# Empty list for the selected images
selects = []


# Class to Move the selected Images

class DraggableImageLabel(QLabel): # child class of QLabel
    def __init__(self, parent=None): # DraggableImageLabel constructor
        super().__init__(parent) # QLabel constructor
        self.setMouseTracking(True)
        self.drag = False
        self.posi = QPoint()
        self.selected = False

    # Method for when an image is selected
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag = True
            self.posi = event.pos()

            # The location, size of the selected image
            print("Selected image's")
            print(f"SIZE: {self.size()}")
            print(f"LOCATION: {self.posi}")
            print("\n")

            # Selected Image state
            self.selected = not self.selected

            if self.selected:
                self.setStyleSheet("""
                                        * {
                                            border: 2px solid 'black';
                                        }
                                    """)
                selects.append(self)  # Add to selected images list
            else:
                self.setStyleSheet("")  # Clear the border style
                selects.remove(self)  # Remove from selected images list

    # Method for when an image is moved
    def mouseMoveEvent(self, event):
        if self.drag and event.buttons() & Qt.MouseButton.LeftButton:
            new_pos = self.pos() + event.pos() - self.posi
            self.move(new_pos)

    # Method for when an image is Released
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag = False


class WindowP(QWidget):  # child class of QWidget

    def __init__(self):  # WindowP constructor

        super().__init__()  # QWidget constructor
        self.title = "Desktop App"
        self.icon = "images/desktop-icon.png"
        self.widthW = self.width()
        self.heightW = self.height()
        self.createUI()

    # Method for the Canvas and two buttons
    def createUI(self):

        # Gets the data from network
        url = "https://api.github.com/repos/hfg-gmuend/openmoji/contents/src/symbols/geometric" # open source repository 
        response = requests.get(url) # Sends a GET request to the specified url
        data = response.json() # JSON is to read data from a web server, and display the data in a web page

        self.image_urls = [] # Empty list

        for item in data:
            if item["type"] == "file" and item["name"].endswith(".svg"):
                self.image_urls.append(item["download_url"])

        # Window title and Icon for the window
        self.setContentsMargins(30, 30, 30, 30)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setStyleSheet("""
                                background: 'wheat';

                           """)
        # Layout for the Window
        self.vbox = QVBoxLayout() # Organizes widgets vertically in a window.
        self.vbox.setSpacing(2)
        self.setLayout(self.vbox) # Set a layout manager on any subclasses of QWidget

        # Function call to set the contents on the window
        self.contents()

    # Method to place the contents on the window
    def contents(self):

        # First button: When clicked, a random geometric image from the
        #  open source repository (https://github.com/hfg-gmuend/openmoji/tree/master/src/symbols/geometric)
        # is downloaded and rendered at any random location on the canvas. It's selectable and movable.
        # An image from that repository appears whenever this button
        # is clicked, without removing/overwriting the previous images

        self.button = QPushButton("Random Image") # A widget which executes an action when a user clicks on it
        self.button.setStyleSheet("""
                                        *{
                                            border: 2px solid 'black';
                                            border-radius: 7px;
                                            background: 'DarkSlateGrey';
                                            font-size: 20px;
                                            color: 'white';
                                         }
                                        *:hover{
                                                   background: 'DimGrey';
                                                   color: 'white';
                                               }
                                 """)
        self.button.clicked.connect(self.button_click)  # button_click() Method is invoked when the button is clicked
        self.vbox.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)  # Adds the button to the window

        # Second button: This button will be used for grouping multiple images as a single object.
        # Select multiple images and click the button.
        # Those images will move as a single object thereafter
        self.button1 = QPushButton("Group Images") # A widget which executes an action when a user clicks on it
        self.button1.setStyleSheet("""
                                        *{
                                            border: 2px solid 'black';
                                            border-radius: 7px;
                                            background: 'DarkSlateGrey';
                                            font-size: 20px;
                                            color: 'white';
                                         }
                                        *:hover{
                                                   background: 'DimGrey';
                                                   color: 'white';
                                               }
                                 """)
        self.button1.clicked.connect(self.group_and_place_images)  # group_and_place_images() Method is invoked when the button is clicked
        self.vbox.addWidget(self.button1, alignment=Qt.AlignmentFlag.AlignCenter)  # Adds the button to the window

    # Method for when a button is clicked
    def button_click(self):

        # Empty lists
        xl = []
        yl = []

        image_paths = []  # List of image paths
        url_image = random.choice(self.image_urls)  # Random image url is chosen from the list of image paths
        image_paths.append(url_image)

        # Retrieving data URL & downloading it
        r = url_image.rsplit('/', 1)
        urllib.request.urlretrieve(url_image, f"{r[-1]}.svg")

        for path in image_paths:

            image = QImage() # Allows direct access to the pixel data & can be used as a paint device.
            image.loadFromData(requests.get(path).content)
            image_label = QLabel(self) # QLabel is used for displaying text or an image
            image_label.setPixmap(QPixmap(image))  #QPixmap can be used to show an image in a PyQT window.

            # To randomly place the images
            item_width = image_label.width()
            item_height = image_label.height()
            while True:
                x = random.randint(0, self.widthW - item_width)
                y = random.randint(0, self.heightW - item_height)
                if x not in xl and y not in yl:
                    xl.append(x)
                    yl.append(x)
                    break;
            
            # The image size is displayed whenever a new image is rendered on the canvas
            print("Image size of new image rendered on the canvas")
            print(f"WIDTH: {item_width}   HEIGHT: {item_height}")
            print("\n")

            # To be able to move those images when selected
            image_label = DraggableImageLabel(self)
            image_label.setPixmap(QPixmap.fromImage(image)) # QPixmap can be used to show an image in a PyQT window.
            image_label.move(x, y)
            image_label.show()
            image_label.setAlignment(Qt.AlignmentFlag.AlignBaseline)
            image_label.adjustSize()


    # Method to group the selected images
    def group_and_place_images(self):
        group_image = QImage(self.widthW, self.heightW, QImage.Format.Format_ARGB32) # Allows direct access to the pixel data & can be used as a paint device.
        group_image.fill(Qt.GlobalColor.lightGray)  # Background for grouped image

        painter = QPainter(group_image) # Class - Performs low-level painting on widgets and other paint devices.

        

        self.delete_selected_images()  # Deletes the selected images 


        # Combines the selected images into a single image
        for image_label in selects:
            painter.drawImage(image_label.pos(), image_label.pixmap().toImage())

        painter.end()

        # To drag/move and select the grouped image
        group_image_label = DraggableImageLabel(self)
        group_image_label.setPixmap(QPixmap.fromImage(group_image)) #QPixmap can be used to show an image in a PyQT window.
        group_image_label.move(400, 400)
        group_image_label.show()
        group_image_label.setAlignment(Qt.AlignmentFlag.AlignBaseline)
        group_image_label.adjustSize()

        selects.clear()  # Makes the list empty

    # Method to delete the selected images
    def delete_selected_images(self):
        for image_label in selects:
            image_label.deleteLater() # The object will be deleted when control returns to the event loop.
