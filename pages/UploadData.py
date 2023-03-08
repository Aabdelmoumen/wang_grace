from PyQt5 import QtWidgets
from functools import partial
from widgets.CustomCheckBox import CustomCheckBox
from ui_app import Ui_MainWindow
from functools import partial
from PyQt5.QtCore import QThreadPool, QDate
from time import sleep
from pages.Worker import Worker

CHECK_BOX_FILES_NAMES_G1 = [f"G1 file name num {index}" for index in range(0, 10)]
CHECK_BOX_FILES_NAMES_G2 = [f"G2 file name num {index}" for index in range(0, 10)]
CHECK_BOX_FILES_NAMES_G3 = [f"G3 file name num {index}" for index in range(0, 10)]


class UploadData:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui: Ui_MainWindow = self.main_window.ui
        self.init_gui()
        self.page_buttons_action()

    def init_gui(self):

        # group one
        for cbg1, cbg2, cbg3 in zip(
            CHECK_BOX_FILES_NAMES_G1, CHECK_BOX_FILES_NAMES_G2, CHECK_BOX_FILES_NAMES_G3
        ):
            custom_check_box_g1 = CustomCheckBox(text=cbg1)
            custom_check_box_g2 = CustomCheckBox(text=cbg2)
            custom_check_box_g3 = CustomCheckBox(text=cbg3)

            self.ui.verticalLayout_6.addWidget(custom_check_box_g1)
            self.ui.verticalLayout_10.addWidget(custom_check_box_g2)
            self.ui.verticalLayout_8.addWidget(custom_check_box_g3)

            custom_check_box_g1.clicked.connect(
                partial(self.check_box_status, custom_check_box_g1)
            )
            custom_check_box_g2.clicked.connect(
                partial(self.check_box_status, custom_check_box_g2)
            )
            custom_check_box_g3.clicked.connect(
                partial(self.check_box_status, custom_check_box_g3)
            )

        # hide the status
        self.ui.status_label.setText("")

        # set the date to the previous day
        date = QDate.currentDate().addDays(-1)  # Get the previous day's date
        self.ui.dateEdit.setDate(date)

    def check_box_status(self, check_box: QtWidgets.QCheckBox):
        """_summary_

        Args:
            check_box (QtWidgets.QCheckBox): check box clicked
        """
        print(check_box.isChecked(), check_box.text())

    def page_buttons_action(self):
        """_summary_"""

        self.ui.upload_pushButton.clicked.connect(partial(self.upload_function))

    def upload_function(self):
        """_summary_"""

        # update the label status
        self.ui.status_label.setText("Uploading ...")

        # init the worker class
        self.thread = QThreadPool()
        self.worker_cls = Worker(
            partial(
                self.upload_thread,
            )
        )
        self.worker_cls.signals.finished.connect(
            partial(
                self.thread_finished,
            )
        )
        self.worker_cls.signals.result.connect(partial(self.thread_result))
        self.thread.start(self.worker_cls)

    ##########################
    # upload thread functions
    ##########################

    def upload_thread(self, progress_callback):
        """_summary_

        Args:
            progress_callback (_type_):
        """

        for i in range(0, 6):
            self.ui.progressBar_2.setValue(i * 20)
            sleep(1)

    def thread_result(self, result):
        pass

    def thread_finished(self):
        self.ui.status_label.setText("uploaded successfully")
