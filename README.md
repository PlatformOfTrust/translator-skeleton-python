# Platform of Trust translator

A Platform Of Trust translator standardizes the responses from a data 
source to the Platform itself. The translator also adds security measures,
such as signature verification and signing the response.

The Python skeleton is built with [Python Bottle](https://bottlepy.org/docs/0.12/)

You can use this skeleton to build your own translators.

In `settings.py` there's the `SHARED_SECRET` that you have to set. The shared 
secret is shown once, when the data product is created in the Platform Of Trust
Product API.

Make sure you implement the `services.get_data()` function that handles
the fetching of the actual data to return to the Data Broker API.

You should also update the unit tests in the `app/tests` to match your changes.