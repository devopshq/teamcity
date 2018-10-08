# teamcity.TestApi

All URIs are relative to *https://teamcity.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tests**](TestApi.md#get_tests) | **GET** /app/rest/tests | 
[**serve_instance**](TestApi.md#serve_instance) | **GET** /app/rest/tests/{testLocator} | 


# **get_tests**
> Tests get_tests(locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.TestApi()
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_tests(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestApi->get_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Tests**](Tests.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_instance**
> Test serve_instance(test_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.TestApi()
test_locator = 'test_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_instance(test_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestApi->serve_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Test**](Test.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

