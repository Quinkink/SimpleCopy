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

        # logLevel DEBUG
        if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
            print('loading view : Minimal')

        self.view = self.app.views['Minimal']
        self.view.buttonReset.grid_remove()

        self.source = self.model.xml_settings.get_element_value('source')
        self.target = self.model.xml_settings.get_element_value('target')

        self.load_model_config()

    def load_model_config(self):
        """
        loads data to view
        :return: void
        """

        # logLevel DEBUG
        if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
            print('method : load_level_config(self)')

        self.application_feedback(self.model.strings['defaultMessageWelcome'], 'BLACK')

        self.view.labelTextValue.set(self.model.strings['defaultLabelValue'])

        self.view.entryTextValue.set(self.model.strings['defaultEntryValue'])
        self.view.entry.bind('<Button-1>', lambda e: self.action_entry_delete(event='<Button-1>'))

        self.view.buttonReset.config(text=(self.model.strings['defaultButtonReset']), command=self.action_reset)
        self.view.buttonReset['state'] = tk.NORMAL

        self.view.buttonCopy.config(text=(self.model.strings['defaultButtonCopy']), command=self.action_copy)
        self.view.buttonCopy['state'] = tk.NORMAL
        self.view.buttonCopy.focus()

    def action_entry_delete(self, event):

        # logLevel DEBUG
        if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
            print('method : action_entry_delete(self, event)')

        self.view.entry.configure(state=tk.NORMAL)
        self.view.entry.delete(0, tk.END)
        self.view.entry.unbind('<Button-1>')
        self.view.entry.bind('<Return>', lambda e: self.action_return_copy(event='<Return>'))

    def action_return_copy(self, event):

        # logLevel DEBUG
        if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
            print('method : action_return_copy(self, event)')

        # self.application_feedback(str(self.app.appView.root.winfo_width()) + " - " + str(self.app.appView.root.winfo_height()), 'ORANGE')

        self.view.entry.unbind('<Return>')
        self.action_copy()

    def action_copy(self):
        feedback = self.model.strings['defaultMessageSuccess']
        colour = 'GREEN'

        # logLevel DEBUG
        if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
            print('method : action_copy(self)')

        if self.view.entryTextValue.get() == self.model.strings['defaultEntryValue']:
            # logLevel DEBUG
            if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                print('    entryTextValue = defaultEntryValue')
            feedback = self.model.strings['defaultMessageFailFolderName']
            colour = 'ORANGE'

        elif self.view.entryTextValue.get() == "":
            # logLevel DEBUG
            if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                print('    entryTextValue = ""')
            feedback = self.model.strings['defaultMessageFailNoFolderName']
            colour = 'ORANGE'

        elif not re.fullmatch('^[^\\\\/?%*:|\"\'<>.]{1,32}$', self.view.entryTextValue.get()):
            # logLevel DEBUG
            if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                print('    entryTextValue = not valid folder name')
            feedback = self.model.strings['defaultMessageFailIllegalCharacters']
            colour = 'ORANGE'

        else:
            feedback = self.model.strings['defaultMessageSuccess']
            colour = 'GREEN'
            # logLevel DEBUG
            if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                print('    attempting COPY')

            try:
                """copy from source to target"""
                shutil.copytree(self.source, self.target + self.view.entry.get())
            except FileExistsError:
                # logLevel DEBUG
                if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                    print('        exception : folder exists error')
                # SHOULD WE OVERWRITE
                if self.app.message_dialogue_user_confirm('title', self.model.strings['popupMessageFileExists']):
                    # logLevel DEBUG
                    if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                        print('        if : user confirms overwrite')
                    try:
                        """remove existing target folder after prompt"""
                        shutil.rmtree(self.target + self.view.entry.get())
                    except FileExistsError:
                        # logLevel DEBUG
                        if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                            print('        exception : folder exists error')
                        feedback = self.model.strings['defaultMessageFailRemove']
                        colour = 'RED'
                    else:
                        try:
                            # logLevel DEBUG
                            if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                                print('            try : copy source to target')

                            shutil.copytree(self.source, self.target + self.view.entry.get())
                        except FileExistsError:
                            feedback = self.model.strings['defaultMessageFailExists']
                            colour = 'RED'
                        else:
                            # logLevel DEBUG
                            if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                                print('            else (try) : no exceptions')
                            # self.view.buttonCopy['state'] = tk.DISABLED
                            self.view.entry['state'] = tk.DISABLED
                            self.view.buttonCopy.grid_remove()
                            self.view.buttonReset.grid()
                            if self.model.settings['openFolderAfterCopy'] == 'True':
                                self.action_open_after_copy()
                        finally:
                            # logLevel DEBUG
                            if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                                print('            finally : nothing')
                            # self.view.buttonCopy['state'] = tk.DISABLED
                    finally:
                        # logLevel DEBUG
                        if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                            print('        finally : nothing')
                # USER CANCELS OVERWRITE
                else:
                    # logLevel DEBUG
                    if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                        print('        else (if) : user cancels overwrite')
                    feedback = self.model.strings['defaultMessageNothingChanged']
                    colour = 'GREEN'
            except PermissionError:
                # logLevel DEBUG
                if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                    print('        except : permission error')
                feedback = self.model.strings['defaultMessageFailPermission']
                colour = 'RED'
            else:
                # logLevel DEBUG
                if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                    print('        else (try) : no exceptions')
                # self.view.buttonCopy['state'] = tk.DISABLED
                self.view.entry['state'] = tk.DISABLED
                self.view.buttonCopy.grid_remove()
                self.view.buttonReset.grid()
                if self.model.settings['openFolderAfterCopy'] == 'True':
                    self.action_open_after_copy()
            finally:
                # logLevel DEBUG
                if self.model.xml_settings.get_element_value('logLevel') == 'DEBUG':
                    print('    finally : nothing')

        self.application_feedback(feedback, colour)

    def action_open_after_copy(self):
        os.system('start ' + self.target + self.view.entry.get())

    def action_reset(self):
        self.application_feedback(self.model.strings['defaultMessageWelcome'], 'BLACK')
        self.view.entry.bind('<Button-1>', lambda e: self.action_entry_delete(event='<Button-1>'))
        self.view.entry['state'] = tk.NORMAL
        self.view.entryTextValue.set(self.model.strings['defaultEntryValue'])
        self.view.buttonReset.grid_remove()
        self.view.buttonCopy.grid()
        self.view.buttonCopy.focus()

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
