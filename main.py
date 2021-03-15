import pyautogui
from pynput.keyboard import Listener, Key
import time

KEY_CHATTING_TRIGGER = Key.f12
# KEY_TOP_SPELL1 = KeyCode(97)


def handle_key_press(key):
    if key == KEY_CHATTING_TRIGGER:
        pyautogui.typewrite(['enter'])
        pyautogui.typewrite('top 15:00 / jg 15:11')
        pyautogui.typewrite(['enter'])


# def handle_key_release(key):
#     print("Released {0}".format(key))
#     if key == Key.esc:
#         return False


if __name__ == "__main__":
    with Listener(on_press=handle_key_press) as listener:
        listener.join()
    # print(pyautogui.position())
    # pyautogui.PAUSE = 1
    # pyautogui.FAILSAFE = True
    # pyautogui.click(104, 594, button='left', clicks=1, interval=2)
    # print("click")
    # pyautogui.typewrite("hello")1