###########
Deployments
###########

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.ProjectDeployment`
  + :class:`teamcity.v4.objects.ProjectDeploymentManager`
  + :attr:`teamcity.v4.objects.Project.deployments`

* TeamCity API: https://docs.teamcity.com/ce/api/deployments.html

Examples
--------

List deployments for a project::

    deployments = project.deployments.list()

Get a single deployment::

    deployment = project.deployments.get(deployment_id)
