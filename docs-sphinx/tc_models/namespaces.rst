##########
Namespaces
##########

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.Namespace`
  + :class:`teamcity.v4.objects.NamespaceManager`
  + :attr:`teamcity.TeamCity.namespaces`

* TeamCity API: https://docs.teamcity.com/ce/api/namespaces.html

Examples
--------

List namespaces::

    namespaces = gl.namespaces.list()

Search namespaces::

    namespaces = gl.namespaces.list(search='foo')
