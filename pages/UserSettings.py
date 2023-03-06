from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from functools import partial
from typeguard import Dict, List


class UserSettings:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = self.main_window.ui