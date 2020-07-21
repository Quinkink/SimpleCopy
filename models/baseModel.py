"""
Created on 17 Mar 2020

@author: Eleonore
"""
from lib import settingsHandler
from lib import stringsHandler


class BaseModel:
    """
    """
    def __init__(self, filenames):
        """

        :param filenames: (dictionary) contains XML file names.
        This dictionary is defined in ApplicationController class
        """
        self.filenames = filenames

        # PLACE HOLDERS FOR FILE DATA
        self.xml_settings = None
        self.xml_strings = None

        # DICTIONARIES
        self.settings = {}
        self.strings = {}

        # LOAD VALUES
        self.load_xml_settings()

    def load_xml_settings(self):
        self.xml_settings = settingsHandler.XMLSettingsHandler(self.filenames['settings'])
        self.settings = self.xml_settings.get_dictionary()

    def load_xml_strings(self, view):
        self.xml_strings = stringsHandler.XMLStringsHandler(self.filenames['strings'])
        self.strings = self.xml_strings.get_dictionary(view)
