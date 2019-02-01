############
Builds
############

Reference
========

  + :class:`dohq_teamcity.custom.models.Builds` (and bases class)
  + Original swagger documentation by class :doc:`/swagger/models/Builds`
  + Some examples you can find in `tests directory <https://github.com/devopshq/teamcity/blob/develop/test>`_

Examples
========
Get builds::

    # Get builds builded on a agent
    agent = "agent name"
    teamcity.builds.get_all_builds("agent:{}".format(agent))

    # Get build older than date 2018-10-01 and time 17:00:30 by build_type_id
    builds = tc.builds.get_all_builds(build_type=build_type_id,
                                  count=10000000,
                                  locator="finishDate:(date:20181001T170030,condition:before)")
    
    # Get SUCCESS builds between today=>today-30days
    after_date = datetime.now() - timedelta(days=days)
    builds = teamcity.builds.get_all_builds(
        locator="agent:{agent},finishDate:(date:{date},condition:after),status:SUCCESS".format(
            agent=agent,
            # dateformat = 20190101T170030
            date=after_date.strftime("%Y%m%dT000000")
        ),
        count=100000,
    )

Run new build::

    # Run new build in specific agent by id:
    agent = dohq_teamcity.Agent(id=agent_id)
    body = dohq_teamcity.Build(build_type_id="BuildTypeID", branch_name="develop", agent=agent)

    new_build = teamcity.build_queues.queue_new_build(body=body, move_to_top=True)
                              


