"""
Plotting machinery
"""
import ast
import logging
import queue
import sys
import threading
import tkinter as tk
import time
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import numpy as np  # Needed for dynamic code.

from debug import create_filelog

LOGGER = logging.getLogger(__name__)


def rate_limited_true():
    """Returns true after a given delay."""
    time.sleep(0.05)
    return True


def parser():
    """The argparser."""
    parser = ArgumentParser()
    parser.add_argument("--num", type=int)
    parser.add_argument("--color", type=ast.literal_eval)
    parser.add_argument("--dpi", type=float)
    return parser


def add_stdin_to_queue(input_queue):
    """Listen to stdin for new data."""
    while rate_limited_true():
        input_queue.put(sys.stdin.readline())
        print(input_queue)


def update_plot(input_queue, fig):
    """Wait for things in the queue."""
    while rate_limited_true():
        if not input_queue.empty():
            command = input_queue.get()
            if command:
                LOGGER.debug(f"exec: {command}")
                exec(command)


def make_thread(fn, args):
    """Makes a new thread for this process."""
    thread = threading.Thread(target=fn, args=args)
    thread.daemon = True
    thread.start()
    return thread


def main(args):
    fig = plt.figure(num=args.num, facecolor=args.color, dpi=args.dpi)

    # Set the toolbar to show at the top of the figure.
    # (I think this only works for Tk backends...)
    fig.canvas.toolbar.pack(side=tk.TOP, fill=tk.X)

    input_queue = queue.Queue()

    input_thread = make_thread(fn=add_stdin_to_queue, args=(input_queue,))
    plot_thread = make_thread(fn=update_plot, args=(input_queue, fig))

    plt.show()


if __name__ == "__main__":
    logging.basicConfig(handlers=[create_filelog("figure")])
    LOGGER.setLevel(logging.DEBUG)
    main(parser().parse_args())
