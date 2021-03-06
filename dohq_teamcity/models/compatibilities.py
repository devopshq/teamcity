# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.compatibility import Compatibility  # noqa: F401,E501


class Compatibilities(TeamCityObject):
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
        'count': 'int',
        'compatibility': 'list[Compatibility]'
    }

    attribute_map = {
        'count': 'count',
        'compatibility': 'compatibility'
    }

    def __init__(self, count=None, compatibility=None, teamcity=None):  # noqa: E501
        """Compatibilities - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._compatibility = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if compatibility is not None:
            self.compatibility = compatibility
        super(Compatibilities, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this Compatibilities.  # noqa: E501


        :return: The count of this Compatibilities.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Compatibilities.


        :param count: The count of this Compatibilities.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def compatibility(self):
        """Gets the compatibility of this Compatibilities.  # noqa: E501


        :return: The compatibility of this Compatibilities.  # noqa: E501
        :rtype: list[Compatibility]
        """
        return self._compatibility

    @compatibility.setter
    def compatibility(self, compatibility):
        """Sets the compatibility of this Compatibilities.


        :param compatibility: The compatibility of this Compatibilities.  # noqa: E501
        :type: list[Compatibility]
        """

        self._compatibility = compatibility
