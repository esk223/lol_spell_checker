import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


INITIAL_SPELL = ["flash", "flash", "flash", "flash", "flash", "teleport", "smite", "ignite", "heal", "exhaust"]
SPELL_LIST = ["flash", "ghost", "teleport", "smite", "ignite", "heal", "cleanse", "barrier", "exhaust"]


class SpellCheckWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.spell_list = []
        self.rune_list = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('LOL SpellTimer')
        self.setWindowIcon(QIcon('image/icon.webp'))
        self.setFixedSize(450, 450)
        self.center()
        self.setStyleSheet("background-color: #060A33;")

        grid = QGridLayout()
        self.setLayout(grid)

        self.add_text(grid, 'SPELL 1', 0, 1)
        self.add_text(grid, 'SPELL 2', 0, 2)
        self.add_text(grid, 'RUNE', 0, 3)

        self.add_image(grid, 'lane/top.png', 1, 0)
        self.add_image(grid, 'lane/jgl.png', 2, 0)
        self.add_image(grid, 'lane/mid.png', 3, 0)
        self.add_image(grid, 'lane/bot.png', 4, 0)
        self.add_image(grid, 'lane/sup.png', 5, 0)

        for i in range(10):
            spell_label = SpellQLabel(INITIAL_SPELL[i])
            self.spell_list.append(spell_label)
            grid.addWidget(spell_label, i%5 + 1, i//5 + 1, Qt.AlignCenter)

        for i in range(1, 6):
            rune_label = RuneQLabel()
            self.rune_list.append(rune_label)
            grid.addWidget(rune_label, i, 3, Qt.AlignCenter)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_text(self, layout, text, x, y):
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


class RuneQLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.rune_on = False
        self.setPixmap(QPixmap('image/rune/rune_off.png'))

    def mousePressEvent(self, event):
        if self.rune_on:
            self.setPixmap(QPixmap('image/rune/rune_off.png'))
        else:
            self.setPixmap(QPixmap('image/rune/rune_on.png'))
        self.rune_on = not self.rune_on

    def rune_status(self):
        return self.rune_on


class SpellQLabel(QLabel):
    def __init__(self, init_spell):
        super().__init__()
        self.setMouseTracking(True)
        self.set_spell(init_spell)

    def set_spell(self, spell):
        self.spell = spell
        self.setPixmap(QPixmap('image/spell/' + spell + '.png'))

    def mousePressEvent(self, event):
        self.spell_window = SpellSelectWidget(self, event.globalX(), event.globalY())
        self.spell_window.show()

    def spell_status(self):
        return self.spell


class SpellSelectWidget(QWidget):
    def __init__(self, spell_qlabel, x, y):
        super().__init__()
        self.spell_qlabel = spell_qlabel
        self.init_ui(x, y)

    def init_ui(self, x, y):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(160, 160)
        # self.setStyleSheet("")
        self.setStyleSheet("background-color: #34495E;")
        self.move(x, y)

        grid = QGridLayout()
        self.setLayout(grid)

        for i in range(9):
            spell_label = SpellSelectQLabel(self, SPELL_LIST[i])
            grid.addWidget(spell_label, i//3, i%3, Qt.AlignCenter)
        self.show()

    def change_spell(self, spell):
        self.spell_qlabel.set_spell(spell)
        self.close()


class SpellSelectQLabel(QLabel):
    def __init__(self, spell_widget, spell):
        super().__init__()
        self.spell_widget = spell_widget
        self.spell = spell
        self.setPixmap(QPixmap('image/spell/' + spell + '.png'))

    def mousePressEvent(self, event):
        self.spell_widget.change_spell(self.spell)


if __name__ == "__main__":
    q_app = QApplication(sys.argv)
    main_window = SpellCheckWidget()
    main_window.show()
    sys.exit(q_app.exec_())
