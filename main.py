from pynput.keyboard import Listener, Key, KeyCode
import time
from position import Position
from spell_calculator import SpellCalculator


sc = SpellCalculator()
TRIGGER_KEYS = {
    'spell_used(Position.TOP, 0)': KeyCode(char='\x01'),     # Ctrl+A
    'spell_used(Position.JGL, 0)': KeyCode(char='\x13'),     # Ctrl+S
    'spell_used(Position.MID, 0)': KeyCode(char='\x04'),     # Ctrl+D
    'spell_used(Position.ADC, 0)': KeyCode(char='\x06'),     # Ctrl+F
    'spell_used(Position.SUP, 0)': KeyCode(char='\x07'),     # Ctrl+G
    'spell_used(Position.TOP, 1)': KeyCode(char='\x1a'),     # Ctrl+Z
    'spell_used(Position.JGL, 1)': KeyCode(char='\x18'),     # Ctrl+X
    'spell_used(Position.MID, 1)': KeyCode(char='\x03'),     # Ctrl+C
    'spell_used(Position.ADC, 1)': KeyCode(char='\x16'),     # Ctrl+V
    'spell_used(Position.SUP, 1)': KeyCode(char='\x02'),     # Ctrl+B
    'spell_log': Key.f5
}


def spell_used(position, spell_num):
    sc.spell_used(position, spell_num)
    print(position, spell_num)


def spell_log():
    sc.type_spell_log()


def handle_key_press(key):
    for action, trigger in TRIGGER_KEYS.items():
        check = True if key == trigger else False
        if check:
            func = eval(action)
            if callable(func):
                func()


if __name__ == "__main__":
    with Listener(on_press=handle_key_press) as listener:
        listener.join()
