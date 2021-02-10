#!/usr/bin/env python3
import time
import subprocess
from typing import Optional

# 15 minutes in between
MINI_BREAK_INTERVAL_S = 15 * 60
# 15 second break
MINI_BREAK_DURATION_S = 15

# 1 hour in between
BIG_BREAK_INTERVAL_S = 60 * 60
# 10 minute break
BIG_BREAK_DURATION_S = 10 * 60


def notify(title: str, msg: str, duration_ms: Optional[int] = None):
    if duration_ms:
        subprocess.run(["notify-send", "-t", str(duration_ms), title, msg])
    else:
        subprocess.run(["notify-send", title, msg])


def do_mini_break():
    notify(
        "Time for a mini break!",
        f"Take your eyes off the screen for {MINI_BREAK_DURATION_S} seconds :)",
    )
    time.sleep(MINI_BREAK_DURATION_S)
    notify("Your mini is break over!", "Back to work!")


def do_big_break():
    notify(
        "Time for a big break!",
        f"Take your eyes off the screen for {BIG_BREAK_DURATION_S} seconds :)",
    )
    time.sleep(BIG_BREAK_DURATION_S)
    notify("Your big is break over!", "Back to work!")


def main():
    start = time.time()
    last_small_break = start
    last_big_break = start

    while True:
        curr = time.time()
        if curr - last_small_break > MINI_BREAK_INTERVAL_S:
            last_small_break = curr
            do_mini_break()

        if curr - last_big_break > BIG_BREAK_INTERVAL_S:
            last_big_break = curr
            last_small_break = curr
            do_big_break()

        time.sleep(10)


if __name__ == "__main__":
    main()
