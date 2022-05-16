"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import N, E, W, S
import lib.tkErrorCatcher as tec
# APP MVC
from controllers.configController import ConfigController
from controllers.minimalController import MinimalController
from models.appModel import AppModel
from models.configModel import ConfigModel
from models.minimalModel import MinimalModel
from views.appView import AppView
# SEND MVC
from models.defaultModel import DefaultModel
from views.configView import ConfigView
from views.defaultView import DefaultView
from controllers.defaultController import DefaultController
# OTHER IMPORTS
import lib.functionEngine as functions
from views.minimalView import MinimalView


class Application(object):
    """
    The main application Controller
    Args: void
    """

    def __init__(self, settings):
        """
        Init for Application
        :param settings: (string) settings xml filename
        """
        self.appModel = AppModel({'settings': functions.find_data_file(settings, 'data'),
                                  'strings': None})
        tk.CallWrapper = tec.TkErrorCatcher
        self.appView = AppView()
        self.appView.root.protocol('WM_DELETE_WINDOW', self.quit)
        self.appView.root.geometry(self.appModel.settings['geometryAppView'])
        self.visibleView = self.appModel.settings['defaultStartView']
        self.lastView = None
        # ADD OTHER MVC FRAMES HERE
        self.app_mvc = {'Default': {'model': DefaultModel,
                                    'view': DefaultView,
                                    'controller': DefaultController,
                                    'geometry': self.appModel.settings['geometryDefaultView']},
                        'Config': {'model': ConfigModel,
                                   'view': ConfigView,
                                   'controller': ConfigController,
                                   'geometry': self.appModel.settings['geometryConfigView']},
                        'Minimal': {'model': MinimalModel,
                                    'view': MinimalView,
                                    'controller': MinimalController,
                                    'geometry': self.appModel.settings['geometryMinimalView']}
                        }
        self.model = None
        self.controller = None
        self.views = {}
        self.load_views()
        self.load_menu()

    def load_views(self):
        """
        loads all GUI views into list for view switching
        :return: void
        """
        for name, mvc in self.app_mvc.items():
            frame = mvc['view'](self.appView.container)
            frame.grid(row=2, column=2, sticky=N+E+W+S)
            self.views[name] = frame
        else:
            self.show_view(self.visibleView)

    def show_view(self, mvc):
        """
        shows selected view and load corresponding controller and model
        :param mvc: (sting) name of view
        :return: void
        """
        # ADD OTHER DATA FILES HERE
        filenames = {'settings': self.appModel.filenames['settings'],
                     'strings': self.appModel.filenames['strings']}
        # LOAD MODEL
        self.model = self.app_mvc[mvc]['model'](filenames)

        # LOAD CONTROLLER
        self.controller = self.app_mvc[mvc]['controller'](self)

        # RAISE VIEW
        self.views[mvc].tkraise()
        self.visibleView = mvc

        # CAUSE REFRESH
        self.appView.root.update_idletasks()
        self.appView.root.geometry(self.app_mvc[mvc]['geometry'])
        self.views[mvc].focus_set()

        # LOAD TOP MENU
        try:
            self.load_menu()
        except AttributeError:
            pass

    def load_menu(self):
        """
        loads application top menu tk object and data. Should this be here or in appView?
        I guess here as I don't know a way to set command to controller methods from view menu
        :return: void
        """
        self.appView.menubar = tk.Menu(self.appView.root)
        # ADD MENU ITEMS
        # self.appView.menubar.add_command(label=(self.appModel.strings['my_string_in_strings_EN.xml']),
        #                                command=(lambda: self.show_view('my_key_in_app_mvc')))
        self.appView.othermenu = tk.Menu(self.appView.menubar, tearoff=0)
        self.appView.othermenu.add_command(label=(self.appModel.strings['menuMinimal']), command=self.minimal)
        self.appView.othermenu.add_command(label=(self.appModel.strings['menuVerbose']), command=self.verbose)
        self.appView.othermenu.add_command(label=(self.appModel.strings['menuSettings']), command=self.settings)
        self.appView.othermenu.add_command(label=(self.appModel.strings['menuAbout']), command=self.about)
        self.appView.othermenu.add_command(label=(self.appModel.strings['menuHelp']), command=self.help)
        self.appView.othermenu.add_command(label=(self.appModel.strings['menuQuit']), command=self.quit)
        self.appView.menubar.add_cascade(label=self.appModel.strings['menuBarOther'], menu=self.appView.othermenu)
        self.appView.root.config(menu=self.appView.menubar)

    def minimal(self):
        """"""
        """self.message_dialogue_information_feedback(self.appModel.strings['messageTitleSettings'],
                                                   self.appModel.strings['messageSettings'])"""
        self.show_view('Minimal')

    def verbose(self):
        """"""
        """self.message_dialogue_information_feedback(self.appModel.strings['messageTitleSettings'],
                                                   self.appModel.strings['messageSettings'])"""
        self.show_view('Default')

    def settings(self):
        """"""
        """self.message_dialogue_information_feedback(self.appModel.strings['messageTitleSettings'],
                                                   self.appModel.strings['messageSettings'])"""
        self.show_view('Config')

    def help(self):
        """"""
        self.message_dialogue_information_feedback(self.appModel.strings['messageTitleHelp'],
                                                   self.appModel.strings['messageHelp'])

    def about(self):
        """"""
        self.message_dialogue_information_feedback(self.appModel.strings['messageTitleAbout'],
                                                   'Application : ' + self.appModel.settings['applicationTitle'] +
                                                   '\nVersion : ' + self.appModel.settings['version'] +
                                                   '\nCodded by Mark for a little fun'
                                                   '\non Github as Quinkink'
                                                   '\nkingston.lewis@gmail.com')

    def run(self):
        """
        called by main. This is the main loop for tkinter
        :return: void
        """
        self.appView.root.title(self.appModel.settings['applicationTitle'])
        self.appView.root.iconbitmap(functions.find_data_file('app.ico', 'src'))
        self.appView.root.deiconify()
        self.appView.root.mainloop()

    def quit(self):
        """
        called by "Quit" button in menu
        :return: void
        """
        self.appView.root.destroy()

    # noinspection PyMethodMayBeStatic
    def message_dialogue_warning_feedback(self, title, message, icon='warning'):
        """
        tkinter messagebox.showwarning GUI maybe this should be in the view...
        :param title: (string) the title of the message
        :param message: (string) message to display to user
        :param icon: (string) the choice of icon for messagebox: error, warning, information
        :return: void
        """
        tk.messagebox.showwarning(title, message, icon=icon)

    # noinspection PyMethodMayBeStatic
    def message_dialogue_error_feedback(self, title, message, icon='error'):
        """
        tkinter messagebox.showerror GUI maybe this should be in the view...
        :param title: (string) the title of the message
        :param message: (string) message to display to user
        :param icon: (string) the choice of icon for messagebox: error, warning, information
        :return: void
        """
        tk.messagebox.showerror(title, message, icon=icon)

    # noinspection PyMethodMayBeStatic
    def message_dialogue_information_feedback(self, title, message, icon='info'):
        """
        tkinter messagebox.showerror GUI maybe this should be in the view...
        :param title: (string) the title of the message
        :param message: (string) message to display to user
        :param icon: (string) the choice of icon for messagebox: error, warning, information
        :return: void
        """
        tk.messagebox.showinfo(title, message, icon=icon)

    # noinspection PyMethodMayBeStatic
    def message_dialogue_user_confirm(self, title, message, icon='warning'):
        """
        tkinter messagebox.askquestion GUI maybe this should be in view...
        :param title: (string) the title of the message
        :param message: (string) message to be displayed to user
        :param icon: icon to be displayed to user
        :return: boolean (YES,NO)
        """
        result = tk.messagebox.askokcancel(title, message, icon=icon)
        return result
