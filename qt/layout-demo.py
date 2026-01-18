# from example on google classroom
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg


# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("75rftyiuh")

        # Create layout
        layout = qtw.QGridLayout()
        form = qtw.QFormLayout()
        
        # Top Form
        self.name = qtw.QLineEdit()
        self.name.setPlaceholderText("Name")
        form.addRow("Name: ", self.name)
        self.location = qtw.QLineEdit()
        self.location.setPlaceholderText("Location")
        form.addRow("Location: ", self.location)

        # middle row
        self.combobox = qtw.QComboBox()
        self.combobox.addItems(["One", "Two", "Three"])
        self.checkbox = qtw.QCheckBox(text="On or off   ")

        # bottom row
        self.ok = qtw.QPushButton("Ok")
        self.ok.clicked.connect(self.quit)
        self.cancel = qtw.QPushButton("Cancel")
        self.cancel.clicked.connect(self.quit)

        # add to layout
        layout.addLayout(form, 0, 0, 1, 3)
        layout.addWidget(self.combobox, 2, 0, 1, 2)
        layout.addWidget(self.checkbox, 2, 2, 1, 1)
        layout.addWidget(self.ok, 3, 1, 1, 1)
        layout.addWidget(self.cancel, 3, 2, 1, 1)


        # display
        widget = qtw.QWidget()
        widget.setLayout(layout)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
    
    def quit(self):
        exit()


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = qtw.QApplication(["9008"])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.
