dohq_teamcity.ChangeApi
######################################

`API examples <../../teamcity_apis/ChangeApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `get_change_attributes`__
     - **GET** ``/app/rest/changes/{changeLocator}/attributes``
   * - `get_change_duplicates`__
     - **GET** ``/app/rest/changes/{changeLocator}/duplicates``
   * - `get_change_field`__
     - **GET** ``/app/rest/changes/{changeLocator}/{field}``
   * - `get_change_first_builds`__
     - **GET** ``/app/rest/changes/{changeLocator}/firstBuilds``
   * - `get_change_issue`__
     - **GET** ``/app/rest/changes/{changeLocator}/issues``
   * - `get_change_parent_revisions`__
     - **GET** ``/app/rest/changes/{changeLocator}/parentRevisions``
   * - `get_change_vcs_root`__
     - **GET** ``/app/rest/changes/{changeLocator}/vcsRoot``
   * - `get_change_vcs_root_instance`__
     - **GET** ``/app/rest/changes/{changeLocator}/vcsRootInstance``
   * - `get_parent_changes`__
     - **GET** ``/app/rest/changes/{changeLocator}/parentChanges``
   * - `get_related_build_types`__
     - **GET** ``/app/rest/changes/{changeLocator}/buildTypes``
   * - `serve_change`__
     - **GET** ``/app/rest/changes/{changeLocator}``
   * - `serve_changes`__
     - **GET** ``/app/rest/changes``

get_change_attributes
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.change_api.get_change_attributes(change_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_change_attributes: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Entries <../models/Entries.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_change_duplicates
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.change_api.get_change_duplicates(change_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_change_duplicates: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Changes <../models/Changes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_change_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.change_api.get_change_field(change_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_change_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_change_first_builds
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.change_api.get_change_first_builds(change_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_change_first_builds: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Builds <../models/Builds.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_change_issue
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 

    try:
        api_response = tc.change_api.get_change_issue(change_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_change_issue: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 

Return type:
    `Issues <../models/Issues.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_change_parent_revisions
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 

    try:
        api_response = tc.change_api.get_change_parent_revisions(change_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_change_parent_revisions: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 

Return type:
    `Items <../models/Items.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_change_vcs_root
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.change_api.get_change_vcs_root(change_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_change_vcs_root: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRootInstance <../models/VcsRootInstance.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_change_vcs_root_instance
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.change_api.get_change_vcs_root_instance(change_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_change_vcs_root_instance: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRootInstance <../models/VcsRootInstance.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_parent_changes
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.change_api.get_parent_changes(change_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_parent_changes: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Changes <../models/Changes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_related_build_types
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.change_api.get_related_build_types(change_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->get_related_build_types: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `BuildTypes <../models/BuildTypes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_change
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        change_locator = 'change_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.change_api.serve_change(change_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->serve_change: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **change_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Change <../models/Change.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_changes
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        project = 'project_example' # str |  (optional)
    build_type = 'build_type_example' # str |  (optional)
    build = 'build_example' # str |  (optional)
    vcs_root = 'vcs_root_example' # str |  (optional)
    since_change = 'since_change_example' # str |  (optional)
    start = 789 # int |  (optional)
    count = 56 # int |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.change_api.serve_changes(project=project, build_type=build_type, build=build, vcs_root=vcs_root, since_change=since_change, start=start, count=count, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChangeApi->serve_changes: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **project**
     - **str**
     - [optional] 
   * - **build_type**
     - **str**
     - [optional] 
   * - **build**
     - **str**
     - [optional] 
   * - **vcs_root**
     - **str**
     - [optional] 
   * - **since_change**
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
    `Changes <../models/Changes.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


