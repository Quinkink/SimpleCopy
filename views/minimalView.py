# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Eleonore\Documents\PycharmProjects\SMSAPI\views\sendView.py
# Compiled at: 2020-06-30 17:38:02
# Size of source mod 2**32: 1417 bytes
"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
from tkinter import StringVar, N, E, W, S
import views.baseView as baseFrame


class MinimalView(baseFrame.BaseView):
    """
    """

    def __init__(self, master):
        super(MinimalView, self).__init__(master)

        self.labelTextValue = StringVar()
        self.entryTextValue = StringVar()

        self.label = tk.Label(self, textvariable=self.labelTextValue)
        self.label.configure(height=1, width=12)
        self.label.grid(row=1, column=0, columnspan=1,
                        ipadx=4, ipady=2, padx=2, pady=2,
                        sticky=N+W+S)

        self.entry = tk.Entry(self, textvariable=self.entryTextValue)
        self.entry.configure(width=32)
        self.entry.grid(row=1, column=1, columnspan=4,
                        ipadx=2, ipady=2, padx=2, pady=2,
                        sticky=N+W+E+S)

        self.buttonCopy = tk.Button(self, width=1, fg="GREEN")
        self.buttonCopy.configure(height=1, width=4)
        self.buttonCopy.grid(row=1, column=5, columnspan=1,
                             ipadx=2, ipady=2, padx=2, pady=2,
                             sticky=N+W+S)