# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.agents import Agents  # noqa: F401,E501
# from dohq_teamcity.models.project import Project  # noqa: F401,E501
# from dohq_teamcity.models.projects import Projects  # noqa: F401,E501


class AgentPool(TeamCityObject):
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
        'id': 'int',
        'name': 'str',
        'href': 'str',
        'max_agents': 'int',
        'owner_project': 'Project',
        'projects': 'Projects',
        'agents': 'Agents',
        'locator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'href': 'href',
        'max_agents': 'maxAgents',
        'owner_project': 'ownerProject',
        'projects': 'projects',
        'agents': 'agents',
        'locator': 'locator'
    }

    def __init__(self, id=None, name=None, href=None, max_agents=None, owner_project=None, projects=None, agents=None, locator=None, teamcity=None):  # noqa: E501
        """AgentPool - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._href = None
        self._max_agents = None
        self._owner_project = None
        self._projects = None
        self._agents = None
        self._locator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if href is not None:
            self.href = href
        if max_agents is not None:
            self.max_agents = max_agents
        if owner_project is not None:
            self.owner_project = owner_project
        if projects is not None:
            self.projects = projects
        if agents is not None:
            self.agents = agents
        if locator is not None:
            self.locator = locator
        super(AgentPool, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this AgentPool.  # noqa: E501


        :return: The id of this AgentPool.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgentPool.


        :param id: The id of this AgentPool.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AgentPool.  # noqa: E501


        :return: The name of this AgentPool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgentPool.


        :param name: The name of this AgentPool.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def href(self):
        """Gets the href of this AgentPool.  # noqa: E501


        :return: The href of this AgentPool.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AgentPool.


        :param href: The href of this AgentPool.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def max_agents(self):
        """Gets the max_agents of this AgentPool.  # noqa: E501


        :return: The max_agents of this AgentPool.  # noqa: E501
        :rtype: int
        """
        return self._max_agents

    @max_agents.setter
    def max_agents(self, max_agents):
        """Sets the max_agents of this AgentPool.


        :param max_agents: The max_agents of this AgentPool.  # noqa: E501
        :type: int
        """

        self._max_agents = max_agents

    @property
    def owner_project(self):
        """Gets the owner_project of this AgentPool.  # noqa: E501


        :return: The owner_project of this AgentPool.  # noqa: E501
        :rtype: Project
        """
        return self._owner_project

    @owner_project.setter
    def owner_project(self, owner_project):
        """Sets the owner_project of this AgentPool.


        :param owner_project: The owner_project of this AgentPool.  # noqa: E501
        :type: Project
        """

        self._owner_project = owner_project

    @property
    def projects(self):
        """Gets the projects of this AgentPool.  # noqa: E501


        :return: The projects of this AgentPool.  # noqa: E501
        :rtype: Projects
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this AgentPool.


        :param projects: The projects of this AgentPool.  # noqa: E501
        :type: Projects
        """

        self._projects = projects

    @property
    def agents(self):
        """Gets the agents of this AgentPool.  # noqa: E501


        :return: The agents of this AgentPool.  # noqa: E501
        :rtype: Agents
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this AgentPool.


        :param agents: The agents of this AgentPool.  # noqa: E501
        :type: Agents
        """

        self._agents = agents

    @property
    def locator(self):
        """Gets the locator of this AgentPool.  # noqa: E501


        :return: The locator of this AgentPool.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this AgentPool.


        :param locator: The locator of this AgentPool.  # noqa: E501
        :type: str
        """

        self._locator = locator
