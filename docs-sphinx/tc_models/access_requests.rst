###############
Access requests
###############

Users can request access to groups and projects.

When access is granted the user should be given a numerical access level. The
following constants are provided to represent the access levels:

* ``teamcity.GUEST_ACCESS``: ``10``
* ``teamcity.REPORTER_ACCESS``: ``20``
* ``teamcity.DEVELOPER_ACCESS``: ``30``
* ``teamcity.MASTER_ACCESS``: ``40``
* ``teamcity.OWNER_ACCESS``: ``50``

References
----------

* v4 API:

  + :class:`teamcity.v4.objects.ProjectAccessRequest`
  + :class:`teamcity.v4.objects.ProjectAccessRequestManager`
  + :attr:`teamcity.v4.objects.Project.accessrequests`
  + :class:`teamcity.v4.objects.GroupAccessRequest`
  + :class:`teamcity.v4.objects.GroupAccessRequestManager`
  + :attr:`teamcity.v4.objects.Group.accessrequests`

* TeamCity API: https://docs.teamcity.com/ce/api/access_requests.html

Examples
--------

List access requests from projects and groups::

    p_ars = project.accessrequests.list()
    g_ars = group.accessrequests.list()

Create an access request::

    p_ar = project.accessrequests.create({})
    g_ar = group.accessrequests.create({})

Approve an access request::

    ar.approve()  # defaults to DEVELOPER level
    ar.approve(access_level=teamcity.MASTER_ACCESS)  # explicitly set access level

Deny (delete) an access request::

    project.accessrequests.delete(user_id)
    group.accessrequests.delete(user_id)
    # or
    ar.delete()
