#########
Templates
#########

You can request templates for different type of files:

* License files
* .gitignore files
* TeamCity CI configuration files
* Dockerfiles

License templates
=================

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.License`
  + :class:`teamcity.v4.objects.LicenseManager`
  + :attr:`teamcity.TeamCity.licenses`

* TeamCity API: https://docs.teamcity.com/ce/api/templates/licenses.html

Examples
--------

List known license templates::

    licenses = gl.licenses.list()

Generate a license content for a project::

    license = gl.licenses.get('apache-2.0', project='foobar', fullname='John Doe')
    print(license.content)

.gitignore templates
====================

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.Gitignore`
  + :class:`teamcity.v4.objects.GitignoreManager`
  + :attr:`teamcity.TeamCity.gitignores`

* TeamCity API: https://docs.teamcity.com/ce/api/templates/gitignores.html

Examples
--------

List known gitignore templates::

    gitignores = gl.gitignores.list()

Get a gitignore template::

    gitignore = gl.gitignores.get('Python')
    print(gitignore.content)

TeamCity CI templates
===================

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.TeamCityciyml`
  + :class:`teamcity.v4.objects.TeamCityciymlManager`
  + :attr:`teamcity.TeamCity.teamcityciymls`

* TeamCity API: https://docs.teamcity.com/ce/api/templates/teamcity_ci_ymls.html

Examples
--------

List known TeamCity CI templates::

    teamcityciymls = gl.teamcityciymls.list()

Get a TeamCity CI template::

    teamcityciyml = gl.teamcityciymls.get('Pelican')
    print(teamcityciyml.content)

Dockerfile templates
====================

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.Dockerfile`
  + :class:`teamcity.v4.objects.DockerfileManager`
  + :attr:`teamcity.TeamCity.teamcityciymls`

* TeamCity API: Not documented.

Examples
--------

List known Dockerfile templates::

    dockerfiles = gl.dockerfiles.list()

Get a Dockerfile template::

    dockerfile = gl.dockerfiles.get('Python')
    print(dockerfile.content)
