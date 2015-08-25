from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from inventory.models import Product_Inventory, ProductOrder
import math

class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")
        print 'self.content_types',self.content_types
        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):        
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
        print 'Clean method'
        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                print content_type
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_('Filetype not supported.'))
        except AttributeError:
            pass        
            
        return data


class HashCode():

    def generate_hash_code(self, amazonordersid):

        product_order = ProductOrder.objects.filter(amazonorders=amazonordersid)
        qty = 0
        product_id = 0
        data = []
        length = product_order.__len__() if int(product_order.__len__()) > 1 else 2
        for product in product_order:
            qty += int(product.quantityordered) if int(product.quantityordered) > 1 else 2
            product_id += int(product.product.id) if int(product.product.id) > 1 else 2

        qty = int(math.pow(qty, length))
        product_id = int(math.pow(product_id, length))
        hashcode = qty * product_id * length
        data.append({'qty': qty, 'product_id': product_id, 'hashcode': hashcode, 'length': length})
        return data
