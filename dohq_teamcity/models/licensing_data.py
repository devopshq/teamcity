# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.license_keys import LicenseKeys  # noqa: F401,E501


class LicensingData(TeamCityObject):
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
        'agents_left': 'int',
        'build_types_left': 'int',
        'license_keys': 'LicenseKeys',
        'license_use_exceeded': 'bool',
        'max_agents': 'int',
        'max_build_types': 'int',
        'server_effective_release_date': 'str',
        'server_license_type': 'str',
        'unlimited_agents': 'bool',
        'unlimited_build_types': 'bool'
    }

    attribute_map = {
        'agents_left': 'agentsLeft',
        'build_types_left': 'buildTypesLeft',
        'license_keys': 'licenseKeys',
        'license_use_exceeded': 'licenseUseExceeded',
        'max_agents': 'maxAgents',
        'max_build_types': 'maxBuildTypes',
        'server_effective_release_date': 'serverEffectiveReleaseDate',
        'server_license_type': 'serverLicenseType',
        'unlimited_agents': 'unlimitedAgents',
        'unlimited_build_types': 'unlimitedBuildTypes'
    }

    def __init__(self, agents_left=None, build_types_left=None, license_keys=None, license_use_exceeded=False, max_agents=None, max_build_types=None, server_effective_release_date=None, server_license_type=None, unlimited_agents=False, unlimited_build_types=False, teamcity=None):  # noqa: E501
        """LicensingData - a model defined in Swagger"""  # noqa: E501

        self._agents_left = None
        self._build_types_left = None
        self._license_keys = None
        self._license_use_exceeded = None
        self._max_agents = None
        self._max_build_types = None
        self._server_effective_release_date = None
        self._server_license_type = None
        self._unlimited_agents = None
        self._unlimited_build_types = None
        self.discriminator = None

        if agents_left is not None:
            self.agents_left = agents_left
        if build_types_left is not None:
            self.build_types_left = build_types_left
        if license_keys is not None:
            self.license_keys = license_keys
        if license_use_exceeded is not None:
            self.license_use_exceeded = license_use_exceeded
        if max_agents is not None:
            self.max_agents = max_agents
        if max_build_types is not None:
            self.max_build_types = max_build_types
        if server_effective_release_date is not None:
            self.server_effective_release_date = server_effective_release_date
        if server_license_type is not None:
            self.server_license_type = server_license_type
        if unlimited_agents is not None:
            self.unlimited_agents = unlimited_agents
        if unlimited_build_types is not None:
            self.unlimited_build_types = unlimited_build_types
        super(LicensingData, self).__init__(teamcity=teamcity)

    @property
    def agents_left(self):
        """Gets the agents_left of this LicensingData.  # noqa: E501


        :return: The agents_left of this LicensingData.  # noqa: E501
        :rtype: int
        """
        return self._agents_left

    @agents_left.setter
    def agents_left(self, agents_left):
        """Sets the agents_left of this LicensingData.


        :param agents_left: The agents_left of this LicensingData.  # noqa: E501
        :type: int
        """

        self._agents_left = agents_left

    @property
    def build_types_left(self):
        """Gets the build_types_left of this LicensingData.  # noqa: E501


        :return: The build_types_left of this LicensingData.  # noqa: E501
        :rtype: int
        """
        return self._build_types_left

    @build_types_left.setter
    def build_types_left(self, build_types_left):
        """Sets the build_types_left of this LicensingData.


        :param build_types_left: The build_types_left of this LicensingData.  # noqa: E501
        :type: int
        """

        self._build_types_left = build_types_left

    @property
    def license_keys(self):
        """Gets the license_keys of this LicensingData.  # noqa: E501


        :return: The license_keys of this LicensingData.  # noqa: E501
        :rtype: LicenseKeys
        """
        return self._license_keys

    @license_keys.setter
    def license_keys(self, license_keys):
        """Sets the license_keys of this LicensingData.


        :param license_keys: The license_keys of this LicensingData.  # noqa: E501
        :type: LicenseKeys
        """

        self._license_keys = license_keys

    @property
    def license_use_exceeded(self):
        """Gets the license_use_exceeded of this LicensingData.  # noqa: E501


        :return: The license_use_exceeded of this LicensingData.  # noqa: E501
        :rtype: bool
        """
        return self._license_use_exceeded

    @license_use_exceeded.setter
    def license_use_exceeded(self, license_use_exceeded):
        """Sets the license_use_exceeded of this LicensingData.


        :param license_use_exceeded: The license_use_exceeded of this LicensingData.  # noqa: E501
        :type: bool
        """

        self._license_use_exceeded = license_use_exceeded

    @property
    def max_agents(self):
        """Gets the max_agents of this LicensingData.  # noqa: E501


        :return: The max_agents of this LicensingData.  # noqa: E501
        :rtype: int
        """
        return self._max_agents

    @max_agents.setter
    def max_agents(self, max_agents):
        """Sets the max_agents of this LicensingData.


        :param max_agents: The max_agents of this LicensingData.  # noqa: E501
        :type: int
        """

        self._max_agents = max_agents

    @property
    def max_build_types(self):
        """Gets the max_build_types of this LicensingData.  # noqa: E501


        :return: The max_build_types of this LicensingData.  # noqa: E501
        :rtype: int
        """
        return self._max_build_types

    @max_build_types.setter
    def max_build_types(self, max_build_types):
        """Sets the max_build_types of this LicensingData.


        :param max_build_types: The max_build_types of this LicensingData.  # noqa: E501
        :type: int
        """

        self._max_build_types = max_build_types

    @property
    def server_effective_release_date(self):
        """Gets the server_effective_release_date of this LicensingData.  # noqa: E501


        :return: The server_effective_release_date of this LicensingData.  # noqa: E501
        :rtype: str
        """
        return self._server_effective_release_date

    @server_effective_release_date.setter
    def server_effective_release_date(self, server_effective_release_date):
        """Sets the server_effective_release_date of this LicensingData.


        :param server_effective_release_date: The server_effective_release_date of this LicensingData.  # noqa: E501
        :type: str
        """

        self._server_effective_release_date = server_effective_release_date

    @property
    def server_license_type(self):
        """Gets the server_license_type of this LicensingData.  # noqa: E501


        :return: The server_license_type of this LicensingData.  # noqa: E501
        :rtype: str
        """
        return self._server_license_type

    @server_license_type.setter
    def server_license_type(self, server_license_type):
        """Sets the server_license_type of this LicensingData.


        :param server_license_type: The server_license_type of this LicensingData.  # noqa: E501
        :type: str
        """

        self._server_license_type = server_license_type

    @property
    def unlimited_agents(self):
        """Gets the unlimited_agents of this LicensingData.  # noqa: E501


        :return: The unlimited_agents of this LicensingData.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_agents

    @unlimited_agents.setter
    def unlimited_agents(self, unlimited_agents):
        """Sets the unlimited_agents of this LicensingData.


        :param unlimited_agents: The unlimited_agents of this LicensingData.  # noqa: E501
        :type: bool
        """

        self._unlimited_agents = unlimited_agents

    @property
    def unlimited_build_types(self):
        """Gets the unlimited_build_types of this LicensingData.  # noqa: E501


        :return: The unlimited_build_types of this LicensingData.  # noqa: E501
        :rtype: bool
        """
        return self._unlimited_build_types

    @unlimited_build_types.setter
    def unlimited_build_types(self, unlimited_build_types):
        """Sets the unlimited_build_types of this LicensingData.


        :param unlimited_build_types: The unlimited_build_types of this LicensingData.  # noqa: E501
        :type: bool
        """

        self._unlimited_build_types = unlimited_build_types
