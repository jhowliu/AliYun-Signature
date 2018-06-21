from urllib.parse import quote, urlencode

import hmac
import base64
import hashlib

class AliYunSign(object):

    @staticmethod
    def encoding(qs):
        qs = quote(qs) # escape encoding
        qs = qs.replace('+', '%20')\
               .replace('*', '%2A')\
               .replace('%7E', '~')

        return qs

    @staticmethod
    def sign(params, secret_key, method):
        qs = urlencode(params)
        qs = AliYunSign.encoding(qs)

        key = secret_key + '&'
        msg = method + '&%2F&' + qs

        h = hmac.new(key.encode('utf8'), msg.encode('utf8'), hashlib.sha1)

        raw_signature = h.digest()

        return AliYunSign.encoding(base64.urlsafe_b64encode(raw_signature).decode('utf8'))
