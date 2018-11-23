# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestTranslatorController::testFetch 1'] = {
}

snapshots['TestTranslatorController::testMissingAttribute 1'] = {
    'error': {
        'message': {
            'productCode': [
                'Missing data for required field.'
            ]
        },
        'status': 422
    }
}
