############
Agent
############

Reference
========

  + :class:`dohq_teamcity.custom.models.Agent` (and bases class)
  + Related main API examples (if exist): :doc:`/examples/api/AgentApi`
  + Original swagger documentation by class :doc:`/swagger/models/Agent`
  + Some examples you can find in `tests directory <https://github.com/devopshq/teamcity/blob/develop/test>`_

Examples
========
Some action::

    # Get pool by agent name
    agent = "linux-ci-01.example.com"
    pool = teamcity.agents.get("name:{}".format(agent)).pool.name



