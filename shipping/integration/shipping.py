# coding=utf-8

class Shipping(object):
    """
    This class provides one point access to USPS apis
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the API can take any argument and keyword argument.
        Generally takes username, apikey, password etc based on the aggregator or service provider
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        self.init_api(*args, **kwargs)

    def init_api(self, *args, **kwargs):
        """
        A method to be called from init. Its content is based on the initialization of class of different provider
        be it aggregator or service provoider.
        It generally contains following infro
        type: aggregator or serviceproviewe (0,1)
        url: API endpoint url

        :param args:
        :type not defined:
        :param kwargs:
        :type key value for usename, api etc:
        :return:
        :rtype:
        """
        self.userid = kwargs['userid']
        self.url = None
        self.type = 0
        self.services = None

    def validate_address(self, address, *args, **kwargs):
        """

        :param address:
        :type dictionary:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return: nothing
        :rtype: raises Exception
        """

        raise NotImplementedError

    def get_price(self, address, parcel, *args, **kwargs):
        """

        :param address:
        :type dictionary:
        :param items:
        :type items list of dictionary of items:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return: nothing
        :rtype: raises Exception
        """

        raise NotImplementedError

    def ship(self, address, parcel, rate, *args, **kwargs):
        """

        :param address:
        :type dictionary:
        :param items:
        :type items list of dictionary of items:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return: nothing
        :rtype: raises Exception
        """

        raise NotImplementedError

    def generate_rma(self, address, parcel, rate,  *args, **kwargs):
        """

        :param address:
        :type dictionary:
        :param items:
        :type items list of dictionary of items:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return: nothing
        :rtype: raises Exception
        """

        raise NotImplementedError

    def track(self, tid, *args, **kwargs):
        """

        :param tid:
        :type tid:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """

        raise NotImplementedError
