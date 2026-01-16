# from test.py
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg


# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Feet to Metres Conversion")

        # Create layout
        layout = qtw.QGridLayout()
        form = qtw.QFormLayout()
        
        # Top Form
        self.feet = qtw.QLineEdit()
        self.feet.textEdited.connect(self.feet_change)
        form.addRow("Feet: ", self.feet)
        self.metres = qtw.QLineEdit()
        self.metres.textEdited.connect(self.metres_change) # WRONG - only change on user input
        form.addRow("Metres: ", self.metres)

        # bottom row
        self.exit = qtw.QPushButton("Exit")
        self.exit.clicked.connect(self.quit)

        # add to layout
        layout.addLayout(form, 0, 0, 1, 3)
        layout.addWidget(self.exit, 1, 1, 1, 1)


        # display
        widget = qtw.QWidget()
        widget.setLayout(layout)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
    
    def quit(self):
        exit()
    
    def feet_change(self, newfeet):
        try:
            noofmetres = float(newfeet)/3.28084
            self.metres.setText(str(noofmetres))
        except ValueError:
            self.metres.setText("NaN")

    def metres_change(self, newmetres):
        try:
            nooffeet = float(newmetres)*3.28084
            self.feet.setText(str(nooffeet))
        except ValueError:
            self.feet.setText("NaN")


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
