# dohq_teamcity.DefaultApi

All URIs are relative to *https://teamcity.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serve_api_version**](DefaultApi.md#serve_api_version) | **GET** /app/rest/apiVersion | 
[**serve_build_field_short**](DefaultApi.md#serve_build_field_short) | **GET** /app/rest/{projectLocator}/{btLocator}/{buildLocator}/{field} | 
[**serve_plugin_info**](DefaultApi.md#serve_plugin_info) | **GET** /app/rest/info | 
[**serve_root**](DefaultApi.md#serve_root) | **GET** /app/rest | 
[**serve_version**](DefaultApi.md#serve_version) | **GET** /app/rest/version | 


# **serve_api_version**
> str serve_api_version()



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.DefaultApi()

try:
    api_response = api_instance.serve_api_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->serve_api_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_field_short**
> str serve_build_field_short(project_locator, bt_locator, build_locator, field)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.DefaultApi()
project_locator = 'project_locator_example' # str | 
bt_locator = 'bt_locator_example' # str | 
build_locator = 'build_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_build_field_short(project_locator, bt_locator, build_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->serve_build_field_short: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **bt_locator** | **str**|  | 
 **build_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_plugin_info**
> Plugin serve_plugin_info(fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.DefaultApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_plugin_info(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->serve_plugin_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_root**
> str serve_root()



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.DefaultApi()

try:
    api_response = api_instance.serve_root()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->serve_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_version**
> str serve_version()



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.DefaultApi()

try:
    api_response = api_instance.serve_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->serve_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

