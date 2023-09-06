# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class VcsRootInstanceLocator(TeamCityObject):
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
        'build_type': 'str',
        'count': 'int',
        'id': 'str',
        'item': 'str',
        'lookup_limit': 'int',
        'project': 'str',
        '_property': 'str',
        'start': 'int',
        'type': 'str',
        'vcs_root': 'str',
        'versioned_settings': 'bool'
    }

    attribute_map = {
        'affected_project': 'affectedProject',
        'build': 'build',
        'build_type': 'buildType',
        'count': 'count',
        'id': 'id',
        'item': 'item',
        'lookup_limit': 'lookupLimit',
        'project': 'project',
        '_property': 'property',
        'start': 'start',
        'type': 'type',
        'vcs_root': 'vcsRoot',
        'versioned_settings': 'versionedSettings'
    }

    def __init__(self, affected_project=None, build=None, build_type=None, count=None, id=None, item=None, lookup_limit=None, project=None, _property=None, start=None, type=None, vcs_root=None, versioned_settings=None, teamcity=None):  # noqa: E501
        """VcsRootInstanceLocator - a model defined in Swagger"""  # noqa: E501

        self._affected_project = None
        self._build = None
        self._build_type = None
        self._count = None
        self._id = None
        self._item = None
        self._lookup_limit = None
        self._project = None
        self.__property = None
        self._start = None
        self._type = None
        self._vcs_root = None
        self._versioned_settings = None
        self.discriminator = None

        if affected_project is not None:
            self.affected_project = affected_project
        if build is not None:
            self.build = build
        if build_type is not None:
            self.build_type = build_type
        if count is not None:
            self.count = count
        if id is not None:
            self.id = id
        if item is not None:
            self.item = item
        if lookup_limit is not None:
            self.lookup_limit = lookup_limit
        if project is not None:
            self.project = project
        if _property is not None:
            self._property = _property
        if start is not None:
            self.start = start
        if type is not None:
            self.type = type
        if vcs_root is not None:
            self.vcs_root = vcs_root
        if versioned_settings is not None:
            self.versioned_settings = versioned_settings
        super(VcsRootInstanceLocator, self).__init__(teamcity=teamcity)

    @property
    def affected_project(self):
        """Gets the affected_project of this VcsRootInstanceLocator.  # noqa: E501

        Project (direct or indirect parent) locator.  # noqa: E501

        :return: The affected_project of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: str
        """
        return self._affected_project

    @affected_project.setter
    def affected_project(self, affected_project):
        """Sets the affected_project of this VcsRootInstanceLocator.

        Project (direct or indirect parent) locator.  # noqa: E501

        :param affected_project: The affected_project of this VcsRootInstanceLocator.  # noqa: E501
        :type: str
        """

        self._affected_project = affected_project

    @property
    def build(self):
        """Gets the build of this VcsRootInstanceLocator.  # noqa: E501

        Build locator.  # noqa: E501

        :return: The build of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this VcsRootInstanceLocator.

        Build locator.  # noqa: E501

        :param build: The build of this VcsRootInstanceLocator.  # noqa: E501
        :type: str
        """

        self._build = build

    @property
    def build_type(self):
        """Gets the build_type of this VcsRootInstanceLocator.  # noqa: E501

        Build type locator.  # noqa: E501

        :return: The build_type of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        """Sets the build_type of this VcsRootInstanceLocator.

        Build type locator.  # noqa: E501

        :param build_type: The build_type of this VcsRootInstanceLocator.  # noqa: E501
        :type: str
        """

        self._build_type = build_type

    @property
    def count(self):
        """Gets the count of this VcsRootInstanceLocator.  # noqa: E501

        For paginated calls, how many entities to return per page.  # noqa: E501

        :return: The count of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this VcsRootInstanceLocator.

        For paginated calls, how many entities to return per page.  # noqa: E501

        :param count: The count of this VcsRootInstanceLocator.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def id(self):
        """Gets the id of this VcsRootInstanceLocator.  # noqa: E501

        Entity ID.  # noqa: E501

        :return: The id of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcsRootInstanceLocator.

        Entity ID.  # noqa: E501

        :param id: The id of this VcsRootInstanceLocator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def item(self):
        """Gets the item of this VcsRootInstanceLocator.  # noqa: E501

        Supply multiple locators and return a union of the results.  # noqa: E501

        :return: The item of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this VcsRootInstanceLocator.

        Supply multiple locators and return a union of the results.  # noqa: E501

        :param item: The item of this VcsRootInstanceLocator.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def lookup_limit(self):
        """Gets the lookup_limit of this VcsRootInstanceLocator.  # noqa: E501

        Limit processing to the latest `<lookupLimit>` entities.  # noqa: E501

        :return: The lookup_limit of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: int
        """
        return self._lookup_limit

    @lookup_limit.setter
    def lookup_limit(self, lookup_limit):
        """Sets the lookup_limit of this VcsRootInstanceLocator.

        Limit processing to the latest `<lookupLimit>` entities.  # noqa: E501

        :param lookup_limit: The lookup_limit of this VcsRootInstanceLocator.  # noqa: E501
        :type: int
        """

        self._lookup_limit = lookup_limit

    @property
    def project(self):
        """Gets the project of this VcsRootInstanceLocator.  # noqa: E501

        Project (direct parent) locator.  # noqa: E501

        :return: The project of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this VcsRootInstanceLocator.

        Project (direct parent) locator.  # noqa: E501

        :param project: The project of this VcsRootInstanceLocator.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def _property(self):
        """Gets the _property of this VcsRootInstanceLocator.  # noqa: E501


        :return: The _property of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this VcsRootInstanceLocator.


        :param _property: The _property of this VcsRootInstanceLocator.  # noqa: E501
        :type: str
        """
        allowed_values = ["exists", "not-exists", "equals", "does-not-equal", "starts-with", "contains", "does-not-contain", "ends-with", "any", "matches", "does-not-match", "more-than", "no-more-than", "less-than", "no-less-than", "ver-more-than", "ver-no-more-than", "ver-less-than", "ver-no-less-than"]  # noqa: E501
        if _property not in allowed_values:
            raise ValueError(
                "Invalid value for `_property` ({0}), must be one of {1}"  # noqa: E501
                .format(_property, allowed_values)
            )

        self.__property = _property

    @property
    def start(self):
        """Gets the start of this VcsRootInstanceLocator.  # noqa: E501

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :return: The start of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this VcsRootInstanceLocator.

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :param start: The start of this VcsRootInstanceLocator.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def type(self):
        """Gets the type of this VcsRootInstanceLocator.  # noqa: E501

        Type of VCS (e.g. jetbrains.git).  # noqa: E501

        :return: The type of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VcsRootInstanceLocator.

        Type of VCS (e.g. jetbrains.git).  # noqa: E501

        :param type: The type of this VcsRootInstanceLocator.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vcs_root(self):
        """Gets the vcs_root of this VcsRootInstanceLocator.  # noqa: E501

        VCS root locator.  # noqa: E501

        :return: The vcs_root of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: str
        """
        return self._vcs_root

    @vcs_root.setter
    def vcs_root(self, vcs_root):
        """Sets the vcs_root of this VcsRootInstanceLocator.

        VCS root locator.  # noqa: E501

        :param vcs_root: The vcs_root of this VcsRootInstanceLocator.  # noqa: E501
        :type: str
        """

        self._vcs_root = vcs_root

    @property
    def versioned_settings(self):
        """Gets the versioned_settings of this VcsRootInstanceLocator.  # noqa: E501

        Is used for versioned settings.  # noqa: E501

        :return: The versioned_settings of this VcsRootInstanceLocator.  # noqa: E501
        :rtype: bool
        """
        return self._versioned_settings

    @versioned_settings.setter
    def versioned_settings(self, versioned_settings):
        """Sets the versioned_settings of this VcsRootInstanceLocator.

        Is used for versioned settings.  # noqa: E501

        :param versioned_settings: The versioned_settings of this VcsRootInstanceLocator.  # noqa: E501
        :type: bool
        """

        self._versioned_settings = versioned_settings
