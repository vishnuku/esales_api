# coding=utf-8
import requests
from lxml import etree
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
        print resposne

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
        self._response_parser(r.text)

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
        return xml

    def _generate_adressvalidaterequest_xml(self, address):
        """

        :param address:
        :type address:
        :return:
        :rtype:
        """
        addresskeymap = {}
        addresskeymap['city'] = 'City'
        addresskeymap['add1'] = 'Address1'
        addresskeymap['add2'] = 'Address2'
        addresskeymap['State'] = 'state'

        xml = etree.Element('AddressValidateRequest', USERID=self.userid)
        add = etree.SubElement(xml, 'Address', ID="0")

        for field in address.keys():
            if field in addresskeymap:
                data = etree.SubElement(add, addresskeymap[field])
                data.text = address[field]
            # elif field == 'postalcode':
            #     zipcode = address[field].split('-')
            #     for zip in zipcode:
            #         if len(zip) == 4:
            #             data = etree.SubElement(add, 'Zip4')
            #             data.text = zip
            #         else:
            #             data = etree.SubElement(add, 'Zip5')
            #             data.text = zip

        return xml