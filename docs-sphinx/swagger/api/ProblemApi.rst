dohq_teamcity.ProblemApi
######################################

`API examples <../../teamcity_apis/ProblemApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `get_problems`__
     - **GET** ``/app/rest/problems``
   * - `serve_instance`__
     - **GET** ``/app/rest/problems/{problemLocator}``

get_problems
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.problem_api.get_problems(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProblemApi->get_problems: %s\n" % e)



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
    [**Problems**](../models/Problems.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_instance
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        problem_locator = 'problem_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.problem_api.serve_instance(problem_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProblemApi->serve_instance: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **problem_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**Problem**](../models/Problem.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



OLD
-------

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_problems**](ProblemApi.md#get_problems) | **GET** /app/rest/problems | 
[**serve_instance**](ProblemApi.md#serve_instance) | **GET** /app/rest/problems/{problemLocator} | 


# **get_problems**
> Problems get_problems(locator=locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.problem_api.get_problems(locator=locator, fields=fields)
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

[**Problems**](../models/Problems.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_instance**
> Problem serve_instance(problem_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

problem_locator = 'problem_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.problem_api.serve_instance(problem_locator, fields=fields)
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

[**Problem**](../models/Problem.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


