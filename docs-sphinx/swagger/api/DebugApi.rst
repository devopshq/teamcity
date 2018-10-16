dohq_teamcity.DebugApi
######################################

`API examples <../../teamcity_apis/DebugApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `delete_current_remember_me`__
     - **DELETE** ``/app/rest/debug/currentRequest/rememberMe``
   * - `empty_task`__
     - **POST** ``/app/rest/debug/emptyTask``
   * - `execute_db_query`__
     - **GET** ``/app/rest/debug/database/query/{query}``
   * - `get_current_session`__
     - **GET** ``/app/rest/debug/currentRequest/session``
   * - `get_current_session_max_inactive_interval`__
     - **GET** ``/app/rest/debug/currentRequest/session/maxInactiveSeconds``
   * - `get_current_user_permissions`__
     - **GET** ``/app/rest/debug/currentUserPermissions``
   * - `get_date`__
     - **GET** ``/app/rest/debug/date/{dateLocator}``
   * - `get_environment_variables`__
     - **GET** ``/app/rest/debug/jvm/environmentVariables``
   * - `get_hashed`__
     - **GET** ``/app/rest/debug/values/transform/{method}``
   * - `get_request_details`__
     - **GET** ``/app/rest/debug/currentRequest/details``
   * - `get_scrambled`__
     - **GET** ``/app/rest/debug/values/password/scrambled``
   * - `get_sessions`__
     - **GET** ``/app/rest/debug/sessions``
   * - `get_system_properties`__
     - **GET** ``/app/rest/debug/jvm/systemProperties``
   * - `get_thread_dump`__
     - **GET** ``/app/rest/debug/threadDump``
   * - `get_unscrambled`__
     - **GET** ``/app/rest/debug/values/password/unscrambled``
   * - `invalidate_current_session`__
     - **DELETE** ``/app/rest/debug/currentRequest/session``
   * - `list_db_tables`__
     - **GET** ``/app/rest/debug/database/tables``
   * - `new_remember_me`__
     - **POST** ``/app/rest/debug/currentRequest/rememberMe``
   * - `save_memory_dump`__
     - **POST** ``/app/rest/debug/memory/dumps``
   * - `schedule_checking_for_changes`__
     - **POST** ``/app/rest/debug/vcsCheckingForChangesQueue``
   * - `set_current_session_max_inactive_interval`__
     - **PUT** ``/app/rest/debug/currentRequest/session/maxInactiveSeconds``

delete_current_remember_me
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    
    try:
        tc.debug_api.delete_current_remember_me()
    except ApiException as e:
        print("Exception when calling DebugApi->delete_current_remember_me: %s\n" % e)


This endpoint does not need any parameter.

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


empty_task
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        time = 'time_example' # str |  (optional)
    load = 56 # int |  (optional)

    try:
        api_response = tc.debug_api.empty_task(time=time, load=load)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->empty_task: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **time**
     - **str**
     - [optional] 
   * - **load**
     - **int**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


execute_db_query
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        query = 'query_example' # str | 
    field_delimiter = ', ' # str |  (optional) (default to , )
    data_retrieve_query = 'data_retrieve_query_example' # str |  (optional)
    count = 1000 # int |  (optional) (default to 1000)

    try:
        api_response = tc.debug_api.execute_db_query(query, field_delimiter=field_delimiter, data_retrieve_query=data_retrieve_query, count=count)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->execute_db_query: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **query**
     - **str**
     - 
   * - **field_delimiter**
     - **str**
     - [optional] [default to ``, ``]
   * - **data_retrieve_query**
     - **str**
     - [optional] 
   * - **count**
     - **int**
     - [optional] [default to ``1000``]

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_current_session
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.debug_api.get_current_session(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_current_session: %s\n" % e)



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
    `Session <../models/Session.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_current_session_max_inactive_interval
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    
    try:
        api_response = tc.debug_api.get_current_session_max_inactive_interval()
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_current_session_max_inactive_interval: %s\n" % e)


This endpoint does not need any parameter.

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_current_user_permissions
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    
    try:
        api_response = tc.debug_api.get_current_user_permissions()
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_current_user_permissions: %s\n" % e)


This endpoint does not need any parameter.

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_date
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        date_locator = 'date_locator_example' # str | 
    format = 'format_example' # str |  (optional)
    timezone = 'timezone_example' # str |  (optional)

    try:
        api_response = tc.debug_api.get_date(date_locator, format=format, timezone=timezone)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_date: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **date_locator**
     - **str**
     - 
   * - **format**
     - **str**
     - [optional] 
   * - **timezone**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_environment_variables
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.debug_api.get_environment_variables(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_environment_variables: %s\n" % e)



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
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_hashed
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        method = 'method_example' # str | 
    value = 'value_example' # str |  (optional)

    try:
        api_response = tc.debug_api.get_hashed(method, value=value)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_hashed: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **method**
     - **str**
     - 
   * - **value**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_request_details
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    
    try:
        api_response = tc.debug_api.get_request_details()
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_request_details: %s\n" % e)


This endpoint does not need any parameter.

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_scrambled
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        value = 'value_example' # str |  (optional)

    try:
        api_response = tc.debug_api.get_scrambled(value=value)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_scrambled: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **value**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_sessions
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        manager = 789 # int |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.debug_api.get_sessions(manager=manager, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_sessions: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **manager**
     - **int**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Sessions <../models/Sessions.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_system_properties
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.debug_api.get_system_properties(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_system_properties: %s\n" % e)



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
    `Properties <../models/Properties.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_thread_dump
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locked_monitors = 'locked_monitors_example' # str |  (optional)
    locked_synchronizers = 'locked_synchronizers_example' # str |  (optional)
    detect_locks = 'detect_locks_example' # str |  (optional)

    try:
        api_response = tc.debug_api.get_thread_dump(locked_monitors=locked_monitors, locked_synchronizers=locked_synchronizers, detect_locks=detect_locks)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_thread_dump: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **locked_monitors**
     - **str**
     - [optional] 
   * - **locked_synchronizers**
     - **str**
     - [optional] 
   * - **detect_locks**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_unscrambled
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        value = 'value_example' # str |  (optional)

    try:
        api_response = tc.debug_api.get_unscrambled(value=value)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->get_unscrambled: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **value**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


invalidate_current_session
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    
    try:
        tc.debug_api.invalidate_current_session()
    except ApiException as e:
        print("Exception when calling DebugApi->invalidate_current_session: %s\n" % e)


This endpoint does not need any parameter.

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


list_db_tables
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    
    try:
        api_response = tc.debug_api.list_db_tables()
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->list_db_tables: %s\n" % e)


This endpoint does not need any parameter.

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


new_remember_me
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    
    try:
        api_response = tc.debug_api.new_remember_me()
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->new_remember_me: %s\n" % e)


This endpoint does not need any parameter.

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


save_memory_dump
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        archived = true # bool |  (optional)

    try:
        api_response = tc.debug_api.save_memory_dump(archived=archived)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->save_memory_dump: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **archived**
     - **bool**
     - [optional] 

Return type:
    **str**

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
        api_response = tc.debug_api.schedule_checking_for_changes(locator=locator, requestor=requestor, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->schedule_checking_for_changes: %s\n" % e)



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
    `VcsRootInstances <../models/VcsRootInstances.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_current_session_max_inactive_interval
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = 'body_example' # str |  (optional)

    try:
        api_response = tc.debug_api.set_current_session_max_inactive_interval(body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling DebugApi->set_current_session_max_inactive_interval: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


