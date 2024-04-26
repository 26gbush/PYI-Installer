import time
import pyautogui

print("Welcome to the PYI installer", "\u00A9", " 2024 26gbush")
print("")
print("The PYI installer uses 'pip' to install apps, and therefore is an EXTENSION of pip")
print("pyautogui is needed to install apps")
while True:
    print("")
    ml = input("PYI INSTALLER: ")
    pyautogui.hotkey('win' , 'r')
    pyautogui.typewrite('powershell')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.typewrite('pip install ' +ml)

    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite('press enter to exit powershell')
    pyautogui.press('enter')
    pyautogui.typewrite('exit')
    print("")
    print("If the installation did not work, check if you misspelled it.")