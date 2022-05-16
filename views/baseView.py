"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
from tkinter import N, E, W, S


class BaseView(tk.Frame):
    """An abstract base class for the frames that sit inside PythonGUI.
    https://stackoverflow.com/questions/26213549/switching-between-frames-in-tkinter-menu

    Args:
      master (tk.Frame): The parent widget.

    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        self.feedback = tk.Text(self, width=0, height=0, state=tk.DISABLED)
        self.feedback.grid(row=0, column=0, columnspan=6, ipadx=2, ipady=2, padx=2, pady=2, sticky=N+E+W+S)
