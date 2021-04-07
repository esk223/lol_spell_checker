import time
import pyautogui
from position import Position


spell_dict = {
    "SMITE": 15,
    "GHOST": 210,
    "HEAL": 240,
    "TELEPORT": 420,      # if level 1 420, else 420 - 10*level
    "CLEANSE": 210,
    "BARRIER": 180,
    "IGNITE": 180,
    "EXHAUST": 210,
    "FLASH": 300,
}


class SpellCalculator:
    def __init__(self):
        self.start_time = time.time()
        self.spell_log_list = [-1] * 10
        self.spell_list = [
            "FLASH", "FLASH", "FLASH", "FLASH", "FLASH", "TELEPORT", "SMITE", "IGNITE", "HEAL", "IGNITE"
        ]
        self.rune_list = [False] * 5
        self.boots_list = [False] * 5

    def initialize(self):
        self.start_time = time.time()
        self.spell_log_list = [-1] * 10
        # self.spell_list
        # self.rune_list
        self.boots_list = [False] * 5

    def change_spell(self, position, spell):
        self.spell_list[position.value] = spell

    def spell_used(self, position):
        idx = position.value
        cooldown = spell_dict[self.spell_list[idx]]

        skill_acc = 0
        if self.rune_list[idx % 5]:
            skill_acc += 18
        if self.boots_list[idx % 5]:
            skill_acc += 12
        cooldown = cooldown * 100 / (100+skill_acc)

        spell_on_time = int(time.time() - self.start_time + cooldown)
        if spell_on_time - self.spell_log_list[idx] < 5:    # if re-hit the same macro in 5 seconds, cancel it
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
                position_str = str(Position(i)).strip("Position.")[:-1]
                spell_str = self.spell_list[i]
                info_tuple = (t, position_str, spell_str)
                list_for_text.append(info_tuple)
        list_for_text.sort()

        text = ""
        for info in list_for_text:
            text += "{0} {1} {2} / ".format(info[1], info[2], self.time_convert(info[0]))
        text = text.rstrip(" / ")

        pyautogui.typewrite("{0}".format(text))
        pyautogui.typewrite(['enter'])
