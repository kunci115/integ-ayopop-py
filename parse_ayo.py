def inq_serializer(data):
    decoder = data.decode()
    mapp = {'no_hp': decoder[41:53],
            'product_code': decoder[61:67]}
    return mapp


def payment_serializer(data):
    decoder = data.decode()
    mapp = {'no_hp': decoder[41:53],
            'product_code': decoder[61:67],
            'inquiryId': decoder[81:87],
            'amount': decoder[91:107],
            'refNumber': decoder[107:157]}
    return mapp


def status_serializer(data):
    decoder = data.decode()
    mapp = {'refNumber': decoder[41:91]}
    return mapp