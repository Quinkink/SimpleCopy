"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
import urllib.error
import urllib.request
from multiprocessing.pool import ThreadPool
from tkinter import filedialog
from tkinter import StringVar

import lib.functionEngine as functions


class ConfigController(object):
    """
    DefaultController for DefaultView and DefaultModel
    """

    def __init__(self, app):
        """
        Init for DefaultController
        :param app: this is the main application controller
        """
        self.app = app
        self.app.lastView = 'Default'
        self.model = self.app.model
        self.view = self.app.views['Config']

        self.load_model_config()

    def load_model_config(self):
        """
        loads data to view
        :return: void
        """
        self.application_feedback(self.model.strings['defaultMessageWelcome'])
        self.view.text['state'] = tk.NORMAL
        self.view.text.delete(1.0, tk.END)
        self.view.text.insert(tk.END, self.model.strings['defaultMessageText'])
        self.view.text['state'] = tk.DISABLED
        self.view.text.focus()

        self.view.entry1['state'] = tk.NORMAL
        self.view.entry1Text.set(self.model.settings['source'])
        self.view.entry1['state'] = tk.DISABLED
        self.view.entry2['state'] = tk.NORMAL
        self.view.entry2Text.set(self.model.settings['target'])
        self.view.entry2['state'] = tk.DISABLED

        self.view.button1.config(text=(self.model.strings['defaultButtonCancel']), command=self.action_cancel)
        self.view.button2.config(text=(self.model.strings['defaultButtonApply']), command=self.action_apply)
        self.view.button3.config(text=(self.model.strings['defaultButtonChoose']), command=self.action_source)
        self.view.button4.config(text=(self.model.strings['defaultButtonChoose']), command=self.action_target)

    def action_cancel(self):
        self.app.show_view('Default')

    def action_apply(self):
        self.view.text.delete(1.0, tk.END)
        self.application_feedback(self.model.strings['defaultMessageClear'], 'GREEN')
        # self.show_view('Config')

    def action_source(self):
        directory = filedialog.askdirectory()
        self.view.text.delete(1.0, tk.END)
        self.application_feedback(directory, 'GREEN')
        self.view.entry1['state'] = tk.NORMAL
        self.view.entry1Text.set(directory)
        self.view.entry1['state'] = tk.DISABLED

    def action_target(self):
        directory = filedialog.askdirectory()
        self.view.text.delete(1.0, tk.END)
        self.application_feedback(directory, 'GREEN')
        self.view.entry2['state'] = tk.NORMAL
        self.view.entry2Text.set(directory)
        self.view.entry2['state'] = tk.DISABLED

    def action(self):
        self.view.text.delete(1.0, tk.END)
        self.application_feedback(self.model.strings['defaultMessageClear'], 'GREEN')

    def application_feedback(self, feedback, bgcolour='BLACK', fgcolour='WHITE'):
        """
        send feedback to user through view.feedback
        :param feedback: this is the message content
        :param bgcolour: background color defaults to WHITE
        :param fgcolour: foreground colour defaults to BLACK
        :return: void
        """
        self.view.feedback.config(state=tk.NORMAL)
        self.view.feedback.delete(1.0, tk.END)
        self.view.feedback.config(background=bgcolour, foreground=fgcolour)
        self.view.feedback.insert(tk.END, feedback)
        self.view.feedback.config(state=tk.DISABLED)

