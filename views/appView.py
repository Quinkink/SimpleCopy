"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
from tkinter import N, E, W, S
import views.baseView as baseFrame


class AppView:
    """
    """

    def __init__(self, resizable_x, resizable_y):
        """

        """

        """LOAD TKINTER ROOT"""
        # LOAD ROOT
        self.root = tk.Tk()
        self.root.resizable(resizable_x, resizable_y)
        """GEOMETRY IS SET IN APPLICATION CONTROLLER"""
        self.root.winfo_toplevel().wm_geometry("")
        # self.root.pack_propagate(1)
        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)

        # WIDGETS
        """MAIN APP CONTAINER FRAME ALL THE VIEWS ARE INCLUDED IN"""
        self.container = tk.Frame(self.root)
        self.menubar = None
        self.navigationmenu = None
        self.othermenu = None

        # GRID
        self.container.grid(row=0, column=0, sticky=N+E+W+S)
