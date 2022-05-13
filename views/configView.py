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
import views.baseView as baseFrame
from tkinter import StringVar, filedialog

from views.defaultView import DefaultView


class ConfigView(baseFrame.BaseView):
    """
    """

    def __init__(self, master):
        super(ConfigView, self).__init__(master)

        self.entry1Text = StringVar()
        self.entry2Text = StringVar()

        self.text = tk.Text(self, height=3)
        self.text.grid(row=1, column=0, columnspan=6, ipadx=0, ipady=0, padx=2, pady=0, sticky='news')
        self.text.grid_columnconfigure(0, weight=1)

        self.button3 = tk.Button(self, width=0, text='')
        self.button3.grid(row=2, column=0, columnspan=1, ipadx=0, ipady=0, padx=4, pady=2, sticky='ew')
        self.button3.grid_columnconfigure(0, weight=1)

        self.entry1 = tk.Entry(self, textvariable=self.entry1Text)
        self.entry1.grid(row=2, column=1, columnspan=5, ipadx=0, ipady=0, padx=2, pady=0, sticky='news')
        self.entry1.grid_columnconfigure(0, weight=1)

        self.button4 = tk.Button(self, width=0, text='')
        self.button4.grid(row=3, column=0, columnspan=1, ipadx=0, ipady=0, padx=4, pady=2, sticky='ew')
        self.button4.grid_columnconfigure(0, weight=1)

        self.entry2 = tk.Entry(self, textvariable=self.entry2Text)
        self.entry2.grid(row=3, column=1, columnspan=5, ipadx=0, ipady=0, padx=2, pady=0, sticky='news')
        self.entry2.grid_columnconfigure(0, weight=1)

        self.button1 = tk.Button(self, width=0, text='')
        self.button1.grid(row=4, column=0, columnspan=3, ipadx=0, ipady=0, padx=4, pady=2, sticky='ew')
        self.button1.grid_columnconfigure(0, weight=1)

        self.button2 = tk.Button(self, width=0, text='')
        self.button2.grid(row=4, column=3, columnspan=3, ipadx=0, ipady=0, padx=4, pady=2, sticky='ew')
        self.button2.grid_columnconfigure(0, weight=1)
