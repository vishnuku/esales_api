# coding=utf-8
import easypost
from shipping import Shipping

class Easypost(Shipping):
    """
    This class provides one point access to USPS apis
    """

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
        self.type = 1
        self.services = None
        self.api = easypost
        self.api.api_key = kwargs.get('apikey', None)
        self.shipment = None
        self.reverseshipment = None

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
        address = self.__address_create(address)
        address = self.__address_parser(address)

        return address

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
        to_address = self.__address_create(address['to'])
        from_address = self.__address_create(address['from'])
        parcel = self.__create_parcel(parcel)

        self.shipment = self.api.Shipment.create(
            to_address=to_address,
            from_address=from_address,
            parcel=parcel,
            options={'address_level_validation': 0}
        )

        return self.shipment.get_rates()['rates']

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
        if rate == 'lowest':
            response = self.shipment.buy(rate=self.shipment.lowest_rate())
        else:
            response = self.shipment.buy(rate=rate)

        return response

    def generate_rma(self, address, parcel, rate, *args, **kwargs):
        """

        :param address:
        :type dictionary:
        :param parcel:
        :type info about parcel:
        :param rate:
        :type either lowest or rate_id:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return: nothing
        :rtype: raises Exception
        """
        to_address = self.__address_create(address['to'])
        from_address = self.__address_create(address['from'])
        parcel = self.__create_parcel(parcel)

        self.reverseshipment = self.api.Shipment.create(
            to_address=from_address,
            from_address=to_address,
            parcel=parcel,
            is_return=True,
            options={'address_level_validation': 0}
        )

        if rate == 'lowest':
            response = self.reverseshipment.buy(rate=self.shipment.lowest_rate())
        else:
            response = self.reverseshipment.buy(rate=rate)

        return response

    def __create_parcel(self, parcel):
        """

        :param parcel:
        :type parcel:
        :return:
        :rtype:
        """
        parcel = self.api.Parcel.create(
            length=parcel.get('length', ''),
            width=parcel.get('width', ''),
            height=parcel.get('height', ''),
            weight=parcel.get('weight', '')
        )

        return parcel

    def __address_create(self, address):
        """

        :param address:
        :type address:
        :return:
        :rtype:
        """
        address = self.api.Address.create_and_verify(
            name=address.get('name', ''),
            street1=address.get('add1', ''),
            street2=address.get('add2', ''),
            city=address.get('city', ''),
            state=address.get('state', ''),
            zip=address.get('zip5', ''),
            country=address.get('country', ''),
            email=address.get('email', '')
        )

        return address

    def __address_parser(self, address):
        """

        :param address:
        :type address:
        :return:
        :rtype:
        """
        return address['address']
