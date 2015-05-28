# coding=utf-8
import requests
from shipping import Shipping
from lxml import etree
from lxml import objectify
from collections import OrderedDict
from shipping.errors import MissingParameter

class Usps(Shipping):
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
        self.userid = kwargs.get('userid', None)
        self.apikey = kwargs.get('apikey', None)
        self.url = 'http://production.shippingapis.com/ShippingAPITest.dll?API={}'
        self.type = 0
        self.services = None

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
            return etree.tostring(self._generate_adressvalidate_request_xml(data))
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

    def _generate_adressvalidate_request_xml(self, address):
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

    def _generate_zipcode_lookup_request_xml(self, address):
        """

        :param address:
        :type address:
        :return:
        :rtype:
        """

        if 'firmname' not in address.keys():
            raise MissingParameter('firmname is missing')

        addressmap = OrderedDict()
        addressmap['FirmName'] = 'firmname'
        addressmap['Address1'] = 'add1'
        addressmap['Address2'] = 'add2'
        addressmap['City'] = 'city'
        addressmap['State'] = 'state'

        xml = etree.Element('ZipCodeLookupRequest', USERID=self.userid)
        add = etree.SubElement(xml, 'Address')

        for field in addressmap.keys():
            data = etree.SubElement(add, field)
            if addressmap[field] in address.keys():
                data.text = address[addressmap[field]]

        return xml

    def _generate_citystate_lookup_request_xml(self, address):
        """

        :param address:
        :type address:
        :return:
        :rtype:
        """

        addressmap = OrderedDict()
        addressmap['Zip5'] = 'zip5'

        xml = etree.Element('CityStateLookupRequest', USERID=self.userid)
        add = etree.SubElement(xml, 'Address')

        for field in addressmap.keys():
            data = etree.SubElement(add, field)
            if addressmap[field] in address.keys():
                data.text = address[addressmap[field]]

        return xml

    def _generate_evs_request_xml(self, address):
        """

        :param address:
        :type address:
        :return:
        :rtype:
        """

        addressmap = OrderedDict()
        addressmap['Option'] = 'option'
        addressmap['Revision'] = 'revision'
        addressmap['ImageParameters'] = 'Imageparameters'
        addressmap['FromName'] = 'fromname'
        addressmap['FromFirm'] = ''
        addressmap['FromAddress1'] = ''
        addressmap['FromCity'] = ''
        addressmap['FromState'] = ''
        addressmap['FromZip5'] = ''
        addressmap['FromZip4'] = ''
        addressmap['FromPhone'] = ''
        addressmap['ToName'] = ''
        addressmap['ToFirm'] = ''
        addressmap['ToAddress1'] = ''
        addressmap['ToAddress2'] = ''
        addressmap['ToCity'] = ''
        addressmap['ToZip5'] = ''
        addressmap['ToZip4'] = ''
        addressmap['ToPhone'] = ''
        addressmap['WeightInOunces'] = ''
        addressmap['ServiceType'] = ''
        addressmap['Container'] = ''
        addressmap['PriceOptions'] = ''
        addressmap['InsuredAmount'] = ''

        addressmap['ExpressMailOptions'] = 'multi'
        addressmap['DeliveryOption'] = 'multi'
        addressmap['WaiverOfSignature'] = 'multi'

        addressmap['ShipDate'] = ''
        addressmap['CustomerRefNo'] = ''
        addressmap['ReceiptOption'] = ''
        addressmap['ImageType'] = ''
        addressmap['HoldForManifest'] = ''
        addressmap['NineDigitRoutingZip'] = ''
        addressmap['ShipInfo'] = ''
        addressmap['CarrierRelease'] = ''
        addressmap['DropOffTime'] = ''
        addressmap['ReturnCommitments'] = ''
        addressmap['PrintCustomerRefNo'] = ''

        addressmap['Content'] = 'multi'
        addressmap['ContentType'] = 'multi'
        addressmap['ContentDescription'] = 'multi'

        addressmap['ContentDescription'] = ''

        xml = etree.Element('eVSCertifyRequest', USERID=self.userid)
        add = etree.SubElement(xml, 'Address')

        for field in addressmap.keys():
            data = etree.SubElement(add, field)
            if addressmap[field] in address.keys():
                data.text = address[addressmap[field]]

        return xml