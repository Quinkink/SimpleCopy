import xml.etree.ElementTree as ElementTree


class XMLSettingsHandler(object):
    """

    """
    def __init__(self, file):
        """

        :param file:
        """
        self.file = file
        self.tree = ElementTree.ElementTree(file=self.file)
        self.root = self.tree.getroot()
        
        # XML SettingsFrame
        self.tree = ElementTree.ElementTree(file=self.file)
        self.root = self.tree.getroot()
    
    def get_dictionary(self):
        """
        :return: (dictionary) dictionary)
        """
        # returns XML Settings file as a python dictionary (associative array)
        dictionary = {}
        for elem in self.tree.iterfind('setting'):
            dictionary[elem.get('key')] = elem.get('value')
        return dictionary
