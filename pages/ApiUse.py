from PyQt5 import QtWidgets
from functools import partial
from ui_app import Ui_MainWindow
from widgets.CustomCheckBox import CustomCheckBox
from time import sleep
from PyQt5.QtCore import QDate
from pages.utils import get_all_widgets_in_layout

CHECK_BOX_FILES_NAMES_G1 = [f"G1 file name num {index}" for index in range(0, 10)]


class ApiUse:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui: Ui_MainWindow = self.main_window.ui
        self.init_gui()
        self.page_buttons_action()

    def init_gui(self):

        # group one
        for cbg1 in CHECK_BOX_FILES_NAMES_G1:
            custom_check_box_g1 = CustomCheckBox(text=cbg1)

            self.ui.verticalLayout_25.addWidget(custom_check_box_g1)

            custom_check_box_g1.clicked.connect(
                partial(self.check_box_status, custom_check_box_g1)
            )

        # hide the status
        self.ui.status_label_3.setText("")

        # set the date to the previous day
        date = QDate.currentDate().addDays(-1)  # Get the previous day's date
        self.ui.dateEdit_3.setDate(date)

    def check_box_status(self, check_box: QtWidgets.QCheckBox):
        """_summary_

        Args:
            check_box (QtWidgets.QCheckBox): check box clicked
        """
        print(check_box.isChecked(), check_box.text())

    def page_buttons_action(self):
        """_summary_"""

        self.ui.generate_file_pushButton.clicked.connect(
            partial(self.generate_file_function)
        )

        self.ui.folder_pushButton.clicked.connect(partial(self.select_folder))

        self.ui.file_pushButton.clicked.connect(partial(self.select_file))

    def generate_file_function(self):
        """_summary_"""

        list_of_checked_widgets_G1 = get_all_widgets_in_layout(
            layout=self.ui.verticalLayout_25
        )

        print(
            "list of the check box selected in G1",
            [check_box.text() for check_box in list_of_checked_widgets_G1],
        )

        # update the label status
        self.ui.status_label_3.setText("Generating file ...")

    def select_folder(self):
        """_summary_"""

        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder")

        self.ui.folder_lineEdit.setText(folder_path)

    def select_file(self):
        """_summary_"""

        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")

        self.ui.file_lineEdit.setText(file_path)
