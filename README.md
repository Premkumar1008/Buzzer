# Time Buzzer

A simple Python countdown timer that plays a beep sound when the countdown finishes. Designed to run on Windows using the built-in `winsound` module.

## Usage

### Command-line

Open a terminal in this folder and run:

```powershell
python timer.py <seconds>
```

Example:

```powershell
python timer.py 90  # 1 minute 30 seconds
```

You can stop the timer early with `Ctrl+C`.

### Graphical UI

If you prefer a simple windowed interface, start the program with the `--gui` flag or without any arguments:

```powershell
python timer.py --gui
# or just
python.timer.py
```

A small Tkinter window will appear allowing you to enter seconds and click **Start**.  The display updates live and beeps when finished.

## Requirements

- Windows OS (for `winsound`) or modify the code to use another sound library.
- Python 3.x


## Optional Enhancements

- Add GUI with Tkinter or PyQt
- Make cross-platform by using `playsound` or `pydub` instead of `winsound`.
