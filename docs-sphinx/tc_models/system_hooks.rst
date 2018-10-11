############
System hooks
############

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.Hook`
  + :class:`teamcity.v4.objects.HookManager`
  + :attr:`teamcity.Gitlab.hooks`

* GitLab API: https://docs.teamcity.com/ce/api/system_hooks.html

Examples
--------

List the system hooks::

    hooks = gl.hooks.list()

Create a system hook::

    gl.hooks.get(hook_id)

Test a system hook. The returned object is not usable (it misses the hook ID)::

    hook = gl.hooks.create({'url': 'http://your.target.url'})

Delete a system hook::

    gl.hooks.delete(hook_id)
    # or
    hook.delete()
