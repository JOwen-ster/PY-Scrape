import sys
import os
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QWidget, QFileDialog


class ImageScraperApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Scraper")
        # center in the middle of users screen instead of x:0, y:0
        self.setGeometry(0, 0, 500, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.url_label = QLabel("Enter Website URL:")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("e.g., https://example.com")

        self.folder_label = QLabel("Save Images to:")
        self.folder_input = QLineEdit()
        self.folder_input.setPlaceholderText("Select Folder")

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_folder)

        self.scrape_button = QPushButton("Scrape and Download")
        self.scrape_button.clicked.connect(self.scrape_and_download)

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_input)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.scrape_button)

        self.central_widget.setLayout(layout)

    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.folder_input.setText(folder_path)

    def scrape_and_download(self):
        url = self.url_input.text()
        folder_path = self.folder_input.text()

        if not url:
            QMessageBox.warning(self, "Warning", "Please enter a website URL.")
            return
        
        elif not folder_path:
            QMessageBox.warning(self, "Warning", "Please select a folder to save images.")
            return

        # Create folder if not exists
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Fetch webpage content
        # Find all image tags
        # Download images

        QMessageBox.information(self, "Success", "Images downloaded successfully")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageScraperApp()
    window.show()
    sys.exit(app.exec_())
