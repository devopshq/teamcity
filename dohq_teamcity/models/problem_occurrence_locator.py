# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class ProblemOccurrenceLocator(TeamCityObject):
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
        'affected_project': 'str',
        'build': 'str',
        'count': 'int',
        'currently_failing': 'bool',
        'currently_investigated': 'bool',
        'currently_muted': 'bool',
        'identity': 'str',
        'item': 'str',
        'lookup_limit': 'int',
        'muted': 'bool',
        'problem': 'str',
        'start': 'int',
        'type': 'str'
    }

    attribute_map = {
        'affected_project': 'affectedProject',
        'build': 'build',
        'count': 'count',
        'currently_failing': 'currentlyFailing',
        'currently_investigated': 'currentlyInvestigated',
        'currently_muted': 'currentlyMuted',
        'identity': 'identity',
        'item': 'item',
        'lookup_limit': 'lookupLimit',
        'muted': 'muted',
        'problem': 'problem',
        'start': 'start',
        'type': 'type'
    }

    def __init__(self, affected_project=None, build=None, count=None, currently_failing=None, currently_investigated=None, currently_muted=None, identity=None, item=None, lookup_limit=None, muted=None, problem=None, start=None, type=None, teamcity=None):  # noqa: E501
        """ProblemOccurrenceLocator - a model defined in Swagger"""  # noqa: E501

        self._affected_project = None
        self._build = None
        self._count = None
        self._currently_failing = None
        self._currently_investigated = None
        self._currently_muted = None
        self._identity = None
        self._item = None
        self._lookup_limit = None
        self._muted = None
        self._problem = None
        self._start = None
        self._type = None
        self.discriminator = None

        if affected_project is not None:
            self.affected_project = affected_project
        if build is not None:
            self.build = build
        if count is not None:
            self.count = count
        if currently_failing is not None:
            self.currently_failing = currently_failing
        if currently_investigated is not None:
            self.currently_investigated = currently_investigated
        if currently_muted is not None:
            self.currently_muted = currently_muted
        if identity is not None:
            self.identity = identity
        if item is not None:
            self.item = item
        if lookup_limit is not None:
            self.lookup_limit = lookup_limit
        if muted is not None:
            self.muted = muted
        if problem is not None:
            self.problem = problem
        if start is not None:
            self.start = start
        if type is not None:
            self.type = type
        super(ProblemOccurrenceLocator, self).__init__(teamcity=teamcity)

    @property
    def affected_project(self):
        """Gets the affected_project of this ProblemOccurrenceLocator.  # noqa: E501

        Project (direct or indirect parent) locator.  # noqa: E501

        :return: The affected_project of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: str
        """
        return self._affected_project

    @affected_project.setter
    def affected_project(self, affected_project):
        """Sets the affected_project of this ProblemOccurrenceLocator.

        Project (direct or indirect parent) locator.  # noqa: E501

        :param affected_project: The affected_project of this ProblemOccurrenceLocator.  # noqa: E501
        :type: str
        """

        self._affected_project = affected_project

    @property
    def build(self):
        """Gets the build of this ProblemOccurrenceLocator.  # noqa: E501

        Build locator.  # noqa: E501

        :return: The build of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ProblemOccurrenceLocator.

        Build locator.  # noqa: E501

        :param build: The build of this ProblemOccurrenceLocator.  # noqa: E501
        :type: str
        """

        self._build = build

    @property
    def count(self):
        """Gets the count of this ProblemOccurrenceLocator.  # noqa: E501

        For paginated calls, how many entities to return per page.  # noqa: E501

        :return: The count of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ProblemOccurrenceLocator.

        For paginated calls, how many entities to return per page.  # noqa: E501

        :param count: The count of this ProblemOccurrenceLocator.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def currently_failing(self):
        """Gets the currently_failing of this ProblemOccurrenceLocator.  # noqa: E501

        Is currently failing.  # noqa: E501

        :return: The currently_failing of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: bool
        """
        return self._currently_failing

    @currently_failing.setter
    def currently_failing(self, currently_failing):
        """Sets the currently_failing of this ProblemOccurrenceLocator.

        Is currently failing.  # noqa: E501

        :param currently_failing: The currently_failing of this ProblemOccurrenceLocator.  # noqa: E501
        :type: bool
        """

        self._currently_failing = currently_failing

    @property
    def currently_investigated(self):
        """Gets the currently_investigated of this ProblemOccurrenceLocator.  # noqa: E501

        Is currently investigated.  # noqa: E501

        :return: The currently_investigated of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: bool
        """
        return self._currently_investigated

    @currently_investigated.setter
    def currently_investigated(self, currently_investigated):
        """Sets the currently_investigated of this ProblemOccurrenceLocator.

        Is currently investigated.  # noqa: E501

        :param currently_investigated: The currently_investigated of this ProblemOccurrenceLocator.  # noqa: E501
        :type: bool
        """

        self._currently_investigated = currently_investigated

    @property
    def currently_muted(self):
        """Gets the currently_muted of this ProblemOccurrenceLocator.  # noqa: E501

        Is currently muted.  # noqa: E501

        :return: The currently_muted of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: bool
        """
        return self._currently_muted

    @currently_muted.setter
    def currently_muted(self, currently_muted):
        """Sets the currently_muted of this ProblemOccurrenceLocator.

        Is currently muted.  # noqa: E501

        :param currently_muted: The currently_muted of this ProblemOccurrenceLocator.  # noqa: E501
        :type: bool
        """

        self._currently_muted = currently_muted

    @property
    def identity(self):
        """Gets the identity of this ProblemOccurrenceLocator.  # noqa: E501


        :return: The identity of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this ProblemOccurrenceLocator.


        :param identity: The identity of this ProblemOccurrenceLocator.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def item(self):
        """Gets the item of this ProblemOccurrenceLocator.  # noqa: E501

        Supply multiple locators and return a union of the results.  # noqa: E501

        :return: The item of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this ProblemOccurrenceLocator.

        Supply multiple locators and return a union of the results.  # noqa: E501

        :param item: The item of this ProblemOccurrenceLocator.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def lookup_limit(self):
        """Gets the lookup_limit of this ProblemOccurrenceLocator.  # noqa: E501

        Limit processing to the latest `<lookupLimit>` entities.  # noqa: E501

        :return: The lookup_limit of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: int
        """
        return self._lookup_limit

    @lookup_limit.setter
    def lookup_limit(self, lookup_limit):
        """Sets the lookup_limit of this ProblemOccurrenceLocator.

        Limit processing to the latest `<lookupLimit>` entities.  # noqa: E501

        :param lookup_limit: The lookup_limit of this ProblemOccurrenceLocator.  # noqa: E501
        :type: int
        """

        self._lookup_limit = lookup_limit

    @property
    def muted(self):
        """Gets the muted of this ProblemOccurrenceLocator.  # noqa: E501

        Has ever been muted.  # noqa: E501

        :return: The muted of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this ProblemOccurrenceLocator.

        Has ever been muted.  # noqa: E501

        :param muted: The muted of this ProblemOccurrenceLocator.  # noqa: E501
        :type: bool
        """

        self._muted = muted

    @property
    def problem(self):
        """Gets the problem of this ProblemOccurrenceLocator.  # noqa: E501


        :return: The problem of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: str
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this ProblemOccurrenceLocator.


        :param problem: The problem of this ProblemOccurrenceLocator.  # noqa: E501
        :type: str
        """

        self._problem = problem

    @property
    def start(self):
        """Gets the start of this ProblemOccurrenceLocator.  # noqa: E501

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :return: The start of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ProblemOccurrenceLocator.

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :param start: The start of this ProblemOccurrenceLocator.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def type(self):
        """Gets the type of this ProblemOccurrenceLocator.  # noqa: E501


        :return: The type of this ProblemOccurrenceLocator.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProblemOccurrenceLocator.


        :param type: The type of this ProblemOccurrenceLocator.  # noqa: E501
        :type: str
        """

        self._type = type
