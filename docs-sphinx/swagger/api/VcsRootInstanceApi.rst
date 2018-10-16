dohq_teamcity.VcsRootInstanceApi
######################################

`API examples <../../teamcity_apis/VcsRootInstanceApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `delete_instance_field`__
     - **DELETE** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field}``
   * - `delete_repository_state`__
     - **DELETE** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState``
   * - `get_children`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/children{path}``
   * - `get_children_alias`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/{path}``
   * - `get_content`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/content{path}``
   * - `get_content_alias`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/files{path}``
   * - `get_metadata`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/metadata{path}``
   * - `get_repository_state`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState``
   * - `get_repository_state_creation_date`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState/creationDate``
   * - `get_root`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest``
   * - `get_zipped`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/archived{path}``
   * - `schedule_checking_for_changes`__
     - **POST** ``/app/rest/vcs-root-instances/checkingForChangesQueue``
   * - `schedule_checking_for_changes_0`__
     - **POST** ``/app/rest/vcs-root-instances/commitHookNotification``
   * - `serve_instance`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}``
   * - `serve_instance_field`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field}``
   * - `serve_instances`__
     - **GET** ``/app/rest/vcs-root-instances``
   * - `serve_root_instance_properties`__
     - **GET** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/properties``
   * - `set_instance_field`__
     - **PUT** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field}``
   * - `set_repository_state`__
     - **PUT** ``/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState``

delete_instance_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        tc.vcs_root_instance_api.delete_instance_field(vcs_root_instance_locator, field)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->delete_instance_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_repository_state
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 

    try:
        tc.vcs_root_instance_api.delete_repository_state(vcs_root_instance_locator)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->delete_repository_state: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_children
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.get_children(path, vcs_root_instance_locator, base_path=base_path, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->get_children: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **vcs_root_instance_locator**
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

Return type:
    [**Files**](../models/Files.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_children_alias
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.get_children_alias(path, vcs_root_instance_locator, base_path=base_path, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->get_children_alias: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **vcs_root_instance_locator**
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

Return type:
    [**Files**](../models/Files.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_content
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 

    try:
        tc.vcs_root_instance_api.get_content(path, vcs_root_instance_locator)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->get_content: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **vcs_root_instance_locator**
     - **str**
     - 

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
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 

    try:
        tc.vcs_root_instance_api.get_content_alias(path, vcs_root_instance_locator)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->get_content_alias: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **vcs_root_instance_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_metadata
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.get_metadata(path, vcs_root_instance_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->get_metadata: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**file**](../models/file.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_repository_state
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.get_repository_state(vcs_root_instance_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->get_repository_state: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**Entries**](../models/Entries.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_repository_state_creation_date
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 

    try:
        api_response = tc.vcs_root_instance_api.get_repository_state_creation_date(vcs_root_instance_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->get_repository_state_creation_date: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
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

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.get_root(vcs_root_instance_locator, base_path=base_path, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->get_root: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
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

Return type:
    [**Files**](../models/Files.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_zipped
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    name = 'name_example' # str |  (optional)

    try:
        tc.vcs_root_instance_api.get_zipped(path, vcs_root_instance_locator, base_path=base_path, locator=locator, name=name)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->get_zipped: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **vcs_root_instance_locator**
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

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


schedule_checking_for_changes
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    requestor = 'requestor_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.schedule_checking_for_changes(locator=locator, requestor=requestor, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->schedule_checking_for_changes: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **locator**
     - **str**
     - [optional] 
   * - **requestor**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**VcsRootInstances**](../models/VcsRootInstances.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


schedule_checking_for_changes_0
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    ok_on_nothing_found = true # bool |  (optional)

    try:
        tc.vcs_root_instance_api.schedule_checking_for_changes_0(locator=locator, ok_on_nothing_found=ok_on_nothing_found)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->schedule_checking_for_changes_0: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **locator**
     - **str**
     - [optional] 
   * - **ok_on_nothing_found**
     - **bool**
     - [optional] 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_instance
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.serve_instance(vcs_root_instance_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->serve_instance: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**VcsRootInstance**](../models/VcsRootInstance.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_instance_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.vcs_root_instance_api.serve_instance_field(vcs_root_instance_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->serve_instance_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_instances
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.serve_instances(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->serve_instances: %s\n" % e)



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
    [**VcsRootInstances**](../models/VcsRootInstances.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_root_instance_properties
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.serve_root_instance_properties(vcs_root_instance_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->serve_root_instance_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**Properties**](../models/Properties.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_instance_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.set_instance_field(vcs_root_instance_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->set_instance_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
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


set_repository_state
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    body = dohq_teamcity.Entries() # Entries |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_instance_api.set_repository_state(vcs_root_instance_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootInstanceApi->set_repository_state: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **body**
     - [**Entries**](Entries.md)
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**Entries**](../models/Entries.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



OLD
-------

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instance_field**](VcsRootInstanceApi.md#delete_instance_field) | **DELETE** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field} | 
[**delete_repository_state**](VcsRootInstanceApi.md#delete_repository_state) | **DELETE** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState | 
[**get_children**](VcsRootInstanceApi.md#get_children) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/children{path} | 
[**get_children_alias**](VcsRootInstanceApi.md#get_children_alias) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/{path} | 
[**get_content**](VcsRootInstanceApi.md#get_content) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/content{path} | 
[**get_content_alias**](VcsRootInstanceApi.md#get_content_alias) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/files{path} | 
[**get_metadata**](VcsRootInstanceApi.md#get_metadata) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/metadata{path} | 
[**get_repository_state**](VcsRootInstanceApi.md#get_repository_state) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState | 
[**get_repository_state_creation_date**](VcsRootInstanceApi.md#get_repository_state_creation_date) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState/creationDate | 
[**get_root**](VcsRootInstanceApi.md#get_root) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest | 
[**get_zipped**](VcsRootInstanceApi.md#get_zipped) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/archived{path} | 
[**schedule_checking_for_changes**](VcsRootInstanceApi.md#schedule_checking_for_changes) | **POST** /app/rest/vcs-root-instances/checkingForChangesQueue | 
[**schedule_checking_for_changes_0**](VcsRootInstanceApi.md#schedule_checking_for_changes_0) | **POST** /app/rest/vcs-root-instances/commitHookNotification | 
[**serve_instance**](VcsRootInstanceApi.md#serve_instance) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator} | 
[**serve_instance_field**](VcsRootInstanceApi.md#serve_instance_field) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field} | 
[**serve_instances**](VcsRootInstanceApi.md#serve_instances) | **GET** /app/rest/vcs-root-instances | 
[**serve_root_instance_properties**](VcsRootInstanceApi.md#serve_root_instance_properties) | **GET** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/properties | 
[**set_instance_field**](VcsRootInstanceApi.md#set_instance_field) | **PUT** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field} | 
[**set_repository_state**](VcsRootInstanceApi.md#set_repository_state) | **PUT** /app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState | 


# **delete_instance_field**
> delete_instance_field(vcs_root_instance_locator, field)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
field = 'field_example' # str | 

try:
    tc.vcs_root_instance_api.delete_instance_field(vcs_root_instance_locator, field)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->delete_instance_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_repository_state**
> delete_repository_state(vcs_root_instance_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 

try:
    tc.vcs_root_instance_api.delete_repository_state(vcs_root_instance_locator)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->delete_repository_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_children**
> Files get_children(path, vcs_root_instance_locator, base_path=base_path, locator=locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

path = 'path_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.get_children(path, vcs_root_instance_locator, base_path=base_path, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->get_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Files**](../models/Files.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_children_alias**
> Files get_children_alias(path, vcs_root_instance_locator, base_path=base_path, locator=locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

path = 'path_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.get_children_alias(path, vcs_root_instance_locator, base_path=base_path, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->get_children_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Files**](../models/Files.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_content**
> get_content(path, vcs_root_instance_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

path = 'path_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 

try:
    tc.vcs_root_instance_api.get_content(path, vcs_root_instance_locator)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->get_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_content_alias**
> get_content_alias(path, vcs_root_instance_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

path = 'path_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 

try:
    tc.vcs_root_instance_api.get_content_alias(path, vcs_root_instance_locator)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->get_content_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_metadata**
> file get_metadata(path, vcs_root_instance_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

path = 'path_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.get_metadata(path, vcs_root_instance_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**file**](../models/file.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_repository_state**
> Entries get_repository_state(vcs_root_instance_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.get_repository_state(vcs_root_instance_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->get_repository_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Entries**](../models/Entries.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_repository_state_creation_date**
> str get_repository_state_creation_date(vcs_root_instance_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 

try:
    api_response = tc.vcs_root_instance_api.get_repository_state_creation_date(vcs_root_instance_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->get_repository_state_creation_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_root**
> Files get_root(vcs_root_instance_locator, base_path=base_path, locator=locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.get_root(vcs_root_instance_locator, base_path=base_path, locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->get_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Files**](../models/Files.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_zipped**
> get_zipped(path, vcs_root_instance_locator, base_path=base_path, locator=locator, name=name)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

path = 'path_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
base_path = 'base_path_example' # str |  (optional)
locator = 'locator_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    tc.vcs_root_instance_api.get_zipped(path, vcs_root_instance_locator, base_path=base_path, locator=locator, name=name)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->get_zipped: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **base_path** | **str**|  | [optional] 
 **locator** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **schedule_checking_for_changes**
> VcsRootInstances schedule_checking_for_changes(locator=locator, requestor=requestor, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
requestor = 'requestor_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.schedule_checking_for_changes(locator=locator, requestor=requestor, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->schedule_checking_for_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **requestor** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootInstances**](../models/VcsRootInstances.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **schedule_checking_for_changes_0**
> schedule_checking_for_changes_0(locator=locator, ok_on_nothing_found=ok_on_nothing_found)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
ok_on_nothing_found = true # bool |  (optional)

try:
    tc.vcs_root_instance_api.schedule_checking_for_changes_0(locator=locator, ok_on_nothing_found=ok_on_nothing_found)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->schedule_checking_for_changes_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **ok_on_nothing_found** | **bool**|  | [optional] 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_instance**
> VcsRootInstance serve_instance(vcs_root_instance_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.serve_instance(vcs_root_instance_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->serve_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootInstance**](../models/VcsRootInstance.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_instance_field**
> str serve_instance_field(vcs_root_instance_locator, field)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = tc.vcs_root_instance_api.serve_instance_field(vcs_root_instance_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->serve_instance_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_instances**
> VcsRootInstances serve_instances(locator=locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.serve_instances(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->serve_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootInstances**](../models/VcsRootInstances.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_root_instance_properties**
> Properties serve_root_instance_properties(vcs_root_instance_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.serve_root_instance_properties(vcs_root_instance_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->serve_root_instance_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](../models/Properties.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **set_instance_field**
> str set_instance_field(vcs_root_instance_locator, field, body=body)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.set_instance_field(vcs_root_instance_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->set_instance_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 
 **field** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **set_repository_state**
> Entries set_repository_state(vcs_root_instance_locator, body=body, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
body = dohq_teamcity.Entries() # Entries |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_instance_api.set_repository_state(vcs_root_instance_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootInstanceApi->set_repository_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_instance_locator** | **str**|  | 
 **body** | [**Entries**](Entries.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Entries**](../models/Entries.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


