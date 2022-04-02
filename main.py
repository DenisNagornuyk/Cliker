import keyboard
import mouse
from time import sleep
import pyautogui 
#відстежуємо клікер (включений чи ні)
isClicking = False
def set_clicker():
	#при кожному визові функції, ми будемо міняти булеву зміну(isClicking = False) на  значеня True False
	global isClicking
	if isClicking:
		isClicking = False
		print("Clicker stop")
	else:
		isClicking = True
		print("Clicker start")
#клавіша зпуску та припинення
keyboard.add_hotkey('Tab + B', set_clicker)

while True:
	if isClicking:
		mouse.double_click(button = 'right')
		sleep(0.01)
