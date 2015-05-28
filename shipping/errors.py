# coding=utf-8
class MissingParameter(Exception):
    """
    Missing Parameter Exception
    """
    def __init__(self, value):
        """
        Initializes missing parameter exception
        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.value = value

    def __str__(self):
        """
        Self str method to give message info
        :return:
        :rtype:
        """
        return repr(self.value)