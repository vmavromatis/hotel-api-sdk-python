# bookingapi.StatusApi

All URIs are relative to *https://api.test.hotelbeds.com/hotel-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status**](StatusApi.md#status) | **GET** /{version}/status | Check API status


# **status**
> StatusRS status(version)

Check API status

Returns the status of the API

### Example 
```python
from __future__ import print_function
import time
import bookingapi
from bookingapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bookingapi.StatusApi()
version = 'version_example' # str | Default version for this operation

try: 
    # Check API status
    api_response = api_instance.status(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Default version for this operation | 

### Return type

[**StatusRS**](StatusRS.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

