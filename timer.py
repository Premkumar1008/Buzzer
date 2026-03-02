import time
import winsound


def countdown(seconds: int):
    """Countdown for the given number of seconds and then play a beep.

    This is a blocking CLI version that prints to stdout. Use
    :func:`gui_countdown` for the Tkinter interface below.
    """
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
        print("00:00")
        # play a simple beep sound multiple times
        for _ in range(3):
            winsound.Beep(1000, 500)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nTimer cancelled.")


def gui_countdown(seconds: int, label):
    """Update a Tkinter label each second and beep when done."""
    def tick():
        nonlocal seconds
        if seconds > 0:
            mins, secs = divmod(seconds, 60)
            label.config(text=f"{mins:02d}:{secs:02d}")
            seconds -= 1
            label.after(1000, tick)
        else:
            label.config(text="00:00")
            for _ in range(3):
                winsound.Beep(1000, 500)
                time.sleep(0.2)
    tick()


def launch_gui():
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.title("Time Buzzer")
    root.geometry("200x120")

    entry = tk.Entry(root, width=10)
    entry.pack(pady=10)
    entry.insert(0, "60")

    label = tk.Label(root, text="00:00", font=("Helvetica", 24))
    label.pack(pady=5)

    def start():
        try:
            secs = int(entry.get())
            if secs < 0:
                raise ValueError
            entry.config(state="disabled")
            start_btn.config(state="disabled")
            gui_countdown(secs, label)
        except ValueError:
            messagebox.showerror("Invalid", "Please enter a non-negative integer.")

    start_btn = tk.Button(root, text="Start", command=start)
    start_btn.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple countdown timer with beep.")
    parser.add_argument("duration", nargs="?", type=int, help="Duration in seconds")
    parser.add_argument("--gui", action="store_true", help="Launch Tkinter GUI")
    args = parser.parse_args()

    if args.gui or args.duration is None:
        launch_gui()
    else:
        countdown(args.duration)
