import pyautogui
from pynput.keyboard import Listener, Key, KeyCode
import time

KEY_CHATTING_TRIGGER = Key.f12
# KEY_TOP_SPELL1 = KeyCode(97)

pressed_set = set()

HOT_KEYS = {
    'f1': set([KeyCode(char='1')])
}

def f1():
    print("Hello")


def handle_key_press(key):
    pressed_set.add(key)

    for action, trigger in HOT_KEYS.items():
        check = all([True if triggerKey in pressed_set else False for triggerKey in trigger])
        if check:
            func = eval(action)
            if callable(func):
                func()
    # print(pressed_set)
    # if key == KEY_CHATTING_TRIGGER:
    #     pyautogui.typewrite(['enter'])
    #     pyautogui.typewrite('"SUPPORT GAP"')
    #     pyautogui.typewrite(['enter'])


def handle_key_release(key):
    if key in pressed_set:
        pressed_set.remove(key)
    # print(pressed_set)


if __name__ == "__main__":
    with Listener(on_press=handle_key_press, on_release=handle_key_release) as listener:
        listener.join()
    # print(pyautogui.position())
    # pyautogui.PAUSE = 1
    # pyautogui.FAILSAFE = True
    # pyautogui.click(104, 594, button='left', clicks=1, interval=2)
    # print("click")
    # pyautogui.typewrite("hello")1