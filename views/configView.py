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


class ListView(baseFrame.BaseView):
    """
    """

    def __init__(self, master):
        super(DefaultView, self).__init__(master)

        self.text = tk.Text(self, height=7)
        self.text.grid(row=1, column=0, columnspan=6, ipadx=0, ipady=0, padx=2, pady=0, sticky=(tk.EW, tk.NS))
        self.text.grid_columnconfigure(0, weight=1)

        self.button = tk.Button(self, width=0, text='')
        self.button.grid(row=2, column=0, columnspan=6, ipadx=0, ipady=0, padx=4, pady=2, sticky=tk.EW)
        self.button.grid_columnconfigure(0, weight=1)
