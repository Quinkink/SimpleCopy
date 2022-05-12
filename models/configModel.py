"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel


class ConfigModel(BaseModel):
    """"""

    def __init__(self, filenames):
        """

        :param filenames: (dictionary) contains XML file names.
        This dictionary is defined in ApplicationController class
        """
        super(ConfigModel, self).__init__(filenames)
        self.load_xml_strings('LIST')
