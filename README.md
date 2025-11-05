# AntiAFK
A lightweight Python script that simulates small key presses to prevent AFK timeouts.

# MoveKey 

A lightweight Python script that keeps your game or app active by periodically sending small key taps (`A` and `D`).  
Perfect for preventing AFK timeouts or idle disconnects.

---

# Features
- Automatically simulates subtle movement every few minutes  
- Hotkeys:
  - **P** — Pause/Resume  
  - **Q** — Quit safely  
- Adjustable timing intervals and tap durations  
- Simple, cross-platform Python script (Windows/Linux/macOS)

---

# Requirements

- Python 3.7+
- Packages:
  ```
  pip install pyautogui keyboard

# Configuration

You can modify these constants at the top of movekey.py
```
INTERVAL_SEC = 300   # Interval between taps (seconds)
TAP_MS = 60          # Duration of each key press (milliseconds)
```

# Disclaimer

Use responsibly. This tool is meant for harmless automation or personal convenience.
Some online games may prohibit automation or macro tools — use at your own risk.


# Contribute

Pull requests and feature ideas are welcome!
If you find this helpful, give it a ⭐ on GitHub.


