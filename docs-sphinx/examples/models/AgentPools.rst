############
AgentPools
############

Reference
========

  + :class:`dohq_teamcity.custom.models.AgentPools` (and bases class)
  + Original swagger documentation by class :doc:`/swagger/models/AgentPools`
  + Some examples you can find in `tests directory <https://github.com/devopshq/teamcity/blob/develop/test>`_

Examples
========
Some action::

    # Get enabled agents in the pool by name
    pool = "My Build Pool"
    _pool = teamcity.agent_pools.get("name:{}".format(pool))
    agents = [agent.read() for agent in _pool.agents]
    agents = [agent.name for agent in agents if agent.enabled]
    print(agents)


