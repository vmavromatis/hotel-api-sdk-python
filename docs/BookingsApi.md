# bookingapi.BookingsApi

All URIs are relative to *https://api.test.hotelbeds.com/hotel-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**booking**](BookingsApi.md#booking) | **POST** /{version}/bookings | Booking confirm
[**booking_cancellation**](BookingsApi.md#booking_cancellation) | **DELETE** /{version}/bookings/{bookingId} | Booking cancellation
[**booking_change**](BookingsApi.md#booking_change) | **PUT** /{version}/bookings/{bookingId} | Booking change
[**booking_detail**](BookingsApi.md#booking_detail) | **GET** /{version}/bookings/{bookingId} | Booking detail


# **booking**
> BookingRS booking(version, body)

Booking confirm

The booking confirmation operation confirms the rate keys selected.

### Example 
```python
from __future__ import print_function
import time
import bookingapi
from bookingapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bookingapi.BookingsApi()
version = 'version_example' # str | Default version for this operation
body = bookingapi.BookingRQ() # BookingRQ | 

try: 
    # Booking confirm
    api_response = api_instance.booking(version, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingsApi->booking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Default version for this operation | 
 **body** | [**BookingRQ**](BookingRQ.md)|  | 

### Return type

[**BookingRS**](BookingRS.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_cancellation**
> BookingCancellationRS booking_cancellation(version, booking_id, cancellation_flag=cancellation_flag, language=language)

Booking cancellation

The BookingCancellation operation cancels a booking or simulates a booking cancellation.

### Example 
```python
from __future__ import print_function
import time
import bookingapi
from bookingapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bookingapi.BookingsApi()
version = 'version_example' # str | Default version for this operation
booking_id = 'booking_id_example' # str | 
cancellation_flag = 'cancellation_flag_example' # str |  (optional)
language = 'language_example' # str |  (optional)

try: 
    # Booking cancellation
    api_response = api_instance.booking_cancellation(version, booking_id, cancellation_flag=cancellation_flag, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingsApi->booking_cancellation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Default version for this operation | 
 **booking_id** | **str**|  | 
 **cancellation_flag** | **str**|  | [optional] 
 **language** | **str**|  | [optional] 

### Return type

[**BookingCancellationRS**](BookingCancellationRS.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_change**
> BookingChangeRS booking_change(version, booking_id, body)

Booking change

The BookingChange operation can be used to change (or simulate) different values of a booking or to partially cancel a booking (i.e: cancel a room of a two room reservation).

### Example 
```python
from __future__ import print_function
import time
import bookingapi
from bookingapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bookingapi.BookingsApi()
version = 'version_example' # str | Default version for this operation
booking_id = 'booking_id_example' # str | 
body = bookingapi.BookingChangeRQ() # BookingChangeRQ | 

try: 
    # Booking change
    api_response = api_instance.booking_change(version, booking_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingsApi->booking_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Default version for this operation | 
 **booking_id** | **str**|  | 
 **body** | [**BookingChangeRQ**](BookingChangeRQ.md)|  | 

### Return type

[**BookingChangeRS**](BookingChangeRS.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_detail**
> BookingDetailRS booking_detail(version, booking_id, language=language)

Booking detail

The BookingDetail operation retuns all the information of the requested booking.

### Example 
```python
from __future__ import print_function
import time
import bookingapi
from bookingapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bookingapi.BookingsApi()
version = 'version_example' # str | Default version for this operation
booking_id = 'booking_id_example' # str | 
language = 'language_example' # str |  (optional)

try: 
    # Booking detail
    api_response = api_instance.booking_detail(version, booking_id, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BookingsApi->booking_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Default version for this operation | 
 **booking_id** | **str**|  | 
 **language** | **str**|  | [optional] 

### Return type

[**BookingDetailRS**](BookingDetailRS.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

