import json
import jwt
from pip._vendor import requests
import parse_ayo


def encoding_jwt(payload_all):
    encoded_jwt = jwt.encode(payload_all, '0eN7R4uR1pxJvwJV7rAkfpQ5TTKCkanfhwN', algorithm='HS256')
    return encoded_jwt


def inquiry_req(data):
    mem = parse_ayo.inq_serializer(data)
    url = 'https://dev.openapi.ayopop.id/api/v1/bill/check'
    payload_inquiry = {
      "partnerId": "mGKm25W0454v",
      "accountNumber": mem['no_hp'],
      "productCode": mem['product_code']
    }
    encoded_jwt = encoding_jwt(payload_inquiry)
    headers = {
        'accept': 'application/json',
        'KEY': 'mGKm25W0454v',
        'TOKEN': encoded_jwt,
        'VERSION': '1.0',
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
    }
    r = requests.post(url, headers=headers)
    return r


def payment_req(data):
    mem = parse_ayo.payment_serializer(data)
    url = 'https://dev.openapi.ayopop.id/api/v1/bill/payment'
    payload_payment = {"partnerId": "mGKm25W0454v",
                       "accountNumber": mem['no_hp'],
                       "productCode": mem['product_code'],
                       "inquiryId": mem['inquiryId'],
                       "amount": mem['amount'],
                       "refNumber": mem['refNumber'],
                       "buyerDetails": {
                           "buyerEmail": "test@gmail.com",
                           "publicBuyerId": "1122457HG23"
                       },
                       "CallbackUrls": [
                           "https://webhook.site/c27733f0-f986-477b-9eb8-222b17f30b4b"
                       ]}

    encoded_jwt = encoding_jwt(payload_payment)
    headers = {
        'accept': 'application/json',
        'KEY': 'mGKm25W0454v',
        'TOKEN': encoded_jwt,
        'VERSION': '1.0',
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
    }
    r = requests.post(url, headers=headers)
    return r


def status_req(data):
    mem = parse_ayo.status_serializer(data)
    url = 'https://dev.openapi.ayopop.id/api/v1/bill/status'
    payload_status = {"partnerId": "mGKm25W0454v",
                      "refNumber": mem['refNumber'],
                       }
    encoded_jwt = encoding_jwt(payload_status)
    headers = {
        'accept': 'application/json',
        'KEY': 'mGKm25W0454v',
        'TOKEN': encoded_jwt,
        'VERSION': '1.0',
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
    }
    r = requests.post(url, headers=headers)
    return r


