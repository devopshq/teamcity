# dohq_teamcity.TestOccurrenceApi

[[API examples]](http://devopshq.github.io/teamcity/teamcity_apis/TestOccurrenceApi.html)

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_test_occurrences**](TestOccurrenceApi.md#get_test_occurrences) | **GET** /app/rest/testOccurrences | 
[**serve_instance**](TestOccurrenceApi.md#serve_instance) | **GET** /app/rest/testOccurrences/{testLocator} | 


# **get_test_occurrences**
> TestOccurrences get_test_occurrences(locator=locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.test_occurrence_api.get_test_occurrences(locator=locator, fields=fields)
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

[**TestOccurrences**](../models/TestOccurrences.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_instance**
> TestOccurrence serve_instance(test_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

test_locator = 'test_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.test_occurrence_api.serve_instance(test_locator, fields=fields)
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

[**TestOccurrence**](../models/TestOccurrence.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


