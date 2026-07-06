print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.encoders import EncoderHandler
from kmk.modules.LED import LED
from kmk.extensions.led import AnimationModes


led = LED(
    led_pin=[board.D8],
    brightness=50,
    brightness_step=5,
    brightness_limit=100,
    breathe_center=1.5,
    animation_mode=AnimationModes.STATIC,
    animation_speed=1,
    user_animation=None,
    val=100,
    )
keyboard.extensions.append(led)

pins=(board.D6,)#I have one switch directly connected to my board

class MyKeyboard(KMKKeyboard): #Used claude and kmk keypad scanner for help to code this.
    def __init__(self):
        super().__init__()
        self.col_pins = (board.D3, board.D4, board.D5,)
        self.row_pins = (board.D1, board.D2,)
    

    
        direct = KeysScanner(
            # require argument:
            pins=pins,
            value_when_pressed=False,
            pull=True,
            interval=0.02, # Matrix sampling interval in ms
            debounce_threshold=None, # Number of samples needed to change state, values greater than 1 enable debouncing. Only applicable for CircuitPython >= 9.2.0
            max_events=64
        )
        matrix = MatrixScanner(
            column_pins=self.col_pins,
            row_pins=self.row_pins,
            columns_to_anodes=DiodeOrientation.COL2ROW,
            interval=.02,
            debounce_threshold=None,
            max_events=64
        )      
        self.matrix = [direct, matrix]

keyboard = MyKeyboard()

#Rotary Switch
encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]
encoder_handler.pins = (
    (board.D10, board.D9)
)
encoder_handler.map = [((KC.UP, KC.DOWN),)]


#Map
keyboard.keymap = [
    [KC.LGUI(KC.C), KC.LGUI(KC.V), KC.LGUI(KC.Q)],
    [KC.LGUI(KC.Z), KC.LGUI(KC.F7), KC.LGUI(KC.F8), KC.LGUI(KC.X)],]



if __name__ == '__main__':
    keyboard.go()