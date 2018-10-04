# teamcity.InvestigationApi

All URIs are relative to *https://teamcity.ptsecurity.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_investigations**](InvestigationApi.md#get_investigations) | **GET** /app/rest/investigations | 
[**serve_instance**](InvestigationApi.md#serve_instance) | **GET** /app/rest/investigations/{investigationLocator} | 


# **get_investigations**
> Investigations get_investigations(locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.InvestigationApi()
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_investigations(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestigationApi->get_investigations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Investigations**](Investigations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_instance**
> Investigation serve_instance(investigation_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.InvestigationApi()
investigation_locator = 'investigation_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_instance(investigation_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvestigationApi->serve_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Investigation**](Investigation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

