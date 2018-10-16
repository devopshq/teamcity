dohq_teamcity.InvestigationApi
######################################

`API examples <../../teamcity_apis/InvestigationApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `get_investigations`__
     - **GET** ``/app/rest/investigations``
   * - `serve_instance`__
     - **GET** ``/app/rest/investigations/{investigationLocator}``

get_investigations
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.investigation_api.get_investigations(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvestigationApi->get_investigations: %s\n" % e)



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
    `Investigations <../models/Investigations.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_instance
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        investigation_locator = 'investigation_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.investigation_api.serve_instance(investigation_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvestigationApi->serve_instance: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **investigation_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Investigation <../models/Investigation.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


