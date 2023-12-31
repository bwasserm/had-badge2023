## MENU = 19
## User = 24
## SAVE = 22
## A=8 B=7 C=1 D=4
## Level=5 RANGE=2
## XY=10 WAVE=16 SCOPE=13
## J=17 JN=20 JS=11 JE=23 JW=14
KEY_MENU=19
KEY_USER=24
KEY_SAVE=22
KEY_A=8
KEY_B=7
KEY_C=1
KEY_D=4
KEY_LEVEL=5
KEY_RANGE=2
KEY_XY=10
KEY_WAVE=16
KEY_SCOPE=13
JOY_PRESS=17
JOY_UP=20
JOY_DN=11
JOY_RT=23
JOY_LF=14
# synonyms and synthetic joystick
JOY_LT=JOY_LF
JOY_N=JOY_UP
JOY_S=JOY_DN
JOY_E=JOY_RT
JOY_W=JOY_LF
JOY_NE=100
JOY_NW=101
JOY_SE=102
JOY_SW=103


JOY_ALL=[JOY_PRESS, JOY_UP, JOY_DN, JOY_RT, JOY_LF, JOY_NE, JOY_NW, JOY_SE, JOY_SW]
KEY_ALL=[KEY_MENU, KEY_USER, KEY_SAVE, KEY_A, KEY_B, KEY_C, KEY_D, KEY_LEVEL, KEY_RANGE, KEY_XY, KEY_WAVE, KEY_SCOPE]
KEY_EVERYTHING=JOY_ALL + KEY_ALL
KEY_ABCD=[KEY_A, KEY_B, KEY_C, KEY_D]

## Numerically
## C, RANGE, [3], D, Level, [6], B, A, [9], XY, JS, [12], SCOPE, JW, [15], WAVE, J, [18], Menu, JN, [21], Save, JE, User

## LEDs
## 1- SIG generator
## 2 - Scope
## 4 - Saw tooth
## 8 - Triangle
## 16 - Square
## 32 - Sine
## 64 - Y
## 128 - X
LED_SIG=1
LED_SCOPE=2
LED_SAW=4
LED_TRI=8
LED_SQ=16
LED_SINE=32
LED_Y=64
LED_X=128
