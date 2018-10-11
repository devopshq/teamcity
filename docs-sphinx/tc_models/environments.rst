############
Environments
############

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.ProjectEnvironment`
  + :class:`teamcity.v4.objects.ProjectEnvironmentManager`
  + :attr:`teamcity.v4.objects.Project.environments`

* GitLab API: https://docs.teamcity.com/ce/api/environments.html

Examples
--------

List environments for a project::

    environments = project.environments.list()

Create an environment for a project::

    environment = project.environments.create({'name': 'production'})

Update an environment for a project::

    environment.external_url = 'http://foo.bar.com'
    environment.save()

Delete an environment for a project::

    environment = project.environments.delete(environment_id)
    # or
    environment.delete()

Stop an environments::

    environment.stop()
