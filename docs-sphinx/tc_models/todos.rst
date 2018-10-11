#####
Todos
#####

Reference
---------

* v4 API:

  + :class:`~teamcity.objects.Todo`
  + :class:`~teamcity.objects.TodoManager`
  + :attr:`teamcity.TeamCity.todos`

* TeamCity API: https://docs.teamcity.com/ce/api/todos.html

Examples
--------

List active todos::

    todos = gl.todos.list()

You can filter the list using the following parameters:

* ``action``: can be ``assigned``, ``mentioned``, ``build_failed``, ``marked``,
  or ``approval_required``
* ``author_id``
* ``project_id``
* ``state``: can be ``pending`` or ``done``
* ``type``: can be ``Issue`` or ``MergeRequest``

For example::

    todos = gl.todos.list(project_id=1)
    todos = gl.todos.list(state='done', type='Issue')

Mark a todo as done::

    gl.todos.delete(todo_id)
    # or
    todo.delete()

Mark all the todos as done::

    nb_of_closed_todos = gl.todos.delete_all()
