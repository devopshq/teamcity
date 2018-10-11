#########
Templates
#########

You can request templates for different type of files:

* License files
* .gitignore files
* GitLab CI configuration files
* Dockerfiles

License templates
=================

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.License`
  + :class:`teamcity.v4.objects.LicenseManager`
  + :attr:`teamcity.Gitlab.licenses`

* GitLab API: https://docs.teamcity.com/ce/api/templates/licenses.html

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
  + :attr:`teamcity.Gitlab.gitignores`

* GitLab API: https://docs.teamcity.com/ce/api/templates/gitignores.html

Examples
--------

List known gitignore templates::

    gitignores = gl.gitignores.list()

Get a gitignore template::

    gitignore = gl.gitignores.get('Python')
    print(gitignore.content)

GitLab CI templates
===================

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.Gitlabciyml`
  + :class:`teamcity.v4.objects.GitlabciymlManager`
  + :attr:`teamcity.Gitlab.teamcityciymls`

* GitLab API: https://docs.teamcity.com/ce/api/templates/teamcity_ci_ymls.html

Examples
--------

List known GitLab CI templates::

    teamcityciymls = gl.teamcityciymls.list()

Get a GitLab CI template::

    teamcityciyml = gl.teamcityciymls.get('Pelican')
    print(teamcityciyml.content)

Dockerfile templates
====================

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.Dockerfile`
  + :class:`teamcity.v4.objects.DockerfileManager`
  + :attr:`teamcity.Gitlab.teamcityciymls`

* GitLab API: Not documented.

Examples
--------

List known Dockerfile templates::

    dockerfiles = gl.dockerfiles.list()

Get a Dockerfile template::

    dockerfile = gl.dockerfiles.get('Python')
    print(dockerfile.content)
