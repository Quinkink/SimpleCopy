"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel
import lib.functionEngine as functions


class AppModel(BaseModel):
    """
    """
    def __init__(self, filenames):
        """

        :param filenames: (dictionary) contains XML file names
        """
        super(AppModel, self).__init__(filenames)
        # SETTINGS FROM FILE & LOAD VALUES
        self.load_xml_settings()

        self.filenames['strings'] = functions.find_data_file(self.settings['filenameLanguage'], 'data')

        # LOAD PLACE HOLDERS
        self.load_xml_strings('APP')
