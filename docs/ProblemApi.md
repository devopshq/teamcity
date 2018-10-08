# teamcity.ProblemApi

All URIs are relative to *https://teamcity.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_problems**](ProblemApi.md#get_problems) | **GET** /app/rest/problems | 
[**serve_instance**](ProblemApi.md#serve_instance) | **GET** /app/rest/problems/{problemLocator} | 


# **get_problems**
> Problems get_problems(locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.ProblemApi()
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_problems(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->get_problems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Problems**](Problems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_instance**
> Problem serve_instance(problem_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.ProblemApi()
problem_locator = 'problem_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_instance(problem_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProblemApi->serve_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **problem_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Problem**](Problem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

