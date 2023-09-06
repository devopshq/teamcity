# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class Customizations(TeamCityObject):
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
        'parameters': 'dict(str, str)',
        'changes': 'dict(str, str)',
        'artifact_dependencies': 'dict(str, str)'
    }

    attribute_map = {
        'parameters': 'parameters',
        'changes': 'changes',
        'artifact_dependencies': 'artifactDependencies'
    }

    def __init__(self, parameters=None, changes=None, artifact_dependencies=None, teamcity=None):  # noqa: E501
        """Customizations - a model defined in Swagger"""  # noqa: E501

        self._parameters = None
        self._changes = None
        self._artifact_dependencies = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        if changes is not None:
            self.changes = changes
        if artifact_dependencies is not None:
            self.artifact_dependencies = artifact_dependencies
        super(Customizations, self).__init__(teamcity=teamcity)

    @property
    def parameters(self):
        """Gets the parameters of this Customizations.  # noqa: E501


        :return: The parameters of this Customizations.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Customizations.


        :param parameters: The parameters of this Customizations.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def changes(self):
        """Gets the changes of this Customizations.  # noqa: E501


        :return: The changes of this Customizations.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this Customizations.


        :param changes: The changes of this Customizations.  # noqa: E501
        :type: dict(str, str)
        """

        self._changes = changes

    @property
    def artifact_dependencies(self):
        """Gets the artifact_dependencies of this Customizations.  # noqa: E501


        :return: The artifact_dependencies of this Customizations.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._artifact_dependencies

    @artifact_dependencies.setter
    def artifact_dependencies(self, artifact_dependencies):
        """Sets the artifact_dependencies of this Customizations.


        :param artifact_dependencies: The artifact_dependencies of this Customizations.  # noqa: E501
        :type: dict(str, str)
        """

        self._artifact_dependencies = artifact_dependencies
