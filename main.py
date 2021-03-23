import pyautogui
from pynput.keyboard import Listener, Key, KeyCode
import time
from position import Position
from spell_calculator import SpellCalculator


sc = SpellCalculator()
pressed_set = set()

HOT_KEYS = {
    'spell_used(Position.TOP, 1)': set([Key.tab, KeyCode(char='1')]),
    'spell_used(Position.JGL, 1)': set([Key.tab, KeyCode(char='2')]),
    'spell_used(Position.MID, 1)': set([Key.tab, KeyCode(char='3')]),
    'spell_used(Position.ADC, 1)': set([Key.tab, KeyCode(char='4')]),
    'spell_used(Position.SUP, 1)': set([Key.tab, KeyCode(char='5')]),
    'spell_used(Position.TOP, 2)': set([Key.tab, Key.f1]),
    'spell_used(Position.JGL, 2)': set([Key.tab, Key.f2]),
    'spell_used(Position.MID, 2)': set([Key.tab, Key.f3]),
    'spell_used(Position.ADC, 2)': set([Key.tab, Key.f4]),
    'spell_used(Position.SUP, 2)': set([Key.tab, Key.f5]),
}


def spell_used(position, spell_num):
    sc.spell_used(position, spell_num)
    print(position, spell_num)


# def tmp():
#     pressed_set.remove(Key.tab)
#     pressed_set.remove(KeyCode(char='1'))
#     pyautogui.typewrite(['enter'])
#     pyautogui.typewrite('"SUPPORT GAP"')
#     pyautogui.typewrite(['enter'])


def handle_key_press(key):
    pressed_set.add(key)
    for action, trigger in HOT_KEYS.items():
        check = all([True if triggerKey in pressed_set else False for triggerKey in trigger])
        if check:
            func = eval(action)
            if callable(func):
                func()


def handle_key_release(key):
    if key in pressed_set:
        pressed_set.remove(key)


if __name__ == "__main__":
    with Listener(on_press=handle_key_press, on_release=handle_key_release) as listener:
        listener.join()
