.. _switching_to_v4:

##########################
Switching to GitLab API v4
##########################

GitLab provides a new API version (v4) since its 9.0 release. ``dohq-teamcity``
provides support for this new version, but the python API has been modified to
solve some problems with the existing one.

GitLab will stop supporting the v3 API soon, and you should consider switching
to v4 if you use a recent version of GitLab (>= 9.0), or if you use
https://teamcity.com.


Using the v4 API
================

dohq-teamcity uses the v4 API by default since the 1.3.0 release. To use the
old v3 API, explicitly define ``api_version`` in the ``Gitlab`` constructor:

.. code-block:: python

   gl = teamcity.Gitlab(..., api_version=3)


If you use the configuration file, also explicitly define the version:

.. code-block:: ini

   [my_teamcity]
   ...
   api_version = 3


Changes between v3 and v4 API
=============================

For a list of GitLab (upstream) API changes, see
https://docs.teamcity.com/ce/api/v3_to_v4.html.

The ``dohq-teamcity`` API reflects these changes. But also consider the
following important changes in the python API:

* managers and objects don't inherit from ``GitlabObject`` and ``BaseManager``
  anymore. They inherit from :class:`~teamcity.base.RESTManager` and
  :class:`~teamcity.base.RESTObject`.

* You should only use the managers to perform CRUD operations.

  The following v3 code:

  .. code-block:: python

     gl = teamcity.Gitlab(...)
     p = Project(gl, project_id)

  Should be replaced with:

  .. code-block:: python

     gl = teamcity.Gitlab(...)
     p = gl.projects.get(project_id)

* Listing methods (``manager.list()`` for instance) can now return generators
  (:class:`~teamcity.base.RESTObjectList`). They handle the calls to the API when
  needed to fetch new items.

  By default you will still get lists. To get generators use ``as_list=False``:

  .. code-block:: python

     all_projects_g = gl.projects.list(as_list=False)

* The "nested" managers (for instance ``gl.project_issues`` or
  ``gl.group_members``) are not available anymore. Their goal was to provide a
  direct way to manage nested objects, and to limit the number of needed API
  calls.

  To limit the number of API calls, you can now use ``get()`` methods with the
  ``lazy=True`` parameter. This creates shallow objects that provide usual
  managers.

  The following v3 code:

  .. code-block:: python

     issues = gl.project_issues.list(project_id=project_id)

  Should be replaced with:

  .. code-block:: python

     issues = gl.projects.get(project_id, lazy=True).issues.list()

  This will make only one API call, instead of two if ``lazy`` is not used.

* The following :class:`~teamcity.Gitlab` methods should not be used anymore for
  v4:

  + ``list()``
  + ``get()``
  + ``create()``
  + ``update()``
  + ``delete()``

* If you need to perform HTTP requests to the GitLab server (which you
  shouldn't), you can use the following :class:`~teamcity.Gitlab` methods:

  + :attr:`~teamcity.Gitlab.http_request`
  + :attr:`~teamcity.Gitlab.http_get`
  + :attr:`~teamcity.Gitlab.http_list`
  + :attr:`~teamcity.Gitlab.http_post`
  + :attr:`~teamcity.Gitlab.http_put`
  + :attr:`~teamcity.Gitlab.http_delete`
