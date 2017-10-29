# AvailabilityRQ

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**echo_token** | **str** |  | [optional] 
**stay** | [**ApiStay**](ApiStay.md) | Booking length of stay element | 
**geolocation** | [**ApiGeoLocation**](ApiGeoLocation.md) |  | [optional] 
**destination** | [**ApiDestination**](ApiDestination.md) |  | [optional] 
**filter** | [**ApiFilter**](ApiFilter.md) |  | [optional] 
**boards** | [**ApiBoards**](ApiBoards.md) |  | [optional] 
**rooms** | [**ApiRooms**](ApiRooms.md) |  | [optional] 
**daily_rate** | **bool** | Displays daily price breakdown | [optional] [default to False]
**source_market** | **str** |  | [optional] 
**source** | [**ApiSource**](ApiSource.md) |  | [optional] 
**aif_use** | **bool** |  | [optional] [default to False]
**platform** | **int** |  | [optional] 
**language** | **str** |  | [optional] 
**occupancy** | [**list[ApiOccupancy]**](ApiOccupancy.md) |  | [optional] 
**keywords** | [**ApiKeywordsFilter**](ApiKeywordsFilter.md) |  | [optional] 
**hotels** | [**ApiHotelsFilter**](ApiHotelsFilter.md) |  | [optional] 
**review** | [**list[ApiReviewFilter]**](ApiReviewFilter.md) |  | [optional] 
**accommodation** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


