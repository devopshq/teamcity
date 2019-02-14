############
Installation
############

``dohq-teamcity`` is compatible with Python 2.7 and 3.4+ (``dohq`` means `DevOpsHQ <https://devopshq.github.io>`_).

Use :command:`pip` to install the latest stable version of ``dohq-teamcity``:

.. code-block:: console

   pip install --upgrade dohq-teamcity

The current development version is available on `github
<https://github.com/devopshq/teamcity>`__. Use :command:`git` and
:command:`python setup.py` to install it:

.. code-block:: console

   git clone https://github.com/devopshq/teamcity
   cd teamcity
   python setup.py install

Try connect to your TeamCity instance

.. code-block:: python

    from dohq_teamcity import TeamCity
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))
    print(tc.server.get_server_info().version)

