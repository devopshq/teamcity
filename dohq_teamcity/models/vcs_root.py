# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.items import Items  # noqa: F401,E501
# from dohq_teamcity.models.project import Project  # noqa: F401,E501
# from dohq_teamcity.models.properties import Properties  # noqa: F401,E501
# from dohq_teamcity.models.vcs_root_instances import VcsRootInstances  # noqa: F401,E501


class VcsRoot(TeamCityObject):
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
        'id': 'str',
        'internal_id': 'str',
        'uuid': 'str',
        'name': 'str',
        'vcs_name': 'str',
        'modification_check_interval': 'int',
        'href': 'str',
        'project': 'Project',
        'properties': 'Properties',
        'vcs_root_instances': 'VcsRootInstances',
        'repository_id_strings': 'Items',
        'locator': 'str',
        'project_locator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'internal_id': 'internalId',
        'uuid': 'uuid',
        'name': 'name',
        'vcs_name': 'vcsName',
        'modification_check_interval': 'modificationCheckInterval',
        'href': 'href',
        'project': 'project',
        'properties': 'properties',
        'vcs_root_instances': 'vcsRootInstances',
        'repository_id_strings': 'repositoryIdStrings',
        'locator': 'locator',
        'project_locator': 'projectLocator'
    }

    def __init__(self, id=None, internal_id=None, uuid=None, name=None, vcs_name=None, modification_check_interval=None, href=None, project=None, properties=None, vcs_root_instances=None, repository_id_strings=None, locator=None, project_locator=None, teamcity=None):  # noqa: E501
        """VcsRoot - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._internal_id = None
        self._uuid = None
        self._name = None
        self._vcs_name = None
        self._modification_check_interval = None
        self._href = None
        self._project = None
        self._properties = None
        self._vcs_root_instances = None
        self._repository_id_strings = None
        self._locator = None
        self._project_locator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if internal_id is not None:
            self.internal_id = internal_id
        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if vcs_name is not None:
            self.vcs_name = vcs_name
        if modification_check_interval is not None:
            self.modification_check_interval = modification_check_interval
        if href is not None:
            self.href = href
        if project is not None:
            self.project = project
        if properties is not None:
            self.properties = properties
        if vcs_root_instances is not None:
            self.vcs_root_instances = vcs_root_instances
        if repository_id_strings is not None:
            self.repository_id_strings = repository_id_strings
        if locator is not None:
            self.locator = locator
        if project_locator is not None:
            self.project_locator = project_locator
        super(VcsRoot, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this VcsRoot.  # noqa: E501


        :return: The id of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcsRoot.


        :param id: The id of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def internal_id(self):
        """Gets the internal_id of this VcsRoot.  # noqa: E501


        :return: The internal_id of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this VcsRoot.


        :param internal_id: The internal_id of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def uuid(self):
        """Gets the uuid of this VcsRoot.  # noqa: E501


        :return: The uuid of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this VcsRoot.


        :param uuid: The uuid of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this VcsRoot.  # noqa: E501


        :return: The name of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VcsRoot.


        :param name: The name of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vcs_name(self):
        """Gets the vcs_name of this VcsRoot.  # noqa: E501


        :return: The vcs_name of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._vcs_name

    @vcs_name.setter
    def vcs_name(self, vcs_name):
        """Sets the vcs_name of this VcsRoot.


        :param vcs_name: The vcs_name of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._vcs_name = vcs_name

    @property
    def modification_check_interval(self):
        """Gets the modification_check_interval of this VcsRoot.  # noqa: E501


        :return: The modification_check_interval of this VcsRoot.  # noqa: E501
        :rtype: int
        """
        return self._modification_check_interval

    @modification_check_interval.setter
    def modification_check_interval(self, modification_check_interval):
        """Sets the modification_check_interval of this VcsRoot.


        :param modification_check_interval: The modification_check_interval of this VcsRoot.  # noqa: E501
        :type: int
        """

        self._modification_check_interval = modification_check_interval

    @property
    def href(self):
        """Gets the href of this VcsRoot.  # noqa: E501


        :return: The href of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this VcsRoot.


        :param href: The href of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def project(self):
        """Gets the project of this VcsRoot.  # noqa: E501


        :return: The project of this VcsRoot.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this VcsRoot.


        :param project: The project of this VcsRoot.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def properties(self):
        """Gets the properties of this VcsRoot.  # noqa: E501


        :return: The properties of this VcsRoot.  # noqa: E501
        :rtype: Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this VcsRoot.


        :param properties: The properties of this VcsRoot.  # noqa: E501
        :type: Properties
        """

        self._properties = properties

    @property
    def vcs_root_instances(self):
        """Gets the vcs_root_instances of this VcsRoot.  # noqa: E501


        :return: The vcs_root_instances of this VcsRoot.  # noqa: E501
        :rtype: VcsRootInstances
        """
        return self._vcs_root_instances

    @vcs_root_instances.setter
    def vcs_root_instances(self, vcs_root_instances):
        """Sets the vcs_root_instances of this VcsRoot.


        :param vcs_root_instances: The vcs_root_instances of this VcsRoot.  # noqa: E501
        :type: VcsRootInstances
        """

        self._vcs_root_instances = vcs_root_instances

    @property
    def repository_id_strings(self):
        """Gets the repository_id_strings of this VcsRoot.  # noqa: E501


        :return: The repository_id_strings of this VcsRoot.  # noqa: E501
        :rtype: Items
        """
        return self._repository_id_strings

    @repository_id_strings.setter
    def repository_id_strings(self, repository_id_strings):
        """Sets the repository_id_strings of this VcsRoot.


        :param repository_id_strings: The repository_id_strings of this VcsRoot.  # noqa: E501
        :type: Items
        """

        self._repository_id_strings = repository_id_strings

    @property
    def locator(self):
        """Gets the locator of this VcsRoot.  # noqa: E501


        :return: The locator of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this VcsRoot.


        :param locator: The locator of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def project_locator(self):
        """Gets the project_locator of this VcsRoot.  # noqa: E501


        :return: The project_locator of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._project_locator

    @project_locator.setter
    def project_locator(self, project_locator):
        """Sets the project_locator of this VcsRoot.


        :param project_locator: The project_locator of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._project_locator = project_locator
