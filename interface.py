import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class SpellCheckWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('LOL SpellTimer')
        self.setWindowIcon(QIcon('image/spell.webp'))
        self.setFixedSize(450, 450)
        self.center()
        self.setStyleSheet("background-color: #060A33;")

        grid = QGridLayout()
        self.setLayout(grid)

        self.add_label(grid, 'SPELL 1', 0, 1)
        self.add_label(grid, 'SPELL 2', 0, 2)
        self.add_label(grid, 'RUNE', 0, 3)

        self.add_image(grid, 'top.png', 1, 0)
        self.add_image(grid, 'jgl.png', 2, 0)
        self.add_image(grid, 'mid.png', 3, 0)
        self.add_image(grid, 'bot.png', 4, 0)
        self.add_image(grid, 'sup.png', 5, 0)

        for i in range(1, 6):
            self.add_rune_label(grid, i, 3)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_label(self, layout, text, x, y):
        label = QLabel(text, self)
        label.setStyleSheet("color: white;")
        label_font = label.font()
        label_font.setFamily('Bahnschrift Condensed')
        label_font.setPointSize(14)
        label.setFont(label_font)
        layout.addWidget(label, x, y, Qt.AlignCenter)

    def add_image(self, layout, img_name, x, y):
        label = QLabel()
        label.setPixmap(QPixmap('image/' + img_name))
        layout.addWidget(label, x, y, Qt.AlignCenter)

    def add_rune_label(self, layout, x, y):
        label = RuneQLabel()
        label.setPixmap(QPixmap('image/rune_off.png'))
        layout.addWidget(label, x, y, Qt.AlignCenter)


class RuneQLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.rune_on = False

    def mousePressEvent(self, event):
        if self.rune_on:
            self.setPixmap(QPixmap('image/rune_off.png'))
        else:
            self.setPixmap(QPixmap('image/rune_on.png'))
        self.rune_on = not self.rune_on


if __name__ == "__main__":
    q_app = QApplication(sys.argv)
    spell_widget = SpellCheckWidget()
    sys.exit(q_app.exec_())
