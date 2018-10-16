dohq_teamcity.ProjectApi
######################################

`API examples <../../teamcity_apis/ProjectApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `add`__
     - **POST** ``/app/rest/projects/{projectLocator}/projectFeatures``
   * - `create_build_type`__
     - **POST** ``/app/rest/projects/{projectLocator}/buildTypes``
   * - `create_build_type_template`__
     - **POST** ``/app/rest/projects/{projectLocator}/templates``
   * - `create_project`__
     - **POST** ``/app/rest/projects``
   * - `delete`__
     - **DELETE** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}``
   * - `delete_all_parameters`__
     - **DELETE** ``/app/rest/projects/{projectLocator}/parameters``
   * - `delete_all_parameters_0`__
     - **DELETE** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties``
   * - `delete_parameter`__
     - **DELETE** ``/app/rest/projects/{projectLocator}/parameters/{name}``
   * - `delete_parameter_0`__
     - **DELETE** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name}``
   * - `delete_project`__
     - **DELETE** ``/app/rest/projects/{projectLocator}``
   * - `delete_project_agent_pools`__
     - **DELETE** ``/app/rest/projects/{projectLocator}/agentPools/{agentPoolLocator}``
   * - `get`__
     - **GET** ``/app/rest/projects/{projectLocator}/projectFeatures``
   * - `get_build_types_order`__
     - **GET** ``/app/rest/projects/{projectLocator}/order/buildTypes``
   * - `get_example_new_project_description`__
     - **GET** ``/app/rest/projects/{projectLocator}/example/newProjectDescription``
   * - `get_example_new_project_description_compatibility_version1`__
     - **GET** ``/app/rest/projects/{projectLocator}/newProjectDescription``
   * - `get_parameter`__
     - **GET** ``/app/rest/projects/{projectLocator}/parameters/{name}``
   * - `get_parameter_0`__
     - **GET** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name}``
   * - `get_parameter_type`__
     - **GET** ``/app/rest/projects/{projectLocator}/parameters/{name}/type``
   * - `get_parameter_type_raw_value`__
     - **GET** ``/app/rest/projects/{projectLocator}/parameters/{name}/type/rawValue``
   * - `get_parameter_value_long`__
     - **GET** ``/app/rest/projects/{projectLocator}/parameters/{name}/value``
   * - `get_parameter_value_long_0`__
     - **GET** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name}/value``
   * - `get_parameters`__
     - **GET** ``/app/rest/projects/{projectLocator}/parameters``
   * - `get_parameters_0`__
     - **GET** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties``
   * - `get_parent_project`__
     - **GET** ``/app/rest/projects/{projectLocator}/parentProject``
   * - `get_project_agent_pools`__
     - **GET** ``/app/rest/projects/{projectLocator}/agentPools``
   * - `get_projects_order`__
     - **GET** ``/app/rest/projects/{projectLocator}/order/projects``
   * - `get_settings_file`__
     - **GET** ``/app/rest/projects/{projectLocator}/settingsFile``
   * - `get_single`__
     - **GET** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}``
   * - `reload_settings_file`__
     - **GET** ``/app/rest/projects/{projectLocator}/latest``
   * - `replace`__
     - **PUT** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}``
   * - `replace_all`__
     - **PUT** ``/app/rest/projects/{projectLocator}/projectFeatures``
   * - `serve_build_field_with_project`__
     - **GET** ``/app/rest/projects/{projectLocator}/buildTypes/{btLocator}/builds/{buildLocator}/{field}``
   * - `serve_build_type`__
     - **GET** ``/app/rest/projects/{projectLocator}/buildTypes/{btLocator}``
   * - `serve_build_type_field_with_project`__
     - **GET** ``/app/rest/projects/{projectLocator}/buildTypes/{btLocator}/{field}``
   * - `serve_build_type_templates`__
     - **GET** ``/app/rest/projects/{projectLocator}/templates/{btLocator}``
   * - `serve_build_types_in_project`__
     - **GET** ``/app/rest/projects/{projectLocator}/buildTypes``
   * - `serve_build_with_project`__
     - **GET** ``/app/rest/projects/{projectLocator}/buildTypes/{btLocator}/builds/{buildLocator}``
   * - `serve_builds`__
     - **GET** ``/app/rest/projects/{projectLocator}/buildTypes/{btLocator}/builds``
   * - `serve_project`__
     - **GET** ``/app/rest/projects/{projectLocator}``
   * - `serve_project_field`__
     - **GET** ``/app/rest/projects/{projectLocator}/{field}``
   * - `serve_projects`__
     - **GET** ``/app/rest/projects``
   * - `serve_templates_in_project`__
     - **GET** ``/app/rest/projects/{projectLocator}/templates``
   * - `set_build_types_order`__
     - **PUT** ``/app/rest/projects/{projectLocator}/order/buildTypes``
   * - `set_parameter`__
     - **POST** ``/app/rest/projects/{projectLocator}/parameters``
   * - `set_parameter_0`__
     - **PUT** ``/app/rest/projects/{projectLocator}/parameters/{name}``
   * - `set_parameter_1`__
     - **POST** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties``
   * - `set_parameter_2`__
     - **PUT** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name}``
   * - `set_parameter_type`__
     - **PUT** ``/app/rest/projects/{projectLocator}/parameters/{name}/type``
   * - `set_parameter_type_raw_value`__
     - **PUT** ``/app/rest/projects/{projectLocator}/parameters/{name}/type/rawValue``
   * - `set_parameter_value_long`__
     - **PUT** ``/app/rest/projects/{projectLocator}/parameters/{name}/value``
   * - `set_parameter_value_long_0`__
     - **PUT** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties/{name}/value``
   * - `set_parameters`__
     - **PUT** ``/app/rest/projects/{projectLocator}/parameters``
   * - `set_parameters_0`__
     - **PUT** ``/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}/properties``
   * - `set_parent_project`__
     - **PUT** ``/app/rest/projects/{projectLocator}/parentProject``
   * - `set_project_agent_pools`__
     - **PUT** ``/app/rest/projects/{projectLocator}/agentPools``
   * - `set_project_agent_pools_0`__
     - **POST** ``/app/rest/projects/{projectLocator}/agentPools``
   * - `set_project_filed`__
     - **PUT** ``/app/rest/projects/{projectLocator}/{field}``
   * - `set_projects_order`__
     - **PUT** ``/app/rest/projects/{projectLocator}/order/projects``

add
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.ProjectFeature() # ProjectFeature |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.add(project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->add: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `ProjectFeature <../models/ProjectFeature.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    **object**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


