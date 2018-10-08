# teamcity.AgentPoolApi

All URIs are relative to *https://teamcity.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_agent**](AgentPoolApi.md#add_agent) | **POST** /app/rest/agentPools/{agentPoolLocator}/agents | 
[**add_project**](AgentPoolApi.md#add_project) | **POST** /app/rest/agentPools/{agentPoolLocator}/projects | 
[**create_pool**](AgentPoolApi.md#create_pool) | **POST** /app/rest/agentPools | 
[**delete_pool**](AgentPoolApi.md#delete_pool) | **DELETE** /app/rest/agentPools/{agentPoolLocator} | 
[**delete_pool_project**](AgentPoolApi.md#delete_pool_project) | **DELETE** /app/rest/agentPools/{agentPoolLocator}/projects/{projectLocator} | 
[**delete_projects**](AgentPoolApi.md#delete_projects) | **DELETE** /app/rest/agentPools/{agentPoolLocator}/projects | 
[**get_field**](AgentPoolApi.md#get_field) | **GET** /app/rest/agentPools/{agentPoolLocator}/{field} | 
[**get_pool**](AgentPoolApi.md#get_pool) | **GET** /app/rest/agentPools/{agentPoolLocator} | 
[**get_pool_agents**](AgentPoolApi.md#get_pool_agents) | **GET** /app/rest/agentPools/{agentPoolLocator}/agents | 
[**get_pool_project**](AgentPoolApi.md#get_pool_project) | **GET** /app/rest/agentPools/{agentPoolLocator}/projects/{projectLocator} | 
[**get_pool_projects**](AgentPoolApi.md#get_pool_projects) | **GET** /app/rest/agentPools/{agentPoolLocator}/projects | 
[**get_pools**](AgentPoolApi.md#get_pools) | **GET** /app/rest/agentPools | 
[**replace_projects**](AgentPoolApi.md#replace_projects) | **PUT** /app/rest/agentPools/{agentPoolLocator}/projects | 
[**set_field**](AgentPoolApi.md#set_field) | **PUT** /app/rest/agentPools/{agentPoolLocator}/{field} | 


# **add_agent**
> Agent add_agent(agent_pool_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
body = teamcity.Agent() # Agent |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.add_agent(agent_pool_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->add_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
 **body** | [**Agent**](Agent.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Agent**](Agent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project**
> Project add_project(agent_pool_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
body = teamcity.Project() # Project |  (optional)

try:
    api_response = api_instance.add_project(agent_pool_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->add_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
 **body** | [**Project**](Project.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pool**
> AgentPool create_pool(body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
body = teamcity.AgentPool() # AgentPool |  (optional)

try:
    api_response = api_instance.create_pool(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->create_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentPool**](AgentPool.md)|  | [optional] 

### Return type

[**AgentPool**](AgentPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pool**
> delete_pool(agent_pool_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 

try:
    api_instance.delete_pool(agent_pool_locator)
except ApiException as e:
    print("Exception when calling AgentPoolApi->delete_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pool_project**
> delete_pool_project(agent_pool_locator, project_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
project_locator = 'project_locator_example' # str | 

try:
    api_instance.delete_pool_project(agent_pool_locator, project_locator)
except ApiException as e:
    print("Exception when calling AgentPoolApi->delete_pool_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
 **project_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_projects**
> delete_projects(agent_pool_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 

try:
    api_instance.delete_projects(agent_pool_locator)
except ApiException as e:
    print("Exception when calling AgentPoolApi->delete_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field**
> str get_field(agent_pool_locator, field)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.get_field(agent_pool_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->get_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool**
> AgentPool get_pool(agent_pool_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_pool(agent_pool_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->get_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**AgentPool**](AgentPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_agents**
> Agents get_pool_agents(agent_pool_locator, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_pool_agents(agent_pool_locator, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->get_pool_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
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

# **get_pool_project**
> Project get_pool_project(agent_pool_locator, project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_pool_project(agent_pool_locator, project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->get_pool_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_projects**
> Projects get_pool_projects(agent_pool_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_pool_projects(agent_pool_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->get_pool_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Projects**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pools**
> AgentPools get_pools(locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_pools(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->get_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**AgentPools**](AgentPools.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_projects**
> Projects replace_projects(agent_pool_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
body = teamcity.Projects() # Projects |  (optional)

try:
    api_response = api_instance.replace_projects(agent_pool_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->replace_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
 **body** | [**Projects**](Projects.md)|  | [optional] 

### Return type

[**Projects**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_field**
> str set_field(agent_pool_locator, field, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.AgentPoolApi()
agent_pool_locator = 'agent_pool_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_field(agent_pool_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentPoolApi->set_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_pool_locator** | **str**|  | 
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

