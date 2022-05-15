"""
Created on 17 Mar 2020

@author: Eleonore
"""
import re
import tkinter as tk
import os
import shutil
import datetime
import urllib.error
import urllib.request
from multiprocessing.pool import ThreadPool
from tkinter import StringVar

import lib.functionEngine as functions


class MinimalController(object):
    """
    MinimalController for MinimalView and MinimalModel
    """

    def __init__(self, app):
        """
        Init for MinimalController
        :param app: this is the main application controller
        """
        self.app = app
        self.app.lastView = 'Minimal'
        self.model = self.app.model
        self.view = self.app.views['Minimal']
        self.view.entry.bind('<Return>', self.action_return_copy(event='<Return>'))
        self.view.entry.focus()

        self.feedback = self.model.strings['defaultMessageSuccess']
        self.colour = 'GREEN'

        self.load_model_config()

    def load_model_config(self):
        """
        loads data to view
        :return: void
        """
        self.application_feedback(self.model.strings['defaultMessageWelcome'], 'BLACK')

        self.view.labelTextValue.set(self.model.strings['defaultLabelValue'])

        self.view.entryTextValue.set(self.model.strings['defaultEntryValue'])

    def action_return_copy(self, event):
        self.action_copy()

    def action_copy(self):

        """now = str(datetime.datetime.now())[:19]
        now = self.now.replace("-", "")
        now = self.now.replace(" ", "")
        now = self.now.replace(":", "")"""

        if self.view.entryTextValue.get() == self.model.strings['defaultEntryValue']:
            self.feedback = self.model.strings['defaultMessageFailFolderName']
            self.colour = 'ORANGE'

        elif self.view.entryTextValue.get() == "":
            self.feedback = self.model.strings['defaultMessageFailNoFolderName']
            self.colour = 'ORANGE'

        elif not re.fullmatch('^[^\\\\/?%*:|\"\'<>.]{1,32}$', self.view.entryTextValue.get()):
            self.feedback = self.model.strings['defaultMessageFailIllegalCharacters']
            self.colour = 'ORANGE'

        else:
            self.feedback = self.model.strings['defaultMessageSuccess']
            self.colour = 'GREEN'
            try:
                """copy from source to target"""
                shutil.copytree(self.source, self.target + self.view.entry.get())
            except FileExistsError:
                if self.app.message_dialogue_user_confirm('title', self.model.strings['popupMessageFileExists']):
                    try:
                        """remove existing target folder after prompt"""
                        shutil.rmtree(self.target + self.view.entry.get())
                    except FileExistsError:
                        self.feedback = self.model.strings['defaultMessageFailRemove']
                        self.colour = 'RED'
                    try:
                        """copy from source to target"""
                        shutil.copytree(self.source, self.target + self.view.entry.get())
                    except FileExistsError:
                        self.feedback = self.model.strings['defaultMessageFailExists']
                        self.colour = 'RED'
                    """finally:
                        self.view.buttonCopy['state'] = tk.DISABLED"""
                else:
                    self.feedback = self.model.strings['defaultMessageNothingChanged']
                    self.colour = 'GREEN'
            except PermissionError:
                self.feedback = self.model.strings['defaultMessageFailPermission']
                self.colour = 'RED'
            finally:
                self.view.buttonCopy['state'] = tk.DISABLED

        self.application_feedback(self.feedback, self.colour)

    def action_reset(self):
        self.feedback = self.model.strings['defaultMessageWelcome']
        self.colour = 'BLACK'
        self.application_feedback(self.feedback, self.colour)
        self.view.entryTextValue.set(self.model.strings['defaultEntryValue'])
        self.view.buttonCopy['state'] = tk.NORMAL

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