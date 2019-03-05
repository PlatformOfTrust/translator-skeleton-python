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
        'signatureValue': 'FCL/Sef+pa5fDKId4k2IPrr+S9Mn+rFG6ub4fpb7zNo1+vAIaIp'
                          'KPPj2CIaBtcSCmi8qdKwKCEvjDF9VlZqqDqj+85kxWl90b9LFPu'
                          'FdAavrh0TD8rMDgBvBnDRElo8Y/C+D9ngfB032LATBRzqCjeaWO'
                          'gRUUZiBhwiC7RnnWVy7cYsu+FaFbCROZQd8tXz/NftmgmdHJFJs'
                          'tddI4L8yZUNk7D7a/7+iyCNriQ0vrZeN32YdtsUxQtQPIq3NVkB'
                          'yCDyUgd5/N3zl18cH3njzd9TGQvLWRCLETqY++BPfltUYb0ohB/'
                          'kcpB/ph9MocoV9tWNwLaQE4FSDUYHu9d0Gf8ncPAWoKBZ6ksnS5'
                          'x5071MHbGr9MDEGDyIsh6XcCLNWTf2aDtaP1EET+a5zeDnLvLxh'
                          'ee0wnXQE1/UCD0iQHkeOhu35DBYFAjlBQ4JSE1BEN5RAEQ7L1ZT'
                          'qn3Lk8BujO4x7L2qj3IkSDC77VtgteTvPrM9UaasAUlGzYpnGp7'
                          'Ixn33EaAyOQknn3Kb/aV6q4fpa3yjNZKCCiiEXo4VjadHPZkc1T'
                          'uLymneRJNe1GI4l12A/BwUG/u6swe2TF3ZTNETLmTug9U+5lyH4'
                          'UDUs4sIJwB5lQmjQKuW896FMwG9/bu72lIgUYyGMvcWqKNoqp4t'
                          'x/6YjyqCbrzCU+QGPNhI=',
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
