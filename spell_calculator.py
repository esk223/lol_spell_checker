import time
import pyautogui
from position import Position

GHOST = 210
HEAL = 240
TELEPORT = 420      # if level 1 420, else 420 - 10*level
CLEANSE = 210
BARRIER = 180
IGNITE = 180
EXHAUST = 210
FLASH = 300

BOOTS = 10.7        # skill acceleration +12
RUNE = 15.3         # skill acceleration +18


class SpellCalculator:
    def __init__(self):
        self.start_time = 0
        self.spell_log_list = [-1]*10

    def game_start(self):
        self.start_time = time.time()

    def spell_used(self, position):
        idx = position.value
        if self.spell_log_list[idx] == -1:
            spell_on_time = int(time.time() - self.start_time) + 300
            self.spell_log_list[idx] = spell_on_time
        else:
            self.spell_log_list[idx] = -1
        print(self.spell_log_list)

    def type_spell_log(self):
        pyautogui.typewrite('"support gap"')
        pyautogui.typewrite(['enter'])