create_build_type
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.NewBuildTypeDescription() # NewBuildTypeDescription |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.create_build_type(project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->create_build_type: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `NewBuildTypeDescription <../models/NewBuildTypeDescription.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildType <../models/BuildType.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


create_build_type_template
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.NewBuildTypeDescription() # NewBuildTypeDescription |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.create_build_type_template(project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->create_build_type_template: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `NewBuildTypeDescription <../models/NewBuildTypeDescription.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildType <../models/BuildType.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


create_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.NewProjectDescription() # NewProjectDescription |  (optional)

    try:
        api_response = tc.project_api.create_project(body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `NewProjectDescription <../models/NewProjectDescription.html>`_
     - [optional] 

Return type:
    `Project <../models/Project.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 

    try:
        tc.project_api.delete(feature_locator, project_locator)
    except ApiException as e:
        print("Exception when calling ProjectApi->delete: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
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

        project_locator = 'project_locator_example' # str | 

    try:
        tc.project_api.delete_all_parameters(project_locator)
    except ApiException as e:
        print("Exception when calling ProjectApi->delete_all_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
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

        feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        tc.project_api.delete_all_parameters_0(feature_locator, project_locator, fields=fields)
    except ApiException as e:
        print("Exception when calling ProjectApi->delete_all_parameters_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

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
    project_locator = 'project_locator_example' # str | 

    try:
        tc.project_api.delete_parameter(name, project_locator)
    except ApiException as e:
        print("Exception when calling ProjectApi->delete_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **project_locator**
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
    feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        tc.project_api.delete_parameter_0(name, feature_locator, project_locator, fields=fields)
    except ApiException as e:
        print("Exception when calling ProjectApi->delete_parameter_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 

    try:
        tc.project_api.delete_project(project_locator)
    except ApiException as e:
        print("Exception when calling ProjectApi->delete_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_project_agent_pools
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    agent_pool_locator = 'agent_pool_locator_example' # str | 

    try:
        tc.project_api.delete_project_agent_pools(project_locator, agent_pool_locator)
    except ApiException as e:
        print("Exception when calling ProjectApi->delete_project_agent_pools: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **agent_pool_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.get(project_locator, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    **object**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_build_types_order
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.project_api.get_build_types_order(project_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_build_types_order: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    `BuildTypes <../models/BuildTypes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_example_new_project_description
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    id = 'id_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_example_new_project_description(project_locator, id=id)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_example_new_project_description: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **id**
     - **str**
     - [optional] 

Return type:
    `NewProjectDescription <../models/NewProjectDescription.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_example_new_project_description_compatibility_version1
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    id = 'id_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_example_new_project_description_compatibility_version1(project_locator, id=id)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_example_new_project_description_compatibility_version1: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **id**
     - **str**
     - [optional] 

Return type:
    `NewProjectDescription <../models/NewProjectDescription.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        name = 'name_example' # str | 
    project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_parameter(name, project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **project_locator**
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
    feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)
    fields2 = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_parameter_0(name, feature_locator, project_locator, fields=fields, fields2=fields2)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_parameter_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 
   * - **fields2**
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
    project_locator = 'project_locator_example' # str | 

    try:
        api_response = tc.project_api.get_parameter_type(name, project_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_parameter_type: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **project_locator**
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
    project_locator = 'project_locator_example' # str | 

    try:
        api_response = tc.project_api.get_parameter_type_raw_value(name, project_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_parameter_type_raw_value: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **project_locator**
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
    project_locator = 'project_locator_example' # str | 

    try:
        api_response = tc.project_api.get_parameter_value_long(name, project_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_parameter_value_long: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **project_locator**
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
    feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_parameter_value_long_0(name, feature_locator, project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_parameter_value_long_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

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

        project_locator = 'project_locator_example' # str | 
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_parameters(project_locator, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
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

        feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    fields2 = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_parameters_0(feature_locator, project_locator, locator=locator, fields=fields, fields2=fields2)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_parameters_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 
   * - **fields2**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parent_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_parent_project(project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_parent_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Project <../models/Project.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_project_agent_pools
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_project_agent_pools(project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_project_agent_pools: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AgentPools <../models/AgentPools.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_projects_order
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.project_api.get_projects_order(project_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_projects_order: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    `Projects <../models/Projects.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_settings_file
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 

    try:
        api_response = tc.project_api.get_settings_file(project_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_settings_file: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_single
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.get_single(feature_locator, project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_single: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    **object**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


reload_settings_file
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.reload_settings_file(project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->reload_settings_file: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Project <../models/Project.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.ProjectFeature() # ProjectFeature |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.replace(feature_locator, project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->replace: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `ProjectFeature <../models/ProjectFeature.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    **object**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_all
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.ProjectFeatures() # ProjectFeatures |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.replace_all(project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->replace_all: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `ProjectFeatures <../models/ProjectFeatures.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    **object**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_field_with_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    build_locator = 'build_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.project_api.serve_build_field_with_project(project_locator, bt_locator, build_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_build_field_with_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
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


serve_build_type
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.serve_build_type(project_locator, bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_build_type: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildType <../models/BuildType.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_type_field_with_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.project_api.serve_build_type_field_with_project(project_locator, bt_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_build_type_field_with_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_type_templates
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.serve_build_type_templates(project_locator, bt_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_build_type_templates: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **bt_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildType <../models/BuildType.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_types_in_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.serve_build_types_in_project(project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_build_types_in_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildTypes <../models/BuildTypes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_build_with_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    bt_locator = 'bt_locator_example' # str | 
    build_locator = 'build_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.serve_build_with_project(project_locator, bt_locator, build_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_build_with_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
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
        api_response = tc.project_api.serve_builds(project_locator, bt_locator, status=status, triggered_by_user=triggered_by_user, include_personal=include_personal, include_canceled=include_canceled, only_pinned=only_pinned, tag=tag, agent_name=agent_name, since_build=since_build, since_date=since_date, start=start, count=count, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_builds: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
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


serve_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.serve_project(project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Project <../models/Project.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_project_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.project_api.serve_project_field(project_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_project_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_projects
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.serve_projects(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_projects: %s\n" % e)



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
    `Projects <../models/Projects.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_templates_in_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.serve_templates_in_project(project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->serve_templates_in_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildTypes <../models/BuildTypes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_build_types_order
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    field = 'field_example' # str | 
    body = dohq_teamcity.BuildTypes() # BuildTypes |  (optional)

    try:
        api_response = tc.project_api.set_build_types_order(project_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_build_types_order: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 
   * - **body**
     - `BuildTypes <../models/BuildTypes.html>`_
     - [optional] 

Return type:
    `BuildTypes <../models/BuildTypes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_parameter(project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
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
    project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_parameter_0(name, project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameter_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **project_locator**
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

        feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
    fields = 'fields_example' # str |  (optional)
    fields2 = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_parameter_1(feature_locator, project_locator, body=body, fields=fields, fields2=fields2)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameter_1: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `ModelProperty <../models/ModelProperty.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 
   * - **fields2**
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
    feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.ModelProperty() # ModelProperty |  (optional)
    fields = 'fields_example' # str |  (optional)
    fields2 = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_parameter_2(name, feature_locator, project_locator, body=body, fields=fields, fields2=fields2)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameter_2: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `ModelProperty <../models/ModelProperty.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 
   * - **fields2**
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
    project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.Type() # Type |  (optional)

    try:
        api_response = tc.project_api.set_parameter_type(name, project_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameter_type: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **project_locator**
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
    project_locator = 'project_locator_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_parameter_type_raw_value(name, project_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameter_type_raw_value: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **project_locator**
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
    project_locator = 'project_locator_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_parameter_value_long(name, project_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameter_value_long: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **project_locator**
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
    feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    body = 'body_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_parameter_value_long_0(name, feature_locator, project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameter_value_long_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **name**
     - **str**
     - 
   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 
   * - **fields**
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

        project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.Properties() # Properties |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_parameters(project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameters: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
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

        feature_locator = 'feature_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.Properties() # Properties |  (optional)
    fields = 'fields_example' # str |  (optional)
    fields2 = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_parameters_0(feature_locator, project_locator, body=body, fields=fields, fields2=fields2)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parameters_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **feature_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `Properties <../models/Properties.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 
   * - **fields2**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_parent_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.Project() # Project |  (optional)

    try:
        api_response = tc.project_api.set_parent_project(project_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_parent_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `Project <../models/Project.html>`_
     - [optional] 

Return type:
    `Project <../models/Project.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_project_agent_pools
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.AgentPools() # AgentPools |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_project_agent_pools(project_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_project_agent_pools: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `AgentPools <../models/AgentPools.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AgentPools <../models/AgentPools.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_project_agent_pools_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    body = dohq_teamcity.AgentPool() # AgentPool |  (optional)

    try:
        api_response = tc.project_api.set_project_agent_pools_0(project_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_project_agent_pools_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **body**
     - `AgentPool <../models/AgentPool.html>`_
     - [optional] 

Return type:
    `AgentPool <../models/AgentPool.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_project_filed
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.project_api.set_project_filed(project_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_project_filed: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
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


set_projects_order
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project_locator = 'project_locator_example' # str | 
    field = 'field_example' # str | 
    body = dohq_teamcity.Projects() # Projects |  (optional)

    try:
        api_response = tc.project_api.set_projects_order(project_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->set_projects_order: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 
   * - **body**
     - `Projects <../models/Projects.html>`_
     - [optional] 

Return type:
    `Projects <../models/Projects.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


