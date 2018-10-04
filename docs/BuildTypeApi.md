# teamcity.BuildTypeApi

All URIs are relative to *https://teamcity.ptsecurity.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_agent_requirement**](BuildTypeApi.md#add_agent_requirement) | **POST** /app/rest/buildTypes/{btLocator}/agent-requirements | 
[**add_artifact_dep**](BuildTypeApi.md#add_artifact_dep) | **POST** /app/rest/buildTypes/{btLocator}/artifact-dependencies | 
[**add_build_type**](BuildTypeApi.md#add_build_type) | **POST** /app/rest/buildTypes | 
[**add_feature**](BuildTypeApi.md#add_feature) | **POST** /app/rest/buildTypes/{btLocator}/features | 
[**add_feature_parameter**](BuildTypeApi.md#add_feature_parameter) | **PUT** /app/rest/buildTypes/{btLocator}/features/{featureId}/parameters/{parameterName} | 
[**add_snapshot_dep**](BuildTypeApi.md#add_snapshot_dep) | **POST** /app/rest/buildTypes/{btLocator}/snapshot-dependencies | 
[**add_step**](BuildTypeApi.md#add_step) | **POST** /app/rest/buildTypes/{btLocator}/steps | 
[**add_step_parameter**](BuildTypeApi.md#add_step_parameter) | **PUT** /app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters/{parameterName} | 
[**add_trigger**](BuildTypeApi.md#add_trigger) | **POST** /app/rest/buildTypes/{btLocator}/triggers | 
[**add_vcs_root_entry**](BuildTypeApi.md#add_vcs_root_entry) | **POST** /app/rest/buildTypes/{btLocator}/vcs-root-entries | 
[**change_artifact_dep_setting**](BuildTypeApi.md#change_artifact_dep_setting) | **PUT** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}/{fieldName} | 
[**change_feature_setting**](BuildTypeApi.md#change_feature_setting) | **PUT** /app/rest/buildTypes/{btLocator}/features/{featureId}/{name} | 
[**change_requirement_setting**](BuildTypeApi.md#change_requirement_setting) | **PUT** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}/{fieldName} | 
[**change_step_setting**](BuildTypeApi.md#change_step_setting) | **PUT** /app/rest/buildTypes/{btLocator}/steps/{stepId}/{fieldName} | 
[**change_trigger_setting**](BuildTypeApi.md#change_trigger_setting) | **PUT** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}/{fieldName} | 
[**delete_agent_requirement**](BuildTypeApi.md#delete_agent_requirement) | **DELETE** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator} | 
[**delete_all_parameters**](BuildTypeApi.md#delete_all_parameters) | **DELETE** /app/rest/buildTypes/{btLocator}/parameters | 
[**delete_all_parameters_0**](BuildTypeApi.md#delete_all_parameters_0) | **DELETE** /app/rest/buildTypes/{btLocator}/settings | 
[**delete_artifact_dep**](BuildTypeApi.md#delete_artifact_dep) | **DELETE** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator} | 
[**delete_build_type**](BuildTypeApi.md#delete_build_type) | **DELETE** /app/rest/buildTypes/{btLocator} | 
[**delete_feature**](BuildTypeApi.md#delete_feature) | **DELETE** /app/rest/buildTypes/{btLocator}/features/{featureId} | 
[**delete_parameter**](BuildTypeApi.md#delete_parameter) | **DELETE** /app/rest/buildTypes/{btLocator}/parameters/{name} | 
[**delete_parameter_0**](BuildTypeApi.md#delete_parameter_0) | **DELETE** /app/rest/buildTypes/{btLocator}/settings/{name} | 
[**delete_snapshot_dep**](BuildTypeApi.md#delete_snapshot_dep) | **DELETE** /app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator} | 
[**delete_step**](BuildTypeApi.md#delete_step) | **DELETE** /app/rest/buildTypes/{btLocator}/steps/{stepId} | 
[**delete_template_association**](BuildTypeApi.md#delete_template_association) | **DELETE** /app/rest/buildTypes/{btLocator}/template | 
[**delete_trigger**](BuildTypeApi.md#delete_trigger) | **DELETE** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator} | 
[**delete_vcs_root_entry**](BuildTypeApi.md#delete_vcs_root_entry) | **DELETE** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator} | 
[**get_agent_requirement**](BuildTypeApi.md#get_agent_requirement) | **GET** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator} | 
[**get_agent_requirements**](BuildTypeApi.md#get_agent_requirements) | **GET** /app/rest/buildTypes/{btLocator}/agent-requirements | 
[**get_aliases**](BuildTypeApi.md#get_aliases) | **GET** /app/rest/buildTypes/{btLocator}/aliases | 
[**get_artifact_dep**](BuildTypeApi.md#get_artifact_dep) | **GET** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator} | 
[**get_artifact_dep_setting**](BuildTypeApi.md#get_artifact_dep_setting) | **GET** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}/{fieldName} | 
[**get_artifact_deps**](BuildTypeApi.md#get_artifact_deps) | **GET** /app/rest/buildTypes/{btLocator}/artifact-dependencies | 
[**get_build_types**](BuildTypeApi.md#get_build_types) | **GET** /app/rest/buildTypes | 
[**get_children**](BuildTypeApi.md#get_children) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/children{path} | 
[**get_children_alias**](BuildTypeApi.md#get_children_alias) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/{path} | 
[**get_content**](BuildTypeApi.md#get_content) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/content{path} | 
[**get_content_alias**](BuildTypeApi.md#get_content_alias) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/files{path} | 
[**get_current_vcs_instances**](BuildTypeApi.md#get_current_vcs_instances) | **GET** /app/rest/buildTypes/{btLocator}/vcs-root-instances | 
[**get_example_new_project_description**](BuildTypeApi.md#get_example_new_project_description) | **GET** /app/rest/buildTypes/{btLocator}/example/newBuildTypeDescription | 
[**get_example_new_project_description_compatibility_version1**](BuildTypeApi.md#get_example_new_project_description_compatibility_version1) | **GET** /app/rest/buildTypes/{btLocator}/newBuildTypeDescription | 
[**get_feature**](BuildTypeApi.md#get_feature) | **GET** /app/rest/buildTypes/{btLocator}/features/{featureId} | 
[**get_feature_parameter**](BuildTypeApi.md#get_feature_parameter) | **GET** /app/rest/buildTypes/{btLocator}/features/{featureId}/parameters/{parameterName} | 
[**get_feature_parameters**](BuildTypeApi.md#get_feature_parameters) | **GET** /app/rest/buildTypes/{btLocator}/features/{featureId}/parameters | 
[**get_feature_setting**](BuildTypeApi.md#get_feature_setting) | **GET** /app/rest/buildTypes/{btLocator}/features/{featureId}/{name} | 
[**get_features**](BuildTypeApi.md#get_features) | **GET** /app/rest/buildTypes/{btLocator}/features | 
[**get_investigations**](BuildTypeApi.md#get_investigations) | **GET** /app/rest/buildTypes/{btLocator}/investigations | 
[**get_metadata**](BuildTypeApi.md#get_metadata) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/metadata{path} | 
[**get_parameter**](BuildTypeApi.md#get_parameter) | **GET** /app/rest/buildTypes/{btLocator}/parameters/{name} | 
[**get_parameter_0**](BuildTypeApi.md#get_parameter_0) | **GET** /app/rest/buildTypes/{btLocator}/settings/{name} | 
[**get_parameter_type**](BuildTypeApi.md#get_parameter_type) | **GET** /app/rest/buildTypes/{btLocator}/parameters/{name}/type | 
[**get_parameter_type_raw_value**](BuildTypeApi.md#get_parameter_type_raw_value) | **GET** /app/rest/buildTypes/{btLocator}/parameters/{name}/type/rawValue | 
[**get_parameter_value_long**](BuildTypeApi.md#get_parameter_value_long) | **GET** /app/rest/buildTypes/{btLocator}/parameters/{name}/value | 
[**get_parameter_value_long_0**](BuildTypeApi.md#get_parameter_value_long_0) | **GET** /app/rest/buildTypes/{btLocator}/settings/{name}/value | 
[**get_parameters**](BuildTypeApi.md#get_parameters) | **GET** /app/rest/buildTypes/{btLocator}/parameters | 
[**get_parameters_0**](BuildTypeApi.md#get_parameters_0) | **GET** /app/rest/buildTypes/{btLocator}/settings | 
[**get_requirement_setting**](BuildTypeApi.md#get_requirement_setting) | **GET** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}/{fieldName} | 
[**get_root**](BuildTypeApi.md#get_root) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest | 
[**get_settings_file**](BuildTypeApi.md#get_settings_file) | **GET** /app/rest/buildTypes/{btLocator}/settingsFile | 
[**get_snapshot_dep**](BuildTypeApi.md#get_snapshot_dep) | **GET** /app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator} | 
[**get_snapshot_deps**](BuildTypeApi.md#get_snapshot_deps) | **GET** /app/rest/buildTypes/{btLocator}/snapshot-dependencies | 
[**get_step**](BuildTypeApi.md#get_step) | **GET** /app/rest/buildTypes/{btLocator}/steps/{stepId} | 
[**get_step_parameter**](BuildTypeApi.md#get_step_parameter) | **GET** /app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters/{parameterName} | 
[**get_step_parameters**](BuildTypeApi.md#get_step_parameters) | **GET** /app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters | 
[**get_step_setting**](BuildTypeApi.md#get_step_setting) | **GET** /app/rest/buildTypes/{btLocator}/steps/{stepId}/{fieldName} | 
[**get_steps**](BuildTypeApi.md#get_steps) | **GET** /app/rest/buildTypes/{btLocator}/steps | 
[**get_template_association**](BuildTypeApi.md#get_template_association) | **PUT** /app/rest/buildTypes/{btLocator}/template | 
[**get_trigger**](BuildTypeApi.md#get_trigger) | **GET** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator} | 
[**get_trigger_setting**](BuildTypeApi.md#get_trigger_setting) | **GET** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}/{fieldName} | 
[**get_triggers**](BuildTypeApi.md#get_triggers) | **GET** /app/rest/buildTypes/{btLocator}/triggers | 
[**get_vcs_labeling_options**](BuildTypeApi.md#get_vcs_labeling_options) | **GET** /app/rest/buildTypes/{btLocator}/vcsLabeling | 
[**get_vcs_root_entries**](BuildTypeApi.md#get_vcs_root_entries) | **GET** /app/rest/buildTypes/{btLocator}/vcs-root-entries | 
[**get_vcs_root_entry**](BuildTypeApi.md#get_vcs_root_entry) | **GET** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator} | 
[**get_vcs_root_entry_checkout_rules**](BuildTypeApi.md#get_vcs_root_entry_checkout_rules) | **GET** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}/checkout-rules | 
[**get_zipped**](BuildTypeApi.md#get_zipped) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/archived{path} | 
[**replace_agent_requirement**](BuildTypeApi.md#replace_agent_requirement) | **PUT** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator} | 
[**replace_agent_requirements**](BuildTypeApi.md#replace_agent_requirements) | **PUT** /app/rest/buildTypes/{btLocator}/agent-requirements | 
[**replace_artifact_dep**](BuildTypeApi.md#replace_artifact_dep) | **PUT** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator} | 
[**replace_artifact_deps**](BuildTypeApi.md#replace_artifact_deps) | **PUT** /app/rest/buildTypes/{btLocator}/artifact-dependencies | 
[**replace_feature**](BuildTypeApi.md#replace_feature) | **PUT** /app/rest/buildTypes/{btLocator}/features/{featureId} | 
[**replace_feature_parameters**](BuildTypeApi.md#replace_feature_parameters) | **PUT** /app/rest/buildTypes/{btLocator}/features/{featureId}/parameters | 
[**replace_features**](BuildTypeApi.md#replace_features) | **PUT** /app/rest/buildTypes/{btLocator}/features | 
[**replace_snapshot_dep**](BuildTypeApi.md#replace_snapshot_dep) | **PUT** /app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator} | 
[**replace_snapshot_deps**](BuildTypeApi.md#replace_snapshot_deps) | **PUT** /app/rest/buildTypes/{btLocator}/snapshot-dependencies | 
[**replace_step**](BuildTypeApi.md#replace_step) | **PUT** /app/rest/buildTypes/{btLocator}/steps/{stepId} | 
[**replace_step_parameters**](BuildTypeApi.md#replace_step_parameters) | **PUT** /app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters | 
[**replace_steps**](BuildTypeApi.md#replace_steps) | **PUT** /app/rest/buildTypes/{btLocator}/steps | 
[**replace_trigger**](BuildTypeApi.md#replace_trigger) | **PUT** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator} | 
[**replace_triggers**](BuildTypeApi.md#replace_triggers) | **PUT** /app/rest/buildTypes/{btLocator}/triggers | 
[**replace_vcs_root_entries**](BuildTypeApi.md#replace_vcs_root_entries) | **PUT** /app/rest/buildTypes/{btLocator}/vcs-root-entries | 
[**serve_branches**](BuildTypeApi.md#serve_branches) | **GET** /app/rest/buildTypes/{btLocator}/branches | 
[**serve_build_field**](BuildTypeApi.md#serve_build_field) | **GET** /app/rest/buildTypes/{btLocator}/builds/{buildLocator}/{field} | 
[**serve_build_type_builds_tags**](BuildTypeApi.md#serve_build_type_builds_tags) | **GET** /app/rest/buildTypes/{btLocator}/buildTags | 
[**serve_build_type_field**](BuildTypeApi.md#serve_build_type_field) | **GET** /app/rest/buildTypes/{btLocator}/{field} | 
[**serve_build_type_template**](BuildTypeApi.md#serve_build_type_template) | **GET** /app/rest/buildTypes/{btLocator}/template | 
[**serve_build_type_xml**](BuildTypeApi.md#serve_build_type_xml) | **GET** /app/rest/buildTypes/{btLocator} | 
[**serve_build_with_project**](BuildTypeApi.md#serve_build_with_project) | **GET** /app/rest/buildTypes/{btLocator}/builds/{buildLocator} | 
[**serve_builds**](BuildTypeApi.md#serve_builds) | **GET** /app/rest/buildTypes/{btLocator}/builds | 
[**set_build_type_field**](BuildTypeApi.md#set_build_type_field) | **PUT** /app/rest/buildTypes/{btLocator}/{field} | 
[**set_parameter**](BuildTypeApi.md#set_parameter) | **POST** /app/rest/buildTypes/{btLocator}/parameters | 
[**set_parameter_0**](BuildTypeApi.md#set_parameter_0) | **PUT** /app/rest/buildTypes/{btLocator}/parameters/{name} | 
[**set_parameter_1**](BuildTypeApi.md#set_parameter_1) | **POST** /app/rest/buildTypes/{btLocator}/settings | 
[**set_parameter_2**](BuildTypeApi.md#set_parameter_2) | **PUT** /app/rest/buildTypes/{btLocator}/settings/{name} | 
[**set_parameter_type**](BuildTypeApi.md#set_parameter_type) | **PUT** /app/rest/buildTypes/{btLocator}/parameters/{name}/type | 
[**set_parameter_type_raw_value**](BuildTypeApi.md#set_parameter_type_raw_value) | **PUT** /app/rest/buildTypes/{btLocator}/parameters/{name}/type/rawValue | 
[**set_parameter_value_long**](BuildTypeApi.md#set_parameter_value_long) | **PUT** /app/rest/buildTypes/{btLocator}/parameters/{name}/value | 
[**set_parameter_value_long_0**](BuildTypeApi.md#set_parameter_value_long_0) | **PUT** /app/rest/buildTypes/{btLocator}/settings/{name}/value | 
[**set_parameters**](BuildTypeApi.md#set_parameters) | **PUT** /app/rest/buildTypes/{btLocator}/parameters | 
[**set_parameters_0**](BuildTypeApi.md#set_parameters_0) | **PUT** /app/rest/buildTypes/{btLocator}/settings | 
[**set_vcs_labeling_options**](BuildTypeApi.md#set_vcs_labeling_options) | **PUT** /app/rest/buildTypes/{btLocator}/vcsLabeling | 
[**update_vcs_root_entry**](BuildTypeApi.md#update_vcs_root_entry) | **PUT** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator} | 
[**update_vcs_root_entry_checkout_rules**](BuildTypeApi.md#update_vcs_root_entry_checkout_rules) | **PUT** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}/checkout-rules | 


# **add_agent_requirement**
> AgentRequirement add_agent_requirement(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.AgentRequirement() # AgentRequirement |  (optional)

try:
    api_response = api_instance.add_agent_requirement(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_agent_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**AgentRequirement**](AgentRequirement.md)|  | [optional] 

### Return type

[**AgentRequirement**](AgentRequirement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_artifact_dep**
> ArtifactDependency add_artifact_dep(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.ArtifactDependency() # ArtifactDependency |  (optional)

try:
    api_response = api_instance.add_artifact_dep(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_artifact_dep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**ArtifactDependency**](ArtifactDependency.md)|  | [optional] 

### Return type

[**ArtifactDependency**](ArtifactDependency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_build_type**
> BuildType add_build_type(body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
body = teamcity.BuildType() # BuildType |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.add_build_type(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_build_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BuildType**](BuildType.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildType**](BuildType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_feature**
> Feature add_feature(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.Feature() # Feature |  (optional)

try:
    api_response = api_instance.add_feature(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**Feature**](Feature.md)|  | [optional] 

### Return type

[**Feature**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_feature_parameter**
> str add_feature_parameter(bt_locator, feature_id, parameter_name, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
feature_id = 'feature_id_example' # str | 
parameter_name = 'parameter_name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.add_feature_parameter(bt_locator, feature_id, parameter_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_feature_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **feature_id** | **str**|  | 
 **parameter_name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_snapshot_dep**
> SnapshotDependency add_snapshot_dep(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.SnapshotDependency() # SnapshotDependency |  (optional)

try:
    api_response = api_instance.add_snapshot_dep(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_snapshot_dep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**SnapshotDependency**](SnapshotDependency.md)|  | [optional] 

### Return type

[**SnapshotDependency**](SnapshotDependency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_step**
> Step add_step(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.Step() # Step |  (optional)

try:
    api_response = api_instance.add_step(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**Step**](Step.md)|  | [optional] 

### Return type

[**Step**](Step.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_step_parameter**
> str add_step_parameter(bt_locator, step_id, parameter_name, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
step_id = 'step_id_example' # str | 
parameter_name = 'parameter_name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.add_step_parameter(bt_locator, step_id, parameter_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_step_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **step_id** | **str**|  | 
 **parameter_name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_trigger**
> Trigger add_trigger(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.Trigger() # Trigger |  (optional)

try:
    api_response = api_instance.add_trigger(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**Trigger**](Trigger.md)|  | [optional] 

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vcs_root_entry**
> VcsRootEntry add_vcs_root_entry(bt_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
body = teamcity.VcsRootEntry() # VcsRootEntry |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.add_vcs_root_entry(bt_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->add_vcs_root_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **body** | [**VcsRootEntry**](VcsRootEntry.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootEntry**](VcsRootEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_artifact_dep_setting**
> str change_artifact_dep_setting(bt_locator, artifact_dep_locator, field_name, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
artifact_dep_locator = 'artifact_dep_locator_example' # str | 
field_name = 'field_name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.change_artifact_dep_setting(bt_locator, artifact_dep_locator, field_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->change_artifact_dep_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **artifact_dep_locator** | **str**|  | 
 **field_name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_feature_setting**
> str change_feature_setting(bt_locator, feature_id, name, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
feature_id = 'feature_id_example' # str | 
name = 'name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.change_feature_setting(bt_locator, feature_id, name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->change_feature_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **feature_id** | **str**|  | 
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

# **change_requirement_setting**
> str change_requirement_setting(bt_locator, agent_requirement_locator, field_name, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
agent_requirement_locator = 'agent_requirement_locator_example' # str | 
field_name = 'field_name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.change_requirement_setting(bt_locator, agent_requirement_locator, field_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->change_requirement_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **agent_requirement_locator** | **str**|  | 
 **field_name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_step_setting**
> str change_step_setting(bt_locator, step_id, field_name, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
step_id = 'step_id_example' # str | 
field_name = 'field_name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.change_step_setting(bt_locator, step_id, field_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->change_step_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **step_id** | **str**|  | 
 **field_name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_trigger_setting**
> str change_trigger_setting(bt_locator, trigger_locator, field_name, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
trigger_locator = 'trigger_locator_example' # str | 
field_name = 'field_name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.change_trigger_setting(bt_locator, trigger_locator, field_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->change_trigger_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **trigger_locator** | **str**|  | 
 **field_name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_requirement**
> delete_agent_requirement(bt_locator, agent_requirement_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
agent_requirement_locator = 'agent_requirement_locator_example' # str | 

try:
    api_instance.delete_agent_requirement(bt_locator, agent_requirement_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_agent_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **agent_requirement_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_parameters**
> delete_all_parameters(bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 

try:
    api_instance.delete_all_parameters(bt_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_all_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_parameters_0**
> delete_all_parameters_0(bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 

try:
    api_instance.delete_all_parameters_0(bt_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_all_parameters_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_dep**
> delete_artifact_dep(bt_locator, artifact_dep_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
artifact_dep_locator = 'artifact_dep_locator_example' # str | 

try:
    api_instance.delete_artifact_dep(bt_locator, artifact_dep_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_artifact_dep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **artifact_dep_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build_type**
> delete_build_type(bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 

try:
    api_instance.delete_build_type(bt_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_build_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature**
> delete_feature(bt_locator, feature_id)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
feature_id = 'feature_id_example' # str | 

try:
    api_instance.delete_feature(bt_locator, feature_id)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **feature_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parameter**
> delete_parameter(name, bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 

try:
    api_instance.delete_parameter(name, bt_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parameter_0**
> delete_parameter_0(name, bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 

try:
    api_instance.delete_parameter_0(name, bt_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_parameter_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_dep**
> delete_snapshot_dep(bt_locator, snapshot_dep_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
snapshot_dep_locator = 'snapshot_dep_locator_example' # str | 

try:
    api_instance.delete_snapshot_dep(bt_locator, snapshot_dep_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_snapshot_dep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **snapshot_dep_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_step**
> delete_step(bt_locator, step_id)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
step_id = 'step_id_example' # str | 

try:
    api_instance.delete_step(bt_locator, step_id)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **step_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_association**
> delete_template_association(bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 

try:
    api_instance.delete_template_association(bt_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_template_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trigger**
> delete_trigger(bt_locator, trigger_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
trigger_locator = 'trigger_locator_example' # str | 

try:
    api_instance.delete_trigger(bt_locator, trigger_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **trigger_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vcs_root_entry**
> delete_vcs_root_entry(bt_locator, vcs_root_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
vcs_root_locator = 'vcs_root_locator_example' # str | 

try:
    api_instance.delete_vcs_root_entry(bt_locator, vcs_root_locator)
except ApiException as e:
    print("Exception when calling BuildTypeApi->delete_vcs_root_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **vcs_root_locator** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_requirement**
> AgentRequirement get_agent_requirement(bt_locator, agent_requirement_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
agent_requirement_locator = 'agent_requirement_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_agent_requirement(bt_locator, agent_requirement_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_agent_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **agent_requirement_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**AgentRequirement**](AgentRequirement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_requirements**
> AgentRequirements get_agent_requirements(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_agent_requirements(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_agent_requirements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**AgentRequirements**](AgentRequirements.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aliases**
> Items get_aliases(bt_locator, field)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.get_aliases(bt_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

[**Items**](Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_dep**
> ArtifactDependency get_artifact_dep(bt_locator, artifact_dep_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
artifact_dep_locator = 'artifact_dep_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_artifact_dep(bt_locator, artifact_dep_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_artifact_dep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **artifact_dep_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**ArtifactDependency**](ArtifactDependency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_dep_setting**
> str get_artifact_dep_setting(bt_locator, artifact_dep_locator, field_name)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
artifact_dep_locator = 'artifact_dep_locator_example' # str | 
field_name = 'field_name_example' # str | 

try:
    api_response = api_instance.get_artifact_dep_setting(bt_locator, artifact_dep_locator, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_artifact_dep_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **artifact_dep_locator** | **str**|  | 
 **field_name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_deps**
> ArtifactDependencies get_artifact_deps(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_artifact_deps(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_artifact_deps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**ArtifactDependencies**](ArtifactDependencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_types**
> BuildTypes get_build_types(locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_build_types(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_build_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildTypes**](BuildTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children**
> Files get_children(path, bt_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
path = 'path_example' # str | 
bt_locator = 'bt_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)

try:
    api_response = api_instance.get_children(path, bt_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **bt_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_children_alias**
> Files get_children_alias(path, bt_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
path = 'path_example' # str | 
bt_locator = 'bt_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)

try:
    api_response = api_instance.get_children_alias(path, bt_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_children_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **bt_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content**
> get_content(path, bt_locator, resolve_parameters=resolve_parameters)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
path = 'path_example' # str | 
bt_locator = 'bt_locator_example' # str | 
resolve_parameters = true # bool |  (optional)

try:
    api_instance.get_content(path, bt_locator, resolve_parameters=resolve_parameters)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **bt_locator** | **str**|  | 
 **resolve_parameters** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_alias**
> get_content_alias(path, bt_locator, resolve_parameters=resolve_parameters)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
path = 'path_example' # str | 
bt_locator = 'bt_locator_example' # str | 
resolve_parameters = true # bool |  (optional)

try:
    api_instance.get_content_alias(path, bt_locator, resolve_parameters=resolve_parameters)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_content_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **bt_locator** | **str**|  | 
 **resolve_parameters** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_vcs_instances**
> VcsRootInstances get_current_vcs_instances(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_current_vcs_instances(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_current_vcs_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootInstances**](VcsRootInstances.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_example_new_project_description**
> NewBuildTypeDescription get_example_new_project_description(bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 

try:
    api_response = api_instance.get_example_new_project_description(bt_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_example_new_project_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 

### Return type

[**NewBuildTypeDescription**](NewBuildTypeDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_example_new_project_description_compatibility_version1**
> NewBuildTypeDescription get_example_new_project_description_compatibility_version1(bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 

try:
    api_response = api_instance.get_example_new_project_description_compatibility_version1(bt_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_example_new_project_description_compatibility_version1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 

### Return type

[**NewBuildTypeDescription**](NewBuildTypeDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature**
> Feature get_feature(bt_locator, feature_id, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
feature_id = 'feature_id_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_feature(bt_locator, feature_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **feature_id** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Feature**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_parameter**
> str get_feature_parameter(bt_locator, feature_id, parameter_name)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
feature_id = 'feature_id_example' # str | 
parameter_name = 'parameter_name_example' # str | 

try:
    api_response = api_instance.get_feature_parameter(bt_locator, feature_id, parameter_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_feature_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **feature_id** | **str**|  | 
 **parameter_name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_parameters**
> Properties get_feature_parameters(bt_locator, feature_id, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
feature_id = 'feature_id_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_feature_parameters(bt_locator, feature_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_feature_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **feature_id** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_setting**
> str get_feature_setting(bt_locator, feature_id, name)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
feature_id = 'feature_id_example' # str | 
name = 'name_example' # str | 

try:
    api_response = api_instance.get_feature_setting(bt_locator, feature_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_feature_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **feature_id** | **str**|  | 
 **name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_features**
> Features get_features(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_features(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Features**](Features.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investigations**
> Investigations get_investigations(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_investigations(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_investigations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Investigations**](Investigations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> file get_metadata(path, bt_locator, fields=fields, resolve_parameters=resolve_parameters)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
path = 'path_example' # str | 
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)

try:
    api_response = api_instance.get_metadata(path, bt_locator, fields=fields, resolve_parameters=resolve_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter**
> ModelProperty get_parameter(name, bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parameter(name, bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 
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
> ModelProperty get_parameter_0(name, bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parameter_0(name, bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_parameter_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_type**
> Type get_parameter_type(name, bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 

try:
    api_response = api_instance.get_parameter_type(name, bt_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_parameter_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 

### Return type

[**Type**](Type.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_type_raw_value**
> str get_parameter_type_raw_value(name, bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 

try:
    api_response = api_instance.get_parameter_type_raw_value(name, bt_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_parameter_type_raw_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_value_long**
> str get_parameter_value_long(name, bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 

try:
    api_response = api_instance.get_parameter_value_long(name, bt_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_parameter_value_long: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_value_long_0**
> str get_parameter_value_long_0(name, bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 

try:
    api_response = api_instance.get_parameter_value_long_0(name, bt_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_parameter_value_long_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameters**
> Properties get_parameters(bt_locator, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parameters(bt_locator, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
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
> Properties get_parameters_0(bt_locator, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_parameters_0(bt_locator, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_parameters_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
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

# **get_requirement_setting**
> str get_requirement_setting(bt_locator, agent_requirement_locator, field_name)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
agent_requirement_locator = 'agent_requirement_locator_example' # str | 
field_name = 'field_name_example' # str | 

try:
    api_response = api_instance.get_requirement_setting(bt_locator, agent_requirement_locator, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_requirement_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **agent_requirement_locator** | **str**|  | 
 **field_name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root**
> Files get_root(bt_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)

try:
    api_response = api_instance.get_root(bt_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 

### Return type

[**Files**](Files.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_file**
> str get_settings_file(bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 

try:
    api_response = api_instance.get_settings_file(bt_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_settings_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_dep**
> SnapshotDependency get_snapshot_dep(bt_locator, snapshot_dep_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
snapshot_dep_locator = 'snapshot_dep_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_snapshot_dep(bt_locator, snapshot_dep_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_snapshot_dep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **snapshot_dep_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**SnapshotDependency**](SnapshotDependency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_deps**
> SnapshotDependencies get_snapshot_deps(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_snapshot_deps(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_snapshot_deps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**SnapshotDependencies**](SnapshotDependencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_step**
> Step get_step(bt_locator, step_id, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
step_id = 'step_id_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_step(bt_locator, step_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **step_id** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Step**](Step.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_step_parameter**
> str get_step_parameter(bt_locator, step_id, parameter_name)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
step_id = 'step_id_example' # str | 
parameter_name = 'parameter_name_example' # str | 

try:
    api_response = api_instance.get_step_parameter(bt_locator, step_id, parameter_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_step_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **step_id** | **str**|  | 
 **parameter_name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_step_parameters**
> Properties get_step_parameters(bt_locator, step_id, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
step_id = 'step_id_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_step_parameters(bt_locator, step_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_step_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **step_id** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](Properties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_step_setting**
> str get_step_setting(bt_locator, step_id, field_name)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
step_id = 'step_id_example' # str | 
field_name = 'field_name_example' # str | 

try:
    api_response = api_instance.get_step_setting(bt_locator, step_id, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_step_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **step_id** | **str**|  | 
 **field_name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_steps**
> Steps get_steps(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_steps(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Steps**](Steps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_association**
> BuildType get_template_association(bt_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
body = 'body_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_template_association(bt_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_template_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **body** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**BuildType**](BuildType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger**
> Trigger get_trigger(bt_locator, trigger_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
trigger_locator = 'trigger_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_trigger(bt_locator, trigger_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **trigger_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger_setting**
> str get_trigger_setting(bt_locator, trigger_locator, field_name)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
trigger_locator = 'trigger_locator_example' # str | 
field_name = 'field_name_example' # str | 

try:
    api_response = api_instance.get_trigger_setting(bt_locator, trigger_locator, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_trigger_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **trigger_locator** | **str**|  | 
 **field_name** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_triggers**
> Triggers get_triggers(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_triggers(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Triggers**](Triggers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_labeling_options**
> VcsLabeling get_vcs_labeling_options(bt_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 

try:
    api_response = api_instance.get_vcs_labeling_options(bt_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_vcs_labeling_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 

### Return type

[**VcsLabeling**](VcsLabeling.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_root_entries**
> VcsRootEntries get_vcs_root_entries(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_vcs_root_entries(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_vcs_root_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootEntries**](VcsRootEntries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_root_entry**
> VcsRootEntry get_vcs_root_entry(bt_locator, vcs_root_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
vcs_root_locator = 'vcs_root_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.get_vcs_root_entry(bt_locator, vcs_root_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_vcs_root_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **vcs_root_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootEntry**](VcsRootEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_root_entry_checkout_rules**
> str get_vcs_root_entry_checkout_rules(bt_locator, vcs_root_locator)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
vcs_root_locator = 'vcs_root_locator_example' # str | 

try:
    api_response = api_instance.get_vcs_root_entry_checkout_rules(bt_locator, vcs_root_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_vcs_root_entry_checkout_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **vcs_root_locator** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zipped**
> get_zipped(path, bt_locator, base_path=base_path, locator=locator, name=name, resolve_parameters=resolve_parameters)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
path = 'path_example' # str | 
bt_locator = 'bt_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
name = 'name_example' # str |  (optional)
resolve_parameters = true # bool |  (optional)

try:
    api_instance.get_zipped(path, bt_locator, base_path=base_path, locator=locator, name=name, resolve_parameters=resolve_parameters)
except ApiException as e:
    print("Exception when calling BuildTypeApi->get_zipped: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **bt_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **resolve_parameters** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_agent_requirement**
> AgentRequirement replace_agent_requirement(bt_locator, agent_requirement_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
agent_requirement_locator = 'agent_requirement_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.AgentRequirement() # AgentRequirement |  (optional)

try:
    api_response = api_instance.replace_agent_requirement(bt_locator, agent_requirement_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_agent_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **agent_requirement_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**AgentRequirement**](AgentRequirement.md)|  | [optional] 

### Return type

[**AgentRequirement**](AgentRequirement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_agent_requirements**
> AgentRequirements replace_agent_requirements(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.AgentRequirements() # AgentRequirements |  (optional)

try:
    api_response = api_instance.replace_agent_requirements(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_agent_requirements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**AgentRequirements**](AgentRequirements.md)|  | [optional] 

### Return type

[**AgentRequirements**](AgentRequirements.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_artifact_dep**
> ArtifactDependency replace_artifact_dep(bt_locator, artifact_dep_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
artifact_dep_locator = 'artifact_dep_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.ArtifactDependency() # ArtifactDependency |  (optional)

try:
    api_response = api_instance.replace_artifact_dep(bt_locator, artifact_dep_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_artifact_dep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **artifact_dep_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**ArtifactDependency**](ArtifactDependency.md)|  | [optional] 

### Return type

[**ArtifactDependency**](ArtifactDependency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_artifact_deps**
> ArtifactDependencies replace_artifact_deps(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.ArtifactDependencies() # ArtifactDependencies |  (optional)

try:
    api_response = api_instance.replace_artifact_deps(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_artifact_deps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**ArtifactDependencies**](ArtifactDependencies.md)|  | [optional] 

### Return type

[**ArtifactDependencies**](ArtifactDependencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_feature**
> Feature replace_feature(bt_locator, feature_id, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
feature_id = 'feature_id_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.Feature() # Feature |  (optional)

try:
    api_response = api_instance.replace_feature(bt_locator, feature_id, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **feature_id** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**Feature**](Feature.md)|  | [optional] 

### Return type

[**Feature**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_feature_parameters**
> Properties replace_feature_parameters(bt_locator, feature_id, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
feature_id = 'feature_id_example' # str | 
body = teamcity.Properties() # Properties |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.replace_feature_parameters(bt_locator, feature_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_feature_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **feature_id** | **str**|  | 
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

# **replace_features**
> Features replace_features(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.Features() # Features |  (optional)

try:
    api_response = api_instance.replace_features(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**Features**](Features.md)|  | [optional] 

### Return type

[**Features**](Features.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_snapshot_dep**
> SnapshotDependency replace_snapshot_dep(bt_locator, snapshot_dep_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
snapshot_dep_locator = 'snapshot_dep_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.SnapshotDependency() # SnapshotDependency |  (optional)

try:
    api_response = api_instance.replace_snapshot_dep(bt_locator, snapshot_dep_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_snapshot_dep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **snapshot_dep_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**SnapshotDependency**](SnapshotDependency.md)|  | [optional] 

### Return type

[**SnapshotDependency**](SnapshotDependency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_snapshot_deps**
> SnapshotDependencies replace_snapshot_deps(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.SnapshotDependencies() # SnapshotDependencies |  (optional)

try:
    api_response = api_instance.replace_snapshot_deps(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_snapshot_deps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**SnapshotDependencies**](SnapshotDependencies.md)|  | [optional] 

### Return type

[**SnapshotDependencies**](SnapshotDependencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_step**
> Step replace_step(bt_locator, step_id, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
step_id = 'step_id_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.Step() # Step |  (optional)

try:
    api_response = api_instance.replace_step(bt_locator, step_id, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **step_id** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**Step**](Step.md)|  | [optional] 

### Return type

[**Step**](Step.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_step_parameters**
> Properties replace_step_parameters(bt_locator, step_id, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
step_id = 'step_id_example' # str | 
body = teamcity.Properties() # Properties |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.replace_step_parameters(bt_locator, step_id, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_step_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **step_id** | **str**|  | 
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

# **replace_steps**
> Steps replace_steps(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.Steps() # Steps |  (optional)

try:
    api_response = api_instance.replace_steps(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**Steps**](Steps.md)|  | [optional] 

### Return type

[**Steps**](Steps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_trigger**
> Trigger replace_trigger(bt_locator, trigger_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
trigger_locator = 'trigger_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.Trigger() # Trigger |  (optional)

try:
    api_response = api_instance.replace_trigger(bt_locator, trigger_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **trigger_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**Trigger**](Trigger.md)|  | [optional] 

### Return type

[**Trigger**](Trigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_triggers**
> Triggers replace_triggers(bt_locator, fields=fields, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)
body = teamcity.Triggers() # Triggers |  (optional)

try:
    api_response = api_instance.replace_triggers(bt_locator, fields=fields, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **body** | [**Triggers**](Triggers.md)|  | [optional] 

### Return type

[**Triggers**](Triggers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_vcs_root_entries**
> VcsRootEntries replace_vcs_root_entries(bt_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
body = teamcity.VcsRootEntries() # VcsRootEntries |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.replace_vcs_root_entries(bt_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->replace_vcs_root_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **body** | [**VcsRootEntries**](VcsRootEntries.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootEntries**](VcsRootEntries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_branches**
> Branches serve_branches(bt_locator, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_branches(bt_locator, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->serve_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Branches**](Branches.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_field**
> str serve_build_field(bt_locator, build_locator, field)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
build_locator = 'build_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_build_field(bt_locator, build_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->serve_build_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **serve_build_type_builds_tags**
> Tags serve_build_type_builds_tags(bt_locator, field)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_build_type_builds_tags(bt_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->serve_build_type_builds_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

[**Tags**](Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_build_type_field**
> str serve_build_type_field(bt_locator, field)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = api_instance.serve_build_type_field(bt_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->serve_build_type_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **serve_build_type_template**
> BuildType serve_build_type_template(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_type_template(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->serve_build_type_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **serve_build_type_xml**
> BuildType serve_build_type_xml(bt_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_type_xml(bt_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->serve_build_type_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **serve_build_with_project**
> Build serve_build_with_project(bt_locator, build_locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
build_locator = 'build_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.serve_build_with_project(bt_locator, build_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->serve_build_with_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
> Builds serve_builds(bt_locator, status=status, triggered_by_user=triggered_by_user, include_personal=include_personal, include_canceled=include_canceled, only_pinned=only_pinned, tag=tag, agent_name=agent_name, since_build=since_build, since_date=since_date, start=start, count=count, locator=locator, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
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
    api_response = api_instance.serve_builds(bt_locator, status=status, triggered_by_user=triggered_by_user, include_personal=include_personal, include_canceled=include_canceled, only_pinned=only_pinned, tag=tag, agent_name=agent_name, since_build=since_build, since_date=since_date, start=start, count=count, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->serve_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **set_build_type_field**
> str set_build_type_field(bt_locator, field, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_build_type_field(bt_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_build_type_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
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

# **set_parameter**
> ModelProperty set_parameter(bt_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
body = teamcity.ModelProperty() # ModelProperty |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter(bt_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
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
> ModelProperty set_parameter_0(name, bt_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 
body = teamcity.ModelProperty() # ModelProperty |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_0(name, bt_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameter_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 
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
> ModelProperty set_parameter_1(bt_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
body = teamcity.ModelProperty() # ModelProperty |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_1(bt_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameter_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
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

# **set_parameter_2**
> ModelProperty set_parameter_2(name, bt_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 
body = teamcity.ModelProperty() # ModelProperty |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_2(name, bt_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameter_2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 
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

# **set_parameter_type**
> Type set_parameter_type(name, bt_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 
body = teamcity.Type() # Type |  (optional)

try:
    api_response = api_instance.set_parameter_type(name, bt_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameter_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 
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
> str set_parameter_type_raw_value(name, bt_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_type_raw_value(name, bt_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameter_type_raw_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 
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
> str set_parameter_value_long(name, bt_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_value_long(name, bt_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameter_value_long: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 
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
> str set_parameter_value_long_0(name, bt_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
name = 'name_example' # str | 
bt_locator = 'bt_locator_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.set_parameter_value_long_0(name, bt_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameter_value_long_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bt_locator** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameters**
> Properties set_parameters(bt_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
body = teamcity.Properties() # Properties |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameters(bt_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
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
> Properties set_parameters_0(bt_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
body = teamcity.Properties() # Properties |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.set_parameters_0(bt_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_parameters_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
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

# **set_vcs_labeling_options**
> VcsLabeling set_vcs_labeling_options(bt_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
body = teamcity.VcsLabeling() # VcsLabeling |  (optional)

try:
    api_response = api_instance.set_vcs_labeling_options(bt_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->set_vcs_labeling_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **body** | [**VcsLabeling**](VcsLabeling.md)|  | [optional] 

### Return type

[**VcsLabeling**](VcsLabeling.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vcs_root_entry**
> VcsRootEntry update_vcs_root_entry(bt_locator, vcs_root_locator, body=body, fields=fields)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
vcs_root_locator = 'vcs_root_locator_example' # str | 
body = teamcity.VcsRootEntry() # VcsRootEntry |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = api_instance.update_vcs_root_entry(bt_locator, vcs_root_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->update_vcs_root_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **vcs_root_locator** | **str**|  | 
 **body** | [**VcsRootEntry**](VcsRootEntry.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootEntry**](VcsRootEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vcs_root_entry_checkout_rules**
> str update_vcs_root_entry_checkout_rules(bt_locator, vcs_root_locator, body=body)



### Example
```python
from __future__ import print_function
import time
import teamcity
from teamcity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = teamcity.BuildTypeApi()
bt_locator = 'bt_locator_example' # str | 
vcs_root_locator = 'vcs_root_locator_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.update_vcs_root_entry_checkout_rules(bt_locator, vcs_root_locator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildTypeApi->update_vcs_root_entry_checkout_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_locator** | **str**|  | 
 **vcs_root_locator** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

