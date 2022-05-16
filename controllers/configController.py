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

        self.view.varOpenFolderAfterCopy.set(self.model.settings['openFolderAfterCopy'])
        self.view.checkbutton.config(text=(self.model.strings['defaultCheckbuttonText']))

        self.view.entry1['state'] = tk.NORMAL
        self.view.varSourceFolderString.set(self.model.settings['source'])
        self.view.entry1['state'] = tk.DISABLED

        self.view.entry2['state'] = tk.NORMAL
        self.view.varTargetFolderString.set(self.model.settings['target'])
        self.view.entry2['state'] = tk.DISABLED

        self.view.buttonCancel.config(text=(self.model.strings['defaultButtonCancel']), command=self.action_cancel)
        self.view.buttonApply.config(text=(self.model.strings['defaultButtonApply']), command=self.action_apply)
        self.view.buttonChooseSource.config(text=(self.model.strings['defaultButtonChoose']), command=self.action_source)
        self.view.buttonChooseTarget.config(text=(self.model.strings['defaultButtonChoose']), command=self.action_target)
        self.view.buttonCancel.focus()

    def action_cancel(self):
        self.app.show_view('Default')

    def action_apply(self):
        self.view.text.delete(1.0, tk.END)
        self.application_feedback(self.model.strings['defaultMessageClear'], 'GREEN')
        self.model.xml_settings.set_element_value('openFolderAfterCopy', self.view.varOpenFolderAfterCopy.get())
        self.model.xml_settings.set_element_value('source', self.view.varSourceFolderString.get())
        self.model.xml_settings.set_element_value('target', self.view.varTargetFolderString.get())
        self.app.show_view('Default')

    def action_source(self):
        directory = filedialog.askdirectory()
        if directory != '':
            self.view.text.delete(1.0, tk.END)
            self.application_feedback(directory, 'GREEN')
            self.view.entry1['state'] = tk.NORMAL
            self.view.varSourceFolderString.set(directory + '/')
            self.view.entry1['state'] = tk.DISABLED
        else:
            self.application_feedback(self.model.strings['defaultMessageCancel'], 'ORANGE')

    def action_target(self):
        directory = filedialog.askdirectory()
        if directory != '':
            self.view.text.delete(1.0, tk.END)
            self.application_feedback(directory, 'GREEN')
            self.view.entry2['state'] = tk.NORMAL
            self.view.varTargetFolderString.set(directory + '/')
            self.view.entry2['state'] = tk.DISABLED
        else:
            self.application_feedback(self.model.strings['defaultMessageCancel'], 'ORANGE')

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
