import win32api
import win32con
import time


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def keep_active():
    while True:
        click(10, 10)
        time.sleep(2)
        click(10, 10)

        time.sleep(240)


keep_active()

