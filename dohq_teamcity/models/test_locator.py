# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class TestLocator(TeamCityObject):
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
        'count': 'int',
        'currently_failing': 'bool',
        'currently_investigated': 'bool',
        'currently_muted': 'bool',
        'id': 'str',
        'item': 'str',
        'lookup_limit': 'int',
        'mute_affected': 'str',
        'name': 'str',
        'start': 'int'
    }

    attribute_map = {
        'affected_project': 'affectedProject',
        'count': 'count',
        'currently_failing': 'currentlyFailing',
        'currently_investigated': 'currentlyInvestigated',
        'currently_muted': 'currentlyMuted',
        'id': 'id',
        'item': 'item',
        'lookup_limit': 'lookupLimit',
        'mute_affected': 'muteAffected',
        'name': 'name',
        'start': 'start'
    }

    def __init__(self, affected_project=None, count=None, currently_failing=None, currently_investigated=None, currently_muted=None, id=None, item=None, lookup_limit=None, mute_affected=None, name=None, start=None, teamcity=None):  # noqa: E501
        """TestLocator - a model defined in Swagger"""  # noqa: E501

        self._affected_project = None
        self._count = None
        self._currently_failing = None
        self._currently_investigated = None
        self._currently_muted = None
        self._id = None
        self._item = None
        self._lookup_limit = None
        self._mute_affected = None
        self._name = None
        self._start = None
        self.discriminator = None

        if affected_project is not None:
            self.affected_project = affected_project
        if count is not None:
            self.count = count
        if currently_failing is not None:
            self.currently_failing = currently_failing
        if currently_investigated is not None:
            self.currently_investigated = currently_investigated
        if currently_muted is not None:
            self.currently_muted = currently_muted
        if id is not None:
            self.id = id
        if item is not None:
            self.item = item
        if lookup_limit is not None:
            self.lookup_limit = lookup_limit
        if mute_affected is not None:
            self.mute_affected = mute_affected
        if name is not None:
            self.name = name
        if start is not None:
            self.start = start
        super(TestLocator, self).__init__(teamcity=teamcity)

    @property
    def affected_project(self):
        """Gets the affected_project of this TestLocator.  # noqa: E501

        Project (direct or indirect parent) locator.  # noqa: E501

        :return: The affected_project of this TestLocator.  # noqa: E501
        :rtype: str
        """
        return self._affected_project

    @affected_project.setter
    def affected_project(self, affected_project):
        """Sets the affected_project of this TestLocator.

        Project (direct or indirect parent) locator.  # noqa: E501

        :param affected_project: The affected_project of this TestLocator.  # noqa: E501
        :type: str
        """

        self._affected_project = affected_project

    @property
    def count(self):
        """Gets the count of this TestLocator.  # noqa: E501

        For paginated calls, how many entities to return per page.  # noqa: E501

        :return: The count of this TestLocator.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TestLocator.

        For paginated calls, how many entities to return per page.  # noqa: E501

        :param count: The count of this TestLocator.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def currently_failing(self):
        """Gets the currently_failing of this TestLocator.  # noqa: E501

        Is currently failing.  # noqa: E501

        :return: The currently_failing of this TestLocator.  # noqa: E501
        :rtype: bool
        """
        return self._currently_failing

    @currently_failing.setter
    def currently_failing(self, currently_failing):
        """Sets the currently_failing of this TestLocator.

        Is currently failing.  # noqa: E501

        :param currently_failing: The currently_failing of this TestLocator.  # noqa: E501
        :type: bool
        """

        self._currently_failing = currently_failing

    @property
    def currently_investigated(self):
        """Gets the currently_investigated of this TestLocator.  # noqa: E501

        Is currently investigated.  # noqa: E501

        :return: The currently_investigated of this TestLocator.  # noqa: E501
        :rtype: bool
        """
        return self._currently_investigated

    @currently_investigated.setter
    def currently_investigated(self, currently_investigated):
        """Sets the currently_investigated of this TestLocator.

        Is currently investigated.  # noqa: E501

        :param currently_investigated: The currently_investigated of this TestLocator.  # noqa: E501
        :type: bool
        """

        self._currently_investigated = currently_investigated

    @property
    def currently_muted(self):
        """Gets the currently_muted of this TestLocator.  # noqa: E501

        Is currently muted.  # noqa: E501

        :return: The currently_muted of this TestLocator.  # noqa: E501
        :rtype: bool
        """
        return self._currently_muted

    @currently_muted.setter
    def currently_muted(self, currently_muted):
        """Sets the currently_muted of this TestLocator.

        Is currently muted.  # noqa: E501

        :param currently_muted: The currently_muted of this TestLocator.  # noqa: E501
        :type: bool
        """

        self._currently_muted = currently_muted

    @property
    def id(self):
        """Gets the id of this TestLocator.  # noqa: E501

        Entity ID.  # noqa: E501

        :return: The id of this TestLocator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestLocator.

        Entity ID.  # noqa: E501

        :param id: The id of this TestLocator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def item(self):
        """Gets the item of this TestLocator.  # noqa: E501

        Supply multiple locators and return a union of the results.  # noqa: E501

        :return: The item of this TestLocator.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this TestLocator.

        Supply multiple locators and return a union of the results.  # noqa: E501

        :param item: The item of this TestLocator.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def lookup_limit(self):
        """Gets the lookup_limit of this TestLocator.  # noqa: E501

        Limit processing to the latest `<lookupLimit>` entities.  # noqa: E501

        :return: The lookup_limit of this TestLocator.  # noqa: E501
        :rtype: int
        """
        return self._lookup_limit

    @lookup_limit.setter
    def lookup_limit(self, lookup_limit):
        """Sets the lookup_limit of this TestLocator.

        Limit processing to the latest `<lookupLimit>` entities.  # noqa: E501

        :param lookup_limit: The lookup_limit of this TestLocator.  # noqa: E501
        :type: int
        """

        self._lookup_limit = lookup_limit

    @property
    def mute_affected(self):
        """Gets the mute_affected of this TestLocator.  # noqa: E501

        Build type locator (for finding out if this test is affected by mutes in build type).  # noqa: E501

        :return: The mute_affected of this TestLocator.  # noqa: E501
        :rtype: str
        """
        return self._mute_affected

    @mute_affected.setter
    def mute_affected(self, mute_affected):
        """Sets the mute_affected of this TestLocator.

        Build type locator (for finding out if this test is affected by mutes in build type).  # noqa: E501

        :param mute_affected: The mute_affected of this TestLocator.  # noqa: E501
        :type: str
        """

        self._mute_affected = mute_affected

    @property
    def name(self):
        """Gets the name of this TestLocator.  # noqa: E501


        :return: The name of this TestLocator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestLocator.


        :param name: The name of this TestLocator.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start(self):
        """Gets the start of this TestLocator.  # noqa: E501

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :return: The start of this TestLocator.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TestLocator.

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :param start: The start of this TestLocator.  # noqa: E501
        :type: int
        """

        self._start = start
