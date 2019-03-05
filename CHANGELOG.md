# Change Log

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this 
project adheres to [Semantic Versioning](http://semver.org/).

## [0.2.1] - 2019-03-05
### Changed
- Switch to use PyCryptodome instead of PyCrypto
- Update tests

## [0.2.0] - 2019-03-05
### Added
- `POT_PUBLIC_KEY`, `PRIVATE_KEY` and `PUBLIC_KEY` environment variables
- Support for signing the response payload
- Validation of headers and signatures
- Add utils.generate_signed_data() and utils.validate_signed_data()
Replaces the generate/validate signature functions.

### Changed
- Move utils to app.utils
- Pipfile with necessary modules, version locking
- X-Pot-App header is now required
- Update API RAML specification
- Update README
- Update CHANGELOG
- Update tests

### Removed
- Shared secret settings
- utils.generate_signature() and utils.validate_signature()

## [0.1.0] - 2018-11-23
### Added
- Skeleton code for Platform of Trust translator
- Tests
- RAML API specification

[Unreleased]: https://github.com/PlatformOfTrust/translator-skeleton-python/compare/0.2.1...HEAD
[0.2.1]: https://github.com/PlatformOfTrust/translator-skeleton-python/tree/0.2.0...0.2.1
[0.2.0]: https://github.com/PlatformOfTrust/translator-skeleton-python/tree/0.1.0...0.2.0
[0.1.0]: https://github.com/PlatformOfTrust/translator-skeleton-python/tree/0.1.0