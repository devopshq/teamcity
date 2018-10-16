dohq_teamcity.AgentPoolApi
######################################

`API examples <../../teamcity_apis/AgentPoolApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `add_agent`__
     - **POST** ``/app/rest/agentPools/{agentPoolLocator}/agents``
   * - `add_project`__
     - **POST** ``/app/rest/agentPools/{agentPoolLocator}/projects``
   * - `create_pool`__
     - **POST** ``/app/rest/agentPools``
   * - `delete_pool`__
     - **DELETE** ``/app/rest/agentPools/{agentPoolLocator}``
   * - `delete_pool_project`__
     - **DELETE** ``/app/rest/agentPools/{agentPoolLocator}/projects/{projectLocator}``
   * - `delete_projects`__
     - **DELETE** ``/app/rest/agentPools/{agentPoolLocator}/projects``
   * - `get_field`__
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}/{field}``
   * - `get_pool`__
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}``
   * - `get_pool_agents`__
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}/agents``
   * - `get_pool_project`__
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}/projects/{projectLocator}``
   * - `get_pool_projects`__
     - **GET** ``/app/rest/agentPools/{agentPoolLocator}/projects``
   * - `get_pools`__
     - **GET** ``/app/rest/agentPools``
   * - `replace_projects`__
     - **PUT** ``/app/rest/agentPools/{agentPoolLocator}/projects``
   * - `set_field`__
     - **PUT** ``/app/rest/agentPools/{agentPoolLocator}/{field}``

add_agent
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    body = dohq_teamcity.Agent() # Agent |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.add_agent(agent_pool_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->add_agent: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **body**
     - `Agent <../models/Agent.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Agent <../models/Agent.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    body = dohq_teamcity.Project() # Project |  (optional)

    try:
        api_response = tc.agent_pool_api.add_project(agent_pool_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->add_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **body**
     - `Project <../models/Project.html>`_
     - [optional] 

Return type:
    `Project <../models/Project.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


create_pool
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.AgentPool() # AgentPool |  (optional)

    try:
        api_response = tc.agent_pool_api.create_pool(body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->create_pool: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `AgentPool <../models/AgentPool.html>`_
     - [optional] 

Return type:
    `AgentPool <../models/AgentPool.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_pool
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 

    try:
        tc.agent_pool_api.delete_pool(agent_pool_locator)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->delete_pool: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_pool_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 

    try:
        tc.agent_pool_api.delete_pool_project(agent_pool_locator, project_locator)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->delete_pool_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_projects
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 

    try:
        tc.agent_pool_api.delete_projects(agent_pool_locator)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->delete_projects: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.agent_pool_api.get_field(agent_pool_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_pool
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pool(agent_pool_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pool: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `AgentPool <../models/AgentPool.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_pool_agents
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pool_agents(agent_pool_locator, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pool_agents: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Agents <../models/Agents.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_pool_project
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    project_locator = 'project_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pool_project(agent_pool_locator, project_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pool_project: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **project_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Project <../models/Project.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_pool_projects
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pool_projects(agent_pool_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pool_projects: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Projects <../models/Projects.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_pools
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.get_pools(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->get_pools: %s\n" % e)



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
    `AgentPools <../models/AgentPools.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_projects
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    body = dohq_teamcity.Projects() # Projects |  (optional)

    try:
        api_response = tc.agent_pool_api.replace_projects(agent_pool_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->replace_projects: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
     - **str**
     - 
   * - **body**
     - `Projects <../models/Projects.html>`_
     - [optional] 

Return type:
    `Projects <../models/Projects.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        agent_pool_locator = 'agent_pool_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.agent_pool_api.set_field(agent_pool_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentPoolApi->set_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **agent_pool_locator**
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


