dohq_teamcity.VcsRootApi
######################################

`API examples <../../teamcity_apis/VcsRootApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `add_root`__
     - **POST** ``/app/rest/vcs-roots``
   * - `change_properties`__
     - **PUT** ``/app/rest/vcs-roots/{vcsRootLocator}/properties``
   * - `delete_all_properties`__
     - **DELETE** ``/app/rest/vcs-roots/{vcsRootLocator}/properties``
   * - `delete_parameter`__
     - **DELETE** ``/app/rest/vcs-roots/{vcsRootLocator}/properties/{name}``
   * - `delete_root`__
     - **DELETE** ``/app/rest/vcs-roots/{vcsRootLocator}``
   * - `get_settings_file`__
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/settingsFile``
   * - `put_parameter`__
     - **PUT** ``/app/rest/vcs-roots/{vcsRootLocator}/properties/{name}``
   * - `serve_field`__
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/{field}``
   * - `serve_instance_field`__
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/{field}``
   * - `serve_properties`__
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/properties``
   * - `serve_property`__
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/properties/{name}``
   * - `serve_root`__
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}``
   * - `serve_root_instance`__
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}``
   * - `serve_root_instance_properties`__
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/properties``
   * - `serve_root_instances`__
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/instances``
   * - `serve_roots`__
     - **GET** ``/app/rest/vcs-roots``
   * - `set_field`__
     - **PUT** ``/app/rest/vcs-roots/{vcsRootLocator}/{field}``
   * - `set_instance_field`__
     - **PUT** ``/app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/{field}``

add_root
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.VcsRoot() # VcsRoot |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.add_root(body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->add_root: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - [**VcsRoot**](VcsRoot.md)
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**VcsRoot**](../models/VcsRoot.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


change_properties
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    body = dohq_teamcity.Properties() # Properties |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.change_properties(vcs_root_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->change_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **body**
     - [**Properties**](Properties.md)
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**Properties**](../models/Properties.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_all_properties
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 

    try:
        tc.vcs_root_api.delete_all_properties(vcs_root_locator)
    except ApiException as e:
        print("Exception when calling VcsRootApi->delete_all_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
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

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        tc.vcs_root_api.delete_parameter(vcs_root_locator, name)
    except ApiException as e:
        print("Exception when calling VcsRootApi->delete_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


delete_root
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 

    try:
        tc.vcs_root_api.delete_root(vcs_root_locator)
    except ApiException as e:
        print("Exception when calling VcsRootApi->delete_root: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 

Return type:
    void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


get_settings_file
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 

    try:
        api_response = tc.vcs_root_api.get_settings_file(vcs_root_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->get_settings_file: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


put_parameter
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    name = 'name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.put_parameter(vcs_root_locator, name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->put_parameter: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
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


serve_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.vcs_root_api.serve_field(vcs_root_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->serve_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_instance_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        api_response = tc.vcs_root_api.serve_instance_field(vcs_root_locator, vcs_root_instance_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->serve_instance_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_properties
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.serve_properties(vcs_root_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->serve_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**Properties**](../models/Properties.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_property
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        api_response = tc.vcs_root_api.serve_property(vcs_root_locator, name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->serve_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    **str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_root
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.serve_root(vcs_root_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->serve_root: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**VcsRoot**](../models/VcsRoot.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_root_instance
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.serve_root_instance(vcs_root_locator, vcs_root_instance_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->serve_root_instance: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**VcsRootInstance**](../models/VcsRootInstance.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_root_instance_properties
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.serve_root_instance_properties(vcs_root_locator, vcs_root_instance_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->serve_root_instance_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **vcs_root_instance_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**Properties**](../models/Properties.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_root_instances
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.serve_root_instances(vcs_root_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->serve_root_instances: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    [**VcsRootInstances**](../models/VcsRootInstances.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_roots
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.serve_roots(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->serve_roots: %s\n" % e)



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
    [**VcsRoots**](../models/VcsRoots.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


set_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.set_field(vcs_root_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->set_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
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


set_instance_field
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        vcs_root_locator = 'vcs_root_locator_example' # str | 
    vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = tc.vcs_root_api.set_instance_field(vcs_root_locator, vcs_root_instance_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->set_instance_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
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



OLD
-------

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_root**](VcsRootApi.md#add_root) | **POST** /app/rest/vcs-roots | 
[**change_properties**](VcsRootApi.md#change_properties) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/properties | 
[**delete_all_properties**](VcsRootApi.md#delete_all_properties) | **DELETE** /app/rest/vcs-roots/{vcsRootLocator}/properties | 
[**delete_parameter**](VcsRootApi.md#delete_parameter) | **DELETE** /app/rest/vcs-roots/{vcsRootLocator}/properties/{name} | 
[**delete_root**](VcsRootApi.md#delete_root) | **DELETE** /app/rest/vcs-roots/{vcsRootLocator} | 
[**get_settings_file**](VcsRootApi.md#get_settings_file) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/settingsFile | 
[**put_parameter**](VcsRootApi.md#put_parameter) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/properties/{name} | 
[**serve_field**](VcsRootApi.md#serve_field) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/{field} | 
[**serve_instance_field**](VcsRootApi.md#serve_instance_field) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/{field} | 
[**serve_properties**](VcsRootApi.md#serve_properties) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/properties | 
[**serve_property**](VcsRootApi.md#serve_property) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/properties/{name} | 
[**serve_root**](VcsRootApi.md#serve_root) | **GET** /app/rest/vcs-roots/{vcsRootLocator} | 
[**serve_root_instance**](VcsRootApi.md#serve_root_instance) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator} | 
[**serve_root_instance_properties**](VcsRootApi.md#serve_root_instance_properties) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/properties | 
[**serve_root_instances**](VcsRootApi.md#serve_root_instances) | **GET** /app/rest/vcs-roots/{vcsRootLocator}/instances | 
[**serve_roots**](VcsRootApi.md#serve_roots) | **GET** /app/rest/vcs-roots | 
[**set_field**](VcsRootApi.md#set_field) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/{field} | 
[**set_instance_field**](VcsRootApi.md#set_instance_field) | **PUT** /app/rest/vcs-roots/{vcsRootLocator}/instances/{vcsRootInstanceLocator}/{field} | 


# **add_root**
> VcsRoot add_root(body=body, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

body = dohq_teamcity.VcsRoot() # VcsRoot |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.add_root(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->add_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VcsRoot**](VcsRoot.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRoot**](../models/VcsRoot.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **change_properties**
> Properties change_properties(vcs_root_locator, body=body, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
body = dohq_teamcity.Properties() # Properties |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.change_properties(vcs_root_locator, body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->change_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **body** | [**Properties**](Properties.md)|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](../models/Properties.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_all_properties**
> delete_all_properties(vcs_root_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 

try:
    tc.vcs_root_api.delete_all_properties(vcs_root_locator)
except ApiException as e:
    print("Exception when calling VcsRootApi->delete_all_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_parameter**
> delete_parameter(vcs_root_locator, name)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
name = 'name_example' # str | 

try:
    tc.vcs_root_api.delete_parameter(vcs_root_locator, name)
except ApiException as e:
    print("Exception when calling VcsRootApi->delete_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **delete_root**
> delete_root(vcs_root_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 

try:
    tc.vcs_root_api.delete_root(vcs_root_locator)
except ApiException as e:
    print("Exception when calling VcsRootApi->delete_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_settings_file**
> str get_settings_file(vcs_root_locator)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 

try:
    api_response = tc.vcs_root_api.get_settings_file(vcs_root_locator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->get_settings_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **put_parameter**
> str put_parameter(vcs_root_locator, name, body=body)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
name = 'name_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.put_parameter(vcs_root_locator, name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->put_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **name** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_field**
> str serve_field(vcs_root_locator, field)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = tc.vcs_root_api.serve_field(vcs_root_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_instance_field**
> str serve_instance_field(vcs_root_locator, vcs_root_instance_locator, field)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
field = 'field_example' # str | 

try:
    api_response = tc.vcs_root_api.serve_instance_field(vcs_root_locator, vcs_root_instance_locator, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_instance_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **field** | **str**|  | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_properties**
> Properties serve_properties(vcs_root_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.serve_properties(vcs_root_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](../models/Properties.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_property**
> str serve_property(vcs_root_locator, name)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
name = 'name_example' # str | 

try:
    api_response = tc.vcs_root_api.serve_property(vcs_root_locator, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **name** | **str**|  | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_root**
> VcsRoot serve_root(vcs_root_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.serve_root(vcs_root_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRoot**](../models/VcsRoot.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_root_instance**
> VcsRootInstance serve_root_instance(vcs_root_locator, vcs_root_instance_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.serve_root_instance(vcs_root_locator, vcs_root_instance_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_root_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootInstance**](../models/VcsRootInstance.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_root_instance_properties**
> Properties serve_root_instance_properties(vcs_root_locator, vcs_root_instance_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.serve_root_instance_properties(vcs_root_locator, vcs_root_instance_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_root_instance_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Properties**](../models/Properties.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_root_instances**
> VcsRootInstances serve_root_instances(vcs_root_locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.serve_root_instances(vcs_root_locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_root_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRootInstances**](../models/VcsRootInstances.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **serve_roots**
> VcsRoots serve_roots(locator=locator, fields=fields)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

locator = 'locator_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.serve_roots(locator=locator, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->serve_roots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**VcsRoots**](../models/VcsRoots.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **set_field**
> str set_field(vcs_root_locator, field, body=body)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.set_field(vcs_root_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->set_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **field** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **set_instance_field**
> str set_instance_field(vcs_root_locator, vcs_root_instance_locator, field, body=body)



### Example
```python
from pprint import pprint
from dohq_teamcity import TeamCity, ApiException

# username/password authentication
tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

vcs_root_locator = 'vcs_root_locator_example' # str | 
vcs_root_instance_locator = 'vcs_root_instance_locator_example' # str | 
field = 'field_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_response = tc.vcs_root_api.set_instance_field(vcs_root_locator, vcs_root_instance_locator, field, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VcsRootApi->set_instance_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vcs_root_locator** | **str**|  | 
 **vcs_root_instance_locator** | **str**|  | 
 **field** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


