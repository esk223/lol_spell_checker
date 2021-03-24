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
        if self.start_time == 0:
            self.start_time = time.time()

    def spell_used(self, position):
        idx = position.value
        if self.spell_log_list[idx] == -1:
            spell_on_time = int(time.time() - self.start_time) + 300
            self.spell_log_list[idx] = spell_on_time
        else:
            self.spell_log_list[idx] = -1
        print(self.spell_log_list)

    def time_convert(self, second):
        minute = second // 60
        second = second % 60
        return "{0:0>2}{1:0>2}".format(minute, second)

    def type_spell_log(self):
        list_for_text = []
        for i, t in enumerate(self.spell_log_list):
            if t == -1:
                continue
            else:
                t_i_pair = (t, str(Position(i)).strip("Position."))
                list_for_text.append(t_i_pair)
        list_for_text.sort()

        text = ""
        for l in list_for_text:
            text += l[1] + " " + self.time_convert(l[0]) + " / "

        pyautogui.typewrite("{0}".format(text))
        pyautogui.typewrite(['enter'])
