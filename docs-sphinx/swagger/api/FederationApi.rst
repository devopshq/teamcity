dohq_teamcity.FederationApi
######################################

`API examples <../../teamcity_apis/FederationApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `add_server`__
     - **PUT** ``/app/rest/federation/servers``
   * - `servers`__
     - **GET** ``/app/rest/federation/servers``

add_server
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        body = dohq_teamcity.Servers() # Servers |  (optional)

    try:
        api_response = tc.federation_api.add_server(body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling FederationApi->add_server: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `Servers <../models/Servers.html>`_
     - [optional] 

Return type:
    `Servers <../models/Servers.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


servers
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.federation_api.servers(fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling FederationApi->servers: %s\n" % e)



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
    `Servers <../models/Servers.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


