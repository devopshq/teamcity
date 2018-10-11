#########
Geo nodes
#########

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.GeoNode`
  + :class:`teamcity.v4.objects.GeoNodeManager`
  + :attr:`teamcity.TeamCity.geonodes`

* TeamCity API: https://docs.teamcity.com/ee/api/geo_nodes.html (EE feature)

Examples
--------

List the geo nodes::

    nodes = gl.geonodes.list()

Get the status of all the nodes::

    status = gl.geonodes.status()

Get a specific node and its status::

    node = gl.geonodes.get(node_id)
    node.status()

Edit a node configuration::

    node.url = 'https://secondary.myteamcity.domain'
    node.save()

Delete a node::

    node.delete()

List the sync failure on the current node::

    failures = gl.geonodes.current_failures()
