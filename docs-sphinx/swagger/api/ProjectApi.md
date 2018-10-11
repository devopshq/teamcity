# dohq_teamcity.ProjectApi

All URIs are relative to *https://teamcity.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](ProjectApi.md#add) | **POST** /app/rest/projects/{projectLocator}/projectFeatures | 
[**create_build_type**](ProjectApi.md#create_build_type) | **POST** /app/rest/projects/{projectLocator}/buildTypes | 
[**create_build_type_template**](ProjectApi.md#create_build_type_template) | **POST** /app/rest/projects/{projectLocator}/templates | 
[**create_project**](ProjectApi.md#create_project) | **POST** /app/rest/projects | 
[**delete**](ProjectApi.md#delete) | **DELETE** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator} | 
[**delete_all_parameters**](ProjectApi.md#delete_all_parameters) | **DELETE** /app/rest/projects/{projectLocator}/parameters | 
[**delete_all_parameters_0**](ProjectApi.md#delete_all_parameters_0) | **DELETE** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties | 
[**delete_parameter**](ProjectApi.md#delete_parameter) | **DELETE** /app/rest/projects/{projectLocator}/parameters/{name} | 
[**delete_parameter_0**](ProjectApi.md#delete_parameter_0) | **DELETE** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name} | 
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /app/rest/projects/{projectLocator} | 
[**delete_project_agent_pools**](ProjectApi.md#delete_project_agent_pools) | **DELETE** /app/rest/projects/{projectLocator}/agentPools/{agentPoolLocator} | 
[**get**](ProjectApi.md#get) | **GET** /app/rest/projects/{projectLocator}/projectFeatures | 
[**get_build_types_order**](ProjectApi.md#get_build_types_order) | **GET** /app/rest/projects/{projectLocator}/order/buildTypes | 
[**get_example_new_project_description**](ProjectApi.md#get_example_new_project_description) | **GET** /app/rest/projects/{projectLocator}/example/newProjectDescription | 
[**get_example_new_project_description_compatibility_version1**](ProjectApi.md#get_example_new_project_description_compatibility_version1) | **GET** /app/rest/projects/{projectLocator}/newProjectDescription | 
[**get_parameter**](ProjectApi.md#get_parameter) | **GET** /app/rest/projects/{projectLocator}/parameters/{name} | 
[**get_parameter_0**](ProjectApi.md#get_parameter_0) | **GET** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name} | 
[**get_parameter_type**](ProjectApi.md#get_parameter_type) | **GET** /app/rest/projects/{projectLocator}/parameters/{name}/type | 
[**get_parameter_type_raw_value**](ProjectApi.md#get_parameter_type_raw_value) | **GET** /app/rest/projects/{projectLocator}/parameters/{name}/type/rawValue | 
[**get_parameter_value_long**](ProjectApi.md#get_parameter_value_long) | **GET** /app/rest/projects/{projectLocator}/parameters/{name}/value | 
[**get_parameter_value_long_0**](ProjectApi.md#get_parameter_value_long_0) | **GET** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name}/value | 
[**get_parameters**](ProjectApi.md#get_parameters) | **GET** /app/rest/projects/{projectLocator}/parameters | 
[**get_parameters_0**](ProjectApi.md#get_parameters_0) | **GET** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties | 
[**get_parent_project**](ProjectApi.md#get_parent_project) | **GET** /app/rest/projects/{projectLocator}/parentProject | 
[**get_project_agent_pools**](ProjectApi.md#get_project_agent_pools) | **GET** /app/rest/projects/{projectLocator}/agentPools | 
[**get_projects_order**](ProjectApi.md#get_projects_order) | **GET** /app/rest/projects/{projectLocator}/order/projects | 
[**get_settings_file**](ProjectApi.md#get_settings_file) | **GET** /app/rest/projects/{projectLocator}/settingsFile | 
[**get_single**](ProjectApi.md#get_single) | **GET** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator} | 
[**reload_settings_file**](ProjectApi.md#reload_settings_file) | **GET** /app/rest/projects/{projectLocator}/latest | 
[**replace**](ProjectApi.md#replace) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator} | 
[**replace_all**](ProjectApi.md#replace_all) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures | 
[**serve_build_field_with_project**](ProjectApi.md#serve_build_field_with_project) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator}/builds/{buildLocator}/{field} | 
[**serve_build_type**](ProjectApi.md#serve_build_type) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator} | 
[**serve_build_type_field_with_project**](ProjectApi.md#serve_build_type_field_with_project) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator}/{field} | 
[**serve_build_type_templates**](ProjectApi.md#serve_build_type_templates) | **GET** /app/rest/projects/{projectLocator}/templates/{btLocator} | 
[**serve_build_types_in_project**](ProjectApi.md#serve_build_types_in_project) | **GET** /app/rest/projects/{projectLocator}/buildTypes | 
[**serve_build_with_project**](ProjectApi.md#serve_build_with_project) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator}/builds/{buildLocator} | 
[**serve_builds**](ProjectApi.md#serve_builds) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator}/builds | 
[**serve_project**](ProjectApi.md#serve_project) | **GET** /app/rest/projects/{projectLocator} | 
[**serve_project_field**](ProjectApi.md#serve_project_field) | **GET** /app/rest/projects/{projectLocator}/{field} | 
[**serve_projects**](ProjectApi.md#serve_projects) | **GET** /app/rest/projects | 
[**serve_templates_in_project**](ProjectApi.md#serve_templates_in_project) | **GET** /app/rest/projects/{projectLocator}/templates | 
[**set_build_types_order**](ProjectApi.md#set_build_types_order) | **PUT** /app/rest/projects/{projectLocator}/order/buildTypes | 
[**set_parameter**](ProjectApi.md#set_parameter) | **POST** /app/rest/projects/{projectLocator}/parameters | 
[**set_parameter_0**](ProjectApi.md#set_parameter_0) | **PUT** /app/rest/projects/{projectLocator}/parameters/{name} | 
[**set_parameter_1**](ProjectApi.md#set_parameter_1) | **POST** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties | 
[**set_parameter_2**](ProjectApi.md#set_parameter_2) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name} | 
[**set_parameter_type**](ProjectApi.md#set_parameter_type) | **PUT** /app/rest/projects/{projectLocator}/parameters/{name}/type | 
[**set_parameter_type_raw_value**](ProjectApi.md#set_parameter_type_raw_value) | **PUT** /app/rest/projects/{projectLocator}/parameters/{name}/type/rawValue | 
[**set_parameter_value_long**](ProjectApi.md#set_parameter_value_long) | **PUT** /app/rest/projects/{projectLocator}/parameters/{name}/value | 
[**set_parameter_value_long_0**](ProjectApi.md#set_parameter_value_long_0) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name}/value | 
[**set_parameters**](ProjectApi.md#set_parameters) | **PUT** /app/rest/projects/{projectLocator}/parameters | 
[**set_parameters_0**](ProjectApi.md#set_parameters_0) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties | 
[**set_parent_project**](ProjectApi.md#set_parent_project) | **PUT** /app/rest/projects/{projectLocator}/parentProject | 
[**set_project_agent_pools**](ProjectApi.md#set_project_agent_pools) | **PUT** /app/rest/projects/{projectLocator}/agentPools | 
[**set_project_agent_pools_0**](ProjectApi.md#set_project_agent_pools_0) | **POST** /app/rest/projects/{projectLocator}/agentPools | 
[**set_project_filed**](ProjectApi.md#set_project_filed) | **PUT** /app/rest/projects/{projectLocator}/{field} | 
[**set_projects_order**](ProjectApi.md#set_projects_order) | **PUT** /app/rest/projects/{projectLocator}/order/projects | 


# **add**
> object add(project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.ProjectFeature() # ProjectFeature |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.add(project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **body** | [**ProjectFeature**](ProjectFeature.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build_type**
> BuildType create_build_type(project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.NewBuildTypeDescription() # NewBuildTypeDescription |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.create_build_type(project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_build_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **body** | [**NewBuildTypeDescription**](NewBuildTypeDescription.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildType**](BuildType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build_type_template**
> BuildType create_build_type_template(project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.NewBuildTypeDescription() # NewBuildTypeDescription |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.create_build_type_template(project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_build_type_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **body** | [**NewBuildTypeDescription**](NewBuildTypeDescription.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildType**](BuildType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
body = dohq_teamcity.NewProjectDescription() # NewProjectDescription |  (optional)

try:
    api_response = api_instance.create_project(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewProjectDescription**](NewProjectDescription.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(feature_locator, project_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 

try:
    api_instance.delete(feature_locator, project_locator)
except ApiException as e:
    print("Exception when calling ProjectApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_parameters**
> delete_all_parameters(project_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 

try:
    api_instance.delete_all_parameters(project_locator)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_all_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_parameters_0**
> delete_all_parameters_0(feature_locator, project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_instance.delete_all_parameters_0(feature_locator, project_locator, fields=fields)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_all_parameters_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parameter**
> delete_parameter(name, project_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
project_locator = 'project_locator_example' # str | 

try:
    api_instance.delete_parameter(name, project_locator)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parameter_0**
> delete_parameter_0(name, feature_locator, project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_instance.delete_parameter_0(name, feature_locator, project_locator, fields=fields)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_parameter_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 

try:
    api_instance.delete_project(project_locator)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_agent_pools**
> delete_project_agent_pools(project_locator, agent_pool_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
agent_pool_locator = 'agent_pool_locator_example' # str | 

try:
    api_instance.delete_project_agent_pools(project_locator, agent_pool_locator)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project_agent_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **agent_pool_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> object get(project_locator, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get(project_locator, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_types_order**
> BuildTypes get_build_types_order(project_locator, field)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.get_build_types_order(project_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_build_types_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

[**BuildTypes**](BuildTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_example_new_project_description**
> NewProjectDescription get_example_new_project_description(project_locator, id=id)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
id = 'id_example' # str |  (optional)

try:
    api_response = api_instance.get_example_new_project_description(project_locator, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_example_new_project_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **id** | **str**|  | [optional] 

### Return type

[**NewProjectDescription**](NewProjectDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_example_new_project_description_compatibility_version1**
> NewProjectDescription get_example_new_project_description_compatibility_version1(project_locator, id=id)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
id = 'id_example' # str |  (optional)

try:
    api_response = api_instance.get_example_new_project_description_compatibility_version1(project_locator, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_example_new_project_description_compatibility_version1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **id** | **str**|  | [optional] 

### Return type

[**NewProjectDescription**](NewProjectDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter**
> ModelProperty get_parameter(name, project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parameter(name, project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_0**
> ModelProperty get_parameter_0(name, feature_locator, project_locator, fields=fields, fields2=fields2)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
fields2 = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parameter_0(name, feature_locator, project_locator, fields=fields, fields2=fields2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_parameter_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **fields2** | **str**|  | [optional] 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_type**
> Type get_parameter_type(name, project_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
project_locator = 'project_locator_example' # str | 

try:
    api_response = api_instance.get_parameter_type(name, project_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_parameter_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_locator** | **str**|  | 

### Return type

[**Type**](Type.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_type_raw_value**
> str get_parameter_type_raw_value(name, project_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
project_locator = 'project_locator_example' # str | 

try:
    api_response = api_instance.get_parameter_type_raw_value(name, project_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_parameter_type_raw_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_value_long**
> str get_parameter_value_long(name, project_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
project_locator = 'project_locator_example' # str | 

try:
    api_response = api_instance.get_parameter_value_long(name, project_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_parameter_value_long: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_value_long_0**
> str get_parameter_value_long_0(name, feature_locator, project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parameter_value_long_0(name, feature_locator, project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_parameter_value_long_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameters**
> Properties get_parameters(project_locator, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parameters(project_locator, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameters_0**
> Properties get_parameters_0(feature_locator, project_locator, locator=locator, fields=fields, fields2=fields2)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
fields2 = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parameters_0(feature_locator, project_locator, locator=locator, fields=fields, fields2=fields2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_parameters_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **fields2** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_project**
> Project get_parent_project(project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parent_project(project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_parent_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_project_agent_pools**
> AgentPools get_project_agent_pools(project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_project_agent_pools(project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_agent_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**AgentPools**](AgentPools.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_order**
> Projects get_projects_order(project_locator, field)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.get_projects_order(project_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_projects_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

[**Projects**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_file**
> str get_settings_file(project_locator)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 

try:
    api_response = api_instance.get_settings_file(project_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_settings_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single**
> object get_single(feature_locator, project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_single(feature_locator, project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_single: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_settings_file**
> Project reload_settings_file(project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.reload_settings_file(project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->reload_settings_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **replace**
> object replace(feature_locator, project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.ProjectFeature() # ProjectFeature |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.replace(feature_locator, project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **body** | [**ProjectFeature**](ProjectFeature.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_all**
> object replace_all(project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.ProjectFeatures() # ProjectFeatures |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.replace_all(project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->replace_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **body** | [**ProjectFeatures**](ProjectFeatures.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_field_with_project**
> str serve_build_field_with_project(project_locator, bt_locator, build_locator, field)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
bt_locator = 'bt_locator_example' # str | 
build_locator = 'build_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_build_field_with_project(project_locator, bt_locator, build_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_build_field_with_project: %s\n" % e)
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

# **serve_build_type**
> BuildType serve_build_type(project_locator, bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_type(project_locator, bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_build_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildType**](BuildType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_type_field_with_project**
> str serve_build_type_field_with_project(project_locator, bt_locator, field)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
bt_locator = 'bt_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_build_type_field_with_project(project_locator, bt_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_build_type_field_with_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **bt_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_type_templates**
> BuildType serve_build_type_templates(project_locator, bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_type_templates(project_locator, bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_build_type_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildType**](BuildType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_types_in_project**
> BuildTypes serve_build_types_in_project(project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_types_in_project(project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_build_types_in_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildTypes**](BuildTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_with_project**
> Build serve_build_with_project(project_locator, bt_locator, build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
bt_locator = 'bt_locator_example' # str | 
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_with_project(project_locator, bt_locator, build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_build_with_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **bt_locator** | **str**|  | 
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

# **serve_builds**
> Builds serve_builds(project_locator, bt_locator, status=status, triggered_by_user=triggered_by_user, include_personal=include_personal, include_canceled=include_canceled, only_pinned=only_pinned, tag=tag, agent_name=agent_name, since_build=since_build, since_date=since_date, start=start, count=count, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
bt_locator = 'bt_locator_example' # str | 
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
    api_response = api_instance.serve_builds(project_locator, bt_locator, status=status, triggered_by_user=triggered_by_user, include_personal=include_personal, include_canceled=include_canceled, only_pinned=only_pinned, tag=tag, agent_name=agent_name, since_build=since_build, since_date=since_date, start=start, count=count, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **bt_locator** | **str**|  | 
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

# **serve_project**
> Project serve_project(project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_project(project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **serve_project_field**
> str serve_project_field(project_locator, field)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_project_field(project_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_project_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_projects**
> Projects serve_projects(locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_projects(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Projects**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_templates_in_project**
> BuildTypes serve_templates_in_project(project_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_templates_in_project(project_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->serve_templates_in_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildTypes**](BuildTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_build_types_order**
> BuildTypes set_build_types_order(project_locator, field, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
field = 'field_example' # str | 
body = dohq_teamcity.BuildTypes() # BuildTypes |  (optional)

try:
    api_response = api_instance.set_build_types_order(project_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_build_types_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **field** | **str**|  | 
 **body** | [**BuildTypes**](BuildTypes.md)|  | [optional] 

### Return type

[**BuildTypes**](BuildTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameter**
> ModelProperty set_parameter(project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter(project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **body** | [**ModelProperty**](ModelProperty.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameter_0**
> ModelProperty set_parameter_0(name, project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_0(name, project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameter_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_locator** | **str**|  | 
 **body** | [**ModelProperty**](ModelProperty.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameter_1**
> ModelProperty set_parameter_1(feature_locator, project_locator, body=body, fields=fields, fields2=fields2)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
fields = 'fields_example' # str |  (optional)
fields2 = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_1(feature_locator, project_locator, body=body, fields=fields, fields2=fields2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameter_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **body** | [**ModelProperty**](ModelProperty.md)|  | [optional] 
 **fields** | **str**|  | [optional] 
 **fields2** | **str**|  | [optional] 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameter_2**
> ModelProperty set_parameter_2(name, feature_locator, project_locator, body=body, fields=fields, fields2=fields2)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
fields = 'fields_example' # str |  (optional)
fields2 = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_2(name, feature_locator, project_locator, body=body, fields=fields, fields2=fields2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameter_2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **body** | [**ModelProperty**](ModelProperty.md)|  | [optional] 
 **fields** | **str**|  | [optional] 
 **fields2** | **str**|  | [optional] 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameter_type**
> Type set_parameter_type(name, project_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.Type() # Type |  (optional)

try:
    api_response = api_instance.set_parameter_type(name, project_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameter_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_locator** | **str**|  | 
 **body** | [**Type**](Type.md)|  | [optional] 

### Return type

[**Type**](Type.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameter_type_raw_value**
> str set_parameter_type_raw_value(name, project_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
project_locator = 'project_locator_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_type_raw_value(name, project_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameter_type_raw_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_locator** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameter_value_long**
> str set_parameter_value_long(name, project_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
project_locator = 'project_locator_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_value_long(name, project_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameter_value_long: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_locator** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameter_value_long_0**
> str set_parameter_value_long_0(name, feature_locator, project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
name = 'name_example' # str | 
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
body = 'body_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_value_long_0(name, feature_locator, project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameter_value_long_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **body** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameters**
> Properties set_parameters(project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.Properties() # Properties |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameters(project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
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

# **set_parameters_0**
> Properties set_parameters_0(feature_locator, project_locator, body=body, fields=fields, fields2=fields2)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
feature_locator = 'feature_locator_example' # str | 
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.Properties() # Properties |  (optional)
fields = 'fields_example' # str |  (optional)
fields2 = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameters_0(feature_locator, project_locator, body=body, fields=fields, fields2=fields2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parameters_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_locator** | **str**|  | 
 **project_locator** | **str**|  | 
 **body** | [**Properties**](Properties.md)|  | [optional] 
 **fields** | **str**|  | [optional] 
 **fields2** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parent_project**
> Project set_parent_project(project_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.Project() # Project |  (optional)

try:
    api_response = api_instance.set_parent_project(project_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_parent_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **body** | [**Project**](Project.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_agent_pools**
> AgentPools set_project_agent_pools(project_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.AgentPools() # AgentPools |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_project_agent_pools(project_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_agent_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **body** | [**AgentPools**](AgentPools.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**AgentPools**](AgentPools.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_agent_pools_0**
> AgentPool set_project_agent_pools_0(project_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
body = dohq_teamcity.AgentPool() # AgentPool |  (optional)

try:
    api_response = api_instance.set_project_agent_pools_0(project_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_agent_pools_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **body** | [**AgentPool**](AgentPool.md)|  | [optional] 

### Return type

[**AgentPool**](AgentPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_filed**
> str set_project_filed(project_locator, field, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_project_filed(project_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_filed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
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

# **set_projects_order**
> Projects set_projects_order(project_locator, field, body=body)



### Example
```python
from __future__ import print_function
import time
import dohq_teamcity
from dohq_teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dohq_teamcity.ProjectApi()
project_locator = 'project_locator_example' # str | 
field = 'field_example' # str | 
body = dohq_teamcity.Projects() # Projects |  (optional)

try:
    api_response = api_instance.set_projects_order(project_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_projects_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_locator** | **str**|  | 
 **field** | **str**|  | 
 **body** | [**Projects**](Projects.md)|  | [optional] 

### Return type

[**Projects**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

