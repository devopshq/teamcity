# swagger_client.ProblemOccurrenceApi

All URIs are relative to *https://teamcity.ptsecurity.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_problems**](ProblemOccurrenceApi.md#get_problems) | **GET** /app/rest/problemOccurrences | 
[**serve_instance**](ProblemOccurrenceApi.md#serve_instance) | **GET** /app/rest/problemOccurrences/{problemLocator} | 


# **get_problems**
> ProblemOccurrences get_problems(locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProblemOccurrenceApi()
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_problems(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemOccurrenceApi->get_problems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**ProblemOccurrences**](ProblemOccurrences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_instance**
> ProblemOccurrence serve_instance(problem_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProblemOccurrenceApi()
problem_locator = 'problem_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_instance(problem_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemOccurrenceApi->serve_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**ProblemOccurrence**](ProblemOccurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

