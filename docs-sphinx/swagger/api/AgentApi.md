# dohq_teamcity.AgentApi

[[API examples]](http://devopshq.github.io/teamcity/teamcity_apis/AgentApi.html)

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_agent**](AgentApi.md#delete_agent) | **DELETE** /app/rest/agents/{agentLocator} | 
[**get_agent_pool**](AgentApi.md#get_agent_pool) | **GET** /app/rest/agents/{agentLocator}/pool | 
[**get_authorized_info**](AgentApi.md#get_authorized_info) | **GET** /app/rest/agents/{agentLocator}/authorizedInfo | 
[**get_compatible_build_types**](AgentApi.md#get_compatible_build_types) | **GET** /app/rest/agents/{agentLocator}/compatibleBuildTypes | 
[**get_enabled_info**](AgentApi.md#get_enabled_info) | **GET** /app/rest/agents/{agentLocator}/enabledInfo | 
[**get_incompatible_build_types**](AgentApi.md#get_incompatible_build_types) | **GET** /app/rest/agents/{agentLocator}/incompatibleBuildTypes | 
[**serve_agent**](AgentApi.md#serve_agent) | **GET** /app/rest/agents/{agentLocator} | 
[**serve_agent_field**](AgentApi.md#serve_agent_field) | **GET** /app/rest/agents/{agentLocator}/{field} | 
[**serve_agents**](AgentApi.md#serve_agents) | **GET** /app/rest/agents | 
[**set_agent_field**](AgentApi.md#set_agent_field) | **PUT** /app/rest/agents/{agentLocator}/{field} | 
[**set_agent_pool**](AgentApi.md#set_agent_pool) | **PUT** /app/rest/agents/{agentLocator}/pool | 
[**set_authorized_info**](AgentApi.md#set_authorized_info) | **PUT** /app/rest/agents/{agentLocator}/authorizedInfo | 
[**set_enabled_info**](AgentApi.md#set_enabled_info) | **PUT** /app/rest/agents/{agentLocator}/enabledInfo | 


# **delete_agent**
> delete_agent(agent_locator)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 

try:
    tc.agent_api.delete_agent(agent_locator)
except ApiException as e:
    print("Exception when calling AgentApi->delete_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_agent_pool**
> AgentPool get_agent_pool(agent_locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.get_agent_pool(agent_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->get_agent_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**AgentPool**](AgentPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_authorized_info**
> AuthorizedInfo get_authorized_info(agent_locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.get_authorized_info(agent_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->get_authorized_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**AuthorizedInfo**](AuthorizedInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_compatible_build_types**
> BuildTypes get_compatible_build_types(agent_locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.get_compatible_build_types(agent_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->get_compatible_build_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildTypes**](BuildTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_enabled_info**
> EnabledInfo get_enabled_info(agent_locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.get_enabled_info(agent_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->get_enabled_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**EnabledInfo**](EnabledInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_incompatible_build_types**
> Compatibilities get_incompatible_build_types(agent_locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.get_incompatible_build_types(agent_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->get_incompatible_build_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Compatibilities**](Compatibilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_agent**
> Agent serve_agent(agent_locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.serve_agent(agent_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->serve_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Agent**](Agent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_agent_field**
> str serve_agent_field(agent_locator, field)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = tc.agent_api.serve_agent_field(agent_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->serve_agent_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_agents**
> Agents serve_agents(include_disconnected=include_disconnected, include_unauthorized=include_unauthorized, locator=locator, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

include_disconnected = true # bool |  (optional)
include_unauthorized = true # bool |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.serve_agents(include_disconnected=include_disconnected, include_unauthorized=include_unauthorized, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->serve_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_disconnected** | **bool**|  | [optional] 
 **include_unauthorized** | **bool**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Agents**](Agents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **set_agent_field**
> str set_agent_field(agent_locator, field, body=body)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = tc.agent_api.set_agent_field(agent_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->set_agent_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
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


# **set_agent_pool**
> AgentPool set_agent_pool(agent_locator, body=body, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
body = dohq_teamcity.AgentPool() # AgentPool |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.set_agent_pool(agent_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->set_agent_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **body** | [**AgentPool**](AgentPool.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**AgentPool**](AgentPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **set_authorized_info**
> AuthorizedInfo set_authorized_info(agent_locator, body=body, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
body = dohq_teamcity.AuthorizedInfo() # AuthorizedInfo |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.set_authorized_info(agent_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->set_authorized_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **body** | [**AuthorizedInfo**](AuthorizedInfo.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**AuthorizedInfo**](AuthorizedInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **set_enabled_info**
> EnabledInfo set_enabled_info(agent_locator, body=body, fields=fields)



### Example
```python
from pprint import pprint
import dohq_teamcity

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

agent_locator = 'agent_locator_example' # str | 
body = dohq_teamcity.EnabledInfo() # EnabledInfo |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.agent_api.set_enabled_info(agent_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentApi->set_enabled_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_locator** | **str**|  | 
 **body** | [**EnabledInfo**](EnabledInfo.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**EnabledInfo**](EnabledInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


