from pynput.keyboard import Listener, Key, KeyCode
from position import Position
from spell_calculator import SpellCalculator


sc = SpellCalculator()
TRIGGER_KEYS = {
    'game_start': Key.f5,
    'spell_used(Position.TOP1)': KeyCode(char='\x01'),     # Ctrl+A
    'spell_used(Position.JGL1)': KeyCode(char='\x13'),     # Ctrl+S
    'spell_used(Position.MID1)': KeyCode(char='\x04'),     # Ctrl+D
    'spell_used(Position.ADC1)': KeyCode(char='\x06'),     # Ctrl+F
    'spell_used(Position.SUP1)': KeyCode(char='\x07'),     # Ctrl+G
    'spell_used(Position.TOP2)': KeyCode(char='\x1a'),     # Ctrl+Z
    'spell_used(Position.JGL2)': KeyCode(char='\x18'),     # Ctrl+X
    'spell_used(Position.MID2)': KeyCode(char='\x03'),     # Ctrl+C
    'spell_used(Position.ADC2)': KeyCode(char='\x16'),     # Ctrl+V
    'spell_used(Position.SUP2)': KeyCode(char='\x02'),     # Ctrl+B
    'spell_log': Key.f8
}


def game_start():
    sc.game_start()


def spell_used(position):
    sc.spell_used(position)


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
