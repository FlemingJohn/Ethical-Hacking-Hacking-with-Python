import keyboard

keys = keyboard.record(until = 'ESC')

input("Ready?")

keyboard.play(keys)
