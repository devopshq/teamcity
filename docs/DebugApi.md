# teamcity.DebugApi

All URIs are relative to *https://teamcity.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_current_remember_me**](DebugApi.md#delete_current_remember_me) | **DELETE** /app/rest/debug/currentRequest/rememberMe | 
[**empty_task**](DebugApi.md#empty_task) | **POST** /app/rest/debug/emptyTask | 
[**execute_db_query**](DebugApi.md#execute_db_query) | **GET** /app/rest/debug/database/query/{query} | 
[**get_current_session**](DebugApi.md#get_current_session) | **GET** /app/rest/debug/currentRequest/session | 
[**get_current_session_max_inactive_interval**](DebugApi.md#get_current_session_max_inactive_interval) | **GET** /app/rest/debug/currentRequest/session/maxInactiveSeconds | 
[**get_current_user_permissions**](DebugApi.md#get_current_user_permissions) | **GET** /app/rest/debug/currentUserPermissions | 
[**get_date**](DebugApi.md#get_date) | **GET** /app/rest/debug/date/{dateLocator} | 
[**get_environment_variables**](DebugApi.md#get_environment_variables) | **GET** /app/rest/debug/jvm/environmentVariables | 
[**get_hashed**](DebugApi.md#get_hashed) | **GET** /app/rest/debug/values/transform/{method} | 
[**get_request_details**](DebugApi.md#get_request_details) | **GET** /app/rest/debug/currentRequest/details | 
[**get_scrambled**](DebugApi.md#get_scrambled) | **GET** /app/rest/debug/values/password/scrambled | 
[**get_sessions**](DebugApi.md#get_sessions) | **GET** /app/rest/debug/sessions | 
[**get_system_properties**](DebugApi.md#get_system_properties) | **GET** /app/rest/debug/jvm/systemProperties | 
[**get_thread_dump**](DebugApi.md#get_thread_dump) | **GET** /app/rest/debug/threadDump | 
[**get_unscrambled**](DebugApi.md#get_unscrambled) | **GET** /app/rest/debug/values/password/unscrambled | 
[**invalidate_current_session**](DebugApi.md#invalidate_current_session) | **DELETE** /app/rest/debug/currentRequest/session | 
[**list_db_tables**](DebugApi.md#list_db_tables) | **GET** /app/rest/debug/database/tables | 
[**new_remember_me**](DebugApi.md#new_remember_me) | **POST** /app/rest/debug/currentRequest/rememberMe | 
[**save_memory_dump**](DebugApi.md#save_memory_dump) | **POST** /app/rest/debug/memory/dumps | 
[**schedule_checking_for_changes**](DebugApi.md#schedule_checking_for_changes) | **POST** /app/rest/debug/vcsCheckingForChangesQueue | 
[**set_current_session_max_inactive_interval**](DebugApi.md#set_current_session_max_inactive_interval) | **PUT** /app/rest/debug/currentRequest/session/maxInactiveSeconds | 


# **delete_current_remember_me**
> delete_current_remember_me()



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()

try:
    api_instance.delete_current_remember_me()
except ApiException as e:
    print("Exception when calling DebugApi->delete_current_remember_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empty_task**
> str empty_task(time=time, load=load)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
time = 'time_example' # str |  (optional)
load = 56 # int |  (optional)

try:
    api_response = api_instance.empty_task(time=time, load=load)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->empty_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | **str**|  | [optional] 
 **load** | **int**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_db_query**
> str execute_db_query(query, field_delimiter=field_delimiter, data_retrieve_query=data_retrieve_query, count=count)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
query = 'query_example' # str | 
field_delimiter = ', ' # str |  (optional) (default to , )
data_retrieve_query = 'data_retrieve_query_example' # str |  (optional)
count = 1000 # int |  (optional) (default to 1000)

try:
    api_response = api_instance.execute_db_query(query, field_delimiter=field_delimiter, data_retrieve_query=data_retrieve_query, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->execute_db_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **field_delimiter** | **str**|  | [optional] [default to , ]
 **data_retrieve_query** | **str**|  | [optional] 
 **count** | **int**|  | [optional] [default to 1000]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_session**
> Session get_current_session(fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_current_session(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_current_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_session_max_inactive_interval**
> str get_current_session_max_inactive_interval()



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()

try:
    api_response = api_instance.get_current_session_max_inactive_interval()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_current_session_max_inactive_interval: %s\n" % e)
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

# **get_current_user_permissions**
> str get_current_user_permissions()



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()

try:
    api_response = api_instance.get_current_user_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_current_user_permissions: %s\n" % e)
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

# **get_date**
> str get_date(date_locator, format=format, timezone=timezone)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
date_locator = 'date_locator_example' # str | 
format = 'format_example' # str |  (optional)
timezone = 'timezone_example' # str |  (optional)

try:
    api_response = api_instance.get_date(date_locator, format=format, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_locator** | **str**|  | 
 **format** | **str**|  | [optional] 
 **timezone** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_variables**
> Properties get_environment_variables(fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_environment_variables(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_environment_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hashed**
> str get_hashed(method, value=value)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
method = 'method_example' # str | 
value = 'value_example' # str |  (optional)

try:
    api_response = api_instance.get_hashed(method, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_hashed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**|  | 
 **value** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_details**
> str get_request_details()



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()

try:
    api_response = api_instance.get_request_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_request_details: %s\n" % e)
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

# **get_scrambled**
> str get_scrambled(value=value)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
value = 'value_example' # str |  (optional)

try:
    api_response = api_instance.get_scrambled(value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_scrambled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions**
> Sessions get_sessions(manager=manager, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
manager = 789 # int |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_sessions(manager=manager, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manager** | **int**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Sessions**](Sessions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_properties**
> Properties get_system_properties(fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_system_properties(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_system_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thread_dump**
> str get_thread_dump(locked_monitors=locked_monitors, locked_synchronizers=locked_synchronizers, detect_locks=detect_locks)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
locked_monitors = 'locked_monitors_example' # str |  (optional)
locked_synchronizers = 'locked_synchronizers_example' # str |  (optional)
detect_locks = 'detect_locks_example' # str |  (optional)

try:
    api_response = api_instance.get_thread_dump(locked_monitors=locked_monitors, locked_synchronizers=locked_synchronizers, detect_locks=detect_locks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_thread_dump: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locked_monitors** | **str**|  | [optional] 
 **locked_synchronizers** | **str**|  | [optional] 
 **detect_locks** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unscrambled**
> str get_unscrambled(value=value)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
value = 'value_example' # str |  (optional)

try:
    api_response = api_instance.get_unscrambled(value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_unscrambled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_current_session**
> invalidate_current_session()



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()

try:
    api_instance.invalidate_current_session()
except ApiException as e:
    print("Exception when calling DebugApi->invalidate_current_session: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_db_tables**
> str list_db_tables()



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()

try:
    api_response = api_instance.list_db_tables()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->list_db_tables: %s\n" % e)
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

# **new_remember_me**
> str new_remember_me()



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()

try:
    api_response = api_instance.new_remember_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->new_remember_me: %s\n" % e)
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

# **save_memory_dump**
> str save_memory_dump(archived=archived)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
archived = true # bool |  (optional)

try:
    api_response = api_instance.save_memory_dump(archived=archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->save_memory_dump: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archived** | **bool**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_checking_for_changes**
> VcsRootInstances schedule_checking_for_changes(locator=locator, requestor=requestor, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
locator = 'locator_example' # str |  (optional)
requestor = 'requestor_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.schedule_checking_for_changes(locator=locator, requestor=requestor, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->schedule_checking_for_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **requestor** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootInstances**](VcsRootInstances.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_current_session_max_inactive_interval**
> str set_current_session_max_inactive_interval(body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.DebugApi()
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_current_session_max_inactive_interval(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->set_current_session_max_inactive_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

