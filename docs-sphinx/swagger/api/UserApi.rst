dohq_teamcity.UserApi
######################################

`API examples <../../teamcity_apis/UserApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `add_group`__
     - **POST** ``/app/rest/users/{userLocator}/groups``
   * - `add_role`__
     - **POST** ``/app/rest/users/{userLocator}/roles``
   * - `add_role_simple`__
     - **PUT** ``/app/rest/users/{userLocator}/roles/{roleId}/{scope}``
   * - `add_role_simple_post`__
     - **POST** ``/app/rest/users/{userLocator}/roles/{roleId}/{scope}``
   * - `create_user`__
     - **POST** ``/app/rest/users``
   * - `delete_remember_me`__
     - **DELETE** ``/app/rest/users/{userLocator}/debug/rememberMe``
   * - `delete_role`__
     - **DELETE** ``/app/rest/users/{userLocator}/roles/{roleId}/{scope}``
   * - `delete_user`__
     - **DELETE** ``/app/rest/users/{userLocator}``
   * - `delete_user_field`__
     - **DELETE** ``/app/rest/users/{userLocator}/{field}``
   * - `get_groups`__
     - **GET** ``/app/rest/users/{userLocator}/groups``
   * - `get_permissions`__
     - **GET** ``/app/rest/users/{userLocator}/debug/permissions``
   * - `list_role`__
     - **GET** ``/app/rest/users/{userLocator}/roles/{roleId}/{scope}``
   * - `list_roles`__
     - **GET** ``/app/rest/users/{userLocator}/roles``
   * - `put_user_property`__
     - **PUT** ``/app/rest/users/{userLocator}/properties/{name}``
   * - `remove_user_property`__
     - **DELETE** ``/app/rest/users/{userLocator}/properties/{name}``
   * - `replace_groups`__
     - **PUT** ``/app/rest/users/{userLocator}/groups``
   * - `replace_roles`__
     - **PUT** ``/app/rest/users/{userLocator}/roles``
   * - `serve_user`__
     - **GET** ``/app/rest/users/{userLocator}``
   * - `serve_user_field`__
     - **GET** ``/app/rest/users/{userLocator}/{field}``
   * - `serve_user_properties`__
     - **GET** ``/app/rest/users/{userLocator}/properties``
   * - `serve_user_property`__
     - **GET** ``/app/rest/users/{userLocator}/properties/{name}``
   * - `serve_users`__
     - **GET** ``/app/rest/users``
   * - `set_user_field`__
     - **PUT** ``/app/rest/users/{userLocator}/{field}``
   * - `update_user`__
     - **PUT** ``/app/rest/users/{userLocator}``

add_group
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.Group() # Group |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.user_api.add_group(user_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->add_group: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
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

        user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.Role() # Role |  (optional)

    try:
        api_response = tc.user_api.add_role(user_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->add_role: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **body**
     - `Role <../models/Role.html>`_
     - [optional] 

Return type:
    `Role <../models/Role.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


add_role_simple
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        api_response = tc.user_api.add_role_simple(user_locator, role_id, scope)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->add_role_simple: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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


add_role_simple_post
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        tc.user_api.add_role_simple_post(user_locator, role_id, scope)
    except ApiException as e:
        print("Exception when calling UserApi->add_role_simple_post: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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


create_user
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.User() # User |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.user_api.create_user(body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `User <../models/User.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `User <../models/User.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_remember_me
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 

    try:
        tc.user_api.delete_remember_me(user_locator)
    except ApiException as e:
        print("Exception when calling UserApi->delete_remember_me: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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

        user_locator = 'user_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        tc.user_api.delete_role(user_locator, role_id, scope)
    except ApiException as e:
        print("Exception when calling UserApi->delete_role: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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


delete_user
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 

    try:
        tc.user_api.delete_user(user_locator)
    except ApiException as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_user_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        tc.user_api.delete_user_field(user_locator, field)
    except ApiException as e:
        print("Exception when calling UserApi->delete_user_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_groups
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.user_api.get_groups(user_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_groups: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Groups <../models/Groups.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_permissions
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 

    try:
        api_response = tc.user_api.get_permissions(user_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_permissions: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


list_role
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        api_response = tc.user_api.list_role(user_locator, role_id, scope)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->list_role: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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

        user_locator = 'user_locator_example' # str | 

    try:
        api_response = tc.user_api.list_roles(user_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->list_roles: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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

        user_locator = 'user_locator_example' # str | 
    name = 'name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.user_api.put_user_property(user_locator, name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->put_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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

        user_locator = 'user_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        tc.user_api.remove_user_property(user_locator, name)
    except ApiException as e:
        print("Exception when calling UserApi->remove_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_groups
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.Groups() # Groups |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.user_api.replace_groups(user_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->replace_groups: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **body**
     - `Groups <../models/Groups.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Groups <../models/Groups.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


replace_roles
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.Roles() # Roles |  (optional)

    try:
        api_response = tc.user_api.replace_roles(user_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->replace_roles: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **body**
     - `Roles <../models/Roles.html>`_
     - [optional] 

Return type:
    `Roles <../models/Roles.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_user
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.user_api.serve_user(user_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->serve_user: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `User <../models/User.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_user_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.user_api.serve_user_field(user_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->serve_user_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_user_properties
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.user_api.serve_user_properties(user_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->serve_user_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_user_property
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        api_response = tc.user_api.serve_user_property(user_locator, name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->serve_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_users
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.user_api.serve_users(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->serve_users: %s\n" % e)



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
    `Users <../models/Users.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_user_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.user_api.set_user_field(user_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->set_user_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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


update_user
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.User() # User |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.user_api.update_user(user_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **body**
     - `User <../models/User.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `User <../models/User.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


