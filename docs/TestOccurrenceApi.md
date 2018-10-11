# dohq_teamcity.TestOccurrenceApi

All URIs are relative to *https://teamcity.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_test_occurrences**](TestOccurrenceApi.md#get_test_occurrences) | **GET** /app/rest/testOccurrences | 
[**serve_instance**](TestOccurrenceApi.md#serve_instance) | **GET** /app/rest/testOccurrences/{testLocator} | 


# **get_test_occurrences**
> TestOccurrences get_test_occurrences(locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.TestOccurrenceApi()
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_test_occurrences(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestOccurrenceApi->get_test_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**TestOccurrences**](TestOccurrences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_instance**
> TestOccurrence serve_instance(test_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.TestOccurrenceApi()
test_locator = 'test_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_instance(test_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestOccurrenceApi->serve_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**TestOccurrence**](TestOccurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

