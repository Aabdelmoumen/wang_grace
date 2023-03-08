from PyQt5 import QtWidgets
from functools import partial
from ui_app import Ui_MainWindow
from typeguard import List
from q_css import vertical_panel_theme, pages_theme


class ThemeSettings:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui: Ui_MainWindow = self.main_window.ui
        self.hover_color_buttons: List[QtWidgets.QRadioButton] = [
            self.ui.radioButton_h_color_1,
            self.ui.radioButton_h_color_2,
            self.ui.radioButton_h_color_3,
        ]
        self.main_color_buttons: List[QtWidgets.QRadioButton] = [
            self.ui.radioButton_m_color_1,
            self.ui.radioButton_m_color_2,
            self.ui.radioButton_m_color_3,
        ]
        self.color_map = {"1": "#3790ca", "2": "#fec10c", "3": "#50b054"}
        self.page_buttons_action()

    def page_buttons_action(self):
        """_summary_"""

        for button in self.main_color_buttons + self.hover_color_buttons:
            button.clicked.connect(partial(self.change_theme))

    def change_theme(self):
        """_summary_"""

        new_main_color = next(
            (
                self.color_map[m_button.objectName().split("_")[-1]]
                for m_button in self.main_color_buttons
                if m_button.isChecked()
            ),
            None,
        )

        new_hover_color = next(
            (
                self.color_map[h_button.objectName().split("_")[-1]]
                for h_button in self.hover_color_buttons
                if h_button.isChecked()
            ),
            None,
        )

        pages_theme_q_css = pages_theme.replace("hover_color", new_hover_color).replace(
            "main_color", new_main_color
        )
        vertical_panel_q_css = vertical_panel_theme.replace(
            "hover_color", new_hover_color
        ).replace("main_color", new_main_color)

      

        self.ui.stackedWidget.setStyleSheet(pages_theme_q_css)
        self.ui.vertical_frame_panel.setStyleSheet(vertical_panel_q_css)
