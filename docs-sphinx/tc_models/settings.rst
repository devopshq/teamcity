########
Settings
########

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.ApplicationSettings`
  + :class:`teamcity.v4.objects.ApplicationSettingsManager`
  + :attr:`teamcity.TeamCity.settings`

* TeamCity API: https://docs.teamcity.com/ce/api/settings.html

Examples
--------

Get the settings::

    settings = gl.settings.get()

Update the settings::

    settings.signin_enabled = False
    settings.save()
