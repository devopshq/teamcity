dohq_teamcity.ProblemOccurrenceApi
######################################

`API examples <../../teamcity_apis/ProblemOccurrenceApi.html>`_

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - `get_problems`__
     - **GET** ``/app/rest/problemOccurrences``
   * - `serve_instance`__
     - **GET** ``/app/rest/problemOccurrences/{problemLocator}``

get_problems
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.problem_occurrence_api.get_problems(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProblemOccurrenceApi->get_problems: %s\n" % e)



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
    `ProblemOccurrences <../models/ProblemOccurrences.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


serve_instance
-----------------
.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

        problem_locator = 'problem_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        api_response = tc.problem_occurrence_api.serve_instance(problem_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProblemOccurrenceApi->serve_instance: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **problem_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `ProblemOccurrence <../models/ProblemOccurrence.html>`_)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


