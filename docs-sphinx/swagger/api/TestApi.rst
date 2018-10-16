dohq_teamcity.TestApi
######################################

`API examples <../../teamcity_apis/TestApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `get_tests`__
     - **GET** ``/app/rest/tests``
   * - `serve_instance`__
     - **GET** ``/app/rest/tests/{testLocator}``

get_tests
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.test_api.get_tests(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestApi->get_tests: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**Tests**](../models/Tests.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_instance
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        test_locator = 'test_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.test_api.serve_instance(test_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestApi->serve_instance: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **test_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**Test**](../models/Test.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



OLD
-------

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tests**](TestApi.md#get_tests) | **GET** /app/rest/tests | 
[**serve_instance**](TestApi.md#serve_instance) | **GET** /app/rest/tests/{testLocator} | 


# **get_tests**
> Tests get_tests(locator=locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.test_api.get_tests(locator=locator, fields=fields)
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

[**Tests**](../models/Tests.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_instance**
> Test serve_instance(test_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

test_locator = 'test_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.test_api.serve_instance(test_locator, fields=fields)
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

[**Test**](../models/Test.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


