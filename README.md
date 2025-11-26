# Keyboard Input Logger

This project demonstrates how to use the *pynput* library in Python to listen for and record keyboard events.  
It is designed *for educational purposes only* to help learners understand how event listeners work in Python.

---

## Features
- Captures all key presses using pynput.keyboard.Listener
- Logs keystrokes to a text file (key_log.txt)
- Handles both character keys and special keys (Enter, Shift, etc.)

---

## How It Works
The script sets up a listener that triggers the on_press function whenever a key is pressed:
- If the key is a character, it writes the character to the log file.
- If the key is a special key (like Key.space), it writes the key name instead.

---
