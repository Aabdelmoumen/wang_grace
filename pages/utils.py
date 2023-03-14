from PyQt5 import QtWidgets
from widgets.CustomCheckBox import CustomCheckBox
from typeguard import List


def get_all_widgets_in_layout(layout: QtWidgets.QVBoxLayout) -> List[CustomCheckBox]:
    """_summary_

    Args:
        layout (QtWidgets.QVBoxLayout): _description_
    """
    # Get the number of widgets in the layout
    widget_count = layout.count()

    list_checked_widgets: List[CustomCheckBox] = []

    # Iterate through the widgets in the layout and print their text
    for i in range(widget_count):
        widget_item = layout.itemAt(i)

        if widget_item is not None:
            widget = widget_item.widget()

            if widget is not None and isinstance(widget, CustomCheckBox):
                if widget.isChecked():
                    list_checked_widgets.append(widget)

    return list_checked_widgets
