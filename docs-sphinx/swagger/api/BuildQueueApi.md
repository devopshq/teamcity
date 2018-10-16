# dohq_teamcity.BuildQueueApi

[[API examples]](http://devopshq.github.io/teamcity/teamcity_apis/BuildQueueApi.html)

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tags**](BuildQueueApi.md#add_tags) | **POST** /app/rest/buildQueue/{buildLocator}/tags | 
[**cancel_build**](BuildQueueApi.md#cancel_build) | **GET** /app/rest/buildQueue/{buildLocator}/example/buildCancelRequest | 
[**cancel_build_0**](BuildQueueApi.md#cancel_build_0) | **POST** /app/rest/buildQueue/{queuedBuildLocator} | 
[**delete_build**](BuildQueueApi.md#delete_build) | **DELETE** /app/rest/buildQueue/{queuedBuildLocator} | 
[**delete_builds_experimental**](BuildQueueApi.md#delete_builds_experimental) | **DELETE** /app/rest/buildQueue | 
[**get_build**](BuildQueueApi.md#get_build) | **GET** /app/rest/buildQueue/{queuedBuildLocator} | 
[**get_builds**](BuildQueueApi.md#get_builds) | **GET** /app/rest/buildQueue | 
[**queue_new_build**](BuildQueueApi.md#queue_new_build) | **POST** /app/rest/buildQueue | 
[**replace_builds**](BuildQueueApi.md#replace_builds) | **PUT** /app/rest/buildQueue | 
[**replace_tags**](BuildQueueApi.md#replace_tags) | **PUT** /app/rest/buildQueue/{buildLocator}/tags | 
[**serve_build_field_by_build_only**](BuildQueueApi.md#serve_build_field_by_build_only) | **GET** /app/rest/buildQueue/{buildLocator}/{field} | 
[**serve_compatible_agents**](BuildQueueApi.md#serve_compatible_agents) | **GET** /app/rest/buildQueue/{queuedBuildLocator}/compatibleAgents | 
[**serve_tags**](BuildQueueApi.md#serve_tags) | **GET** /app/rest/buildQueue/{buildLocator}/tags | 
[**set_build_queue_order**](BuildQueueApi.md#set_build_queue_order) | **PUT** /app/rest/buildQueue/order | 


# **add_tags**
> add_tags(build_locator, body=body)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

build_locator = 'build_locator_example' # str | 
body = dohq_teamcity.Tags() # Tags |  (optional)

try:
    tc.build_queue_api.add_tags(build_locator, body=body)
except ApiException as e:
    print("Exception when calling BuildQueueApi->add_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_locator** | **str**|  | 
 **body** | [**Tags**](Tags.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **cancel_build**
> BuildCancelRequest cancel_build(build_locator)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

build_locator = 'build_locator_example' # str | 

try:
    api_response = tc.build_queue_api.cancel_build(build_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->cancel_build: %s\n" % e)
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


# **cancel_build_0**
> Build cancel_build_0(queued_build_locator, body=body)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

queued_build_locator = 'queued_build_locator_example' # str | 
body = dohq_teamcity.BuildCancelRequest() # BuildCancelRequest |  (optional)

try:
    api_response = tc.build_queue_api.cancel_build_0(queued_build_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->cancel_build_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queued_build_locator** | **str**|  | 
 **body** | [**BuildCancelRequest**](BuildCancelRequest.md)|  | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_build**
> delete_build(queued_build_locator)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

queued_build_locator = 'queued_build_locator_example' # str | 

try:
    tc.build_queue_api.delete_build(queued_build_locator)
except ApiException as e:
    print("Exception when calling BuildQueueApi->delete_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queued_build_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_builds_experimental**
> delete_builds_experimental(locator=locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    tc.build_queue_api.delete_builds_experimental(locator=locator, fields=fields)
except ApiException as e:
    print("Exception when calling BuildQueueApi->delete_builds_experimental: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_build**
> Build get_build(queued_build_locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

queued_build_locator = 'queued_build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.build_queue_api.get_build(queued_build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->get_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queued_build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_builds**
> Builds get_builds(locator=locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.build_queue_api.get_builds(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->get_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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


# **queue_new_build**
> Build queue_new_build(body=body, move_to_top=move_to_top)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

body = dohq_teamcity.Build() # Build |  (optional)
move_to_top = true # bool |  (optional)

try:
    api_response = tc.build_queue_api.queue_new_build(body=body, move_to_top=move_to_top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->queue_new_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Build**](Build.md)|  | [optional] 
 **move_to_top** | **bool**|  | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **replace_builds**
> Builds replace_builds(body=body, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

body = dohq_teamcity.Builds() # Builds |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.build_queue_api.replace_builds(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->replace_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Builds**](Builds.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Builds**](Builds.md)

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
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

build_locator = 'build_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
body = dohq_teamcity.Tags() # Tags |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.build_queue_api.replace_tags(build_locator, locator=locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->replace_tags: %s\n" % e)
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


# **serve_build_field_by_build_only**
> str serve_build_field_by_build_only(build_locator, field)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

build_locator = 'build_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = tc.build_queue_api.serve_build_field_by_build_only(build_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->serve_build_field_by_build_only: %s\n" % e)
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


# **serve_compatible_agents**
> Agents serve_compatible_agents(queued_build_locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

queued_build_locator = 'queued_build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.build_queue_api.serve_compatible_agents(queued_build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->serve_compatible_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queued_build_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Agents**](Agents.md)

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
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

build_locator = 'build_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.build_queue_api.serve_tags(build_locator, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->serve_tags: %s\n" % e)
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


# **set_build_queue_order**
> Builds set_build_queue_order(fields, body=body)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

fields = 'fields_example' # str | 
body = dohq_teamcity.Builds() # Builds |  (optional)

try:
    api_response = tc.build_queue_api.set_build_queue_order(fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildQueueApi->set_build_queue_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | 
 **body** | [**Builds**](Builds.md)|  | [optional] 

### Return type

[**Builds**](Builds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


