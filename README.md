# Platform of Trust translator

[![Build Status](https://travis-ci.org/PlatformOfTrust/translator-skeleton-python.svg?branch=master)](https://travis-ci.org/PlatformOfTrust/translator-skeleton-python)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A Platform Of Trust translator standardizes the responses from a data 
source to the Platform itself. The translator also adds security measures,
such as signature verification and signing the response.

The Python skeleton is built with [Python Bottle](https://bottlepy.org/docs/0.12/)

You can use this skeleton to build your own translators.

## Implementing a translator

In `settings.py` there's the `SHARED_SECRET` that you have to set. The shared 
secret is shown once, when the data product is created in the Platform Of Trust
Product API.

Make sure you implement the `services.get_data()` function that handles
the getting of the actual data to return to the Data Broker API.

You should also update the unit tests in the `app/tests` to match your changes.

Make sure you update the `@request_args()`-decorator for the `parameter`-field if you
require any additional parameters. For now, the `parameters.name` is required.

## License

MIT, see [LICENSE](LICENSE).