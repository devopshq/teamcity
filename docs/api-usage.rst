.. include:: <isonum.txt>

############################
Getting started with the API
############################

``dohq_teamcity.TeamCity`` class
================================

To connect to a TeamCity server, create a :class:`dohq_teamcity.TeamCity` object (``dohq`` means `DevOpsHQ <https://devopshq.github.io>`_):

.. code-block:: python

   from dohq_teamcity import TeamCity

   # username/password authentication
   tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))



Managers
========

The ``dohq_teamcity.TeamCity`` class provides managers (APIs) to access the TeamCity resources.
Each manager provides a set of methods to act on the resources. The available
methods depend on the resource type.

Manager (API) have two alias:

  + More readable: ``tc.agents``, ``tc.builds``, ``tc.server``
  + with api: ``tc.agent_api``, ``tc.build_api``, ``tc.server_api``

Examples:

.. code-block:: python

   # list all the projects
   projects = tc.projects.get_projects()
   # OR
   # projects = tc.project_api.get_projects()
   for project in projects:
       print(project)

   # get the group with name = groupname
   group = tc.group.get('name:groupname')
   print(group)
       
   # get the user with name = username
   user = tc.user.get('username:devopshq')
   print(user)

   # create a new user and delete
    from dohq_teamcity import User
    new_user = User(name='New user', username='new_user')
    new_user = tc.users.create_user(body=new_user)
    new_user.delete()

    # other way - create object, connect with exist instance and load it
    import dohq_teamcity
    bt = dohq_teamcity.BuildType(id='MyBuildTypeId', teamcity=tc)
    bt = bt.read()


The attributes of objects are defined upon object creation, and depend on the
TeamCity API itself. To list the available information associated with an object
use the ``attributes`` attribute:

.. code-block:: python

   project = tc.projects.get(1)
   print(project.attribute_map.keys())

Managers functions
-----------------
Many Managers function have parameters:

.. list-table::
   :widths: 15 15 70
   :header-rows: 1

   * - Functions
     - Parameters
     - Description
   * - ``get_*`` and ``serve_*``
     - ``some_locator``
     - Positional or named argument, can be string or one of ``dohq_teamcity.TeamCityObject``.

       Read more about locator in `TeamCity Documantation <https://confluence.jetbrains.com/display/TCD10/REST+API#RESTAPI-Locator>`_
   * - ``set_*``, ``add_**`` or ``create_*``
     - ``body``
     - **named** argument, must be one of ``dohq_teamcity.TeamCityObject`` object
   * - All functions
     - ``async_req=True|False``
     - For asynchronous requests. Read more in `Asynchronous requests`__

TeamCity Objects
==============

You can delete a remote object when it exists locally:

.. code-block:: python

   # delete the resource
   project = tc.projects.get('id:MyProject')
   project.delete()

Some classes provide additional methods, allowing more actions on the TeamCity
resources. For example:

.. code-block:: python

   # Add property to build type
   from dohq_teamcit import Type, ModeProperty
   bt1 = tc.build_types.get('id:MyBuildType')
   tp = Type(raw_value="text display='normal' validationMode='any'")
   pr = ModelProperty(name="from_script", value="testnew", type=tp)
   pr = bt.set_parameter(body=pr)

Read function
-------------
If some objects contains other object (eg - ``Project`` contain ``BuildType``) we need execute ``read()`` function to get **full** object, because it does not contain full information about related object and we must reload object.

.. code-block:: python

   # list the build_type properties for a project
   project = tc.projects.get('id:MyProject')
   bt = project.build_types[0]
   bt.parameters # None
   bt = bt.read()
   bt.parameters # Properties object like list[Property]

   # get agents for pool which used in build
   build = tc.builds.get('id:123456') # Make 1 API call
   agents = build.read().agent.read().pool.read().agents # Make 3 API calls
   print([x.name for agents])

We try to user auto-read when we get property and if ``self._property_name is None``,
but this way have problem in debug-mode (PyCharm Debug Configuration)
- it makes endless recursive API calls for viewing object in debugger.

We also try detect "Debug-mode", and don't make call, but but then the behavior in Debug-mode is different
from Production-mode. And for now, we have ``read`` function which
must be called before accessing the nested object if we want to get the full object :)

    Explicit is better than implicit |copy| PEP 20


Lazy objects
------------

All objects are a ``lazy``-object - it's not make API call on create, only on `get read update` operations. You can create object directly and not make API call.

The following example will only make one API call to the TeamCity server to set parameter in a project:

.. code-block:: python

   # project
   project = tc.projects.get('id:MyProject')  # API call, full object
   project.set_parameter(body=parameter_obj)  # API call

   # project lazy
   from dohq_teamcity import Project
   project = Project(id='MyProject', teamcity=tc) # no API call
   project.set_parameter(body=parameter_obj)  # API call

   # project lazy 2
   from dohq_teamcity import Project
   project = Project(id='MyProject') # no API call
   tc.projects.set_parameter(project, body=parameter_obj)  # API call

List objects
------------
Some ``TeamCityObject`` are essentially containers and their purpose is only to store other objects.

For example, when searching, we get a list, we can see how its attributes, and make a cycle on objects:

.. code-block:: python

    builds = tc.builds.get_all_builds(count=100)
    print(builds.count)
    ids_ = [x.id for x in builds.build]
    ids = [x.id for x in builds]
    print(ids)
    print(ids_)
    print(ids == ids_)

    # If you need work with some build - don't forget use read() function
    agent_0 = builds[0].read().agent



Base types
==========

The ``dohq_teamcity`` package provides some base types.

* ``dohq_teamcity.TeamCity`` is the primary class, handling the HTTP requests. It holds
  the TeamCity URL and authentication information.
* ``dohq_teamcity.custom.base_model`` is the base class for all the TeamCity objects.
  These objects provide an abstraction for TeamCity resources (projects, groups,
  and so on).
* ``dohq_teamcity.custom.models`` is the extended class for  objects managers,
  providing the API to manipulate the resources and their attributes.
* ``dohq_teamcity.custom.api`` is the extended class for  objects, providing the friendly API to manipulate the resources.
* ``dohq_teamcity.models.*`` autogenerated Models object by swagger.
* ``dohq_teamcity.api.*`` autogenerated objects Managers and APIs by swagger.

.. note::

    Most objects and managers and their functions genereted automatically by https://github.com/swagger-api/swagger-codegen - see more ``swagger.sh`` file and other swagger files.
    Custom interfaces for apis and objects are in folder **dohq_teamcity/custom**

    For more information, please see the section on :doc:`development`.



Advanced HTTP configuration
===========================

``dohq-teamcity`` relies on ``urllib3`` objects to perform all the
HTTP requests to the TeamCity servers.


Asynchronous requests
---------------------
All method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please pass ``async_req=True``.

.. code-block:: python

    thread = tc.builds.get(bt_locator, async_req=True)
    # If the method is called asynchronously, returns the request thread.
    result = thread.get()

.. code-block:: python

   # get all archived projects build types ids
    prs = tc.projects.get_projects(locator='archived:true') #
    hr = [x.read(async_req=True) for x in prs.project[]] # async request
    rs = [x.get() for x in thr]
    bt_ids = list()
    for pr in prs:
        bt_pr = [x.id for x in pr.build_types.build_type]
        bt_ids.extend(bt_pr)
    print('\n'.join(bt_pr))


Debug and troubleshooting
--------------------------
You can use logging for debug query

.. code-block:: python

    logging.getLogger("urllib3").setLevel(logging.DEBUG)
    logging.getLogger("dohq_teamcity").setLevel(logging.DEBUG)
