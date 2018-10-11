# dohq_teamcity.VcsRootApi

All URIs are relative to *https://teamcity.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_root**](VcsRootApi.md#add_root) | **POST** /app/rest/vcs-roots | 
[**change_properties**](VcsRootApi.md#change_properties) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/properties | 
[**delete_all_properties**](VcsRootApi.md#delete_all_properties) | **DELETE** /app/rest/vcs-roots/{vcsRootLocator}/properties | 
[**delete_parameter**](VcsRootApi.md#delete_parameter) | **DELETE** /app/rest/vcs-roots/{vcsRootLocator}/properties/{name} | 
[**delete_root**](VcsRootApi.md#delete_root) | **DELETE** /app/rest/vcs-roots/{vcsRootLocator} | 
[**get_settings_file**](VcsRootApi.md#get_settings_file) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/settingsFile | 
[**put_parameter**](VcsRootApi.md#put_parameter) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/properties/{name} | 
[**serve_field**](VcsRootApi.md#serve_field) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/{field} | 
[**serve_instance_field**](VcsRootApi.md#serve_instance_field) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/{field} | 
[**serve_properties**](VcsRootApi.md#serve_properties) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/properties | 
[**serve_property**](VcsRootApi.md#serve_property) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/properties/{name} | 
[**serve_root**](VcsRootApi.md#serve_root) | **GET** /app/rest/vcs-roots/{vcsRootLocator} | 
[**serve_root_instance**](VcsRootApi.md#serve_root_instance) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator} | 
[**serve_root_instance_properties**](VcsRootApi.md#serve_root_instance_properties) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/properties | 
[**serve_root_instances**](VcsRootApi.md#serve_root_instances) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances | 
[**serve_roots**](VcsRootApi.md#serve_roots) | **GET** /app/rest/vcs-roots | 
[**set_field**](VcsRootApi.md#set_field) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/{field} | 
[**set_instance_field**](VcsRootApi.md#set_instance_field) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/{field} | 


# **add_root**
> VcsRoot add_root(body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
body = dohq_teamcity.VcsRoot() # VcsRoot |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.add_root(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->add_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VcsRoot**](VcsRoot.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRoot**](VcsRoot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_properties**
> Properties change_properties(vcs_root_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
body = dohq_teamcity.Properties() # Properties |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.change_properties(vcs_root_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->change_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **body** | [**Properties**](Properties.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_properties**
> delete_all_properties(vcs_root_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 

try:
    api_instance.delete_all_properties(vcs_root_locator)
except ApiException as e:
    print("Exception when calling VcsRootApi->delete_all_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parameter**
> delete_parameter(vcs_root_locator, name)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
name = 'name_example' # str | 

try:
    api_instance.delete_parameter(vcs_root_locator, name)
except ApiException as e:
    print("Exception when calling VcsRootApi->delete_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_root**
> delete_root(vcs_root_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 

try:
    api_instance.delete_root(vcs_root_locator)
except ApiException as e:
    print("Exception when calling VcsRootApi->delete_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_file**
> str get_settings_file(vcs_root_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 

try:
    api_response = api_instance.get_settings_file(vcs_root_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->get_settings_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_parameter**
> str put_parameter(vcs_root_locator, name, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
name = 'name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.put_parameter(vcs_root_locator, name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->put_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_field**
> str serve_field(vcs_root_locator, field)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_field(vcs_root_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_instance_field**
> str serve_instance_field(vcs_root_locator, vcs_root_instance_locator, field)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_instance_field(vcs_root_locator, vcs_root_instance_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_instance_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_properties**
> Properties serve_properties(vcs_root_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_properties(vcs_root_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_property**
> str serve_property(vcs_root_locator, name)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
name = 'name_example' # str | 

try:
    api_response = api_instance.serve_property(vcs_root_locator, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_root**
> VcsRoot serve_root(vcs_root_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_root(vcs_root_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRoot**](VcsRoot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_root_instance**
> VcsRootInstance serve_root_instance(vcs_root_locator, vcs_root_instance_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_root_instance(vcs_root_locator, vcs_root_instance_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_root_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootInstance**](VcsRootInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_root_instance_properties**
> Properties serve_root_instance_properties(vcs_root_locator, vcs_root_instance_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_root_instance_properties(vcs_root_locator, vcs_root_instance_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_root_instance_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_root_instances**
> VcsRootInstances serve_root_instances(vcs_root_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_root_instances(vcs_root_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_root_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootInstances**](VcsRootInstances.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_roots**
> VcsRoots serve_roots(locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_roots(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_roots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRoots**](VcsRoots.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_field**
> str set_field(vcs_root_locator, field, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_field(vcs_root_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->set_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **field** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_instance_field**
> str set_instance_field(vcs_root_locator, vcs_root_instance_locator, field, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.VcsRootApi()
vcs_root_locator = 'vcs_root_locator_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_instance_field(vcs_root_locator, vcs_root_instance_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->set_instance_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **field** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

