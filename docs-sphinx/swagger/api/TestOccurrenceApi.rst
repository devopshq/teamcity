dohq_teamcity.TestOccurrenceApi
######################################

`API examples <../../teamcity_apis/TestOccurrenceApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `get_test_occurrences`__
     - **GET** ``/app/rest/testOccurrences``
   * - `serve_instance`__
     - **GET** ``/app/rest/testOccurrences/{testLocator}``

get_test_occurrences
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.test_occurrence_api.get_test_occurrences(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestOccurrenceApi->get_test_occurrences: %s\n" % e)



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
    `TestOccurrences <../models/TestOccurrences.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_instance
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        test_locator = 'test_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.test_occurrence_api.serve_instance(test_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestOccurrenceApi->serve_instance: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **test_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `TestOccurrence <../models/TestOccurrence.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


