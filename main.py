import pyautogui
import time

if __name__ == "__main__":
    # print(pyautogui.position())
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True

    while True:
        pyautogui.click(104, 594, button='left', clicks=1, interval=2)
        print("click")