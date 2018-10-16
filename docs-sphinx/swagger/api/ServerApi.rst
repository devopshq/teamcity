dohq_teamcity.ServerApi
######################################

`API examples <../../teamcity_apis/ServerApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `add_license_keys`__
     - **POST** ``/app/rest/server/licensingData/licenseKeys``
   * - `delete_license_key`__
     - **DELETE** ``/app/rest/server/licensingData/licenseKeys/{licenseKey}``
   * - `get_backup_status`__
     - **GET** ``/app/rest/server/backup``
   * - `get_children`__
     - **GET** ``/app/rest/server/files/{areaId}/children{path}``
   * - `get_children_alias`__
     - **GET** ``/app/rest/server/files/{areaId}/{path}``
   * - `get_content`__
     - **GET** ``/app/rest/server/files/{areaId}/content{path}``
   * - `get_content_alias`__
     - **GET** ``/app/rest/server/files/{areaId}/files{path}``
   * - `get_license_key`__
     - **GET** ``/app/rest/server/licensingData/licenseKeys/{licenseKey}``
   * - `get_license_keys`__
     - **GET** ``/app/rest/server/licensingData/licenseKeys``
   * - `get_licensing_data`__
     - **GET** ``/app/rest/server/licensingData``
   * - `get_metadata`__
     - **GET** ``/app/rest/server/files/{areaId}/metadata{path}``
   * - `get_root`__
     - **GET** ``/app/rest/server/files/{areaId}``
   * - `get_zipped`__
     - **GET** ``/app/rest/server/files/{areaId}/archived{path}``
   * - `serve_plugins`__
     - **GET** ``/app/rest/server/plugins``
   * - `serve_server_info`__
     - **GET** ``/app/rest/server``
   * - `serve_server_version`__
     - **GET** ``/app/rest/server/{field}``
   * - `start_backup`__
     - **POST** ``/app/rest/server/backup``

add_license_keys
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = 'body_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.add_license_keys(body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->add_license_keys: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `LicenseKeys <../models/LicenseKeys.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_license_key
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        license_key = 'license_key_example' # str | 

    try:
        tc.server_api.delete_license_key(license_key)
    except ApiException as e:
        print("Exception when calling ServerApi->delete_license_key: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **license_key**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_backup_status
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.BackupProcessManager() # BackupProcessManager |  (optional)

    try:
        api_response = tc.server_api.get_backup_status(body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->get_backup_status: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `BackupProcessManager <../models/BackupProcessManager.html>`_
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_children
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    area_id = 'area_id_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.get_children(path, area_id, base_path=base_path, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->get_children: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **area_id**
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
    area_id = 'area_id_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.get_children_alias(path, area_id, base_path=base_path, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->get_children_alias: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **area_id**
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
    area_id = 'area_id_example' # str | 

    try:
        tc.server_api.get_content(path, area_id)
    except ApiException as e:
        print("Exception when calling ServerApi->get_content: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **area_id**
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
    area_id = 'area_id_example' # str | 

    try:
        tc.server_api.get_content_alias(path, area_id)
    except ApiException as e:
        print("Exception when calling ServerApi->get_content_alias: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **area_id**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_license_key
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        license_key = 'license_key_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.get_license_key(license_key, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->get_license_key: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **license_key**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `LicenseKey <../models/LicenseKey.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_license_keys
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.get_license_keys(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->get_license_keys: %s\n" % e)



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
    `LicenseKeys <../models/LicenseKeys.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_licensing_data
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.get_licensing_data(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->get_licensing_data: %s\n" % e)



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
    `LicensingData <../models/LicensingData.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_metadata
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    area_id = 'area_id_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.get_metadata(path, area_id, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->get_metadata: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **area_id**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `file <../models/file.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_root
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        area_id = 'area_id_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.get_root(area_id, base_path=base_path, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->get_root: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **area_id**
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
    `Files <../models/Files.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_zipped
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        path = 'path_example' # str | 
    area_id = 'area_id_example' # str | 
    base_path = 'base_path_example' # str |  (optional)
    locator = 'locator_example' # str |  (optional)
    name = 'name_example' # str |  (optional)

    try:
        tc.server_api.get_zipped(path, area_id, base_path=base_path, locator=locator, name=name)
    except ApiException as e:
        print("Exception when calling ServerApi->get_zipped: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **path**
     - **str**
     - 
   * - **area_id**
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


serve_plugins
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.serve_plugins(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->serve_plugins: %s\n" % e)



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
    `Plugins <../models/Plugins.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_server_info
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.server_api.serve_server_info(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->serve_server_info: %s\n" % e)



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
    `Server <../models/Server.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_server_version
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        field = 'field_example' # str | 

    try:
        api_response = tc.server_api.serve_server_version(field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->serve_server_version: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


start_backup
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        file_name = 'file_name_example' # str |  (optional)
    add_timestamp = true # bool |  (optional)
    include_configs = true # bool |  (optional)
    include_database = true # bool |  (optional)
    include_build_logs = true # bool |  (optional)
    include_personal_changes = true # bool |  (optional)
    include_running_builds = true # bool |  (optional)
    include_supplimentary_data = true # bool |  (optional)
    body = dohq_teamcity.BackupProcessManager() # BackupProcessManager |  (optional)

    try:
        api_response = tc.server_api.start_backup(file_name=file_name, add_timestamp=add_timestamp, include_configs=include_configs, include_database=include_database, include_build_logs=include_build_logs, include_personal_changes=include_personal_changes, include_running_builds=include_running_builds, include_supplimentary_data=include_supplimentary_data, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServerApi->start_backup: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **file_name**
     - **str**
     - [optional] 
   * - **add_timestamp**
     - **bool**
     - [optional] 
   * - **include_configs**
     - **bool**
     - [optional] 
   * - **include_database**
     - **bool**
     - [optional] 
   * - **include_build_logs**
     - **bool**
     - [optional] 
   * - **include_personal_changes**
     - **bool**
     - [optional] 
   * - **include_running_builds**
     - **bool**
     - [optional] 
   * - **include_supplimentary_data**
     - **bool**
     - [optional] 
   * - **body**
     - `BackupProcessManager <../models/BackupProcessManager.html>`_
     - [optional] 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


