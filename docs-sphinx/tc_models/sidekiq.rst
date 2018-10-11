###############
Sidekiq metrics
###############

Reference
---------

* v4 API:

  + :class:`teamcity.v4.objects.SidekiqManager`
  + :attr:`teamcity.TeamCity.sidekiq`

* TeamCity API: https://docs.teamcity.com/ce/api/sidekiq_metrics.html

Examples
--------

.. code-block:: python

   gl.sidekiq.queue_metrics()
   gl.sidekiq.process_metrics()
   gl.sidekiq.job_stats()
   gl.sidekiq.compound_metrics()
