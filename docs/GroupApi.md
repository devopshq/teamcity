# swagger_client.GroupApi

All URIs are relative to *https://teamcity.ptsecurity.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](GroupApi.md#add_group) | **POST** /app/rest/userGroups | 
[**add_role**](GroupApi.md#add_role) | **POST** /app/rest/userGroups/{groupLocator}/roles | 
[**add_role_put**](GroupApi.md#add_role_put) | **PUT** /app/rest/userGroups/{groupLocator}/roles | 
[**add_role_simple**](GroupApi.md#add_role_simple) | **POST** /app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope} | 
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /app/rest/userGroups/{groupLocator} | 
[**delete_role**](GroupApi.md#delete_role) | **DELETE** /app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope} | 
[**get_permissions**](GroupApi.md#get_permissions) | **GET** /app/rest/userGroups/{groupLocator}/debug/permissions | 
[**get_properties**](GroupApi.md#get_properties) | **GET** /app/rest/userGroups/{groupLocator}/properties | 
[**list_role**](GroupApi.md#list_role) | **GET** /app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope} | 
[**list_roles**](GroupApi.md#list_roles) | **GET** /app/rest/userGroups/{groupLocator}/roles | 
[**put_user_property**](GroupApi.md#put_user_property) | **PUT** /app/rest/userGroups/{groupLocator}/properties/{name} | 
[**remove_user_property**](GroupApi.md#remove_user_property) | **DELETE** /app/rest/userGroups/{groupLocator}/properties/{name} | 
[**serve_group**](GroupApi.md#serve_group) | **GET** /app/rest/userGroups/{groupLocator} | 
[**serve_groups**](GroupApi.md#serve_groups) | **GET** /app/rest/userGroups | 
[**serve_user_properties**](GroupApi.md#serve_user_properties) | **GET** /app/rest/userGroups/{groupLocator}/properties/{name} | 


# **add_group**
> Group add_group(body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
body = swagger_client.Group() # Group |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.add_group(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->add_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role**
> Role add_role(group_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
body = swagger_client.Role() # Role |  (optional)

try:
    api_response = api_instance.add_role(group_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
 **body** | [**Role**](Role.md)|  | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_put**
> Roles add_role_put(group_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
body = swagger_client.Roles() # Roles |  (optional)

try:
    api_response = api_instance.add_role_put(group_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->add_role_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
 **body** | [**Roles**](Roles.md)|  | [optional] 

### Return type

[**Roles**](Roles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_simple**
> Role add_role_simple(group_locator, role_id, scope)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
role_id = 'role_id_example' # str | 
scope = 'scope_example' # str | 

try:
    api_response = api_instance.add_role_simple(group_locator, role_id, scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->add_role_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
 **role_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 

try:
    api_instance.delete_group(group_locator)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(group_locator, role_id, scope)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
role_id = 'role_id_example' # str | 
scope = 'scope_example' # str | 

try:
    api_instance.delete_role(group_locator, role_id, scope)
except ApiException as e:
    print("Exception when calling GroupApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
 **role_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions**
> str get_permissions(group_locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 

try:
    api_response = api_instance.get_permissions(group_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties**
> Properties get_properties(group_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_properties(group_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role**
> Role list_role(group_locator, role_id, scope)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
role_id = 'role_id_example' # str | 
scope = 'scope_example' # str | 

try:
    api_response = api_instance.list_role(group_locator, role_id, scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
 **role_id** | **str**|  | 
 **scope** | **str**|  | 

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> Roles list_roles(group_locator)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 

try:
    api_response = api_instance.list_roles(group_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 

### Return type

[**Roles**](Roles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user_property**
> str put_user_property(group_locator, name, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
name = 'name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.put_user_property(group_locator, name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->put_user_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
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

# **remove_user_property**
> remove_user_property(group_locator, name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
name = 'name_example' # str | 

try:
    api_instance.remove_user_property(group_locator, name)
except ApiException as e:
    print("Exception when calling GroupApi->remove_user_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_group**
> Group serve_group(group_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_group(group_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->serve_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_groups**
> Groups serve_groups(fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_groups(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->serve_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**Groups**](Groups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_user_properties**
> str serve_user_properties(group_locator, name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
group_locator = 'group_locator_example' # str | 
name = 'name_example' # str | 

try:
    api_response = api_instance.serve_user_properties(group_locator, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->serve_user_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_locator** | **str**|  | 
 **name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

