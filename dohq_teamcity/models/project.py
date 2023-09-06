# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.build_type import BuildType  # noqa: F401,E501
# from dohq_teamcity.models.build_types import BuildTypes  # noqa: F401,E501
# from dohq_teamcity.models.cloud_profiles import CloudProfiles  # noqa: F401,E501
# from dohq_teamcity.models.links import Links  # noqa: F401,E501
# from dohq_teamcity.models.project import Project  # noqa: F401,E501
# from dohq_teamcity.models.project_features import ProjectFeatures  # noqa: F401,E501
# from dohq_teamcity.models.projects import Projects  # noqa: F401,E501
# from dohq_teamcity.models.properties import Properties  # noqa: F401,E501
# from dohq_teamcity.models.state_field import StateField  # noqa: F401,E501
# from dohq_teamcity.models.vcs_roots import VcsRoots  # noqa: F401,E501


class Project(TeamCityObject):
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
        'parent_project_id': 'str',
        'parent_project_internal_id': 'str',
        'parent_project_name': 'str',
        'archived': 'bool',
        'virtual': 'bool',
        'description': 'str',
        'href': 'str',
        'web_url': 'str',
        'links': 'Links',
        'parent_project': 'Project',
        'read_only_ui': 'StateField',
        'default_template': 'BuildType',
        'build_types': 'BuildTypes',
        'templates': 'BuildTypes',
        'parameters': 'Properties',
        'vcs_roots': 'VcsRoots',
        'project_features': 'ProjectFeatures',
        'projects': 'Projects',
        'cloud_profiles': 'CloudProfiles',
        'ancestor_projects': 'Projects',
        'locator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'internal_id': 'internalId',
        'uuid': 'uuid',
        'name': 'name',
        'parent_project_id': 'parentProjectId',
        'parent_project_internal_id': 'parentProjectInternalId',
        'parent_project_name': 'parentProjectName',
        'archived': 'archived',
        'virtual': 'virtual',
        'description': 'description',
        'href': 'href',
        'web_url': 'webUrl',
        'links': 'links',
        'parent_project': 'parentProject',
        'read_only_ui': 'readOnlyUI',
        'default_template': 'defaultTemplate',
        'build_types': 'buildTypes',
        'templates': 'templates',
        'parameters': 'parameters',
        'vcs_roots': 'vcsRoots',
        'project_features': 'projectFeatures',
        'projects': 'projects',
        'cloud_profiles': 'cloudProfiles',
        'ancestor_projects': 'ancestorProjects',
        'locator': 'locator'
    }

    def __init__(self, id=None, internal_id=None, uuid=None, name=None, parent_project_id=None, parent_project_internal_id=None, parent_project_name=None, archived=None, virtual=None, description=None, href=None, web_url=None, links=None, parent_project=None, read_only_ui=None, default_template=None, build_types=None, templates=None, parameters=None, vcs_roots=None, project_features=None, projects=None, cloud_profiles=None, ancestor_projects=None, locator=None, teamcity=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._internal_id = None
        self._uuid = None
        self._name = None
        self._parent_project_id = None
        self._parent_project_internal_id = None
        self._parent_project_name = None
        self._archived = None
        self._virtual = None
        self._description = None
        self._href = None
        self._web_url = None
        self._links = None
        self._parent_project = None
        self._read_only_ui = None
        self._default_template = None
        self._build_types = None
        self._templates = None
        self._parameters = None
        self._vcs_roots = None
        self._project_features = None
        self._projects = None
        self._cloud_profiles = None
        self._ancestor_projects = None
        self._locator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if internal_id is not None:
            self.internal_id = internal_id
        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if parent_project_id is not None:
            self.parent_project_id = parent_project_id
        if parent_project_internal_id is not None:
            self.parent_project_internal_id = parent_project_internal_id
        if parent_project_name is not None:
            self.parent_project_name = parent_project_name
        if archived is not None:
            self.archived = archived
        if virtual is not None:
            self.virtual = virtual
        if description is not None:
            self.description = description
        if href is not None:
            self.href = href
        if web_url is not None:
            self.web_url = web_url
        if links is not None:
            self.links = links
        if parent_project is not None:
            self.parent_project = parent_project
        if read_only_ui is not None:
            self.read_only_ui = read_only_ui
        if default_template is not None:
            self.default_template = default_template
        if build_types is not None:
            self.build_types = build_types
        if templates is not None:
            self.templates = templates
        if parameters is not None:
            self.parameters = parameters
        if vcs_roots is not None:
            self.vcs_roots = vcs_roots
        if project_features is not None:
            self.project_features = project_features
        if projects is not None:
            self.projects = projects
        if cloud_profiles is not None:
            self.cloud_profiles = cloud_profiles
        if ancestor_projects is not None:
            self.ancestor_projects = ancestor_projects
        if locator is not None:
            self.locator = locator
        super(Project, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def internal_id(self):
        """Gets the internal_id of this Project.  # noqa: E501


        :return: The internal_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this Project.


        :param internal_id: The internal_id of this Project.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def uuid(self):
        """Gets the uuid of this Project.  # noqa: E501


        :return: The uuid of this Project.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Project.


        :param uuid: The uuid of this Project.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_project_id(self):
        """Gets the parent_project_id of this Project.  # noqa: E501


        :return: The parent_project_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._parent_project_id

    @parent_project_id.setter
    def parent_project_id(self, parent_project_id):
        """Sets the parent_project_id of this Project.


        :param parent_project_id: The parent_project_id of this Project.  # noqa: E501
        :type: str
        """

        self._parent_project_id = parent_project_id

    @property
    def parent_project_internal_id(self):
        """Gets the parent_project_internal_id of this Project.  # noqa: E501


        :return: The parent_project_internal_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._parent_project_internal_id

    @parent_project_internal_id.setter
    def parent_project_internal_id(self, parent_project_internal_id):
        """Sets the parent_project_internal_id of this Project.


        :param parent_project_internal_id: The parent_project_internal_id of this Project.  # noqa: E501
        :type: str
        """

        self._parent_project_internal_id = parent_project_internal_id

    @property
    def parent_project_name(self):
        """Gets the parent_project_name of this Project.  # noqa: E501


        :return: The parent_project_name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._parent_project_name

    @parent_project_name.setter
    def parent_project_name(self, parent_project_name):
        """Sets the parent_project_name of this Project.


        :param parent_project_name: The parent_project_name of this Project.  # noqa: E501
        :type: str
        """

        self._parent_project_name = parent_project_name

    @property
    def archived(self):
        """Gets the archived of this Project.  # noqa: E501


        :return: The archived of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Project.


        :param archived: The archived of this Project.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def virtual(self):
        """Gets the virtual of this Project.  # noqa: E501


        :return: The virtual of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._virtual

    @virtual.setter
    def virtual(self, virtual):
        """Sets the virtual of this Project.


        :param virtual: The virtual of this Project.  # noqa: E501
        :type: bool
        """

        self._virtual = virtual

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501


        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.


        :param description: The description of this Project.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def href(self):
        """Gets the href of this Project.  # noqa: E501


        :return: The href of this Project.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Project.


        :param href: The href of this Project.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def web_url(self):
        """Gets the web_url of this Project.  # noqa: E501


        :return: The web_url of this Project.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this Project.


        :param web_url: The web_url of this Project.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

    @property
    def links(self):
        """Gets the links of this Project.  # noqa: E501


        :return: The links of this Project.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Project.


        :param links: The links of this Project.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def parent_project(self):
        """Gets the parent_project of this Project.  # noqa: E501


        :return: The parent_project of this Project.  # noqa: E501
        :rtype: Project
        """
        return self._parent_project

    @parent_project.setter
    def parent_project(self, parent_project):
        """Sets the parent_project of this Project.


        :param parent_project: The parent_project of this Project.  # noqa: E501
        :type: Project
        """

        self._parent_project = parent_project

    @property
    def read_only_ui(self):
        """Gets the read_only_ui of this Project.  # noqa: E501


        :return: The read_only_ui of this Project.  # noqa: E501
        :rtype: StateField
        """
        return self._read_only_ui

    @read_only_ui.setter
    def read_only_ui(self, read_only_ui):
        """Sets the read_only_ui of this Project.


        :param read_only_ui: The read_only_ui of this Project.  # noqa: E501
        :type: StateField
        """

        self._read_only_ui = read_only_ui

    @property
    def default_template(self):
        """Gets the default_template of this Project.  # noqa: E501


        :return: The default_template of this Project.  # noqa: E501
        :rtype: BuildType
        """
        return self._default_template

    @default_template.setter
    def default_template(self, default_template):
        """Sets the default_template of this Project.


        :param default_template: The default_template of this Project.  # noqa: E501
        :type: BuildType
        """

        self._default_template = default_template

    @property
    def build_types(self):
        """Gets the build_types of this Project.  # noqa: E501


        :return: The build_types of this Project.  # noqa: E501
        :rtype: BuildTypes
        """
        return self._build_types

    @build_types.setter
    def build_types(self, build_types):
        """Sets the build_types of this Project.


        :param build_types: The build_types of this Project.  # noqa: E501
        :type: BuildTypes
        """

        self._build_types = build_types

    @property
    def templates(self):
        """Gets the templates of this Project.  # noqa: E501


        :return: The templates of this Project.  # noqa: E501
        :rtype: BuildTypes
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this Project.


        :param templates: The templates of this Project.  # noqa: E501
        :type: BuildTypes
        """

        self._templates = templates

    @property
    def parameters(self):
        """Gets the parameters of this Project.  # noqa: E501


        :return: The parameters of this Project.  # noqa: E501
        :rtype: Properties
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Project.


        :param parameters: The parameters of this Project.  # noqa: E501
        :type: Properties
        """

        self._parameters = parameters

    @property
    def vcs_roots(self):
        """Gets the vcs_roots of this Project.  # noqa: E501


        :return: The vcs_roots of this Project.  # noqa: E501
        :rtype: VcsRoots
        """
        return self._vcs_roots

    @vcs_roots.setter
    def vcs_roots(self, vcs_roots):
        """Sets the vcs_roots of this Project.


        :param vcs_roots: The vcs_roots of this Project.  # noqa: E501
        :type: VcsRoots
        """

        self._vcs_roots = vcs_roots

    @property
    def project_features(self):
        """Gets the project_features of this Project.  # noqa: E501


        :return: The project_features of this Project.  # noqa: E501
        :rtype: ProjectFeatures
        """
        return self._project_features

    @project_features.setter
    def project_features(self, project_features):
        """Sets the project_features of this Project.


        :param project_features: The project_features of this Project.  # noqa: E501
        :type: ProjectFeatures
        """

        self._project_features = project_features

    @property
    def projects(self):
        """Gets the projects of this Project.  # noqa: E501


        :return: The projects of this Project.  # noqa: E501
        :rtype: Projects
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this Project.


        :param projects: The projects of this Project.  # noqa: E501
        :type: Projects
        """

        self._projects = projects

    @property
    def cloud_profiles(self):
        """Gets the cloud_profiles of this Project.  # noqa: E501


        :return: The cloud_profiles of this Project.  # noqa: E501
        :rtype: CloudProfiles
        """
        return self._cloud_profiles

    @cloud_profiles.setter
    def cloud_profiles(self, cloud_profiles):
        """Sets the cloud_profiles of this Project.


        :param cloud_profiles: The cloud_profiles of this Project.  # noqa: E501
        :type: CloudProfiles
        """

        self._cloud_profiles = cloud_profiles

    @property
    def ancestor_projects(self):
        """Gets the ancestor_projects of this Project.  # noqa: E501


        :return: The ancestor_projects of this Project.  # noqa: E501
        :rtype: Projects
        """
        return self._ancestor_projects

    @ancestor_projects.setter
    def ancestor_projects(self, ancestor_projects):
        """Sets the ancestor_projects of this Project.


        :param ancestor_projects: The ancestor_projects of this Project.  # noqa: E501
        :type: Projects
        """

        self._ancestor_projects = ancestor_projects

    @property
    def locator(self):
        """Gets the locator of this Project.  # noqa: E501


        :return: The locator of this Project.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this Project.


        :param locator: The locator of this Project.  # noqa: E501
        :type: str
        """

        self._locator = locator
