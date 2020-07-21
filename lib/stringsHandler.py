import xml.etree.ElementTree as ElementTree


class XMLStringsHandler(object):
    """

    """
    def __init__(self, file):
        """

        :param file:
        """
        self.file = file
        self.tree = ElementTree.ElementTree(file=self.file)
        self.root = self.tree.getroot()
        
        # XML StringsFrame
        self.tree = ElementTree.ElementTree(file=self.file)
        self.root = self.tree.getroot()
    
    def get_dictionary(self, view):
        """

        :param view:
        :return:
        """
        # returns XML Strings file as a python dictionary (associative array)
        dictionary = {}
        for elem in self.tree.iterfind('view'):
            if elem.get('frame') == view:
                for child in elem.iter():
                    dictionary[child.get('key')] = child.get('value')
        return dictionary
