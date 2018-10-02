# swagger_client.BuildApi

All URIs are relative to *https://teamcity.ptsecurity.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tags**](BuildApi.md#add_tags) | **POST** /app/rest/builds/{buildLocator}/tags | 
[**cancel_build**](BuildApi.md#cancel_build) | **POST** /app/rest/builds/{buildLocator} | 
[**cancel_build_0**](BuildApi.md#cancel_build_0) | **GET** /app/rest/builds/{buildLocator}/example/buildCancelRequest | 
[**delete_build**](BuildApi.md#delete_build) | **DELETE** /app/rest/builds/{buildLocator} | 
[**delete_builds**](BuildApi.md#delete_builds) | **DELETE** /app/rest/builds | 
[**delete_comment**](BuildApi.md#delete_comment) | **DELETE** /app/rest/builds/{buildLocator}/comment | 
[**get_artifacts_directory**](BuildApi.md#get_artifacts_directory) | **GET** /app/rest/builds/{buildLocator}/artifactsDirectory | 
[**get_canceled_info**](BuildApi.md#get_canceled_info) | **GET** /app/rest/builds/{buildLocator}/canceledInfo | 
[**get_children**](BuildApi.md#get_children) | **GET** /app/rest/builds/{buildLocator}/artifacts/children{path} | 
[**get_children_alias**](BuildApi.md#get_children_alias) | **GET** /app/rest/builds/{buildLocator}/artifacts/{path} | 
[**get_content**](BuildApi.md#get_content) | **GET** /app/rest/builds/{buildLocator}/artifacts/content{path} | 
[**get_content_alias**](BuildApi.md#get_content_alias) | **GET** /app/rest/builds/{buildLocator}/artifacts/files{path} | 
[**get_metadata**](BuildApi.md#get_metadata) | **GET** /app/rest/builds/{buildLocator}/artifacts/metadata{path} | 
[**get_parameter**](BuildApi.md#get_parameter) | **GET** /app/rest/builds/{buildLocator}/resulting-properties/{propertyName} | 
[**get_pinned**](BuildApi.md#get_pinned) | **GET** /app/rest/builds/{buildLocator}/pin | 
[**get_problems**](BuildApi.md#get_problems) | **GET** /app/rest/builds/{buildLocator}/problemOccurrences | 
[**get_root**](BuildApi.md#get_root) | **GET** /app/rest/builds/{buildLocator}/artifacts | 
[**get_tests**](BuildApi.md#get_tests) | **GET** /app/rest/builds/{buildLocator}/testOccurrences | 
[**get_zipped**](BuildApi.md#get_zipped) | **GET** /app/rest/builds/{buildLocator}/artifacts/archived{path} | 
[**pin_build**](BuildApi.md#pin_build) | **PUT** /app/rest/builds/{buildLocator}/pin | 
[**replace_comment**](BuildApi.md#replace_comment) | **PUT** /app/rest/builds/{buildLocator}/comment | 
[**replace_tags**](BuildApi.md#replace_tags) | **PUT** /app/rest/builds/{buildLocator}/tags | 
[**serve_aggregated_build_status**](BuildApi.md#serve_aggregated_build_status) | **GET** /app/rest/builds/aggregated/{buildLocator}/status | 
[**serve_aggregated_build_status_icon**](BuildApi.md#serve_aggregated_build_status_icon) | **GET** /app/rest/builds/aggregated/{buildLocator}/statusIcon{suffix} | 
[**serve_all_builds**](BuildApi.md#serve_all_builds) | **GET** /app/rest/builds | 
[**serve_build**](BuildApi.md#serve_build) | **GET** /app/rest/builds/{buildLocator} | 
[**serve_build_actual_parameters**](BuildApi.md#serve_build_actual_parameters) | **GET** /app/rest/builds/{buildLocator}/resulting-properties | 
[**serve_build_field_by_build_only**](BuildApi.md#serve_build_field_by_build_only) | **GET** /app/rest/builds/{buildLocator}/{field} | 
[**serve_build_related_issues**](BuildApi.md#serve_build_related_issues) | **GET** /app/rest/builds/{buildLocator}/relatedIssues | 
[**serve_build_related_issues_old**](BuildApi.md#serve_build_related_issues_old) | **GET** /app/rest/builds/{buildLocator}/related-issues | 
[**serve_build_statistic_value**](BuildApi.md#serve_build_statistic_value) | **GET** /app/rest/builds/{buildLocator}/statistics/{name} | 
[**serve_build_statistic_values**](BuildApi.md#serve_build_statistic_values) | **GET** /app/rest/builds/{buildLocator}/statistics | 
[**serve_build_status_icon**](BuildApi.md#serve_build_status_icon) | **GET** /app/rest/builds/{buildLocator}/statusIcon{suffix} | 
[**serve_source_file**](BuildApi.md#serve_source_file) | **GET** /app/rest/builds/{buildLocator}/sources/files/{fileName} | 
[**serve_tags**](BuildApi.md#serve_tags) | **GET** /app/rest/builds/{buildLocator}/tags | 
[**unpin_build**](BuildApi.md#unpin_build) | **DELETE** /app/rest/builds/{buildLocator}/pin | 


# **add_tags**
> Tags add_tags(build_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
body = swagger_client.Tags() # Tags |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.add_tags(build_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->add_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **body** | [**Tags**](Tags.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Tags**](Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_build**
> Build cancel_build(build_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
body = swagger_client.BuildCancelRequest() # BuildCancelRequest |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.cancel_build(build_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->cancel_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **body** | [**BuildCancelRequest**](BuildCancelRequest.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_build_0**
> BuildCancelRequest cancel_build_0(build_locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 

try:
    api_response = api_instance.cancel_build_0(build_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->cancel_build_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 

### Return type

[**BuildCancelRequest**](BuildCancelRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build**
> delete_build(build_locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 

try:
    api_instance.delete_build(build_locator)
except ApiException as e:
    print("Exception when calling BuildApi->delete_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_builds**
> delete_builds(locator=locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
locator = 'locator_example' # str |  (optional)

try:
    api_instance.delete_builds(locator=locator)
except ApiException as e:
    print("Exception when calling BuildApi->delete_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(build_locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 

try:
    api_instance.delete_comment(build_locator)
except ApiException as e:
    print("Exception when calling BuildApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifacts_directory**
> str get_artifacts_directory(build_locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 

try:
    api_response = api_instance.get_artifacts_directory(build_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_artifacts_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canceled_info**
> Comment get_canceled_info(build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_canceled_info(build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_canceled_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children**
> Files get_children(path, build_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
path = 'path_example' # str | 
build_locator = 'build_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)
log_build_usage = true # bool |  (optional)

try:
    api_response = api_instance.get_children(path, build_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **build_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 
 **log_build_usage** | **bool**|  | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children_alias**
> Files get_children_alias(path, build_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
path = 'path_example' # str | 
build_locator = 'build_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)
log_build_usage = true # bool |  (optional)

try:
    api_response = api_instance.get_children_alias(path, build_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_children_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **build_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 
 **log_build_usage** | **bool**|  | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content**
> get_content(path, build_locator, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
path = 'path_example' # str | 
build_locator = 'build_locator_example' # str | 
resolve_parameters = true # bool |  (optional)
log_build_usage = true # bool |  (optional)

try:
    api_instance.get_content(path, build_locator, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)
except ApiException as e:
    print("Exception when calling BuildApi->get_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **build_locator** | **str**|  | 
 **resolve_parameters** | **bool**|  | [optional] 
 **log_build_usage** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_alias**
> get_content_alias(path, build_locator, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
path = 'path_example' # str | 
build_locator = 'build_locator_example' # str | 
resolve_parameters = true # bool |  (optional)
log_build_usage = true # bool |  (optional)

try:
    api_instance.get_content_alias(path, build_locator, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)
except ApiException as e:
    print("Exception when calling BuildApi->get_content_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **build_locator** | **str**|  | 
 **resolve_parameters** | **bool**|  | [optional] 
 **log_build_usage** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> file get_metadata(path, build_locator, fields=fields, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
path = 'path_example' # str | 
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)
log_build_usage = true # bool |  (optional)

try:
    api_response = api_instance.get_metadata(path, build_locator, fields=fields, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 
 **log_build_usage** | **bool**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter**
> str get_parameter(build_locator, property_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
property_name = 'property_name_example' # str | 

try:
    api_response = api_instance.get_parameter(build_locator, property_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **property_name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pinned**
> str get_pinned(build_locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 

try:
    api_response = api_instance.get_pinned(build_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_pinned: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_problems**
> ProblemOccurrences get_problems(build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_problems(build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_problems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**ProblemOccurrences**](ProblemOccurrences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root**
> Files get_root(build_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)
log_build_usage = true # bool |  (optional)

try:
    api_response = api_instance.get_root(build_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 
 **log_build_usage** | **bool**|  | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tests**
> TestOccurrences get_tests(build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_tests(build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**TestOccurrences**](TestOccurrences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zipped**
> get_zipped(path, build_locator, base_path=base_path, locator=locator, name=name, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
path = 'path_example' # str | 
build_locator = 'build_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
name = 'name_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)
log_build_usage = true # bool |  (optional)

try:
    api_instance.get_zipped(path, build_locator, base_path=base_path, locator=locator, name=name, resolve_parameters=resolve_parameters, log_build_usage=log_build_usage)
except ApiException as e:
    print("Exception when calling BuildApi->get_zipped: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **build_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 
 **log_build_usage** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_build**
> pin_build(build_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_instance.pin_build(build_locator, body=body)
except ApiException as e:
    print("Exception when calling BuildApi->pin_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_comment**
> replace_comment(build_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_instance.replace_comment(build_locator, body=body)
except ApiException as e:
    print("Exception when calling BuildApi->replace_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_tags**
> Tags replace_tags(build_locator, locator=locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
body = swagger_client.Tags() # Tags |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.replace_tags(build_locator, locator=locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->replace_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **locator** | **str**|  | [optional] 
 **body** | [**Tags**](Tags.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Tags**](Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_aggregated_build_status**
> str serve_aggregated_build_status(build_locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 

try:
    api_response = api_instance.serve_aggregated_build_status(build_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_aggregated_build_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_aggregated_build_status_icon**
> serve_aggregated_build_status_icon(build_locator, suffix)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
suffix = 'suffix_example' # str | 

try:
    api_instance.serve_aggregated_build_status_icon(build_locator, suffix)
except ApiException as e:
    print("Exception when calling BuildApi->serve_aggregated_build_status_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **suffix** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_all_builds**
> Builds serve_all_builds(build_type=build_type, status=status, triggered_by_user=triggered_by_user, include_personal=include_personal, include_canceled=include_canceled, only_pinned=only_pinned, tag=tag, agent_name=agent_name, since_build=since_build, since_date=since_date, start=start, count=count, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_type = 'build_type_example' # str |  (optional)
status = 'status_example' # str |  (optional)
triggered_by_user = 'triggered_by_user_example' # str |  (optional)
include_personal = true # bool |  (optional)
include_canceled = true # bool |  (optional)
only_pinned = true # bool |  (optional)
tag = ['tag_example'] # list[str] |  (optional)
agent_name = 'agent_name_example' # str |  (optional)
since_build = 'since_build_example' # str |  (optional)
since_date = 'since_date_example' # str |  (optional)
start = 789 # int |  (optional)
count = 56 # int |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_all_builds(build_type=build_type, status=status, triggered_by_user=triggered_by_user, include_personal=include_personal, include_canceled=include_canceled, only_pinned=only_pinned, tag=tag, agent_name=agent_name, since_build=since_build, since_date=since_date, start=start, count=count, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_all_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_type** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **triggered_by_user** | **str**|  | [optional] 
 **include_personal** | **bool**|  | [optional] 
 **include_canceled** | **bool**|  | [optional] 
 **only_pinned** | **bool**|  | [optional] 
 **tag** | [**list[str]**](str.md)|  | [optional] 
 **agent_name** | **str**|  | [optional] 
 **since_build** | **str**|  | [optional] 
 **since_date** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
 **count** | **int**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Builds**](Builds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build**
> Build serve_build(build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build(build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_actual_parameters**
> Properties serve_build_actual_parameters(build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_actual_parameters(build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_build_actual_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_field_by_build_only**
> str serve_build_field_by_build_only(build_locator, field)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_build_field_by_build_only(build_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_build_field_by_build_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **serve_build_related_issues**
> IssuesUsages serve_build_related_issues(build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_related_issues(build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_build_related_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**IssuesUsages**](IssuesUsages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_related_issues_old**
> IssuesUsages serve_build_related_issues_old(build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_related_issues_old(build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_build_related_issues_old: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**IssuesUsages**](IssuesUsages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_statistic_value**
> str serve_build_statistic_value(build_locator, name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
name = 'name_example' # str | 

try:
    api_response = api_instance.serve_build_statistic_value(build_locator, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_build_statistic_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_statistic_values**
> Properties serve_build_statistic_values(build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_statistic_values(build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_build_statistic_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_status_icon**
> serve_build_status_icon(build_locator, suffix)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
suffix = 'suffix_example' # str | 

try:
    api_instance.serve_build_status_icon(build_locator, suffix)
except ApiException as e:
    print("Exception when calling BuildApi->serve_build_status_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **suffix** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_source_file**
> serve_source_file(build_locator, file_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
file_name = 'file_name_example' # str | 

try:
    api_instance.serve_source_file(build_locator, file_name)
except ApiException as e:
    print("Exception when calling BuildApi->serve_source_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **file_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_tags**
> Tags serve_tags(build_locator, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_tags(build_locator, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->serve_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Tags**](Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpin_build**
> unpin_build(build_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BuildApi()
build_locator = 'build_locator_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_instance.unpin_build(build_locator, body=body)
except ApiException as e:
    print("Exception when calling BuildApi->unpin_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

