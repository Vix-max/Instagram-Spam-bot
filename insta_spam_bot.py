import pyautogui, time
def repeat():
    time.sleep(1)
    f = open(, 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
while True:
    repeat()