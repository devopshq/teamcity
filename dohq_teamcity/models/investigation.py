# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.comment import Comment  # noqa: F401,E501
# from dohq_teamcity.models.problem_scope import ProblemScope  # noqa: F401,E501
# from dohq_teamcity.models.problem_target import ProblemTarget  # noqa: F401,E501
# from dohq_teamcity.models.resolution import Resolution  # noqa: F401,E501
# from dohq_teamcity.models.user import User  # noqa: F401,E501


class Investigation(TeamCityObject):
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
        'state': 'str',
        'href': 'str',
        'assignee': 'User',
        'assignment': 'Comment',
        'scope': 'ProblemScope',
        'target': 'ProblemTarget',
        'resolution': 'Resolution',
        'responsible': 'User'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'href': 'href',
        'assignee': 'assignee',
        'assignment': 'assignment',
        'scope': 'scope',
        'target': 'target',
        'resolution': 'resolution',
        'responsible': 'responsible'
    }

    def __init__(self, id=None, state=None, href=None, assignee=None, assignment=None, scope=None, target=None, resolution=None, responsible=None, teamcity=None):  # noqa: E501
        """Investigation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._state = None
        self._href = None
        self._assignee = None
        self._assignment = None
        self._scope = None
        self._target = None
        self._resolution = None
        self._responsible = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if href is not None:
            self.href = href
        if assignee is not None:
            self.assignee = assignee
        if assignment is not None:
            self.assignment = assignment
        if scope is not None:
            self.scope = scope
        if target is not None:
            self.target = target
        if resolution is not None:
            self.resolution = resolution
        if responsible is not None:
            self.responsible = responsible
        super(Investigation, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this Investigation.  # noqa: E501


        :return: The id of this Investigation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Investigation.


        :param id: The id of this Investigation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this Investigation.  # noqa: E501


        :return: The state of this Investigation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Investigation.


        :param state: The state of this Investigation.  # noqa: E501
        :type: str
        """
        allowed_values = ["TAKEN", "FIXED", "GIVEN_UP", "NONE"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def href(self):
        """Gets the href of this Investigation.  # noqa: E501


        :return: The href of this Investigation.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Investigation.


        :param href: The href of this Investigation.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def assignee(self):
        """Gets the assignee of this Investigation.  # noqa: E501


        :return: The assignee of this Investigation.  # noqa: E501
        :rtype: User
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this Investigation.


        :param assignee: The assignee of this Investigation.  # noqa: E501
        :type: User
        """

        self._assignee = assignee

    @property
    def assignment(self):
        """Gets the assignment of this Investigation.  # noqa: E501


        :return: The assignment of this Investigation.  # noqa: E501
        :rtype: Comment
        """
        return self._assignment

    @assignment.setter
    def assignment(self, assignment):
        """Sets the assignment of this Investigation.


        :param assignment: The assignment of this Investigation.  # noqa: E501
        :type: Comment
        """

        self._assignment = assignment

    @property
    def scope(self):
        """Gets the scope of this Investigation.  # noqa: E501


        :return: The scope of this Investigation.  # noqa: E501
        :rtype: ProblemScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Investigation.


        :param scope: The scope of this Investigation.  # noqa: E501
        :type: ProblemScope
        """

        self._scope = scope

    @property
    def target(self):
        """Gets the target of this Investigation.  # noqa: E501


        :return: The target of this Investigation.  # noqa: E501
        :rtype: ProblemTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Investigation.


        :param target: The target of this Investigation.  # noqa: E501
        :type: ProblemTarget
        """

        self._target = target

    @property
    def resolution(self):
        """Gets the resolution of this Investigation.  # noqa: E501


        :return: The resolution of this Investigation.  # noqa: E501
        :rtype: Resolution
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this Investigation.


        :param resolution: The resolution of this Investigation.  # noqa: E501
        :type: Resolution
        """

        self._resolution = resolution

    @property
    def responsible(self):
        """Gets the responsible of this Investigation.  # noqa: E501


        :return: The responsible of this Investigation.  # noqa: E501
        :rtype: User
        """
        return self._responsible

    @responsible.setter
    def responsible(self, responsible):
        """Sets the responsible of this Investigation.


        :param responsible: The responsible of this Investigation.  # noqa: E501
        :type: User
        """

        self._responsible = responsible
