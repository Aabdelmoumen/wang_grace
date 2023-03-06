from PyQt5.QtCore import (
    QEasingCurve,
    Qt,
    QPropertyAnimation,
    QRect,
    QPoint,
    pyqtProperty,
)
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QCheckBox


class CustomCheckBox(QCheckBox):
    def __init__(
        self,
        text,
        parent=None,
        width=40,
        bg_color="#777",
        circle_color="#DDD",
        circle_color_checked="#DDD",
        active_color="#00BCFF",
        animation_curve=QEasingCurve.OutBounce,
        text_width=250,
        spacing=6,
    ):
        # QCheckBox.__init__(self)
        super().__init__(parent)
        self.setFixedSize(width + text_width + spacing, 20)
        self.setCursor(Qt.PointingHandCursor)

        self.check_box_width = width
        self.spacing = spacing
        self.text_width = text_width

        # COLORS
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._circle_color_checked = circle_color_checked
        self._active_color = active_color

        self._position = 3
        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)
        self.stateChanged.connect(self.setup_animation)

        # set the text 
        self.setText(text)

        if parent is not None:
            self.show()

    @pyqtProperty(float)
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
        self.update()

    # START STOP ANIMATION
    def setup_animation(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.check_box_width - 19)
        else:
            self.animation.setEndValue(4)
        self.animation.start()

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        # SET PEN
        p.setPen(Qt.NoPen)
        if not self.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0, 0, self.check_box_width, 20, 10, 10)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(int(self._position), 2, 16, 16)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0, 0, self.check_box_width, 20, 10, 10)
            p.setBrush(QColor(self._circle_color_checked))
            p.drawEllipse(int(self._position), 2, 16, 16)

        # DRAW TEXT
        text_rect = QRect(
            self.check_box_width + self.spacing, 0, self.text_width, self.height()
        )
        text = self.text()
        font = p.font()
        font.setPixelSize(12)
        p.setFont(font)
        p.setPen(QColor("#FFF"))
        p.drawText(text_rect, Qt.AlignLeft | Qt.AlignVCenter, text)

        p.end()
