"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
import views.baseView as baseFrame


class AppView:
    """
    """

    def __init__(self):
        """

        """

        """Load tkinter root"""
        # LOAD ROOT
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        """Geometry set in applicationController"""
        self.root.winfo_toplevel().wm_geometry("")
        self.root.pack_propagate(1)

        # WIDGETS
        """MAIN APP CONTAINER FRAME"""
        self.container = tk.Frame(self.root)
        self.menubar = None
        self.navigationmenu = None
        self.othermenu = None

        # GRID
        self.container.grid(row=0, column=0, sticky='ew')
        self.container.grid_columnconfigure(0, weight=1)
