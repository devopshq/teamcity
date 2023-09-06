# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class AgentLocator(TeamCityObject):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'authorized': 'bool',
        'build': 'str',
        'compatible': 'str',
        'connected': 'bool',
        'count': 'int',
        'enabled': 'bool',
        'id': 'str',
        'ip': 'str',
        'item': 'str',
        'name': 'str',
        'parameter': 'str',
        'pool': 'str',
        'start': 'int'
    }

    attribute_map = {
        'authorized': 'authorized',
        'build': 'build',
        'compatible': 'compatible',
        'connected': 'connected',
        'count': 'count',
        'enabled': 'enabled',
        'id': 'id',
        'ip': 'ip',
        'item': 'item',
        'name': 'name',
        'parameter': 'parameter',
        'pool': 'pool',
        'start': 'start'
    }

    def __init__(self, authorized=None, build=None, compatible=None, connected=None, count=None, enabled=None, id=None, ip=None, item=None, name=None, parameter=None, pool=None, start=None, teamcity=None):  # noqa: E501
        """AgentLocator - a model defined in Swagger"""  # noqa: E501

        self._authorized = None
        self._build = None
        self._compatible = None
        self._connected = None
        self._count = None
        self._enabled = None
        self._id = None
        self._ip = None
        self._item = None
        self._name = None
        self._parameter = None
        self._pool = None
        self._start = None
        self.discriminator = None

        if authorized is not None:
            self.authorized = authorized
        if build is not None:
            self.build = build
        if compatible is not None:
            self.compatible = compatible
        if connected is not None:
            self.connected = connected
        if count is not None:
            self.count = count
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if item is not None:
            self.item = item
        if name is not None:
            self.name = name
        if parameter is not None:
            self.parameter = parameter
        if pool is not None:
            self.pool = pool
        if start is not None:
            self.start = start
        super(AgentLocator, self).__init__(teamcity=teamcity)

    @property
    def authorized(self):
        """Gets the authorized of this AgentLocator.  # noqa: E501

        Is the agent authorized.  # noqa: E501

        :return: The authorized of this AgentLocator.  # noqa: E501
        :rtype: bool
        """
        return self._authorized

    @authorized.setter
    def authorized(self, authorized):
        """Sets the authorized of this AgentLocator.

        Is the agent authorized.  # noqa: E501

        :param authorized: The authorized of this AgentLocator.  # noqa: E501
        :type: bool
        """

        self._authorized = authorized

    @property
    def build(self):
        """Gets the build of this AgentLocator.  # noqa: E501

        Build locator.  # noqa: E501

        :return: The build of this AgentLocator.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this AgentLocator.

        Build locator.  # noqa: E501

        :param build: The build of this AgentLocator.  # noqa: E501
        :type: str
        """

        self._build = build

    @property
    def compatible(self):
        """Gets the compatible of this AgentLocator.  # noqa: E501

        Compatible build types locator.  # noqa: E501

        :return: The compatible of this AgentLocator.  # noqa: E501
        :rtype: str
        """
        return self._compatible

    @compatible.setter
    def compatible(self, compatible):
        """Sets the compatible of this AgentLocator.

        Compatible build types locator.  # noqa: E501

        :param compatible: The compatible of this AgentLocator.  # noqa: E501
        :type: str
        """

        self._compatible = compatible

    @property
    def connected(self):
        """Gets the connected of this AgentLocator.  # noqa: E501

        Is the agent connected.  # noqa: E501

        :return: The connected of this AgentLocator.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this AgentLocator.

        Is the agent connected.  # noqa: E501

        :param connected: The connected of this AgentLocator.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def count(self):
        """Gets the count of this AgentLocator.  # noqa: E501

        For paginated calls, how many entities to return per page.  # noqa: E501

        :return: The count of this AgentLocator.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AgentLocator.

        For paginated calls, how many entities to return per page.  # noqa: E501

        :param count: The count of this AgentLocator.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def enabled(self):
        """Gets the enabled of this AgentLocator.  # noqa: E501

        Is the agent enabled.  # noqa: E501

        :return: The enabled of this AgentLocator.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AgentLocator.

        Is the agent enabled.  # noqa: E501

        :param enabled: The enabled of this AgentLocator.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this AgentLocator.  # noqa: E501

        Entity ID.  # noqa: E501

        :return: The id of this AgentLocator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgentLocator.

        Entity ID.  # noqa: E501

        :param id: The id of this AgentLocator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this AgentLocator.  # noqa: E501


        :return: The ip of this AgentLocator.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this AgentLocator.


        :param ip: The ip of this AgentLocator.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def item(self):
        """Gets the item of this AgentLocator.  # noqa: E501

        Supply multiple locators and return a union of the results.  # noqa: E501

        :return: The item of this AgentLocator.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this AgentLocator.

        Supply multiple locators and return a union of the results.  # noqa: E501

        :param item: The item of this AgentLocator.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def name(self):
        """Gets the name of this AgentLocator.  # noqa: E501


        :return: The name of this AgentLocator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgentLocator.


        :param name: The name of this AgentLocator.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parameter(self):
        """Gets the parameter of this AgentLocator.  # noqa: E501


        :return: The parameter of this AgentLocator.  # noqa: E501
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this AgentLocator.


        :param parameter: The parameter of this AgentLocator.  # noqa: E501
        :type: str
        """

        self._parameter = parameter

    @property
    def pool(self):
        """Gets the pool of this AgentLocator.  # noqa: E501

        Agent pool locator.  # noqa: E501

        :return: The pool of this AgentLocator.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this AgentLocator.

        Agent pool locator.  # noqa: E501

        :param pool: The pool of this AgentLocator.  # noqa: E501
        :type: str
        """

        self._pool = pool

    @property
    def start(self):
        """Gets the start of this AgentLocator.  # noqa: E501

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :return: The start of this AgentLocator.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this AgentLocator.

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :param start: The start of this AgentLocator.  # noqa: E501
        :type: int
        """

        self._start = start
