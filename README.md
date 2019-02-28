# Platform of Trust translator

[![Build Status](https://travis-ci.org/PlatformOfTrust/translator-skeleton-python.svg?branch=master)](https://travis-ci.org/PlatformOfTrust/translator-skeleton-python)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A Platform Of Trust translator standardizes the responses from a data 
source to the Platform itself. The translator also adds security measures,
such as signature verification and signing the response.

The Python skeleton is built with [Python Bottle](https://bottlepy.org/docs/0.12/)

You can use this skeleton to build your own translators.

## Requirements

You need the following installed on your computer:

- Python 3.6
- Pipenv (`pip install pipenv`)
- [Yarn](https://yarnpkg.com/lang/en/docs/install/) - For documentation

## Implementing a translator

Add the Platform Of Trust public key to the `settings.py` `POT_PUBLIC_KEY`
environment variable. This public key is used for validating the signature
header sent from the Platform Of Trust Data Broker API.

You need to create a private/public key pair to be used with the translator.
The public key URL MUST be added to the data product when creating it in the 
Platform Of Trust Product API. It is defined in the `organizationPublicKeys`
list:

    "organizationPublicKeys": [
        {
            "type": "RsaSignature2018",
            "url": "https://example.com/public-key.pub"
        }
    ]

See [Generating private and public keys](.#Generating-private-and-public-keys)

Now define the created keys in `settings.py` as the environment variables
`PRIVATE_KEY` and `PUBLIC_KEY` respectively. *IMPORTANT*: Do NOT commit the 
private key to the repository, but instead use e.g. encryption or docker
environment variables for it. 

Make sure you implement the `services.get_data()` function that handles
the getting of the actual data to return to the Data Broker API.

There are placeholders for some of the mandatory parameters in the skeleton code.
Make sure you implement the correct values for the response.

You should also update the unit tests in the `app/tests` to match your changes.

Make sure you update the `@request_args()`-decorator for the `parameter`-field if you
require any additional parameters. For now, the `parameters.name` is required.

# Tests

The tests for controllers are found under [app/tests/](app/tests).
Remember to update the tests when creating the translator.
There is an `invoke` task for running tests, run `pipenv run invoke test`.
Or run the command `ENV=test python -m pytest` to run the tests on the command
line.

# Generating private and public keys

To generate the PEM keys used for the signing of data:

    ssh-keygen -t rsa -b 4096 -m PEM -f RS256.key
    # Don't add passphrase
    openssl rsa -in RS256.key -pubout -outform PEM -out RS256.key.pub

Base64 encode the public and private keys
    
    cat RS256.key | base64
    cat RS256.key.pub | base64

## API documentation

The API uses [RAML](https://github.com/raml-org/raml-spec/blob/master/versions/raml-10/raml-10.md)
to document the API. To generate the documentation you need to install Yarn,
and run `pipenv run invoke docs`.

This will generate an `index.html`-file under `docs/`. Open the file in your 
browser to check that the documentation is in order.

The HTML API documentation for the skeleton can be found [here](https://platformoftrust.github.io/translator-skeleton-python/)

## Changes

Changes in the translator skeleton can be found in the [CHANGELOG](CHANGELOG.md).

## License

MIT, see [LICENSE](LICENSE).