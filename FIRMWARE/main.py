import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
keyboard.extensions.append(MediaKeys())
keyboard.col_pins = (board.GPIO27, board.GPIO28, board.GPIO29)
keyboard.row_pins = (board.GPIO4, board.GPIO2, board.GPIO1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# The macros look strange because i am using autohotkey to quickly launch them for me.
OPEN_DISCORD = KC.MACRO(KC.LCTL(KC.LALT(KC.LSFT(KC.F1))))
OPEN_STEAM   = KC.MACRO(KC.LCTL(KC.LALT(KC.LSFT(KC.F2))))
OPEN_LOGITECH = KC.MACRO(KC.LCTL(KC.LALT(KC.LSFT(KC.F3))))

rows = [
    [OPEN_DISCORD,       OPEN_STEAM,         OPEN_LOGITECH],
    [KC.AUDIO_VOL_UP,    KC.AUDIO_VOL_DOWN,  KC.AUDIO_MUTE],
    [KC.MEDIA_PREV_TRACK, KC.MEDIA_STOP,      KC.MEDIA_NEXT_TRACK]
]

keyboard.keymap = [rows]

if __name__ == '__main__':
    keyboard.go()