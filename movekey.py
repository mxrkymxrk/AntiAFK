import time
import keyboard
import pyautogui
from datetime import datetime

INTERVAL_SEC = 300   # 5 minutes in seconds when to tap happens 
TAP_MS = 60          # how long to hold A/D in milliseconds

def tap(key: str, ms: int):
    pyautogui.keyDown(key)
    time.sleep(ms / 1000.0)
    pyautogui.keyUp(key)

def main():
    print("Movement tapper running.")
    print("Hotkeys: 'p' pause/resume, 'q' quit.")
    paused = False
    last = time.time()

    while True:
        # Hotkeys
        if keyboard.is_pressed('q'):
            print("Quitting…")
            break
        if keyboard.is_pressed('p'):
            paused = not paused
            print("Paused" if paused else "Resumed")
            time.sleep(0.4)  # debounce

        now = time.time()
        if not paused and (now - last) >= INTERVAL_SEC:
            # Do a tiny right (D) then left (A) tap
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Tap D/A")
            tap('d', TAP_MS)
            time.sleep(0.08)  # tiny gap
            tap('a', TAP_MS)
            last = now

        time.sleep(0.05)  # keep CPU low

if __name__ == "__main__":
    print("Focus your game window (it must be the active window).")
    main()
