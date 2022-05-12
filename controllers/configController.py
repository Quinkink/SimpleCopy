"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
import urllib.error
import urllib.request
from multiprocessing.pool import ThreadPool

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
        self.view.text.insert(tk.END, self.model.strings['defaultMessageText'])
        self.view.text.focus()
        self.view.button.config(text=(self.model.strings['defaultButton']), command=self.action)

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

