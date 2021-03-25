import time
import pyautogui
from enum import Enum
from position import Position


class Cooldown(Enum):
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
        # self.spell_list = []

    def game_start(self):
        if self.start_time == 0:
            self.start_time = time.time()

    def spell_used(self, position):
        idx = position.value
        spell_on_time = int(time.time() - self.start_time) + 300    # should be modified
        if spell_on_time - self.spell_log_list[idx] < 5:    # re-hit the same macro in 5 seconds, cancel it
            self.spell_log_list[idx] = -1
        else:
            self.spell_log_list[idx] = spell_on_time
        print(self.spell_log_list)

    def time_convert(self, second):
        minute = second // 60
        second = second % 60
        return "{0:0>2}{1:0>2}".format(minute, second)

    def type_spell_log(self):
        cur_time = int(time.time() - self.start_time)
        list_for_text = []
        for i, t in enumerate(self.spell_log_list):
            if t == -1:
                continue
            elif cur_time >= t:
                continue
            else:
                t_i_pair = (t, str(Position(i)).strip("Position.")) # should be modified
                list_for_text.append(t_i_pair)
        list_for_text.sort()

        text = ""
        for info in list_for_text:
            text += info[1] + " " + self.time_convert(info[0]) + " / "
        text = text.rstrip(" / ")

        pyautogui.typewrite("{0}".format(text))
        pyautogui.typewrite(['enter'])
