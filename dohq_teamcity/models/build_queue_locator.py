# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class BuildQueueLocator(TeamCityObject):
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
        'agent': 'str',
        'build_type': 'str',
        'count': 'int',
        'id': 'str',
        'item': 'str',
        'personal': 'bool',
        'pool': 'str',
        'project': 'str',
        'start': 'int',
        'task_id': 'str',
        'user': 'str'
    }

    attribute_map = {
        'agent': 'agent',
        'build_type': 'buildType',
        'count': 'count',
        'id': 'id',
        'item': 'item',
        'personal': 'personal',
        'pool': 'pool',
        'project': 'project',
        'start': 'start',
        'task_id': 'taskId',
        'user': 'user'
    }

    def __init__(self, agent=None, build_type=None, count=None, id=None, item=None, personal=None, pool=None, project=None, start=None, task_id=None, user=None, teamcity=None):  # noqa: E501
        """BuildQueueLocator - a model defined in Swagger"""  # noqa: E501

        self._agent = None
        self._build_type = None
        self._count = None
        self._id = None
        self._item = None
        self._personal = None
        self._pool = None
        self._project = None
        self._start = None
        self._task_id = None
        self._user = None
        self.discriminator = None

        if agent is not None:
            self.agent = agent
        if build_type is not None:
            self.build_type = build_type
        if count is not None:
            self.count = count
        if id is not None:
            self.id = id
        if item is not None:
            self.item = item
        if personal is not None:
            self.personal = personal
        if pool is not None:
            self.pool = pool
        if project is not None:
            self.project = project
        if start is not None:
            self.start = start
        if task_id is not None:
            self.task_id = task_id
        if user is not None:
            self.user = user
        super(BuildQueueLocator, self).__init__(teamcity=teamcity)

    @property
    def agent(self):
        """Gets the agent of this BuildQueueLocator.  # noqa: E501

        Agent locator.  # noqa: E501

        :return: The agent of this BuildQueueLocator.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this BuildQueueLocator.

        Agent locator.  # noqa: E501

        :param agent: The agent of this BuildQueueLocator.  # noqa: E501
        :type: str
        """

        self._agent = agent

    @property
    def build_type(self):
        """Gets the build_type of this BuildQueueLocator.  # noqa: E501

        Build type locator.  # noqa: E501

        :return: The build_type of this BuildQueueLocator.  # noqa: E501
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        """Sets the build_type of this BuildQueueLocator.

        Build type locator.  # noqa: E501

        :param build_type: The build_type of this BuildQueueLocator.  # noqa: E501
        :type: str
        """

        self._build_type = build_type

    @property
    def count(self):
        """Gets the count of this BuildQueueLocator.  # noqa: E501

        For paginated calls, how many entities to return per page.  # noqa: E501

        :return: The count of this BuildQueueLocator.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BuildQueueLocator.

        For paginated calls, how many entities to return per page.  # noqa: E501

        :param count: The count of this BuildQueueLocator.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def id(self):
        """Gets the id of this BuildQueueLocator.  # noqa: E501

        Entity ID.  # noqa: E501

        :return: The id of this BuildQueueLocator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BuildQueueLocator.

        Entity ID.  # noqa: E501

        :param id: The id of this BuildQueueLocator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def item(self):
        """Gets the item of this BuildQueueLocator.  # noqa: E501

        Supply multiple locators and return a union of the results.  # noqa: E501

        :return: The item of this BuildQueueLocator.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this BuildQueueLocator.

        Supply multiple locators and return a union of the results.  # noqa: E501

        :param item: The item of this BuildQueueLocator.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def personal(self):
        """Gets the personal of this BuildQueueLocator.  # noqa: E501

        Is personal.  # noqa: E501

        :return: The personal of this BuildQueueLocator.  # noqa: E501
        :rtype: bool
        """
        return self._personal

    @personal.setter
    def personal(self, personal):
        """Sets the personal of this BuildQueueLocator.

        Is personal.  # noqa: E501

        :param personal: The personal of this BuildQueueLocator.  # noqa: E501
        :type: bool
        """

        self._personal = personal

    @property
    def pool(self):
        """Gets the pool of this BuildQueueLocator.  # noqa: E501

        Agent pool locator.  # noqa: E501

        :return: The pool of this BuildQueueLocator.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this BuildQueueLocator.

        Agent pool locator.  # noqa: E501

        :param pool: The pool of this BuildQueueLocator.  # noqa: E501
        :type: str
        """

        self._pool = pool

    @property
    def project(self):
        """Gets the project of this BuildQueueLocator.  # noqa: E501

        Project locator.  # noqa: E501

        :return: The project of this BuildQueueLocator.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this BuildQueueLocator.

        Project locator.  # noqa: E501

        :param project: The project of this BuildQueueLocator.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def start(self):
        """Gets the start of this BuildQueueLocator.  # noqa: E501

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :return: The start of this BuildQueueLocator.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this BuildQueueLocator.

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :param start: The start of this BuildQueueLocator.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def task_id(self):
        """Gets the task_id of this BuildQueueLocator.  # noqa: E501

        Deprecated.  # noqa: E501

        :return: The task_id of this BuildQueueLocator.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this BuildQueueLocator.

        Deprecated.  # noqa: E501

        :param task_id: The task_id of this BuildQueueLocator.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def user(self):
        """Gets the user of this BuildQueueLocator.  # noqa: E501

        User locator.  # noqa: E501

        :return: The user of this BuildQueueLocator.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BuildQueueLocator.

        User locator.  # noqa: E501

        :param user: The user of this BuildQueueLocator.  # noqa: E501
        :type: str
        """

        self._user = user
