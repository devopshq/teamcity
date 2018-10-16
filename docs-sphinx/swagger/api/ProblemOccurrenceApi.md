# dohq_teamcity.ProblemOccurrenceApi

[[API examples]](http://devopshq.github.io/teamcity/teamcity_apis/ProblemOccurrenceApi.html)

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_problems**](ProblemOccurrenceApi.md#get_problems) | **GET** /app/rest/problemOccurrences | 
[**serve_instance**](ProblemOccurrenceApi.md#serve_instance) | **GET** /app/rest/problemOccurrences/{problemLocator} | 


# **get_problems**
> ProblemOccurrences get_problems(locator=locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.problem_occurrence_api.get_problems(locator=locator, fields=fields)
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
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

problem_locator = 'problem_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.problem_occurrence_api.serve_instance(problem_locator, fields=fields)
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


