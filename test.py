from aliyunSign import AliYunSign

import unittest
import uuid
import time

class AliYunSignTest(unittest.TestCase):

    def test_sign(self):
        # you have to sort params first
        params = {
            'AccessKeyId': 'ACCESS_ID',
            'Action': 'DescribeScalingGroups', # which api you want to call
            'Format': 'JSON', # response format, default is XML
            'RegionId': 'ap-southeast-1', # where your server host
            'SignatureMethod': 'HMAC-SHA1', # constant
            'SignatureNonce': '1529549187', # You can use uuid() or timestamp
            'SignatureVersion': '1.0', # constant
            'Timestamp': '2018-06-21T10:20:00Z', # YY-mm-ddTHH:MM:SSZ
            'Version': '2014-08-28', # constant
        }

        signature = AliYunSign.sign(params, 'ACCESS_SECRET', 'GET')
        self.assertEqual(signature, 'CqEqUQ6ky2rvTXdv_VRM8YVX3Kk%3D')

if __name__ == '__main__':
    unittest.main()