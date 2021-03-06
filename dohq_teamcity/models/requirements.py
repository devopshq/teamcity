# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class Requirements(TeamCityObject):
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
        'description': 'str'
    }

    attribute_map = {
        'description': 'description'
    }

    def __init__(self, description=None, teamcity=None):  # noqa: E501
        """Requirements - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self.discriminator = None

        if description is not None:
            self.description = description
        super(Requirements, self).__init__(teamcity=teamcity)

    @property
    def description(self):
        """Gets the description of this Requirements.  # noqa: E501


        :return: The description of this Requirements.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Requirements.


        :param description: The description of this Requirements.  # noqa: E501
        :type: str
        """

        self._description = description
