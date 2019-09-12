import pyautogui
import pyperclip

string = input("Enter the text you want to spam : ")
count = int(input("Enter the count of spams : "))

def spam():
	pyperclip.copy(string)
	pyautogui.moveTo(738,691)
	pyautogui.click()
	pyautogui.hotkey('ctrl','v')
	pyautogui.hotkey('enter')
	pyautogui.click()

for i in range(count):
	spam()

