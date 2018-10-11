######
Events
######

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.Event`
  + :class:`teamcity.v4.objects.EventManager`
  + :attr:`teamcity.TeamCity.events`
  + :class:`teamcity.v4.objects.ProjectEvent`
  + :class:`teamcity.v4.objects.ProjectEventManager`
  + :attr:`teamcity.v4.objects.Project.events`
  + :class:`teamcity.v4.objects.UserEvent`
  + :class:`teamcity.v4.objects.UserEventManager`
  + :attr:`teamcity.v4.objects.User.events`

* TeamCity API: https://docs.teamcity.com/ce/api/events.html

Examples
--------

You can list events for an entire TeamCity instance (admin), users and projects.
You can filter you events you want to retrieve using the ``action`` and
``target_type`` attributes. The possible values for these attributes are
available on `the teamcity documentation
<https://docs.teamcity.com/ce/api/events.html>`_.

List all the events (paginated)::

    events = gl.events.list()

List the issue events on a project::

    events = project.events.list(target_type='issue')

List the user events::

    events = project.events.list()
