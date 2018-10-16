dohq_teamcity.BuildTypeApi
######################################

`API examples <../../teamcity_apis/BuildTypeApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `add_agent_requirement`__
     - **POST** ``/app/rest/buildTypes/{btLocator}/agent-requirements``
   * - `add_artifact_dep`__
     - **POST** ``/app/rest/buildTypes/{btLocator}/artifact-dependencies``
   * - `add_build_type`__
     - **POST** ``/app/rest/buildTypes``
   * - `add_feature`__
     - **POST** ``/app/rest/buildTypes/{btLocator}/features``
   * - `add_feature_parameter`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/features/{featureId}/parameters/{parameterName}``
   * - `add_snapshot_dep`__
     - **POST** ``/app/rest/buildTypes/{btLocator}/snapshot-dependencies``
   * - `add_step`__
     - **POST** ``/app/rest/buildTypes/{btLocator}/steps``
   * - `add_step_parameter`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters/{parameterName}``
   * - `add_trigger`__
     - **POST** ``/app/rest/buildTypes/{btLocator}/triggers``
   * - `add_vcs_root_entry`__
     - **POST** ``/app/rest/buildTypes/{btLocator}/vcs-root-entries``
   * - `change_artifact_dep_setting`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}/{fieldName}``
   * - `change_feature_setting`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/features/{featureId}/{name}``
   * - `change_requirement_setting`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}/{fieldName}``
   * - `change_step_setting`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/steps/{stepId}/{fieldName}``
   * - `change_trigger_setting`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}/{fieldName}``
   * - `delete_agent_requirement`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}``
   * - `delete_all_parameters`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/parameters``
   * - `delete_all_parameters_0`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/settings``
   * - `delete_artifact_dep`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}``
   * - `delete_build_type`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}``
   * - `delete_feature`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/features/{featureId}``
   * - `delete_parameter`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/parameters/{name}``
   * - `delete_parameter_0`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/settings/{name}``
   * - `delete_snapshot_dep`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator}``
   * - `delete_step`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/steps/{stepId}``
   * - `delete_template_association`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/template``
   * - `delete_trigger`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}``
   * - `delete_vcs_root_entry`__
     - **DELETE** ``/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}``
   * - `get_agent_requirement`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}``
   * - `get_agent_requirements`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/agent-requirements``
   * - `get_aliases`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/aliases``
   * - `get_artifact_dep`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}``
   * - `get_artifact_dep_setting`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}/{fieldName}``
   * - `get_artifact_deps`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/artifact-dependencies``
   * - `get_build_types`__
     - **GET** ``/app/rest/buildTypes``
   * - `get_children`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs/files/latest/children{path}``
   * - `get_children_alias`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs/files/latest/{path}``
   * - `get_content`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs/files/latest/content{path}``
   * - `get_content_alias`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs/files/latest/files{path}``
   * - `get_current_vcs_instances`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs-root-instances``
   * - `get_example_new_project_description`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/example/newBuildTypeDescription``
   * - `get_example_new_project_description_compatibility_version1`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/newBuildTypeDescription``
   * - `get_feature`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/features/{featureId}``
   * - `get_feature_parameter`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/features/{featureId}/parameters/{parameterName}``
   * - `get_feature_parameters`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/features/{featureId}/parameters``
   * - `get_feature_setting`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/features/{featureId}/{name}``
   * - `get_features`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/features``
   * - `get_investigations`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/investigations``
   * - `get_metadata`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs/files/latest/metadata{path}``
   * - `get_parameter`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/parameters/{name}``
   * - `get_parameter_0`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/settings/{name}``
   * - `get_parameter_type`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/parameters/{name}/type``
   * - `get_parameter_type_raw_value`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/parameters/{name}/type/rawValue``
   * - `get_parameter_value_long`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/parameters/{name}/value``
   * - `get_parameter_value_long_0`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/settings/{name}/value``
   * - `get_parameters`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/parameters``
   * - `get_parameters_0`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/settings``
   * - `get_requirement_setting`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}/{fieldName}``
   * - `get_root`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs/files/latest``
   * - `get_settings_file`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/settingsFile``
   * - `get_snapshot_dep`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator}``
   * - `get_snapshot_deps`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/snapshot-dependencies``
   * - `get_step`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/steps/{stepId}``
   * - `get_step_parameter`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters/{parameterName}``
   * - `get_step_parameters`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters``
   * - `get_step_setting`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/steps/{stepId}/{fieldName}``
   * - `get_steps`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/steps``
   * - `get_template_association`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/template``
   * - `get_trigger`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}``
   * - `get_trigger_setting`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}/{fieldName}``
   * - `get_triggers`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/triggers``
   * - `get_vcs_labeling_options`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcsLabeling``
   * - `get_vcs_root_entries`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs-root-entries``
   * - `get_vcs_root_entry`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}``
   * - `get_vcs_root_entry_checkout_rules`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}/checkout-rules``
   * - `get_zipped`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/vcs/files/latest/archived{path}``
   * - `replace_agent_requirement`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}``
   * - `replace_agent_requirements`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/agent-requirements``
   * - `replace_artifact_dep`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}``
   * - `replace_artifact_deps`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/artifact-dependencies``
   * - `replace_feature`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/features/{featureId}``
   * - `replace_feature_parameters`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/features/{featureId}/parameters``
   * - `replace_features`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/features``
   * - `replace_snapshot_dep`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator}``
   * - `replace_snapshot_deps`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/snapshot-dependencies``
   * - `replace_step`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/steps/{stepId}``
   * - `replace_step_parameters`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters``
   * - `replace_steps`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/steps``
   * - `replace_trigger`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}``
   * - `replace_triggers`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/triggers``
   * - `replace_vcs_root_entries`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/vcs-root-entries``
   * - `serve_branches`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/branches``
   * - `serve_build_field`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/builds/{buildLocator}/{field}``
   * - `serve_build_type_builds_tags`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/buildTags``
   * - `serve_build_type_field`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/{field}``
   * - `serve_build_type_template`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/template``
   * - `serve_build_type_xml`__
     - **GET** ``/app/rest/buildTypes/{btLocator}``
   * - `serve_build_with_project`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/builds/{buildLocator}``
   * - `serve_builds`__
     - **GET** ``/app/rest/buildTypes/{btLocator}/builds``
   * - `set_build_type_field`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/{field}``
   * - `set_parameter`__
     - **POST** ``/app/rest/buildTypes/{btLocator}/parameters``
   * - `set_parameter_0`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/parameters/{name}``
   * - `set_parameter_1`__
     - **POST** ``/app/rest/buildTypes/{btLocator}/settings``
   * - `set_parameter_2`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/settings/{name}``
   * - `set_parameter_type`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/parameters/{name}/type``
   * - `set_parameter_type_raw_value`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/parameters/{name}/type/rawValue``
   * - `set_parameter_value_long`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/parameters/{name}/value``
   * - `set_parameter_value_long_0`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/settings/{name}/value``
   * - `set_parameters`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/parameters``
   * - `set_parameters_0`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/settings``
   * - `set_vcs_labeling_options`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/vcsLabeling``
   * - `update_vcs_root_entry`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}``
   * - `update_vcs_root_entry_checkout_rules`__
     - **PUT** ``/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}/checkout-rules``

add_agent_requirement
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.AgentRequirement() # AgentRequirement |  (optional)

    try:
        api_response = tc.build_type_api.add_agent_requirement(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_agent_requirement: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `AgentRequirement <../models/AgentRequirement.html>`_
     - [optional] 

Return type:
    `AgentRequirement <../models/AgentRequirement.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_artifact_dep
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.ArtifactDependency() # ArtifactDependency |  (optional)

    try:
        api_response = tc.build_type_api.add_artifact_dep(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_artifact_dep: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `ArtifactDependency <../models/ArtifactDependency.html>`_
     - [optional] 

Return type:
    `ArtifactDependency <../models/ArtifactDependency.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_build_type
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.BuildType() # BuildType |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.add_build_type(body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_build_type: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `BuildType <../models/BuildType.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildType <../models/BuildType.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_feature
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.Feature() # Feature |  (optional)

    try:
        api_response = tc.build_type_api.add_feature(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_feature: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `Feature <../models/Feature.html>`_
     - [optional] 

Return type:
    `Feature <../models/Feature.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_feature_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    feature_id = 'feature_id_example' # str | 
    parameter_name = 'parameter_name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.add_feature_parameter(bt_locator, feature_id, parameter_name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_feature_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **feature_id**
     - **str**
     - 
   * - **parameter_name**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_snapshot_dep
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.SnapshotDependency() # SnapshotDependency |  (optional)

    try:
        api_response = tc.build_type_api.add_snapshot_dep(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_snapshot_dep: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `SnapshotDependency <../models/SnapshotDependency.html>`_
     - [optional] 

Return type:
    `SnapshotDependency <../models/SnapshotDependency.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_step
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.Step() # Step |  (optional)

    try:
        api_response = tc.build_type_api.add_step(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_step: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `Step <../models/Step.html>`_
     - [optional] 

Return type:
    `Step <../models/Step.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_step_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    step_id = 'step_id_example' # str | 
    parameter_name = 'parameter_name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.add_step_parameter(bt_locator, step_id, parameter_name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_step_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **step_id**
     - **str**
     - 
   * - **parameter_name**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_trigger
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.Trigger() # Trigger |  (optional)

    try:
        api_response = tc.build_type_api.add_trigger(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_trigger: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `Trigger <../models/Trigger.html>`_
     - [optional] 

Return type:
    `Trigger <../models/Trigger.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_vcs_root_entry
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.VcsRootEntry() # VcsRootEntry |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.add_vcs_root_entry(bt_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->add_vcs_root_entry: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `VcsRootEntry <../models/VcsRootEntry.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRootEntry <../models/VcsRootEntry.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


change_artifact_dep_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    artifact_dep_locator = 'artifact_dep_locator_example' # str | 
    field_name = 'field_name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.change_artifact_dep_setting(bt_locator, artifact_dep_locator, field_name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->change_artifact_dep_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **artifact_dep_locator**
     - **str**
     - 
   * - **field_name**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


change_feature_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    feature_id = 'feature_id_example' # str | 
    name = 'name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.change_feature_setting(bt_locator, feature_id, name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->change_feature_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **feature_id**
     - **str**
     - 
   * - **name**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


change_requirement_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    agent_requirement_locator = 'agent_requirement_locator_example' # str | 
    field_name = 'field_name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.change_requirement_setting(bt_locator, agent_requirement_locator, field_name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->change_requirement_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **agent_requirement_locator**
     - **str**
     - 
   * - **field_name**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


change_step_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    step_id = 'step_id_example' # str | 
    field_name = 'field_name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.change_step_setting(bt_locator, step_id, field_name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->change_step_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **step_id**
     - **str**
     - 
   * - **field_name**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


change_trigger_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    trigger_locator = 'trigger_locator_example' # str | 
    field_name = 'field_name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.change_trigger_setting(bt_locator, trigger_locator, field_name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->change_trigger_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **trigger_locator**
     - **str**
     - 
   * - **field_name**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_agent_requirement
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    agent_requirement_locator = 'agent_requirement_locator_example' # str | 

    try:
        tc.build_type_api.delete_agent_requirement(bt_locator, agent_requirement_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_agent_requirement: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **agent_requirement_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_all_parameters
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 

    try:
        tc.build_type_api.delete_all_parameters(bt_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_all_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_all_parameters_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 

    try:
        tc.build_type_api.delete_all_parameters_0(bt_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_all_parameters_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_artifact_dep
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    artifact_dep_locator = 'artifact_dep_locator_example' # str | 

    try:
        tc.build_type_api.delete_artifact_dep(bt_locator, artifact_dep_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_artifact_dep: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **artifact_dep_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_build_type
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 

    try:
        tc.build_type_api.delete_build_type(bt_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_build_type: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_feature
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    feature_id = 'feature_id_example' # str | 

    try:
        tc.build_type_api.delete_feature(bt_locator, feature_id)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_feature: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **feature_id**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 

    try:
        tc.build_type_api.delete_parameter(name, bt_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_parameter_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 

    try:
        tc.build_type_api.delete_parameter_0(name, bt_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_parameter_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_snapshot_dep
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    snapshot_dep_locator = 'snapshot_dep_locator_example' # str | 

    try:
        tc.build_type_api.delete_snapshot_dep(bt_locator, snapshot_dep_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_snapshot_dep: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **snapshot_dep_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_step
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    step_id = 'step_id_example' # str | 

    try:
        tc.build_type_api.delete_step(bt_locator, step_id)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_step: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **step_id**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_template_association
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 

    try:
        tc.build_type_api.delete_template_association(bt_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_template_association: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_trigger
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    trigger_locator = 'trigger_locator_example' # str | 

    try:
        tc.build_type_api.delete_trigger(bt_locator, trigger_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_trigger: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **trigger_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_vcs_root_entry
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    vcs_root_locator = 'vcs_root_locator_example' # str | 

    try:
        tc.build_type_api.delete_vcs_root_entry(bt_locator, vcs_root_locator)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->delete_vcs_root_entry: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **vcs_root_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_agent_requirement
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    agent_requirement_locator = 'agent_requirement_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_agent_requirement(bt_locator, agent_requirement_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_agent_requirement: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **agent_requirement_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AgentRequirement <../models/AgentRequirement.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_agent_requirements
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_agent_requirements(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_agent_requirements: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AgentRequirements <../models/AgentRequirements.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_aliases
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.build_type_api.get_aliases(bt_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_aliases: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    `Items <../models/Items.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_artifact_dep
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    artifact_dep_locator = 'artifact_dep_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_artifact_dep(bt_locator, artifact_dep_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_artifact_dep: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **artifact_dep_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `ArtifactDependency <../models/ArtifactDependency.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_artifact_dep_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    artifact_dep_locator = 'artifact_dep_locator_example' # str | 
    field_name = 'field_name_example' # str | 

    try:
        api_response = tc.build_type_api.get_artifact_dep_setting(bt_locator, artifact_dep_locator, field_name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_artifact_dep_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **artifact_dep_locator**
     - **str**
     - 
   * - **field_name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_artifact_deps
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_artifact_deps(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_artifact_deps: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `ArtifactDependencies <../models/ArtifactDependencies.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_build_types
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_build_types(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_build_types: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildTypes <../models/BuildTypes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_children
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    resolve_parameters = true # bool |  (optional)

    try:
        api_response = tc.build_type_api.get_children(path, bt_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_children: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **base_path**
     - **str**
     - [optional] 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 
   * - **resolve_parameters**
     - **bool**
     - [optional] 

Return type:
    `Files <../models/Files.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_children_alias
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    resolve_parameters = true # bool |  (optional)

    try:
        api_response = tc.build_type_api.get_children_alias(path, bt_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_children_alias: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **base_path**
     - **str**
     - [optional] 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 
   * - **resolve_parameters**
     - **bool**
     - [optional] 

Return type:
    `Files <../models/Files.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_content
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    resolve_parameters = true # bool |  (optional)

    try:
        tc.build_type_api.get_content(path, bt_locator, resolve_parameters=resolve_parameters)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_content: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **resolve_parameters**
     - **bool**
     - [optional] 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_content_alias
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    resolve_parameters = true # bool |  (optional)

    try:
        tc.build_type_api.get_content_alias(path, bt_locator, resolve_parameters=resolve_parameters)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_content_alias: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **resolve_parameters**
     - **bool**
     - [optional] 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_current_vcs_instances
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_current_vcs_instances(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_current_vcs_instances: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRootInstances <../models/VcsRootInstances.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_example_new_project_description
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 

    try:
        api_response = tc.build_type_api.get_example_new_project_description(bt_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_example_new_project_description: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 

Return type:
    `NewBuildTypeDescription <../models/NewBuildTypeDescription.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_example_new_project_description_compatibility_version1
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 

    try:
        api_response = tc.build_type_api.get_example_new_project_description_compatibility_version1(bt_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_example_new_project_description_compatibility_version1: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 

Return type:
    `NewBuildTypeDescription <../models/NewBuildTypeDescription.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_feature
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    feature_id = 'feature_id_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_feature(bt_locator, feature_id, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_feature: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **feature_id**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Feature <../models/Feature.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_feature_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    feature_id = 'feature_id_example' # str | 
    parameter_name = 'parameter_name_example' # str | 

    try:
        api_response = tc.build_type_api.get_feature_parameter(bt_locator, feature_id, parameter_name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_feature_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **feature_id**
     - **str**
     - 
   * - **parameter_name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_feature_parameters
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    feature_id = 'feature_id_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_feature_parameters(bt_locator, feature_id, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_feature_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **feature_id**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_feature_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    feature_id = 'feature_id_example' # str | 
    name = 'name_example' # str | 

    try:
        api_response = tc.build_type_api.get_feature_setting(bt_locator, feature_id, name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_feature_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **feature_id**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_features
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_features(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_features: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Features <../models/Features.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_investigations
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_investigations(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_investigations: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Investigations <../models/Investigations.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_metadata
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    resolve_parameters = true # bool |  (optional)

    try:
        api_response = tc.build_type_api.get_metadata(path, bt_locator, fields=fields, resolve_parameters=resolve_parameters)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_metadata: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **resolve_parameters**
     - **bool**
     - [optional] 

Return type:
    `file <../models/file.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_parameter(name, bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `ModelProperty <../models/ModelProperty.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parameter_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_parameter_0(name, bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_parameter_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `ModelProperty <../models/ModelProperty.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parameter_type
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 

    try:
        api_response = tc.build_type_api.get_parameter_type(name, bt_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_parameter_type: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 

Return type:
    `Type <../models/Type.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parameter_type_raw_value
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 

    try:
        api_response = tc.build_type_api.get_parameter_type_raw_value(name, bt_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_parameter_type_raw_value: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parameter_value_long
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 

    try:
        api_response = tc.build_type_api.get_parameter_value_long(name, bt_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_parameter_value_long: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parameter_value_long_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 

    try:
        api_response = tc.build_type_api.get_parameter_value_long_0(name, bt_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_parameter_value_long_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parameters
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_parameters(bt_locator, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parameters_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_parameters_0(bt_locator, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_parameters_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_requirement_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    agent_requirement_locator = 'agent_requirement_locator_example' # str | 
    field_name = 'field_name_example' # str | 

    try:
        api_response = tc.build_type_api.get_requirement_setting(bt_locator, agent_requirement_locator, field_name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_requirement_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **agent_requirement_locator**
     - **str**
     - 
   * - **field_name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_root
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    resolve_parameters = true # bool |  (optional)

    try:
        api_response = tc.build_type_api.get_root(bt_locator, base_path=base_path, locator=locator, fields=fields, resolve_parameters=resolve_parameters)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_root: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **base_path**
     - **str**
     - [optional] 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 
   * - **resolve_parameters**
     - **bool**
     - [optional] 

Return type:
    `Files <../models/Files.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_settings_file
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 

    try:
        api_response = tc.build_type_api.get_settings_file(bt_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_settings_file: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_snapshot_dep
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    snapshot_dep_locator = 'snapshot_dep_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_snapshot_dep(bt_locator, snapshot_dep_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_snapshot_dep: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **snapshot_dep_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `SnapshotDependency <../models/SnapshotDependency.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_snapshot_deps
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_snapshot_deps(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_snapshot_deps: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `SnapshotDependencies <../models/SnapshotDependencies.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_step
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    step_id = 'step_id_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_step(bt_locator, step_id, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_step: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **step_id**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Step <../models/Step.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_step_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    step_id = 'step_id_example' # str | 
    parameter_name = 'parameter_name_example' # str | 

    try:
        api_response = tc.build_type_api.get_step_parameter(bt_locator, step_id, parameter_name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_step_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **step_id**
     - **str**
     - 
   * - **parameter_name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_step_parameters
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    step_id = 'step_id_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_step_parameters(bt_locator, step_id, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_step_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **step_id**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_step_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    step_id = 'step_id_example' # str | 
    field_name = 'field_name_example' # str | 

    try:
        api_response = tc.build_type_api.get_step_setting(bt_locator, step_id, field_name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_step_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **step_id**
     - **str**
     - 
   * - **field_name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_steps
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_steps(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_steps: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Steps <../models/Steps.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_template_association
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    body = 'body_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_template_association(bt_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_template_association: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildType <../models/BuildType.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_trigger
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    trigger_locator = 'trigger_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_trigger(bt_locator, trigger_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_trigger: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **trigger_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Trigger <../models/Trigger.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_trigger_setting
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    trigger_locator = 'trigger_locator_example' # str | 
    field_name = 'field_name_example' # str | 

    try:
        api_response = tc.build_type_api.get_trigger_setting(bt_locator, trigger_locator, field_name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_trigger_setting: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **trigger_locator**
     - **str**
     - 
   * - **field_name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_triggers
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_triggers(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_triggers: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Triggers <../models/Triggers.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_vcs_labeling_options
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 

    try:
        api_response = tc.build_type_api.get_vcs_labeling_options(bt_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_vcs_labeling_options: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 

Return type:
    `VcsLabeling <../models/VcsLabeling.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_vcs_root_entries
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_vcs_root_entries(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_vcs_root_entries: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRootEntries <../models/VcsRootEntries.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_vcs_root_entry
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    vcs_root_locator = 'vcs_root_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.get_vcs_root_entry(bt_locator, vcs_root_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_vcs_root_entry: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **vcs_root_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRootEntry <../models/VcsRootEntry.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_vcs_root_entry_checkout_rules
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    vcs_root_locator = 'vcs_root_locator_example' # str | 

    try:
        api_response = tc.build_type_api.get_vcs_root_entry_checkout_rules(bt_locator, vcs_root_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_vcs_root_entry_checkout_rules: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **vcs_root_locator**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_zipped
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    resolve_parameters = true # bool |  (optional)

    try:
        tc.build_type_api.get_zipped(path, bt_locator, base_path=base_path, locator=locator, name=name, resolve_parameters=resolve_parameters)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->get_zipped: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **base_path**
     - **str**
     - [optional] 
   * - **locator**
     - **str**
     - [optional] 
   * - **name**
     - **str**
     - [optional] 
   * - **resolve_parameters**
     - **bool**
     - [optional] 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_agent_requirement
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    agent_requirement_locator = 'agent_requirement_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.AgentRequirement() # AgentRequirement |  (optional)

    try:
        api_response = tc.build_type_api.replace_agent_requirement(bt_locator, agent_requirement_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_agent_requirement: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **agent_requirement_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `AgentRequirement <../models/AgentRequirement.html>`_
     - [optional] 

Return type:
    `AgentRequirement <../models/AgentRequirement.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_agent_requirements
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.AgentRequirements() # AgentRequirements |  (optional)

    try:
        api_response = tc.build_type_api.replace_agent_requirements(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_agent_requirements: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `AgentRequirements <../models/AgentRequirements.html>`_
     - [optional] 

Return type:
    `AgentRequirements <../models/AgentRequirements.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_artifact_dep
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    artifact_dep_locator = 'artifact_dep_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.ArtifactDependency() # ArtifactDependency |  (optional)

    try:
        api_response = tc.build_type_api.replace_artifact_dep(bt_locator, artifact_dep_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_artifact_dep: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **artifact_dep_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `ArtifactDependency <../models/ArtifactDependency.html>`_
     - [optional] 

Return type:
    `ArtifactDependency <../models/ArtifactDependency.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_artifact_deps
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.ArtifactDependencies() # ArtifactDependencies |  (optional)

    try:
        api_response = tc.build_type_api.replace_artifact_deps(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_artifact_deps: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `ArtifactDependencies <../models/ArtifactDependencies.html>`_
     - [optional] 

Return type:
    `ArtifactDependencies <../models/ArtifactDependencies.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_feature
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    feature_id = 'feature_id_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.Feature() # Feature |  (optional)

    try:
        api_response = tc.build_type_api.replace_feature(bt_locator, feature_id, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_feature: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **feature_id**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `Feature <../models/Feature.html>`_
     - [optional] 

Return type:
    `Feature <../models/Feature.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_feature_parameters
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    feature_id = 'feature_id_example' # str | 
    body = dohq_teamcity.Properties() # Properties |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.replace_feature_parameters(bt_locator, feature_id, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_feature_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **feature_id**
     - **str**
     - 
   * - **body**
     - `Properties <../models/Properties.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_features
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.Features() # Features |  (optional)

    try:
        api_response = tc.build_type_api.replace_features(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_features: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `Features <../models/Features.html>`_
     - [optional] 

Return type:
    `Features <../models/Features.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_snapshot_dep
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    snapshot_dep_locator = 'snapshot_dep_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.SnapshotDependency() # SnapshotDependency |  (optional)

    try:
        api_response = tc.build_type_api.replace_snapshot_dep(bt_locator, snapshot_dep_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_snapshot_dep: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **snapshot_dep_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `SnapshotDependency <../models/SnapshotDependency.html>`_
     - [optional] 

Return type:
    `SnapshotDependency <../models/SnapshotDependency.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_snapshot_deps
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.SnapshotDependencies() # SnapshotDependencies |  (optional)

    try:
        api_response = tc.build_type_api.replace_snapshot_deps(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_snapshot_deps: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `SnapshotDependencies <../models/SnapshotDependencies.html>`_
     - [optional] 

Return type:
    `SnapshotDependencies <../models/SnapshotDependencies.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_step
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    step_id = 'step_id_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.Step() # Step |  (optional)

    try:
        api_response = tc.build_type_api.replace_step(bt_locator, step_id, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_step: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **step_id**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `Step <../models/Step.html>`_
     - [optional] 

Return type:
    `Step <../models/Step.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_step_parameters
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    step_id = 'step_id_example' # str | 
    body = dohq_teamcity.Properties() # Properties |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.replace_step_parameters(bt_locator, step_id, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_step_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **step_id**
     - **str**
     - 
   * - **body**
     - `Properties <../models/Properties.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_steps
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.Steps() # Steps |  (optional)

    try:
        api_response = tc.build_type_api.replace_steps(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_steps: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `Steps <../models/Steps.html>`_
     - [optional] 

Return type:
    `Steps <../models/Steps.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_trigger
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    trigger_locator = 'trigger_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.Trigger() # Trigger |  (optional)

    try:
        api_response = tc.build_type_api.replace_trigger(bt_locator, trigger_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_trigger: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **trigger_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `Trigger <../models/Trigger.html>`_
     - [optional] 

Return type:
    `Trigger <../models/Trigger.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_triggers
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    body = dohq_teamcity.Triggers() # Triggers |  (optional)

    try:
        api_response = tc.build_type_api.replace_triggers(bt_locator, fields=fields, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_triggers: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **body**
     - `Triggers <../models/Triggers.html>`_
     - [optional] 

Return type:
    `Triggers <../models/Triggers.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_vcs_root_entries
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.VcsRootEntries() # VcsRootEntries |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.replace_vcs_root_entries(bt_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->replace_vcs_root_entries: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `VcsRootEntries <../models/VcsRootEntries.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRootEntries <../models/VcsRootEntries.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_branches
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.serve_branches(bt_locator, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->serve_branches: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Branches <../models/Branches.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    build_locator = 'build_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.build_type_api.serve_build_field(bt_locator, build_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->serve_build_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **build_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_type_builds_tags
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.build_type_api.serve_build_type_builds_tags(bt_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->serve_build_type_builds_tags: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    `Tags <../models/Tags.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_type_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.build_type_api.serve_build_type_field(bt_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->serve_build_type_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_type_template
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.serve_build_type_template(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->serve_build_type_template: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildType <../models/BuildType.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_type_xml
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.serve_build_type_xml(bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->serve_build_type_xml: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildType <../models/BuildType.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_with_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    build_locator = 'build_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.serve_build_with_project(bt_locator, build_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->serve_build_with_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **build_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Build <../models/Build.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_builds
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

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
        api_response = tc.build_type_api.serve_builds(bt_locator, status=status, triggered_by_user=triggered_by_user, include_personal=include_personal, include_canceled=include_canceled, only_pinned=only_pinned, tag=tag, agent_name=agent_name, since_build=since_build, since_date=since_date, start=start, count=count, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->serve_builds: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **status**
     - **str**
     - [optional] 
   * - **triggered_by_user**
     - **str**
     - [optional] 
   * - **include_personal**
     - **bool**
     - [optional] 
   * - **include_canceled**
     - **bool**
     - [optional] 
   * - **only_pinned**
     - **bool**
     - [optional] 
   * - **tag**
     - `list[str] <../models/str.html>`_
     - [optional] 
   * - **agent_name**
     - **str**
     - [optional] 
   * - **since_build**
     - **str**
     - [optional] 
   * - **since_date**
     - **str**
     - [optional] 
   * - **start**
     - **int**
     - [optional] 
   * - **count**
     - **int**
     - [optional] 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Builds <../models/Builds.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_build_type_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_build_type_field(bt_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_build_type_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_parameter(bt_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `ModelProperty <../models/ModelProperty.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `ModelProperty <../models/ModelProperty.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameter_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_parameter_0(name, bt_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameter_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `ModelProperty <../models/ModelProperty.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `ModelProperty <../models/ModelProperty.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameter_1
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_parameter_1(bt_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameter_1: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `ModelProperty <../models/ModelProperty.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `ModelProperty <../models/ModelProperty.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameter_2
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_parameter_2(name, bt_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameter_2: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `ModelProperty <../models/ModelProperty.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `ModelProperty <../models/ModelProperty.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameter_type
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.Type() # Type |  (optional)

    try:
        api_response = tc.build_type_api.set_parameter_type(name, bt_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameter_type: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `Type <../models/Type.html>`_
     - [optional] 

Return type:
    `Type <../models/Type.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameter_type_raw_value
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_parameter_type_raw_value(name, bt_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameter_type_raw_value: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameter_value_long
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_parameter_value_long(name, bt_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameter_value_long: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameter_value_long_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_parameter_value_long_0(name, bt_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameter_value_long_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameters
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.Properties() # Properties |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_parameters(bt_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `Properties <../models/Properties.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameters_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.Properties() # Properties |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.set_parameters_0(bt_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_parameters_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `Properties <../models/Properties.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_vcs_labeling_options
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    body = dohq_teamcity.VcsLabeling() # VcsLabeling |  (optional)

    try:
        api_response = tc.build_type_api.set_vcs_labeling_options(bt_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->set_vcs_labeling_options: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **body**
     - `VcsLabeling <../models/VcsLabeling.html>`_
     - [optional] 

Return type:
    `VcsLabeling <../models/VcsLabeling.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


update_vcs_root_entry
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    vcs_root_locator = 'vcs_root_locator_example' # str | 
    body = dohq_teamcity.VcsRootEntry() # VcsRootEntry |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.update_vcs_root_entry(bt_locator, vcs_root_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->update_vcs_root_entry: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **vcs_root_locator**
     - **str**
     - 
   * - **body**
     - `VcsRootEntry <../models/VcsRootEntry.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRootEntry <../models/VcsRootEntry.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


update_vcs_root_entry_checkout_rules
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        bt_locator = 'bt_locator_example' # str | 
    vcs_root_locator = 'vcs_root_locator_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.build_type_api.update_vcs_root_entry_checkout_rules(bt_locator, vcs_root_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildTypeApi->update_vcs_root_entry_checkout_rules: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **bt_locator**
     - **str**
     - 
   * - **vcs_root_locator**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


