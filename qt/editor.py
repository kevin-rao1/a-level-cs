import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QColorDialog, QMessageBox, \
    QFileDialog, QTextEdit, QHBoxLayout
import PyQt6.QtCore as qtc 

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Markdown Editor")

        layout = QVBoxLayout()
        bottomrow = QHBoxLayout()

        self.main_text = QTextEdit()
        text = self.main_text.toMarkdown()
        text = self.main_text.setMarkdown(text)
        layout.addWidget(self.main_text)

        # Create another button
        #quit_btn = QPushButton("Quit")
        #quit_btn.clicked.connect(self.quit)
        #bottomrow.addWidget(quit_btn)

        # Create another button
        #open_btn = QPushButton("Open")
        #open_btn.clicked.connect(self.open_btn_click)
        #bottomrow.addWidget(open_btn)

        # Create another button
        #save_btn = QPushButton("Save")
        #save_btn.clicked.connect(self.save_btn_click)
        #bottomrow.addWidget(save_btn)

        layout.addLayout(bottomrow)

        # menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction("&Open", self.open_btn_click)
        file_menu.addAction("&Save", self.save_btn_click)
        file_menu.addSeparator()
        file_menu.addAction("\0&Quit", self.quit)

        # Create the windows central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_btn_click(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Markdown Files (*.md)")
        if filename:
            with open(filename, "r") as file:
                file_contents = file.read()
                self.main_text.setMarkdown(file_contents)

    def save_btn_click(self):
        save_text = self.main_text.toPlainText()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.md)")
        if filename:
            with open(filename, "w") as file:
                file.write(save_text)

    def quit(self):
        dlg = QMessageBox.warning(self, "Quit?", "Are you sure", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        print(dlg)
        if dlg == QMessageBox.StandardButton.Ok:
            # qtc.QCoreApplication.quit()
            self.app.quit()



app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()
