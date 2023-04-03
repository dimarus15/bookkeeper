from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

class PaletteMode(QPalette):
    def __init__(self, is_dark_mode=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if is_dark_mode:
            self.setColor(QPalette.Window, QColor(202, 202, 202))
            self.setColor(QPalette.WindowText, Qt.black)
            self.setColor(QPalette.Base, QColor(230, 230, 230))
            self.setColor(QPalette.AlternateBase, QColor(202, 202, 202))
            self.setColor(QPalette.ToolTipBase, Qt.white)
            self.setColor(QPalette.ToolTipText, Qt.black)
            self.setColor(QPalette.Text, Qt.black)
            self.setColor(QPalette.Button, QColor(202, 202, 202))
            self.setColor(QPalette.ButtonText, Qt.black)
            self.setColor(QPalette.BrightText, Qt.red)
            self.setColor(QPalette.Link, QColor(213, 125, 37))
            self.setColor(QPalette.Highlight, QColor(213, 125, 37))
            self.setColor(QPalette.HighlightedText, Qt.white)