dohq_teamcity.GroupApi
######################################

`API examples <../../teamcity_apis/GroupApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `add_group`__
     - **POST** ``/app/rest/userGroups``
   * - `add_role`__
     - **POST** ``/app/rest/userGroups/{groupLocator}/roles``
   * - `add_role_put`__
     - **PUT** ``/app/rest/userGroups/{groupLocator}/roles``
   * - `add_role_simple`__
     - **POST** ``/app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope}``
   * - `delete_group`__
     - **DELETE** ``/app/rest/userGroups/{groupLocator}``
   * - `delete_role`__
     - **DELETE** ``/app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope}``
   * - `get_permissions`__
     - **GET** ``/app/rest/userGroups/{groupLocator}/debug/permissions``
   * - `get_properties`__
     - **GET** ``/app/rest/userGroups/{groupLocator}/properties``
   * - `list_role`__
     - **GET** ``/app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope}``
   * - `list_roles`__
     - **GET** ``/app/rest/userGroups/{groupLocator}/roles``
   * - `put_user_property`__
     - **PUT** ``/app/rest/userGroups/{groupLocator}/properties/{name}``
   * - `remove_user_property`__
     - **DELETE** ``/app/rest/userGroups/{groupLocator}/properties/{name}``
   * - `serve_group`__
     - **GET** ``/app/rest/userGroups/{groupLocator}``
   * - `serve_groups`__
     - **GET** ``/app/rest/userGroups``
   * - `serve_user_properties`__
     - **GET** ``/app/rest/userGroups/{groupLocator}/properties/{name}``

add_group
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.Group() # Group |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.group_api.add_group(body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->add_group: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `Group <../models/Group.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Group <../models/Group.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_role
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    body = dohq_teamcity.Role() # Role |  (optional)

    try:
        api_response = tc.group_api.add_role(group_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->add_role: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **body**
     - `Role <../models/Role.html>`_
     - [optional] 

Return type:
    `Role <../models/Role.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_role_put
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    body = dohq_teamcity.Roles() # Roles |  (optional)

    try:
        api_response = tc.group_api.add_role_put(group_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->add_role_put: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **body**
     - `Roles <../models/Roles.html>`_
     - [optional] 

Return type:
    `Roles <../models/Roles.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_role_simple
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        api_response = tc.group_api.add_role_simple(group_locator, role_id, scope)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->add_role_simple: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **role_id**
     - **str**
     - 
   * - **scope**
     - **str**
     - 

Return type:
    `Role <../models/Role.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_group
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 

    try:
        tc.group_api.delete_group(group_locator)
    except ApiException as e:
        print("Exception when calling GroupApi->delete_group: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_role
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        tc.group_api.delete_role(group_locator, role_id, scope)
    except ApiException as e:
        print("Exception when calling GroupApi->delete_role: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **role_id**
     - **str**
     - 
   * - **scope**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_permissions
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 

    try:
        api_response = tc.group_api.get_permissions(group_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->get_permissions: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_properties
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.group_api.get_properties(group_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->get_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


list_role
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        api_response = tc.group_api.list_role(group_locator, role_id, scope)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->list_role: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **role_id**
     - **str**
     - 
   * - **scope**
     - **str**
     - 

Return type:
    `Role <../models/Role.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


list_roles
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 

    try:
        api_response = tc.group_api.list_roles(group_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->list_roles: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 

Return type:
    `Roles <../models/Roles.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


put_user_property
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    name = 'name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.group_api.put_user_property(group_locator, name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->put_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
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


remove_user_property
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        tc.group_api.remove_user_property(group_locator, name)
    except ApiException as e:
        print("Exception when calling GroupApi->remove_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_group
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.group_api.serve_group(group_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->serve_group: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Group <../models/Group.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_groups
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.group_api.serve_groups(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->serve_groups: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Groups <../models/Groups.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_user_properties
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        group_locator = 'group_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        api_response = tc.group_api.serve_user_properties(group_locator, name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupApi->serve_user_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **group_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


