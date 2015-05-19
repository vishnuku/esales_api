# coding=utf-8
import requests
from lxml import etree
from lxml import objectify
from collections import OrderedDict


class Usps(object):
    """
    This class provides one point access to USPS apis
    """

    def __init__(self, *args, **kwargs):
        self.userid = kwargs['userid']
        # self.url = 'http://production.shippingapis.com/ShippingAPITest.dll?API={}'
        self.url = 'http://production.shippingapis.com/ShippingAPITest.dll?API={}'

    def _response_parser(self, resposne):
        """

        :param resposne:
        :type resposne:
        :return:
        :rtype:
        """

        root = objectify.fromstring(resposne)
        return root

    def send_request(self, xml, *args, **kwargs):



        """

        :param xml:
        :type xml:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        url = self.url.format(kwargs['type'])
        payload = {'XML': xml}
        r = requests.post(url, data=payload)
        self._response_parser(r.content)
        return

    def generate_xml(self, type, data, *args, **kwargs):
        """

        :param type:
        :type type:
        :param data:
        :type data:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        if type == 'ADDRESSVALIDATEREQUEST':
            return etree.tostring(self._generate_adressvalidaterequest_xml(data))
        else:
            # raise error invalid type provided
            return
            pass

    def address_info(self, address):
        """

        :param address:
        :type address:
        :return:
        :rtype:
        """
        xml = self.generate_xml('ADDRESSVALIDATEREQUEST', address)

        self.send_request(xml, type='Verify')
        return

    def _generate_adressvalidaterequest_xml(self, address):
        """

        :param address:
        :type address:
        :return:
        :rtype:
        """

        if 'postalcode' in address.keys():
            postalcode = address['postalcode'].split('-')

            for code in postalcode:
                if len(code) == 4:
                    address['zip4'] = code
                elif len(code) == 5:
                    address['zip5'] = code


        addressmap = OrderedDict()
        addressmap['Address1'] = 'add1'
        addressmap['Address2'] = 'add2'
        addressmap['City'] = 'city'
        addressmap['State'] = 'state'
        addressmap['Zip5'] = 'zip5'
        addressmap['Zip4'] = 'zip4'

        xml = etree.Element('AddressValidateRequest', USERID=self.userid)
        add = etree.SubElement(xml, 'Address')

        for field in addressmap.keys():
            data = etree.SubElement(add, field)
            if addressmap[field] in address.keys():
                data.text = address[addressmap[field]]

        return xml