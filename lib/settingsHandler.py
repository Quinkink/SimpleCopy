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

    def get_element_value(self, key):
        """

        """
        result = False
        for elem in self.tree.iterfind('setting'):
            if elem.get('key') == key:
                result = elem.get('value')
        return result

    def set_element_value(self, key, value):
        """

        """
        result = False
        for elem in self.tree.iterfind('setting'):
            if elem.get('key') == key:
                elem.set('value', value)
                # elem.set('new_attribute', 'new_value')
                if elem.get('value') == value:
                    result = True
                    try:
                        with open(self.file, 'wb') as f:
                            self.tree.write(f, encoding='utf-8')
                    except FileNotFoundError:
                        result = False
        return result
