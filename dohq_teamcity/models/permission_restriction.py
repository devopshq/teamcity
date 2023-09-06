# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.permission import Permission  # noqa: F401,E501
# from dohq_teamcity.models.project import Project  # noqa: F401,E501


class PermissionRestriction(TeamCityObject):
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
        'is_global_scope': 'bool',
        'project': 'Project',
        'permission': 'Permission'
    }

    attribute_map = {
        'is_global_scope': 'isGlobalScope',
        'project': 'project',
        'permission': 'permission'
    }

    def __init__(self, is_global_scope=None, project=None, permission=None, teamcity=None):  # noqa: E501
        """PermissionRestriction - a model defined in Swagger"""  # noqa: E501

        self._is_global_scope = None
        self._project = None
        self._permission = None
        self.discriminator = None

        if is_global_scope is not None:
            self.is_global_scope = is_global_scope
        if project is not None:
            self.project = project
        if permission is not None:
            self.permission = permission
        super(PermissionRestriction, self).__init__(teamcity=teamcity)

    @property
    def is_global_scope(self):
        """Gets the is_global_scope of this PermissionRestriction.  # noqa: E501


        :return: The is_global_scope of this PermissionRestriction.  # noqa: E501
        :rtype: bool
        """
        return self._is_global_scope

    @is_global_scope.setter
    def is_global_scope(self, is_global_scope):
        """Sets the is_global_scope of this PermissionRestriction.


        :param is_global_scope: The is_global_scope of this PermissionRestriction.  # noqa: E501
        :type: bool
        """

        self._is_global_scope = is_global_scope

    @property
    def project(self):
        """Gets the project of this PermissionRestriction.  # noqa: E501


        :return: The project of this PermissionRestriction.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this PermissionRestriction.


        :param project: The project of this PermissionRestriction.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def permission(self):
        """Gets the permission of this PermissionRestriction.  # noqa: E501


        :return: The permission of this PermissionRestriction.  # noqa: E501
        :rtype: Permission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this PermissionRestriction.


        :param permission: The permission of this PermissionRestriction.  # noqa: E501
        :type: Permission
        """

        self._permission = permission
