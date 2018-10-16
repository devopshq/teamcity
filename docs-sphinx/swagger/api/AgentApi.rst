dohq_teamcity.AgentApi
######################################

`API examples <../../teamcity_apis/AgentApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `delete_agent`__
     - **DELETE** ``/app/rest/agents/{agentLocator}``
   * - `get_agent_pool`__
     - **GET** ``/app/rest/agents/{agentLocator}/pool``
   * - `get_authorized_info`__
     - **GET** ``/app/rest/agents/{agentLocator}/authorizedInfo``
   * - `get_compatible_build_types`__
     - **GET** ``/app/rest/agents/{agentLocator}/compatibleBuildTypes``
   * - `get_enabled_info`__
     - **GET** ``/app/rest/agents/{agentLocator}/enabledInfo``
   * - `get_incompatible_build_types`__
     - **GET** ``/app/rest/agents/{agentLocator}/incompatibleBuildTypes``
   * - `serve_agent`__
     - **GET** ``/app/rest/agents/{agentLocator}``
   * - `serve_agent_field`__
     - **GET** ``/app/rest/agents/{agentLocator}/{field}``
   * - `serve_agents`__
     - **GET** ``/app/rest/agents``
   * - `set_agent_field`__
     - **PUT** ``/app/rest/agents/{agentLocator}/{field}``
   * - `set_agent_pool`__
     - **PUT** ``/app/rest/agents/{agentLocator}/pool``
   * - `set_authorized_info`__
     - **PUT** ``/app/rest/agents/{agentLocator}/authorizedInfo``
   * - `set_enabled_info`__
     - **PUT** ``/app/rest/agents/{agentLocator}/enabledInfo``

delete_agent
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_locator = 'agent_locator_example' # str | 

    try:
        tc.agent_api.delete_agent(agent_locator)
    except ApiException as e:
        print("Exception when calling AgentApi->delete_agent: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_agent_pool
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_locator = 'agent_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_api.get_agent_pool(agent_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentApi->get_agent_pool: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AgentPool <../models/AgentPool.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_authorized_info
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_locator = 'agent_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_api.get_authorized_info(agent_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentApi->get_authorized_info: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AuthorizedInfo <../models/AuthorizedInfo.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_compatible_build_types
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_locator = 'agent_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_api.get_compatible_build_types(agent_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentApi->get_compatible_build_types: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildTypes <../models/BuildTypes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_enabled_info
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_locator = 'agent_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_api.get_enabled_info(agent_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentApi->get_enabled_info: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `EnabledInfo <../models/EnabledInfo.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_incompatible_build_types
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_locator = 'agent_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_api.get_incompatible_build_types(agent_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentApi->get_incompatible_build_types: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Compatibilities <../models/Compatibilities.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_agent
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_locator = 'agent_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_api.serve_agent(agent_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentApi->serve_agent: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Agent <../models/Agent.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_agent_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_locator = 'agent_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.agent_api.serve_agent_field(agent_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentApi->serve_agent_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_agents
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

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



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **include_disconnected**
     - **bool**
     - [optional] 
   * - **include_unauthorized**
     - **bool**
     - [optional] 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Agents <../models/Agents.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_agent_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

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



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
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


set_agent_pool
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

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



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **body**
     - `AgentPool <../models/AgentPool.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AgentPool <../models/AgentPool.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_authorized_info
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

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



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **body**
     - `AuthorizedInfo <../models/AuthorizedInfo.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AuthorizedInfo <../models/AuthorizedInfo.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_enabled_info
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

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



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_locator**
     - **str**
     - 
   * - **body**
     - `EnabledInfo <../models/EnabledInfo.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `EnabledInfo <../models/EnabledInfo.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


