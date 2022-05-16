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
from tkinter import StringVar, N, E, W, S

from views.defaultView import DefaultView


class ConfigView(baseFrame.BaseView):
    """
    """

    def __init__(self, master):
        super(ConfigView, self).__init__(master)

        self.varOpenFolderAfterCopy = StringVar()
        self.varSourceFolderString = StringVar()
        self.varTargetFolderString= StringVar()

        self.text = tk.Text(self, height=1)
        self.text.grid(row=1, column=0, columnspan=6, ipadx=0, ipady=0, padx=2, pady=0, sticky=N+E+W+S)
        self.text.grid_columnconfigure(0, weight=1)

        self.checkbutton = tk.Checkbutton(self, variable=self.varOpenFolderAfterCopy, onvalue='True', offvalue='False')
        self.checkbutton.grid(row=2, column=0, columnspan=6, ipadx=0, ipady=0, padx=4, pady=2, sticky=N+W+S)
        self.checkbutton.grid_columnconfigure(0, weight=1)

        self.buttonChooseSource = tk.Button(self, width=0, text='')
        self.buttonChooseSource.grid(row=3, column=0, columnspan=1, ipadx=0, ipady=0, padx=4, pady=2, sticky=E+W)
        self.buttonChooseSource.grid_columnconfigure(0, weight=1)

        self.entry1 = tk.Entry(self, textvariable=self.varSourceFolderString)
        self.entry1.grid(row=3, column=1, columnspan=5, ipadx=0, ipady=0, padx=2, pady=0, sticky=N+E+W+S)
        self.entry1.grid_columnconfigure(0, weight=1)

        self.buttonChooseTarget = tk.Button(self, width=0, text='')
        self.buttonChooseTarget.grid(row=4, column=0, columnspan=1, ipadx=0, ipady=0, padx=4, pady=2, sticky=E+W)
        self.buttonChooseTarget.grid_columnconfigure(0, weight=1)

        self.entry2 = tk.Entry(self, textvariable=self.varTargetFolderString)
        self.entry2.grid(row=4, column=1, columnspan=5, ipadx=0, ipady=0, padx=2, pady=0, sticky=N+E+W+S)
        self.entry2.grid_columnconfigure(0, weight=1)

        self.buttonCancel = tk.Button(self, width=0, text='')
        self.buttonCancel.grid(row=5, column=0, columnspan=3, ipadx=0, ipady=0, padx=4, pady=2, sticky=E+W)
        self.buttonCancel.grid_columnconfigure(0, weight=1)

        self.buttonApply = tk.Button(self, width=0, text='')
        self.buttonApply.grid(row=5, column=3, columnspan=3, ipadx=0, ipady=0, padx=4, pady=2, sticky=E+W)
        self.buttonApply.grid_columnconfigure(0, weight=1)
