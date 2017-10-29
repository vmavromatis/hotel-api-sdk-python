# bookingapi.CheckratesApi

All URIs are relative to *https://api.test.hotelbeds.com/hotel-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_rate**](CheckratesApi.md#check_rate) | **POST** /{version}/checkrates | Check Availability Rates


# **check_rate**
> CheckRateRS check_rate(version, body)

Check Availability Rates

The checkrates method can complement the booking process, as it returns additional information to the availability request. However, when the rateType value is \"RECHECK\", the checkrates method is mandatory.  The rateType value \"RECHECK\" is returned for rates that do not have real-time availability. This is, that come from accommodation partners that update their products in our system periodically, with varying frequency depending on the supplier itself, the destination, hotels, etc.  The checkrates method response contains the same information provided in the availability response, but returns information only for a specific hotel and rate. The purpose of this method is double check availability and prices for any particular hotel/rate.  The prices obtained via this method are always up-to-date; along with some other information: rate breakdown, rate comments and upselling options.

### Example 
```python
from __future__ import print_function
import time
import bookingapi
from bookingapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bookingapi.CheckratesApi()
version = 'version_example' # str | Default version for this operation
body = bookingapi.CheckRateRQ() # CheckRateRQ | Request body

try: 
    # Check Availability Rates
    api_response = api_instance.check_rate(version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckratesApi->check_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Default version for this operation | 
 **body** | [**CheckRateRQ**](CheckRateRQ.md)| Request body | 

### Return type

[**CheckRateRS**](CheckRateRS.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

