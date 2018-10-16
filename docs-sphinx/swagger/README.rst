## Documentation for API Endpoints



sadfasldf

All URIs are relative to *https://teamcity.example.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentApi* | [**delete_agent**](api/AgentApi.md#delete_agent) | **DELETE** /app/rest/agents/{agentLocator} | 
*AgentApi* | [**get_agent_pool**](api/AgentApi.md#get_agent_pool) | **GET** /app/rest/agents/{agentLocator}/pool | 
*AgentApi* | [**get_authorized_info**](api/AgentApi.md#get_authorized_info) | **GET** /app/rest/agents/{agentLocator}/authorizedInfo | 
*AgentApi* | [**get_compatible_build_types**](api/AgentApi.md#get_compatible_build_types) | **GET** /app/rest/agents/{agentLocator}/compatibleBuildTypes | 
*AgentApi* | [**get_enabled_info**](api/AgentApi.md#get_enabled_info) | **GET** /app/rest/agents/{agentLocator}/enabledInfo | 
*AgentApi* | [**get_incompatible_build_types**](api/AgentApi.md#get_incompatible_build_types) | **GET** /app/rest/agents/{agentLocator}/incompatibleBuildTypes | 
*AgentApi* | [**serve_agent**](api/AgentApi.md#serve_agent) | **GET** /app/rest/agents/{agentLocator} | 
*AgentApi* | [**serve_agent_field**](api/AgentApi.md#serve_agent_field) | **GET** /app/rest/agents/{agentLocator}/{field} | 
*AgentApi* | [**serve_agents**](api/AgentApi.md#serve_agents) | **GET** /app/rest/agents | 
*AgentApi* | [**set_agent_field**](api/AgentApi.md#set_agent_field) | **PUT** /app/rest/agents/{agentLocator}/{field} | 
*AgentApi* | [**set_agent_pool**](api/AgentApi.md#set_agent_pool) | **PUT** /app/rest/agents/{agentLocator}/pool | 
*AgentApi* | [**set_authorized_info**](api/AgentApi.md#set_authorized_info) | **PUT** /app/rest/agents/{agentLocator}/authorizedInfo | 
*AgentApi* | [**set_enabled_info**](api/AgentApi.md#set_enabled_info) | **PUT** /app/rest/agents/{agentLocator}/enabledInfo | 
*AgentPoolApi* | [**add_agent**](api/AgentPoolApi.md#add_agent) | **POST** /app/rest/agentPools/{agentPoolLocator}/agents | 
*AgentPoolApi* | [**add_project**](api/AgentPoolApi.md#add_project) | **POST** /app/rest/agentPools/{agentPoolLocator}/projects | 
*AgentPoolApi* | [**create_pool**](api/AgentPoolApi.md#create_pool) | **POST** /app/rest/agentPools | 
*AgentPoolApi* | [**delete_pool**](api/AgentPoolApi.md#delete_pool) | **DELETE** /app/rest/agentPools/{agentPoolLocator} | 
*AgentPoolApi* | [**delete_pool_project**](api/AgentPoolApi.md#delete_pool_project) | **DELETE** /app/rest/agentPools/{agentPoolLocator}/projects/{projectLocator} | 
*AgentPoolApi* | [**delete_projects**](api/AgentPoolApi.md#delete_projects) | **DELETE** /app/rest/agentPools/{agentPoolLocator}/projects | 
*AgentPoolApi* | [**get_field**](api/AgentPoolApi.md#get_field) | **GET** /app/rest/agentPools/{agentPoolLocator}/{field} | 
*AgentPoolApi* | [**get_pool**](api/AgentPoolApi.md#get_pool) | **GET** /app/rest/agentPools/{agentPoolLocator} | 
*AgentPoolApi* | [**get_pool_agents**](api/AgentPoolApi.md#get_pool_agents) | **GET** /app/rest/agentPools/{agentPoolLocator}/agents | 
*AgentPoolApi* | [**get_pool_project**](api/AgentPoolApi.md#get_pool_project) | **GET** /app/rest/agentPools/{agentPoolLocator}/projects/{projectLocator} | 
*AgentPoolApi* | [**get_pool_projects**](api/AgentPoolApi.md#get_pool_projects) | **GET** /app/rest/agentPools/{agentPoolLocator}/projects | 
*AgentPoolApi* | [**get_pools**](api/AgentPoolApi.md#get_pools) | **GET** /app/rest/agentPools | 
*AgentPoolApi* | [**replace_projects**](api/AgentPoolApi.md#replace_projects) | **PUT** /app/rest/agentPools/{agentPoolLocator}/projects | 
*AgentPoolApi* | [**set_field**](api/AgentPoolApi.md#set_field) | **PUT** /app/rest/agentPools/{agentPoolLocator}/{field} | 
*BuildApi* | [**add_tags**](api/BuildApi.md#add_tags) | **POST** /app/rest/builds/{buildLocator}/tags | 
*BuildApi* | [**cancel_build**](api/BuildApi.md#cancel_build) | **POST** /app/rest/builds/{buildLocator} | 
*BuildApi* | [**cancel_build_0**](api/BuildApi.md#cancel_build_0) | **GET** /app/rest/builds/{buildLocator}/example/buildCancelRequest | 
*BuildApi* | [**delete_build**](api/BuildApi.md#delete_build) | **DELETE** /app/rest/builds/{buildLocator} | 
*BuildApi* | [**delete_builds**](api/BuildApi.md#delete_builds) | **DELETE** /app/rest/builds | 
*BuildApi* | [**delete_comment**](api/BuildApi.md#delete_comment) | **DELETE** /app/rest/builds/{buildLocator}/comment | 
*BuildApi* | [**get_artifacts_directory**](api/BuildApi.md#get_artifacts_directory) | **GET** /app/rest/builds/{buildLocator}/artifactsDirectory | 
*BuildApi* | [**get_canceled_info**](api/BuildApi.md#get_canceled_info) | **GET** /app/rest/builds/{buildLocator}/canceledInfo | 
*BuildApi* | [**get_children**](api/BuildApi.md#get_children) | **GET** /app/rest/builds/{buildLocator}/artifacts/children{path} | 
*BuildApi* | [**get_children_alias**](api/BuildApi.md#get_children_alias) | **GET** /app/rest/builds/{buildLocator}/artifacts/{path} | 
*BuildApi* | [**get_content**](api/BuildApi.md#get_content) | **GET** /app/rest/builds/{buildLocator}/artifacts/content{path} | 
*BuildApi* | [**get_content_alias**](api/BuildApi.md#get_content_alias) | **GET** /app/rest/builds/{buildLocator}/artifacts/files{path} | 
*BuildApi* | [**get_metadata**](api/BuildApi.md#get_metadata) | **GET** /app/rest/builds/{buildLocator}/artifacts/metadata{path} | 
*BuildApi* | [**get_parameter**](api/BuildApi.md#get_parameter) | **GET** /app/rest/builds/{buildLocator}/resulting-properties/{propertyName} | 
*BuildApi* | [**get_pinned**](api/BuildApi.md#get_pinned) | **GET** /app/rest/builds/{buildLocator}/pin | 
*BuildApi* | [**get_problems**](api/BuildApi.md#get_problems) | **GET** /app/rest/builds/{buildLocator}/problemOccurrences | 
*BuildApi* | [**get_root**](api/BuildApi.md#get_root) | **GET** /app/rest/builds/{buildLocator}/artifacts | 
*BuildApi* | [**get_tests**](api/BuildApi.md#get_tests) | **GET** /app/rest/builds/{buildLocator}/testOccurrences | 
*BuildApi* | [**get_zipped**](api/BuildApi.md#get_zipped) | **GET** /app/rest/builds/{buildLocator}/artifacts/archived{path} | 
*BuildApi* | [**pin_build**](api/BuildApi.md#pin_build) | **PUT** /app/rest/builds/{buildLocator}/pin | 
*BuildApi* | [**replace_comment**](api/BuildApi.md#replace_comment) | **PUT** /app/rest/builds/{buildLocator}/comment | 
*BuildApi* | [**replace_tags**](api/BuildApi.md#replace_tags) | **PUT** /app/rest/builds/{buildLocator}/tags | 
*BuildApi* | [**serve_aggregated_build_status**](api/BuildApi.md#serve_aggregated_build_status) | **GET** /app/rest/builds/aggregated/{buildLocator}/status | 
*BuildApi* | [**serve_aggregated_build_status_icon**](api/BuildApi.md#serve_aggregated_build_status_icon) | **GET** /app/rest/builds/aggregated/{buildLocator}/statusIcon{suffix} | 
*BuildApi* | [**serve_all_builds**](api/BuildApi.md#serve_all_builds) | **GET** /app/rest/builds | 
*BuildApi* | [**serve_build**](api/BuildApi.md#serve_build) | **GET** /app/rest/builds/{buildLocator} | 
*BuildApi* | [**serve_build_actual_parameters**](api/BuildApi.md#serve_build_actual_parameters) | **GET** /app/rest/builds/{buildLocator}/resulting-properties | 
*BuildApi* | [**serve_build_field_by_build_only**](api/BuildApi.md#serve_build_field_by_build_only) | **GET** /app/rest/builds/{buildLocator}/{field} | 
*BuildApi* | [**serve_build_related_issues**](api/BuildApi.md#serve_build_related_issues) | **GET** /app/rest/builds/{buildLocator}/relatedIssues | 
*BuildApi* | [**serve_build_related_issues_old**](api/BuildApi.md#serve_build_related_issues_old) | **GET** /app/rest/builds/{buildLocator}/related-issues | 
*BuildApi* | [**serve_build_statistic_value**](api/BuildApi.md#serve_build_statistic_value) | **GET** /app/rest/builds/{buildLocator}/statistics/{name} | 
*BuildApi* | [**serve_build_statistic_values**](api/BuildApi.md#serve_build_statistic_values) | **GET** /app/rest/builds/{buildLocator}/statistics | 
*BuildApi* | [**serve_build_status_icon**](api/BuildApi.md#serve_build_status_icon) | **GET** /app/rest/builds/{buildLocator}/statusIcon{suffix} | 
*BuildApi* | [**serve_source_file**](api/BuildApi.md#serve_source_file) | **GET** /app/rest/builds/{buildLocator}/sources/files/{fileName} | 
*BuildApi* | [**serve_tags**](api/BuildApi.md#serve_tags) | **GET** /app/rest/builds/{buildLocator}/tags | 
*BuildApi* | [**unpin_build**](api/BuildApi.md#unpin_build) | **DELETE** /app/rest/builds/{buildLocator}/pin | 
*BuildQueueApi* | [**add_tags**](api/BuildQueueApi.md#add_tags) | **POST** /app/rest/buildQueue/{buildLocator}/tags | 
*BuildQueueApi* | [**cancel_build**](api/BuildQueueApi.md#cancel_build) | **GET** /app/rest/buildQueue/{buildLocator}/example/buildCancelRequest | 
*BuildQueueApi* | [**cancel_build_0**](api/BuildQueueApi.md#cancel_build_0) | **POST** /app/rest/buildQueue/{queuedBuildLocator} | 
*BuildQueueApi* | [**delete_build**](api/BuildQueueApi.md#delete_build) | **DELETE** /app/rest/buildQueue/{queuedBuildLocator} | 
*BuildQueueApi* | [**delete_builds_experimental**](api/BuildQueueApi.md#delete_builds_experimental) | **DELETE** /app/rest/buildQueue | 
*BuildQueueApi* | [**get_build**](api/BuildQueueApi.md#get_build) | **GET** /app/rest/buildQueue/{queuedBuildLocator} | 
*BuildQueueApi* | [**get_builds**](api/BuildQueueApi.md#get_builds) | **GET** /app/rest/buildQueue | 
*BuildQueueApi* | [**queue_new_build**](api/BuildQueueApi.md#queue_new_build) | **POST** /app/rest/buildQueue | 
*BuildQueueApi* | [**replace_builds**](api/BuildQueueApi.md#replace_builds) | **PUT** /app/rest/buildQueue | 
*BuildQueueApi* | [**replace_tags**](api/BuildQueueApi.md#replace_tags) | **PUT** /app/rest/buildQueue/{buildLocator}/tags | 
*BuildQueueApi* | [**serve_build_field_by_build_only**](api/BuildQueueApi.md#serve_build_field_by_build_only) | **GET** /app/rest/buildQueue/{buildLocator}/{field} | 
*BuildQueueApi* | [**serve_compatible_agents**](api/BuildQueueApi.md#serve_compatible_agents) | **GET** /app/rest/buildQueue/{queuedBuildLocator}/compatibleAgents | 
*BuildQueueApi* | [**serve_tags**](api/BuildQueueApi.md#serve_tags) | **GET** /app/rest/buildQueue/{buildLocator}/tags | 
*BuildQueueApi* | [**set_build_queue_order**](api/BuildQueueApi.md#set_build_queue_order) | **PUT** /app/rest/buildQueue/order | 
*BuildTypeApi* | [**add_agent_requirement**](api/BuildTypeApi.md#add_agent_requirement) | **POST** /app/rest/buildTypes/{btLocator}/agent-requirements | 
*BuildTypeApi* | [**add_artifact_dep**](api/BuildTypeApi.md#add_artifact_dep) | **POST** /app/rest/buildTypes/{btLocator}/artifact-dependencies | 
*BuildTypeApi* | [**add_build_type**](api/BuildTypeApi.md#add_build_type) | **POST** /app/rest/buildTypes | 
*BuildTypeApi* | [**add_feature**](api/BuildTypeApi.md#add_feature) | **POST** /app/rest/buildTypes/{btLocator}/features | 
*BuildTypeApi* | [**add_feature_parameter**](api/BuildTypeApi.md#add_feature_parameter) | **PUT** /app/rest/buildTypes/{btLocator}/features/{featureId}/parameters/{parameterName} | 
*BuildTypeApi* | [**add_snapshot_dep**](api/BuildTypeApi.md#add_snapshot_dep) | **POST** /app/rest/buildTypes/{btLocator}/snapshot-dependencies | 
*BuildTypeApi* | [**add_step**](api/BuildTypeApi.md#add_step) | **POST** /app/rest/buildTypes/{btLocator}/steps | 
*BuildTypeApi* | [**add_step_parameter**](api/BuildTypeApi.md#add_step_parameter) | **PUT** /app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters/{parameterName} | 
*BuildTypeApi* | [**add_trigger**](api/BuildTypeApi.md#add_trigger) | **POST** /app/rest/buildTypes/{btLocator}/triggers | 
*BuildTypeApi* | [**add_vcs_root_entry**](api/BuildTypeApi.md#add_vcs_root_entry) | **POST** /app/rest/buildTypes/{btLocator}/vcs-root-entries | 
*BuildTypeApi* | [**change_artifact_dep_setting**](api/BuildTypeApi.md#change_artifact_dep_setting) | **PUT** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}/{fieldName} | 
*BuildTypeApi* | [**change_feature_setting**](api/BuildTypeApi.md#change_feature_setting) | **PUT** /app/rest/buildTypes/{btLocator}/features/{featureId}/{name} | 
*BuildTypeApi* | [**change_requirement_setting**](api/BuildTypeApi.md#change_requirement_setting) | **PUT** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}/{fieldName} | 
*BuildTypeApi* | [**change_step_setting**](api/BuildTypeApi.md#change_step_setting) | **PUT** /app/rest/buildTypes/{btLocator}/steps/{stepId}/{fieldName} | 
*BuildTypeApi* | [**change_trigger_setting**](api/BuildTypeApi.md#change_trigger_setting) | **PUT** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}/{fieldName} | 
*BuildTypeApi* | [**delete_agent_requirement**](api/BuildTypeApi.md#delete_agent_requirement) | **DELETE** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator} | 
*BuildTypeApi* | [**delete_all_parameters**](api/BuildTypeApi.md#delete_all_parameters) | **DELETE** /app/rest/buildTypes/{btLocator}/parameters | 
*BuildTypeApi* | [**delete_all_parameters_0**](api/BuildTypeApi.md#delete_all_parameters_0) | **DELETE** /app/rest/buildTypes/{btLocator}/settings | 
*BuildTypeApi* | [**delete_artifact_dep**](api/BuildTypeApi.md#delete_artifact_dep) | **DELETE** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator} | 
*BuildTypeApi* | [**delete_build_type**](api/BuildTypeApi.md#delete_build_type) | **DELETE** /app/rest/buildTypes/{btLocator} | 
*BuildTypeApi* | [**delete_feature**](api/BuildTypeApi.md#delete_feature) | **DELETE** /app/rest/buildTypes/{btLocator}/features/{featureId} | 
*BuildTypeApi* | [**delete_parameter**](api/BuildTypeApi.md#delete_parameter) | **DELETE** /app/rest/buildTypes/{btLocator}/parameters/{name} | 
*BuildTypeApi* | [**delete_parameter_0**](api/BuildTypeApi.md#delete_parameter_0) | **DELETE** /app/rest/buildTypes/{btLocator}/settings/{name} | 
*BuildTypeApi* | [**delete_snapshot_dep**](api/BuildTypeApi.md#delete_snapshot_dep) | **DELETE** /app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator} | 
*BuildTypeApi* | [**delete_step**](api/BuildTypeApi.md#delete_step) | **DELETE** /app/rest/buildTypes/{btLocator}/steps/{stepId} | 
*BuildTypeApi* | [**delete_template_association**](api/BuildTypeApi.md#delete_template_association) | **DELETE** /app/rest/buildTypes/{btLocator}/template | 
*BuildTypeApi* | [**delete_trigger**](api/BuildTypeApi.md#delete_trigger) | **DELETE** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator} | 
*BuildTypeApi* | [**delete_vcs_root_entry**](api/BuildTypeApi.md#delete_vcs_root_entry) | **DELETE** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator} | 
*BuildTypeApi* | [**get_agent_requirement**](api/BuildTypeApi.md#get_agent_requirement) | **GET** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator} | 
*BuildTypeApi* | [**get_agent_requirements**](api/BuildTypeApi.md#get_agent_requirements) | **GET** /app/rest/buildTypes/{btLocator}/agent-requirements | 
*BuildTypeApi* | [**get_aliases**](api/BuildTypeApi.md#get_aliases) | **GET** /app/rest/buildTypes/{btLocator}/aliases | 
*BuildTypeApi* | [**get_artifact_dep**](api/BuildTypeApi.md#get_artifact_dep) | **GET** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator} | 
*BuildTypeApi* | [**get_artifact_dep_setting**](api/BuildTypeApi.md#get_artifact_dep_setting) | **GET** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}/{fieldName} | 
*BuildTypeApi* | [**get_artifact_deps**](api/BuildTypeApi.md#get_artifact_deps) | **GET** /app/rest/buildTypes/{btLocator}/artifact-dependencies | 
*BuildTypeApi* | [**get_build_types**](api/BuildTypeApi.md#get_build_types) | **GET** /app/rest/buildTypes | 
*BuildTypeApi* | [**get_children**](api/BuildTypeApi.md#get_children) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/children{path} | 
*BuildTypeApi* | [**get_children_alias**](api/BuildTypeApi.md#get_children_alias) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/{path} | 
*BuildTypeApi* | [**get_content**](api/BuildTypeApi.md#get_content) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/content{path} | 
*BuildTypeApi* | [**get_content_alias**](api/BuildTypeApi.md#get_content_alias) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/files{path} | 
*BuildTypeApi* | [**get_current_vcs_instances**](api/BuildTypeApi.md#get_current_vcs_instances) | **GET** /app/rest/buildTypes/{btLocator}/vcs-root-instances | 
*BuildTypeApi* | [**get_example_new_project_description**](api/BuildTypeApi.md#get_example_new_project_description) | **GET** /app/rest/buildTypes/{btLocator}/example/newBuildTypeDescription | 
*BuildTypeApi* | [**get_example_new_project_description_compatibility_version1**](api/BuildTypeApi.md#get_example_new_project_description_compatibility_version1) | **GET** /app/rest/buildTypes/{btLocator}/newBuildTypeDescription | 
*BuildTypeApi* | [**get_feature**](api/BuildTypeApi.md#get_feature) | **GET** /app/rest/buildTypes/{btLocator}/features/{featureId} | 
*BuildTypeApi* | [**get_feature_parameter**](api/BuildTypeApi.md#get_feature_parameter) | **GET** /app/rest/buildTypes/{btLocator}/features/{featureId}/parameters/{parameterName} | 
*BuildTypeApi* | [**get_feature_parameters**](api/BuildTypeApi.md#get_feature_parameters) | **GET** /app/rest/buildTypes/{btLocator}/features/{featureId}/parameters | 
*BuildTypeApi* | [**get_feature_setting**](api/BuildTypeApi.md#get_feature_setting) | **GET** /app/rest/buildTypes/{btLocator}/features/{featureId}/{name} | 
*BuildTypeApi* | [**get_features**](api/BuildTypeApi.md#get_features) | **GET** /app/rest/buildTypes/{btLocator}/features | 
*BuildTypeApi* | [**get_investigations**](api/BuildTypeApi.md#get_investigations) | **GET** /app/rest/buildTypes/{btLocator}/investigations | 
*BuildTypeApi* | [**get_metadata**](api/BuildTypeApi.md#get_metadata) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/metadata{path} | 
*BuildTypeApi* | [**get_parameter**](api/BuildTypeApi.md#get_parameter) | **GET** /app/rest/buildTypes/{btLocator}/parameters/{name} | 
*BuildTypeApi* | [**get_parameter_0**](api/BuildTypeApi.md#get_parameter_0) | **GET** /app/rest/buildTypes/{btLocator}/settings/{name} | 
*BuildTypeApi* | [**get_parameter_type**](api/BuildTypeApi.md#get_parameter_type) | **GET** /app/rest/buildTypes/{btLocator}/parameters/{name}/type | 
*BuildTypeApi* | [**get_parameter_type_raw_value**](api/BuildTypeApi.md#get_parameter_type_raw_value) | **GET** /app/rest/buildTypes/{btLocator}/parameters/{name}/type/rawValue | 
*BuildTypeApi* | [**get_parameter_value_long**](api/BuildTypeApi.md#get_parameter_value_long) | **GET** /app/rest/buildTypes/{btLocator}/parameters/{name}/value | 
*BuildTypeApi* | [**get_parameter_value_long_0**](api/BuildTypeApi.md#get_parameter_value_long_0) | **GET** /app/rest/buildTypes/{btLocator}/settings/{name}/value | 
*BuildTypeApi* | [**get_parameters**](api/BuildTypeApi.md#get_parameters) | **GET** /app/rest/buildTypes/{btLocator}/parameters | 
*BuildTypeApi* | [**get_parameters_0**](api/BuildTypeApi.md#get_parameters_0) | **GET** /app/rest/buildTypes/{btLocator}/settings | 
*BuildTypeApi* | [**get_requirement_setting**](api/BuildTypeApi.md#get_requirement_setting) | **GET** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}/{fieldName} | 
*BuildTypeApi* | [**get_root**](api/BuildTypeApi.md#get_root) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest | 
*BuildTypeApi* | [**get_settings_file**](api/BuildTypeApi.md#get_settings_file) | **GET** /app/rest/buildTypes/{btLocator}/settingsFile | 
*BuildTypeApi* | [**get_snapshot_dep**](api/BuildTypeApi.md#get_snapshot_dep) | **GET** /app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator} | 
*BuildTypeApi* | [**get_snapshot_deps**](api/BuildTypeApi.md#get_snapshot_deps) | **GET** /app/rest/buildTypes/{btLocator}/snapshot-dependencies | 
*BuildTypeApi* | [**get_step**](api/BuildTypeApi.md#get_step) | **GET** /app/rest/buildTypes/{btLocator}/steps/{stepId} | 
*BuildTypeApi* | [**get_step_parameter**](api/BuildTypeApi.md#get_step_parameter) | **GET** /app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters/{parameterName} | 
*BuildTypeApi* | [**get_step_parameters**](api/BuildTypeApi.md#get_step_parameters) | **GET** /app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters | 
*BuildTypeApi* | [**get_step_setting**](api/BuildTypeApi.md#get_step_setting) | **GET** /app/rest/buildTypes/{btLocator}/steps/{stepId}/{fieldName} | 
*BuildTypeApi* | [**get_steps**](api/BuildTypeApi.md#get_steps) | **GET** /app/rest/buildTypes/{btLocator}/steps | 
*BuildTypeApi* | [**get_template_association**](api/BuildTypeApi.md#get_template_association) | **PUT** /app/rest/buildTypes/{btLocator}/template | 
*BuildTypeApi* | [**get_trigger**](api/BuildTypeApi.md#get_trigger) | **GET** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator} | 
*BuildTypeApi* | [**get_trigger_setting**](api/BuildTypeApi.md#get_trigger_setting) | **GET** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}/{fieldName} | 
*BuildTypeApi* | [**get_triggers**](api/BuildTypeApi.md#get_triggers) | **GET** /app/rest/buildTypes/{btLocator}/triggers | 
*BuildTypeApi* | [**get_vcs_labeling_options**](api/BuildTypeApi.md#get_vcs_labeling_options) | **GET** /app/rest/buildTypes/{btLocator}/vcsLabeling | 
*BuildTypeApi* | [**get_vcs_root_entries**](api/BuildTypeApi.md#get_vcs_root_entries) | **GET** /app/rest/buildTypes/{btLocator}/vcs-root-entries | 
*BuildTypeApi* | [**get_vcs_root_entry**](api/BuildTypeApi.md#get_vcs_root_entry) | **GET** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator} | 
*BuildTypeApi* | [**get_vcs_root_entry_checkout_rules**](api/BuildTypeApi.md#get_vcs_root_entry_checkout_rules) | **GET** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}/checkout-rules | 
*BuildTypeApi* | [**get_zipped**](api/BuildTypeApi.md#get_zipped) | **GET** /app/rest/buildTypes/{btLocator}/vcs/files/latest/archived{path} | 
*BuildTypeApi* | [**replace_agent_requirement**](api/BuildTypeApi.md#replace_agent_requirement) | **PUT** /app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator} | 
*BuildTypeApi* | [**replace_agent_requirements**](api/BuildTypeApi.md#replace_agent_requirements) | **PUT** /app/rest/buildTypes/{btLocator}/agent-requirements | 
*BuildTypeApi* | [**replace_artifact_dep**](api/BuildTypeApi.md#replace_artifact_dep) | **PUT** /app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator} | 
*BuildTypeApi* | [**replace_artifact_deps**](api/BuildTypeApi.md#replace_artifact_deps) | **PUT** /app/rest/buildTypes/{btLocator}/artifact-dependencies | 
*BuildTypeApi* | [**replace_feature**](api/BuildTypeApi.md#replace_feature) | **PUT** /app/rest/buildTypes/{btLocator}/features/{featureId} | 
*BuildTypeApi* | [**replace_feature_parameters**](api/BuildTypeApi.md#replace_feature_parameters) | **PUT** /app/rest/buildTypes/{btLocator}/features/{featureId}/parameters | 
*BuildTypeApi* | [**replace_features**](api/BuildTypeApi.md#replace_features) | **PUT** /app/rest/buildTypes/{btLocator}/features | 
*BuildTypeApi* | [**replace_snapshot_dep**](api/BuildTypeApi.md#replace_snapshot_dep) | **PUT** /app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator} | 
*BuildTypeApi* | [**replace_snapshot_deps**](api/BuildTypeApi.md#replace_snapshot_deps) | **PUT** /app/rest/buildTypes/{btLocator}/snapshot-dependencies | 
*BuildTypeApi* | [**replace_step**](api/BuildTypeApi.md#replace_step) | **PUT** /app/rest/buildTypes/{btLocator}/steps/{stepId} | 
*BuildTypeApi* | [**replace_step_parameters**](api/BuildTypeApi.md#replace_step_parameters) | **PUT** /app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters | 
*BuildTypeApi* | [**replace_steps**](api/BuildTypeApi.md#replace_steps) | **PUT** /app/rest/buildTypes/{btLocator}/steps | 
*BuildTypeApi* | [**replace_trigger**](api/BuildTypeApi.md#replace_trigger) | **PUT** /app/rest/buildTypes/{btLocator}/triggers/{triggerLocator} | 
*BuildTypeApi* | [**replace_triggers**](api/BuildTypeApi.md#replace_triggers) | **PUT** /app/rest/buildTypes/{btLocator}/triggers | 
*BuildTypeApi* | [**replace_vcs_root_entries**](api/BuildTypeApi.md#replace_vcs_root_entries) | **PUT** /app/rest/buildTypes/{btLocator}/vcs-root-entries | 
*BuildTypeApi* | [**serve_branches**](api/BuildTypeApi.md#serve_branches) | **GET** /app/rest/buildTypes/{btLocator}/branches | 
*BuildTypeApi* | [**serve_build_field**](api/BuildTypeApi.md#serve_build_field) | **GET** /app/rest/buildTypes/{btLocator}/builds/{buildLocator}/{field} | 
*BuildTypeApi* | [**serve_build_type_builds_tags**](api/BuildTypeApi.md#serve_build_type_builds_tags) | **GET** /app/rest/buildTypes/{btLocator}/buildTags | 
*BuildTypeApi* | [**serve_build_type_field**](api/BuildTypeApi.md#serve_build_type_field) | **GET** /app/rest/buildTypes/{btLocator}/{field} | 
*BuildTypeApi* | [**serve_build_type_template**](api/BuildTypeApi.md#serve_build_type_template) | **GET** /app/rest/buildTypes/{btLocator}/template | 
*BuildTypeApi* | [**serve_build_type_xml**](api/BuildTypeApi.md#serve_build_type_xml) | **GET** /app/rest/buildTypes/{btLocator} | 
*BuildTypeApi* | [**serve_build_with_project**](api/BuildTypeApi.md#serve_build_with_project) | **GET** /app/rest/buildTypes/{btLocator}/builds/{buildLocator} | 
*BuildTypeApi* | [**serve_builds**](api/BuildTypeApi.md#serve_builds) | **GET** /app/rest/buildTypes/{btLocator}/builds | 
*BuildTypeApi* | [**set_build_type_field**](api/BuildTypeApi.md#set_build_type_field) | **PUT** /app/rest/buildTypes/{btLocator}/{field} | 
*BuildTypeApi* | [**set_parameter**](api/BuildTypeApi.md#set_parameter) | **POST** /app/rest/buildTypes/{btLocator}/parameters | 
*BuildTypeApi* | [**set_parameter_0**](api/BuildTypeApi.md#set_parameter_0) | **PUT** /app/rest/buildTypes/{btLocator}/parameters/{name} | 
*BuildTypeApi* | [**set_parameter_1**](api/BuildTypeApi.md#set_parameter_1) | **POST** /app/rest/buildTypes/{btLocator}/settings | 
*BuildTypeApi* | [**set_parameter_2**](api/BuildTypeApi.md#set_parameter_2) | **PUT** /app/rest/buildTypes/{btLocator}/settings/{name} | 
*BuildTypeApi* | [**set_parameter_type**](api/BuildTypeApi.md#set_parameter_type) | **PUT** /app/rest/buildTypes/{btLocator}/parameters/{name}/type | 
*BuildTypeApi* | [**set_parameter_type_raw_value**](api/BuildTypeApi.md#set_parameter_type_raw_value) | **PUT** /app/rest/buildTypes/{btLocator}/parameters/{name}/type/rawValue | 
*BuildTypeApi* | [**set_parameter_value_long**](api/BuildTypeApi.md#set_parameter_value_long) | **PUT** /app/rest/buildTypes/{btLocator}/parameters/{name}/value | 
*BuildTypeApi* | [**set_parameter_value_long_0**](api/BuildTypeApi.md#set_parameter_value_long_0) | **PUT** /app/rest/buildTypes/{btLocator}/settings/{name}/value | 
*BuildTypeApi* | [**set_parameters**](api/BuildTypeApi.md#set_parameters) | **PUT** /app/rest/buildTypes/{btLocator}/parameters | 
*BuildTypeApi* | [**set_parameters_0**](api/BuildTypeApi.md#set_parameters_0) | **PUT** /app/rest/buildTypes/{btLocator}/settings | 
*BuildTypeApi* | [**set_vcs_labeling_options**](api/BuildTypeApi.md#set_vcs_labeling_options) | **PUT** /app/rest/buildTypes/{btLocator}/vcsLabeling | 
*BuildTypeApi* | [**update_vcs_root_entry**](api/BuildTypeApi.md#update_vcs_root_entry) | **PUT** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator} | 
*BuildTypeApi* | [**update_vcs_root_entry_checkout_rules**](api/BuildTypeApi.md#update_vcs_root_entry_checkout_rules) | **PUT** /app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}/checkout-rules | 
*ChangeApi* | [**get_change_attributes**](api/ChangeApi.md#get_change_attributes) | **GET** /app/rest/changes/{changeLocator}/attributes | 
*ChangeApi* | [**get_change_duplicates**](api/ChangeApi.md#get_change_duplicates) | **GET** /app/rest/changes/{changeLocator}/duplicates | 
*ChangeApi* | [**get_change_field**](api/ChangeApi.md#get_change_field) | **GET** /app/rest/changes/{changeLocator}/{field} | 
*ChangeApi* | [**get_change_first_builds**](api/ChangeApi.md#get_change_first_builds) | **GET** /app/rest/changes/{changeLocator}/firstBuilds | 
*ChangeApi* | [**get_change_issue**](api/ChangeApi.md#get_change_issue) | **GET** /app/rest/changes/{changeLocator}/issues | 
*ChangeApi* | [**get_change_parent_revisions**](api/ChangeApi.md#get_change_parent_revisions) | **GET** /app/rest/changes/{changeLocator}/parentRevisions | 
*ChangeApi* | [**get_change_vcs_root**](api/ChangeApi.md#get_change_vcs_root) | **GET** /app/rest/changes/{changeLocator}/vcsRoot | 
*ChangeApi* | [**get_change_vcs_root_instance**](api/ChangeApi.md#get_change_vcs_root_instance) | **GET** /app/rest/changes/{changeLocator}/vcsRootInstance | 
*ChangeApi* | [**get_parent_changes**](api/ChangeApi.md#get_parent_changes) | **GET** /app/rest/changes/{changeLocator}/parentChanges | 
*ChangeApi* | [**get_related_build_types**](api/ChangeApi.md#get_related_build_types) | **GET** /app/rest/changes/{changeLocator}/buildTypes | 
*ChangeApi* | [**serve_change**](api/ChangeApi.md#serve_change) | **GET** /app/rest/changes/{changeLocator} | 
*ChangeApi* | [**serve_changes**](api/ChangeApi.md#serve_changes) | **GET** /app/rest/changes | 
*DebugApi* | [**delete_current_remember_me**](api/DebugApi.md#delete_current_remember_me) | **DELETE** /app/rest/debug/currentRequest/rememberMe | 
*DebugApi* | [**empty_task**](api/DebugApi.md#empty_task) | **POST** /app/rest/debug/emptyTask | 
*DebugApi* | [**execute_db_query**](api/DebugApi.md#execute_db_query) | **GET** /app/rest/debug/database/query/{query} | 
*DebugApi* | [**get_current_session**](api/DebugApi.md#get_current_session) | **GET** /app/rest/debug/currentRequest/session | 
*DebugApi* | [**get_current_session_max_inactive_interval**](api/DebugApi.md#get_current_session_max_inactive_interval) | **GET** /app/rest/debug/currentRequest/session/maxInactiveSeconds | 
*DebugApi* | [**get_current_user_permissions**](api/DebugApi.md#get_current_user_permissions) | **GET** /app/rest/debug/currentUserPermissions | 
*DebugApi* | [**get_date**](api/DebugApi.md#get_date) | **GET** /app/rest/debug/date/{dateLocator} | 
*DebugApi* | [**get_environment_variables**](api/DebugApi.md#get_environment_variables) | **GET** /app/rest/debug/jvm/environmentVariables | 
*DebugApi* | [**get_hashed**](api/DebugApi.md#get_hashed) | **GET** /app/rest/debug/values/transform/{method} | 
*DebugApi* | [**get_request_details**](api/DebugApi.md#get_request_details) | **GET** /app/rest/debug/currentRequest/details | 
*DebugApi* | [**get_scrambled**](api/DebugApi.md#get_scrambled) | **GET** /app/rest/debug/values/password/scrambled | 
*DebugApi* | [**get_sessions**](api/DebugApi.md#get_sessions) | **GET** /app/rest/debug/sessions | 
*DebugApi* | [**get_system_properties**](api/DebugApi.md#get_system_properties) | **GET** /app/rest/debug/jvm/systemProperties | 
*DebugApi* | [**get_thread_dump**](api/DebugApi.md#get_thread_dump) | **GET** /app/rest/debug/threadDump | 
*DebugApi* | [**get_unscrambled**](api/DebugApi.md#get_unscrambled) | **GET** /app/rest/debug/values/password/unscrambled | 
*DebugApi* | [**invalidate_current_session**](api/DebugApi.md#invalidate_current_session) | **DELETE** /app/rest/debug/currentRequest/session | 
*DebugApi* | [**list_db_tables**](api/DebugApi.md#list_db_tables) | **GET** /app/rest/debug/database/tables | 
*DebugApi* | [**new_remember_me**](api/DebugApi.md#new_remember_me) | **POST** /app/rest/debug/currentRequest/rememberMe | 
*DebugApi* | [**save_memory_dump**](api/DebugApi.md#save_memory_dump) | **POST** /app/rest/debug/memory/dumps | 
*DebugApi* | [**schedule_checking_for_changes**](api/DebugApi.md#schedule_checking_for_changes) | **POST** /app/rest/debug/vcsCheckingForChangesQueue | 
*DebugApi* | [**set_current_session_max_inactive_interval**](api/DebugApi.md#set_current_session_max_inactive_interval) | **PUT** /app/rest/debug/currentRequest/session/maxInactiveSeconds | 
*FederationApi* | [**add_server**](api/FederationApi.md#add_server) | **PUT** /app/rest/federation/servers | 
*FederationApi* | [**servers**](api/FederationApi.md#servers) | **GET** /app/rest/federation/servers | 
*GroupApi* | [**add_group**](api/GroupApi.md#add_group) | **POST** /app/rest/userGroups | 
*GroupApi* | [**add_role**](api/GroupApi.md#add_role) | **POST** /app/rest/userGroups/{groupLocator}/roles | 
*GroupApi* | [**add_role_put**](api/GroupApi.md#add_role_put) | **PUT** /app/rest/userGroups/{groupLocator}/roles | 
*GroupApi* | [**add_role_simple**](api/GroupApi.md#add_role_simple) | **POST** /app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope} | 
*GroupApi* | [**delete_group**](api/GroupApi.md#delete_group) | **DELETE** /app/rest/userGroups/{groupLocator} | 
*GroupApi* | [**delete_role**](api/GroupApi.md#delete_role) | **DELETE** /app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope} | 
*GroupApi* | [**get_permissions**](api/GroupApi.md#get_permissions) | **GET** /app/rest/userGroups/{groupLocator}/debug/permissions | 
*GroupApi* | [**get_properties**](api/GroupApi.md#get_properties) | **GET** /app/rest/userGroups/{groupLocator}/properties | 
*GroupApi* | [**list_role**](api/GroupApi.md#list_role) | **GET** /app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope} | 
*GroupApi* | [**list_roles**](api/GroupApi.md#list_roles) | **GET** /app/rest/userGroups/{groupLocator}/roles | 
*GroupApi* | [**put_user_property**](api/GroupApi.md#put_user_property) | **PUT** /app/rest/userGroups/{groupLocator}/properties/{name} | 
*GroupApi* | [**remove_user_property**](api/GroupApi.md#remove_user_property) | **DELETE** /app/rest/userGroups/{groupLocator}/properties/{name} | 
*GroupApi* | [**serve_group**](api/GroupApi.md#serve_group) | **GET** /app/rest/userGroups/{groupLocator} | 
*GroupApi* | [**serve_groups**](api/GroupApi.md#serve_groups) | **GET** /app/rest/userGroups | 
*GroupApi* | [**serve_user_properties**](api/GroupApi.md#serve_user_properties) | **GET** /app/rest/userGroups/{groupLocator}/properties/{name} | 
*InvestigationApi* | [**get_investigations**](api/InvestigationApi.md#get_investigations) | **GET** /app/rest/investigations | 
*InvestigationApi* | [**serve_instance**](api/InvestigationApi.md#serve_instance) | **GET** /app/rest/investigations/{investigationLocator} | 
*ProblemApi* | [**get_problems**](api/ProblemApi.md#get_problems) | **GET** /app/rest/problems | 
*ProblemApi* | [**serve_instance**](api/ProblemApi.md#serve_instance) | **GET** /app/rest/problems/{problemLocator} | 
*ProblemOccurrenceApi* | [**get_problems**](api/ProblemOccurrenceApi.md#get_problems) | **GET** /app/rest/problemOccurrences | 
*ProblemOccurrenceApi* | [**serve_instance**](api/ProblemOccurrenceApi.md#serve_instance) | **GET** /app/rest/problemOccurrences/{problemLocator} | 
*ProjectApi* | [**add**](api/ProjectApi.md#add) | **POST** /app/rest/projects/{projectLocator}/projectFeatures | 
*ProjectApi* | [**create_build_type**](api/ProjectApi.md#create_build_type) | **POST** /app/rest/projects/{projectLocator}/buildTypes | 
*ProjectApi* | [**create_build_type_template**](api/ProjectApi.md#create_build_type_template) | **POST** /app/rest/projects/{projectLocator}/templates | 
*ProjectApi* | [**create_project**](api/ProjectApi.md#create_project) | **POST** /app/rest/projects | 
*ProjectApi* | [**delete**](api/ProjectApi.md#delete) | **DELETE** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator} | 
*ProjectApi* | [**delete_all_parameters**](api/ProjectApi.md#delete_all_parameters) | **DELETE** /app/rest/projects/{projectLocator}/parameters | 
*ProjectApi* | [**delete_all_parameters_0**](api/ProjectApi.md#delete_all_parameters_0) | **DELETE** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties | 
*ProjectApi* | [**delete_parameter**](api/ProjectApi.md#delete_parameter) | **DELETE** /app/rest/projects/{projectLocator}/parameters/{name} | 
*ProjectApi* | [**delete_parameter_0**](api/ProjectApi.md#delete_parameter_0) | **DELETE** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name} | 
*ProjectApi* | [**delete_project**](api/ProjectApi.md#delete_project) | **DELETE** /app/rest/projects/{projectLocator} | 
*ProjectApi* | [**delete_project_agent_pools**](api/ProjectApi.md#delete_project_agent_pools) | **DELETE** /app/rest/projects/{projectLocator}/agentPools/{agentPoolLocator} | 
*ProjectApi* | [**get**](api/ProjectApi.md#get) | **GET** /app/rest/projects/{projectLocator}/projectFeatures | 
*ProjectApi* | [**get_build_types_order**](api/ProjectApi.md#get_build_types_order) | **GET** /app/rest/projects/{projectLocator}/order/buildTypes | 
*ProjectApi* | [**get_example_new_project_description**](api/ProjectApi.md#get_example_new_project_description) | **GET** /app/rest/projects/{projectLocator}/example/newProjectDescription | 
*ProjectApi* | [**get_example_new_project_description_compatibility_version1**](api/ProjectApi.md#get_example_new_project_description_compatibility_version1) | **GET** /app/rest/projects/{projectLocator}/newProjectDescription | 
*ProjectApi* | [**get_parameter**](api/ProjectApi.md#get_parameter) | **GET** /app/rest/projects/{projectLocator}/parameters/{name} | 
*ProjectApi* | [**get_parameter_0**](api/ProjectApi.md#get_parameter_0) | **GET** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name} | 
*ProjectApi* | [**get_parameter_type**](api/ProjectApi.md#get_parameter_type) | **GET** /app/rest/projects/{projectLocator}/parameters/{name}/type | 
*ProjectApi* | [**get_parameter_type_raw_value**](api/ProjectApi.md#get_parameter_type_raw_value) | **GET** /app/rest/projects/{projectLocator}/parameters/{name}/type/rawValue | 
*ProjectApi* | [**get_parameter_value_long**](api/ProjectApi.md#get_parameter_value_long) | **GET** /app/rest/projects/{projectLocator}/parameters/{name}/value | 
*ProjectApi* | [**get_parameter_value_long_0**](api/ProjectApi.md#get_parameter_value_long_0) | **GET** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name}/value | 
*ProjectApi* | [**get_parameters**](api/ProjectApi.md#get_parameters) | **GET** /app/rest/projects/{projectLocator}/parameters | 
*ProjectApi* | [**get_parameters_0**](api/ProjectApi.md#get_parameters_0) | **GET** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties | 
*ProjectApi* | [**get_parent_project**](api/ProjectApi.md#get_parent_project) | **GET** /app/rest/projects/{projectLocator}/parentProject | 
*ProjectApi* | [**get_project_agent_pools**](api/ProjectApi.md#get_project_agent_pools) | **GET** /app/rest/projects/{projectLocator}/agentPools | 
*ProjectApi* | [**get_projects_order**](api/ProjectApi.md#get_projects_order) | **GET** /app/rest/projects/{projectLocator}/order/projects | 
*ProjectApi* | [**get_settings_file**](api/ProjectApi.md#get_settings_file) | **GET** /app/rest/projects/{projectLocator}/settingsFile | 
*ProjectApi* | [**get_single**](api/ProjectApi.md#get_single) | **GET** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator} | 
*ProjectApi* | [**reload_settings_file**](api/ProjectApi.md#reload_settings_file) | **GET** /app/rest/projects/{projectLocator}/latest | 
*ProjectApi* | [**replace**](api/ProjectApi.md#replace) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator} | 
*ProjectApi* | [**replace_all**](api/ProjectApi.md#replace_all) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures | 
*ProjectApi* | [**serve_build_field_with_project**](api/ProjectApi.md#serve_build_field_with_project) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator}/builds/{buildLocator}/{field} | 
*ProjectApi* | [**serve_build_type**](api/ProjectApi.md#serve_build_type) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator} | 
*ProjectApi* | [**serve_build_type_field_with_project**](api/ProjectApi.md#serve_build_type_field_with_project) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator}/{field} | 
*ProjectApi* | [**serve_build_type_templates**](api/ProjectApi.md#serve_build_type_templates) | **GET** /app/rest/projects/{projectLocator}/templates/{btLocator} | 
*ProjectApi* | [**serve_build_types_in_project**](api/ProjectApi.md#serve_build_types_in_project) | **GET** /app/rest/projects/{projectLocator}/buildTypes | 
*ProjectApi* | [**serve_build_with_project**](api/ProjectApi.md#serve_build_with_project) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator}/builds/{buildLocator} | 
*ProjectApi* | [**serve_builds**](api/ProjectApi.md#serve_builds) | **GET** /app/rest/projects/{projectLocator}/buildTypes/{btLocator}/builds | 
*ProjectApi* | [**serve_project**](api/ProjectApi.md#serve_project) | **GET** /app/rest/projects/{projectLocator} | 
*ProjectApi* | [**serve_project_field**](api/ProjectApi.md#serve_project_field) | **GET** /app/rest/projects/{projectLocator}/{field} | 
*ProjectApi* | [**serve_projects**](api/ProjectApi.md#serve_projects) | **GET** /app/rest/projects | 
*ProjectApi* | [**serve_templates_in_project**](api/ProjectApi.md#serve_templates_in_project) | **GET** /app/rest/projects/{projectLocator}/templates | 
*ProjectApi* | [**set_build_types_order**](api/ProjectApi.md#set_build_types_order) | **PUT** /app/rest/projects/{projectLocator}/order/buildTypes | 
*ProjectApi* | [**set_parameter**](api/ProjectApi.md#set_parameter) | **POST** /app/rest/projects/{projectLocator}/parameters | 
*ProjectApi* | [**set_parameter_0**](api/ProjectApi.md#set_parameter_0) | **PUT** /app/rest/projects/{projectLocator}/parameters/{name} | 
*ProjectApi* | [**set_parameter_1**](api/ProjectApi.md#set_parameter_1) | **POST** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties | 
*ProjectApi* | [**set_parameter_2**](api/ProjectApi.md#set_parameter_2) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name} | 
*ProjectApi* | [**set_parameter_type**](api/ProjectApi.md#set_parameter_type) | **PUT** /app/rest/projects/{projectLocator}/parameters/{name}/type | 
*ProjectApi* | [**set_parameter_type_raw_value**](api/ProjectApi.md#set_parameter_type_raw_value) | **PUT** /app/rest/projects/{projectLocator}/parameters/{name}/type/rawValue | 
*ProjectApi* | [**set_parameter_value_long**](api/ProjectApi.md#set_parameter_value_long) | **PUT** /app/rest/projects/{projectLocator}/parameters/{name}/value | 
*ProjectApi* | [**set_parameter_value_long_0**](api/ProjectApi.md#set_parameter_value_long_0) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name}/value | 
*ProjectApi* | [**set_parameters**](api/ProjectApi.md#set_parameters) | **PUT** /app/rest/projects/{projectLocator}/parameters | 
*ProjectApi* | [**set_parameters_0**](api/ProjectApi.md#set_parameters_0) | **PUT** /app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties | 
*ProjectApi* | [**set_parent_project**](api/ProjectApi.md#set_parent_project) | **PUT** /app/rest/projects/{projectLocator}/parentProject | 
*ProjectApi* | [**set_project_agent_pools**](api/ProjectApi.md#set_project_agent_pools) | **PUT** /app/rest/projects/{projectLocator}/agentPools | 
*ProjectApi* | [**set_project_agent_pools_0**](api/ProjectApi.md#set_project_agent_pools_0) | **POST** /app/rest/projects/{projectLocator}/agentPools | 
*ProjectApi* | [**set_project_filed**](api/ProjectApi.md#set_project_filed) | **PUT** /app/rest/projects/{projectLocator}/{field} | 
*ProjectApi* | [**set_projects_order**](api/ProjectApi.md#set_projects_order) | **PUT** /app/rest/projects/{projectLocator}/order/projects | 
*ServerApi* | [**add_license_keys**](api/ServerApi.md#add_license_keys) | **POST** /app/rest/server/licensingData/licenseKeys | 
*ServerApi* | [**delete_license_key**](api/ServerApi.md#delete_license_key) | **DELETE** /app/rest/server/licensingData/licenseKeys/{licenseKey} | 
*ServerApi* | [**get_backup_status**](api/ServerApi.md#get_backup_status) | **GET** /app/rest/server/backup | 
*ServerApi* | [**get_children**](api/ServerApi.md#get_children) | **GET** /app/rest/server/files/{areaId}/children{path} | 
*ServerApi* | [**get_children_alias**](api/ServerApi.md#get_children_alias) | **GET** /app/rest/server/files/{areaId}/{path} | 
*ServerApi* | [**get_content**](api/ServerApi.md#get_content) | **GET** /app/rest/server/files/{areaId}/content{path} | 
*ServerApi* | [**get_content_alias**](api/ServerApi.md#get_content_alias) | **GET** /app/rest/server/files/{areaId}/files{path} | 
*ServerApi* | [**get_license_key**](api/ServerApi.md#get_license_key) | **GET** /app/rest/server/licensingData/licenseKeys/{licenseKey} | 
*ServerApi* | [**get_license_keys**](api/ServerApi.md#get_license_keys) | **GET** /app/rest/server/licensingData/licenseKeys | 
*ServerApi* | [**get_licensing_data**](api/ServerApi.md#get_licensing_data) | **GET** /app/rest/server/licensingData | 
*ServerApi* | [**get_metadata**](api/ServerApi.md#get_metadata) | **GET** /app/rest/server/files/{areaId}/metadata{path} | 
*ServerApi* | [**get_root**](api/ServerApi.md#get_root) | **GET** /app/rest/server/files/{areaId} | 
*ServerApi* | [**get_zipped**](api/ServerApi.md#get_zipped) | **GET** /app/rest/server/files/{areaId}/archived{path} | 
*ServerApi* | [**serve_plugins**](api/ServerApi.md#serve_plugins) | **GET** /app/rest/server/plugins | 
*ServerApi* | [**serve_server_info**](api/ServerApi.md#serve_server_info) | **GET** /app/rest/server | 
*ServerApi* | [**serve_server_version**](api/ServerApi.md#serve_server_version) | **GET** /app/rest/server/{field} | 
*ServerApi* | [**start_backup**](api/ServerApi.md#start_backup) | **POST** /app/rest/server/backup | 
*TestApi* | [**get_tests**](api/TestApi.md#get_tests) | **GET** /app/rest/tests | 
*TestApi* | [**serve_instance**](api/TestApi.md#serve_instance) | **GET** /app/rest/tests/{testLocator} | 
*TestOccurrenceApi* | [**get_test_occurrences**](api/TestOccurrenceApi.md#get_test_occurrences) | **GET** /app/rest/testOccurrences | 
*TestOccurrenceApi* | [**serve_instance**](api/TestOccurrenceApi.md#serve_instance) | **GET** /app/rest/testOccurrences/{testLocator} | 
*UserApi* | [**add_group**](api/UserApi.md#add_group) | **POST** /app/rest/users/{userLocator}/groups | 
*UserApi* | [**add_role**](api/UserApi.md#add_role) | **POST** /app/rest/users/{userLocator}/roles | 
*UserApi* | [**add_role_simple**](api/UserApi.md#add_role_simple) | **PUT** /app/rest/users/{userLocator}/roles/{roleId}/{scope} | 
*UserApi* | [**add_role_simple_post**](api/UserApi.md#add_role_simple_post) | **POST** /app/rest/users/{userLocator}/roles/{roleId}/{scope} | 
*UserApi* | [**create_user**](api/UserApi.md#create_user) | **POST** /app/rest/users | 
*UserApi* | [**delete_remember_me**](api/UserApi.md#delete_remember_me) | **DELETE** /app/rest/users/{userLocator}/debug/rememberMe | 
*UserApi* | [**delete_role**](api/UserApi.md#delete_role) | **DELETE** /app/rest/users/{userLocator}/roles/{roleId}/{scope} | 
*UserApi* | [**delete_user**](api/UserApi.md#delete_user) | **DELETE** /app/rest/users/{userLocator} | 
*UserApi* | [**delete_user_field**](api/UserApi.md#delete_user_field) | **DELETE** /app/rest/users/{userLocator}/{field} | 
*UserApi* | [**get_groups**](api/UserApi.md#get_groups) | **GET** /app/rest/users/{userLocator}/groups | 
*UserApi* | [**get_permissions**](api/UserApi.md#get_permissions) | **GET** /app/rest/users/{userLocator}/debug/permissions | 
*UserApi* | [**list_role**](api/UserApi.md#list_role) | **GET** /app/rest/users/{userLocator}/roles/{roleId}/{scope} | 
*UserApi* | [**list_roles**](api/UserApi.md#list_roles) | **GET** /app/rest/users/{userLocator}/roles | 
*UserApi* | [**put_user_property**](api/UserApi.md#put_user_property) | **PUT** /app/rest/users/{userLocator}/properties/{name} | 
*UserApi* | [**remove_user_property**](api/UserApi.md#remove_user_property) | **DELETE** /app/rest/users/{userLocator}/properties/{name} | 
*UserApi* | [**replace_groups**](api/UserApi.md#replace_groups) | **PUT** /app/rest/users/{userLocator}/groups | 
*UserApi* | [**replace_roles**](api/UserApi.md#replace_roles) | **PUT** /app/rest/users/{userLocator}/roles | 
*UserApi* | [**serve_user**](api/UserApi.md#serve_user) | **GET** /app/rest/users/{userLocator} | 
*UserApi* | [**serve_user_field**](api/UserApi.md#serve_user_field) | **GET** /app/rest/users/{userLocator}/{field} | 
*UserApi* | [**serve_user_properties**](api/UserApi.md#serve_user_properties) | **GET** /app/rest/users/{userLocator}/properties | 
*UserApi* | [**serve_user_property**](api/UserApi.md#serve_user_property) | **GET** /app/rest/users/{userLocator}/properties/{name} | 
*UserApi* | [**serve_users**](api/UserApi.md#serve_users) | **GET** /app/rest/users | 
*UserApi* | [**set_user_field**](api/UserApi.md#set_user_field) | **PUT** /app/rest/users/{userLocator}/{field} | 
*UserApi* | [**update_user**](api/UserApi.md#update_user) | **PUT** /app/rest/users/{userLocator} | 
*VcsRootApi* | [**add_root**](api/VcsRootApi.md#add_root) | **POST** /app/rest/vcs-roots | 
*VcsRootApi* | [**change_properties**](api/VcsRootApi.md#change_properties) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/properties | 
*VcsRootApi* | [**delete_all_properties**](api/VcsRootApi.md#delete_all_properties) | **DELETE** /app/rest/vcs-roots/{vcsRootLocator}/properties | 
*VcsRootApi* | [**delete_parameter**](api/VcsRootApi.md#delete_parameter) | **DELETE** /app/rest/vcs-roots/{vcsRootLocator}/properties/{name} | 
*VcsRootApi* | [**delete_root**](api/VcsRootApi.md#delete_root) | **DELETE** /app/rest/vcs-roots/{vcsRootLocator} | 
*VcsRootApi* | [**get_settings_file**](api/VcsRootApi.md#get_settings_file) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/settingsFile | 
*VcsRootApi* | [**put_parameter**](api/VcsRootApi.md#put_parameter) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/properties/{name} | 
*VcsRootApi* | [**serve_field**](api/VcsRootApi.md#serve_field) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/{field} | 
*VcsRootApi* | [**serve_instance_field**](api/VcsRootApi.md#serve_instance_field) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/{field} | 
*VcsRootApi* | [**serve_properties**](api/VcsRootApi.md#serve_properties) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/properties | 
*VcsRootApi* | [**serve_property**](api/VcsRootApi.md#serve_property) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/properties/{name} | 
*VcsRootApi* | [**serve_root**](api/VcsRootApi.md#serve_root) | **GET** /app/rest/vcs-roots/{vcsRootLocator} | 
*VcsRootApi* | [**serve_root_instance**](api/VcsRootApi.md#serve_root_instance) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator} | 
*VcsRootApi* | [**serve_root_instance_properties**](api/VcsRootApi.md#serve_root_instance_properties) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/properties | 
*VcsRootApi* | [**serve_root_instances**](api/VcsRootApi.md#serve_root_instances) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances | 
*VcsRootApi* | [**serve_roots**](api/VcsRootApi.md#serve_roots) | **GET** /app/rest/vcs-roots | 
*VcsRootApi* | [**set_field**](api/VcsRootApi.md#set_field) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/{field} | 
*VcsRootApi* | [**set_instance_field**](api/VcsRootApi.md#set_instance_field) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/{field} | 
*VcsRootInstanceApi* | [**delete_instance_field**](api/VcsRootInstanceApi.md#delete_instance_field) | **DELETE** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field} | 
*VcsRootInstanceApi* | [**delete_repository_state**](api/VcsRootInstanceApi.md#delete_repository_state) | **DELETE** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState | 
*VcsRootInstanceApi* | [**get_children**](api/VcsRootInstanceApi.md#get_children) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/children{path} | 
*VcsRootInstanceApi* | [**get_children_alias**](api/VcsRootInstanceApi.md#get_children_alias) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/{path} | 
*VcsRootInstanceApi* | [**get_content**](api/VcsRootInstanceApi.md#get_content) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/content{path} | 
*VcsRootInstanceApi* | [**get_content_alias**](api/VcsRootInstanceApi.md#get_content_alias) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/files{path} | 
*VcsRootInstanceApi* | [**get_metadata**](api/VcsRootInstanceApi.md#get_metadata) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/metadata{path} | 
*VcsRootInstanceApi* | [**get_repository_state**](api/VcsRootInstanceApi.md#get_repository_state) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState | 
*VcsRootInstanceApi* | [**get_repository_state_creation_date**](api/VcsRootInstanceApi.md#get_repository_state_creation_date) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState/creationDate | 
*VcsRootInstanceApi* | [**get_root**](api/VcsRootInstanceApi.md#get_root) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest | 
*VcsRootInstanceApi* | [**get_zipped**](api/VcsRootInstanceApi.md#get_zipped) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/archived{path} | 
*VcsRootInstanceApi* | [**schedule_checking_for_changes**](api/VcsRootInstanceApi.md#schedule_checking_for_changes) | **POST** /app/rest/vcs-root-instances/checkingForChangesQueue | 
*VcsRootInstanceApi* | [**schedule_checking_for_changes_0**](api/VcsRootInstanceApi.md#schedule_checking_for_changes_0) | **POST** /app/rest/vcs-root-instances/commitHookNotification | 
*VcsRootInstanceApi* | [**serve_instance**](api/VcsRootInstanceApi.md#serve_instance) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator} | 
*VcsRootInstanceApi* | [**serve_instance_field**](api/VcsRootInstanceApi.md#serve_instance_field) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field} | 
*VcsRootInstanceApi* | [**serve_instances**](api/VcsRootInstanceApi.md#serve_instances) | **GET** /app/rest/vcs-root-instances | 
*VcsRootInstanceApi* | [**serve_root_instance_properties**](api/VcsRootInstanceApi.md#serve_root_instance_properties) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/properties | 
*VcsRootInstanceApi* | [**set_instance_field**](api/VcsRootInstanceApi.md#set_instance_field) | **PUT** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field} | 
*VcsRootInstanceApi* | [**set_repository_state**](api/VcsRootInstanceApi.md#set_repository_state) | **PUT** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState | 
*DefaultApi* | [**serve_api_version**](api/DefaultApi.md#serve_api_version) | **GET** /app/rest/apiVersion | 
*DefaultApi* | [**serve_build_field_short**](api/DefaultApi.md#serve_build_field_short) | **GET** /app/rest/{projectLocator}/{btLocator}/{buildLocator}/{field} | 
*DefaultApi* | [**serve_plugin_info**](api/DefaultApi.md#serve_plugin_info) | **GET** /app/rest/info | 
*DefaultApi* | [**serve_root**](api/DefaultApi.md#serve_root) | **GET** /app/rest | 
*DefaultApi* | [**serve_version**](api/DefaultApi.md#serve_version) | **GET** /app/rest/version | 


## Documentation For Models

 - [Agent](models/Agent.md)
 - [AgentPool](models/AgentPool.md)
 - [AgentPools](models/AgentPools.md)
 - [AgentRequirement](models/AgentRequirement.md)
 - [AgentRequirements](models/AgentRequirements.md)
 - [Agents](models/Agents.md)
 - [ArtifactDependencies](models/ArtifactDependencies.md)
 - [ArtifactDependency](models/ArtifactDependency.md)
 - [AuthorizedInfo](models/AuthorizedInfo.md)
 - [BackupProcess](models/BackupProcess.md)
 - [BackupProcessInfo](models/BackupProcessInfo.md)
 - [BackupProcessManager](models/BackupProcessManager.md)
 - [Branch](models/Branch.md)
 - [BranchVersion](models/BranchVersion.md)
 - [Branches](models/Branches.md)
 - [Build](models/Build.md)
 - [BuildCancelRequest](models/BuildCancelRequest.md)
 - [BuildTriggeringOptions](models/BuildTriggeringOptions.md)
 - [BuildType](models/BuildType.md)
 - [BuildTypes](models/BuildTypes.md)
 - [Builds](models/Builds.md)
 - [Change](models/Change.md)
 - [Changes](models/Changes.md)
 - [Comment](models/Comment.md)
 - [Compatibilities](models/Compatibilities.md)
 - [Compatibility](models/Compatibility.md)
 - [Datas](models/Datas.md)
 - [EnabledInfo](models/EnabledInfo.md)
 - [Entries](models/Entries.md)
 - [Entry](models/Entry.md)
 - [Exception](models/Exception.md)
 - [Feature](models/Feature.md)
 - [Features](models/Features.md)
 - [FederationServer](models/FederationServer.md)
 - [File](models/File.md)
 - [FileChange](models/FileChange.md)
 - [FileChanges](models/FileChanges.md)
 - [Files](models/Files.md)
 - [Group](models/Group.md)
 - [Groups](models/Groups.md)
 - [Href](models/Href.md)
 - [Investigation](models/Investigation.md)
 - [Investigations](models/Investigations.md)
 - [Issue](models/Issue.md)
 - [IssueUsage](models/IssueUsage.md)
 - [Issues](models/Issues.md)
 - [IssuesUsages](models/IssuesUsages.md)
 - [Items](models/Items.md)
 - [LicenseKey](models/LicenseKey.md)
 - [LicenseKeys](models/LicenseKeys.md)
 - [LicensingData](models/LicensingData.md)
 - [Link](models/Link.md)
 - [Links](models/Links.md)
 - [MetaData](models/MetaData.md)
 - [ModelProperty](models/ModelProperty.md)
 - [Mute](models/Mute.md)
 - [Mutes](models/Mutes.md)
 - [NewBuildTypeDescription](models/NewBuildTypeDescription.md)
 - [NewProjectDescription](models/NewProjectDescription.md)
 - [Plugin](models/Plugin.md)
 - [Plugins](models/Plugins.md)
 - [Problem](models/Problem.md)
 - [ProblemOccurrence](models/ProblemOccurrence.md)
 - [ProblemOccurrences](models/ProblemOccurrences.md)
 - [ProblemScope](models/ProblemScope.md)
 - [ProblemTarget](models/ProblemTarget.md)
 - [Problems](models/Problems.md)
 - [ProgressInfo](models/ProgressInfo.md)
 - [Project](models/Project.md)
 - [ProjectFeature](models/ProjectFeature.md)
 - [ProjectFeatures](models/ProjectFeatures.md)
 - [Projects](models/Projects.md)
 - [Properties](models/Properties.md)
 - [RepositoryState](models/RepositoryState.md)
 - [Requirements](models/Requirements.md)
 - [Resolution](models/Resolution.md)
 - [Revision](models/Revision.md)
 - [Revisions](models/Revisions.md)
 - [Role](models/Role.md)
 - [Roles](models/Roles.md)
 - [Server](models/Server.md)
 - [Servers](models/Servers.md)
 - [Session](models/Session.md)
 - [Sessions](models/Sessions.md)
 - [SnapshotDependencies](models/SnapshotDependencies.md)
 - [SnapshotDependency](models/SnapshotDependency.md)
 - [StackTraceElement](models/StackTraceElement.md)
 - [StateField](models/StateField.md)
 - [Step](models/Step.md)
 - [Steps](models/Steps.md)
 - [Tag](models/Tag.md)
 - [Tags](models/Tags.md)
 - [Test](models/Test.md)
 - [TestOccurrence](models/TestOccurrence.md)
 - [TestOccurrences](models/TestOccurrences.md)
 - [Tests](models/Tests.md)
 - [Throwable](models/Throwable.md)
 - [Trigger](models/Trigger.md)
 - [TriggeredBy](models/TriggeredBy.md)
 - [Triggers](models/Triggers.md)
 - [Type](models/Type.md)
 - [User](models/User.md)
 - [Users](models/Users.md)
 - [VcsCheckStatus](models/VcsCheckStatus.md)
 - [VcsLabeling](models/VcsLabeling.md)
 - [VcsRoot](models/VcsRoot.md)
 - [VcsRootEntries](models/VcsRootEntries.md)
 - [VcsRootEntry](models/VcsRootEntry.md)
 - [VcsRootInstance](models/VcsRootInstance.md)
 - [VcsRootInstances](models/VcsRootInstances.md)
 - [VcsRoots](models/VcsRoots.md)
 - [VcsStatus](models/VcsStatus.md)
