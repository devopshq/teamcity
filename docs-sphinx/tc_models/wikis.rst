##########
Wiki pages
##########


References
==========

* v4 API:

  + :class:`teamcity.v4.objects.ProjectWiki`
  + :class:`teamcity.v4.objects.ProjectWikiManager`
  + :attr:`teamcity.v4.objects.Project.wikis`

* GitLab API: https://docs.teamcity.com/ce/api/wikis.html

Examples
--------

Get the list of wiki pages for a project::

    pages = project.wikis.list()

Get a single wiki page::

    page = project.wikis.get(page_slug)

Create a wiki page::

    page = project.wikis.create({'title': 'Wiki Page 1',
                                 'content': open(a_file).read()})

Update a wiki page::

    page.content = 'My new content'
    page.save()

Delete a wiki page::

    page.delete()
