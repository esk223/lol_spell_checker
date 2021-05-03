import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


INITIAL_SPELL = ["flash", "flash", "flash", "flash", "flash", "teleport", "smite", "ignite", "heal", "exhaust"]
SPELL_LIST = ["flash", "ghost", "teleport", "smite", "ignite", "heal", "cleanse", "barrier", "exhaust"]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.spell_list = []
        self.rune_list = []
        self.sub_window = None
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
            spell_label = SpellQLabel(self, i, INITIAL_SPELL[i])
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

    def open_sub_window(self, i):
        self.sub_window = SubWindow(self, i)
        # self.sub_window.show()

    def change_spell(self, i, new_spell):
        old_spell = self.spell_list[i].get_spell()
        pair_spell_label = self.spell_list[(i+5) % 10]
        if pair_spell_label.get_spell() == new_spell:
            pair_spell_label.set_spell(old_spell)
        self.spell_list[i].set_spell(new_spell)


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
    def __init__(self, main_window, idx, init_spell):
        super().__init__()
        self.main_window = main_window
        self.idx = idx
        self.set_spell(init_spell)

    def set_spell(self, spell):
        self.spell = spell
        self.setPixmap(QPixmap('image/spell/' + spell + '.png'))

    def get_spell(self):
        return self.spell

    def mousePressEvent(self, event):
        self.main_window.open_sub_window(self.idx)


class SubWindow(QWidget):
    def __init__(self, main_window, i):
        super().__init__()
        self.main_window = main_window
        self.idx = i
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(160, 160)
        self.setStyleSheet("background-color: #34495E;")
        self.move_ui()

        grid = QGridLayout()
        self.setLayout(grid)
        for i in range(9):
            spell_label = SpellSubQLabel(self, SPELL_LIST[i])
            grid.addWidget(spell_label, i // 3, i % 3, Qt.AlignCenter)
        self.show()

    def move_ui(self):
        main_pos = self.main_window.pos()
        dx_list = [171, 278]
        dy_list = [146, 217, 289, 360, 432]
        self.move(main_pos.x() + dx_list[self.idx // 5], main_pos.y() + dy_list[self.idx % 5])

    def change_spell(self, new_spell):
        self.main_window.change_spell(self.idx, new_spell)
        self.close()


class SpellSubQLabel(QLabel):
    def __init__(self, sub_window, spell):
        super().__init__()
        self.sub_window = sub_window
        self.spell = spell
        self.setPixmap(QPixmap('image/spell/' + spell + '.png'))

    def mousePressEvent(self, event):
        self.sub_window.change_spell(self.spell)


if __name__ == "__main__":
    q_app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(q_app.exec_())
