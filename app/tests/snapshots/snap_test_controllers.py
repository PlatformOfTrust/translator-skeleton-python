# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestTranslatorController::test_fetch 1'] = {
    '@context': '',
    '@type': '',
    'data': {
    },
    'signature': {
        'created': '2019-03-01T08:31:26+00:00',
        'creator': '',
        'signatureValue': 'MuGwiD8Fwubij43YKo6+cpkajOtnNObJpe8pTF/hOyGdWY10IvNMRjtguSBn55VwqCe5K2uwzIg7kNp80YeVFYjJ3Tb7ZbSdjtLAthbUdIuVTYOR9gCUUHVY2wKrhz8HN+RrONIsqLYwk3o6+ebb1AXPmzyu4MCir491x1W+kaeM5gKFVUTDbB3j6rjlvFu3mvjgBPqyuOBE92dtfP30PZtU0OjZbkWotHKvtukU93cexqxdjTRzFfeLAqTQbQlBrGsxFV93+i2hyGCQ95jMkqHBvPS9Lgp4v84F4dSn5Jzytsl8khNZR3cUR3ZgblGE1/wRIykCKl5QOaOt6TCI/uqOgBey+jNMzQ5I4DqF9CR16JAjRfiA4IClYrUpFohrOS+Idl1kjL+Xga/q+HiFwZMrQb7xBblzm9jHIwo6DZro4UmPkPPQoq7fnuNnd1BBHDwMelKlUmmyIngh5KyaMrmvY/fkD2bo/n/l3kgJs1df5sk4k5DVfcghjspNMACY+KqKJ1NvP5hp8NOlQ8eFXBurXzhX4iS1kkHvNjzW2gDzlkaxrw9OvZQsh+CJRQk8Q89sY3ApIF3ygWgZxAQko4Oe1eLELTTUairTdYzpCIs8pEipEa6n9T+aFvGaGpyASkvXNN1XIp3F0bSRZhIj7ZZIGtdmy3ZcId0XeqrAKuY=',
        'type': ''
    }
}

snapshots['TestTranslatorController::test_missing_attribute 1'] = {
    'error': {
        'message': {
            'productCode': [
                'Missing data for required field.'
            ]
        },
        'status': 422
    }
}
