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
from tkinter import StringVar


class DefaultView(baseFrame.BaseView):
    """
    """

    def __init__(self, master):
        super(DefaultView, self).__init__(master)

        self.labelTextValue = StringVar()
        self.entryTextValue = StringVar()

        self.label = tk.Label(self, textvariable=self.labelTextValue)
        self.label.grid(row=1, column=0, columnspan=2, ipadx=0, ipady=0, padx=2, pady=0, sticky='wns')

        self.entry = tk.Entry(self, textvariable=self.entryTextValue)
        self.entry.grid(row=1, column=2, columnspan=4, ipadx=0, ipady=0, padx=2, pady=0, sticky='news')

        self.text = tk.Text(self, height=6)
        self.text.grid(row=2, column=0, columnspan=6, ipadx=0, ipady=0, padx=2, pady=0, sticky='news')

        self.buttonReset = tk.Button(self, width=0, text='')
        self.buttonReset.grid(row=3, column=0, columnspan=3, ipadx=0, ipady=0, padx=4, pady=2, sticky='ew')

        self.buttonCopy = tk.Button(self, width=0, text='')
        self.buttonCopy.grid(row=3, column=3, columnspan=3, ipadx=0, ipady=0, padx=4, pady=2, sticky='ew')




