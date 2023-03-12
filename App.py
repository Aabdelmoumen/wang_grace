from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication 
from functools import partial
import sys
from ui_app import Ui_MainWindow
from PyQt5.QtCore import QPropertyAnimation
from typeguard import Dict, List
from pages.UploadData import UploadData
from pages.RunReports import RunReports
from pages.ApiUse import ApiUse
from pages.UserSettings import UserSettings
from pages.ThemeSettings import ThemeSettings
from q_css import pages_theme , vertical_panel_theme

class MainWindow(QMainWindow):
    def __init__(self):
        """_summary_"""
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.page_buttons: List[QtWidgets.QRadioButton] = [
            self.ui.upload_data_button,
            self.ui.run_reports_button,
            self.ui.api_use_button,
            self.ui.user_settings_button,
            self.ui.theme_settings_button,
        ]
        self.page_buttons_index_map: Dict[str, int] = {
            button.objectName(): index for index, button in enumerate(self.page_buttons)
        }
        self.init_pages()
        self.pages_buttons_action()
        self.show()

    def init_pages(self):
        """_summary_"""
        

        UploadData(main_window=self)
        RunReports(main_window=self)
        ApiUse(main_window=self)
        UserSettings(main_window=self)
        ThemeSettings(main_window=self)

    def pages_buttons_action(self) -> None:
        """_summary_"""
        self.ui.logo_button.clicked.connect(partial(self.animate_left_panel))

        for button in self.page_buttons:
            button.clicked.connect(partial(self.switch_page, button))

    def animate_left_panel(self) -> None:
        """_summary_"""
        width = self.ui.vertical_frame_panel.width()
        min_width = 58
        max_width = 250

        if width == min_width:
            widthExtended = max_width

        else:
            widthExtended = min_width

        self.animation = QPropertyAnimation(
            self.ui.vertical_frame_panel, b"minimumWidth"
        )
        self.animation.setDuration(350)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def switch_page(self, button: QtWidgets.QRadioButton) -> None:
        """_summary_

        Args:
            button (QtWidgets.QRadioButton): the page button clicked
        """
        button_index = self.page_buttons_index_map[button.objectName()]
        if self.ui.stackedWidget.currentIndex() != button_index:
            self.ui.stackedWidget.setCurrentIndex(button_index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())





