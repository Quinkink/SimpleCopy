"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel


class MinimalModel(BaseModel):
    """"""

    def __init__(self, filenames):
        """

        :param filenames: (dictionary) contains XML file names.
        This dictionary is defined in ApplicationController class
        """
        super(MinimalModel, self).__init__(filenames)
        self.load_xml_strings('MINIMAL')
