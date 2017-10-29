# bookingapi.HotelsApi

All URIs are relative to *https://api.test.hotelbeds.com/hotel-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availability**](HotelsApi.md#availability) | **POST** /{version}/hotels | Hotel availability


# **availability**
> AvailabilityRS availability(version, body)

Hotel availability

This method is used to request room availability. Some filters and special features can be applied before sending an availability request.   A flexible date search allows customers to retrieve available rates for a specified number of days prior to and post check-in.  The response generated is a list of hotels with the different room types, board types, and rates available for those hotels; but not only restricted to the dates selected.  BookingAPI prices are final. Our rates include supplements and discounts and no additional price calculations are required.  It can also return cancellation fees in the availability response, providing amounts and dates at the first step of the booking.

### Example 
```python
from __future__ import print_function
import time
import bookingapi
from bookingapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bookingapi.HotelsApi()
version = 'version_example' # str | Default version for this operation
body = bookingapi.AvailabilityRQ() # AvailabilityRQ | Request body

try: 
    # Hotel availability
    api_response = api_instance.availability(version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HotelsApi->availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Default version for this operation | 
 **body** | [**AvailabilityRQ**](AvailabilityRQ.md)| Request body | 

### Return type

[**AvailabilityRS**](AvailabilityRS.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

