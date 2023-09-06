# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.typed_value import TypedValue  # noqa: F401,E501


class TestRunMetadata(TeamCityObject):
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
        'typed_values': 'list[TypedValue]'
    }

    attribute_map = {
        'count': 'count',
        'typed_values': 'typedValues'
    }

    def __init__(self, count=None, typed_values=None, teamcity=None):  # noqa: E501
        """TestRunMetadata - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._typed_values = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if typed_values is not None:
            self.typed_values = typed_values
        super(TestRunMetadata, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this TestRunMetadata.  # noqa: E501


        :return: The count of this TestRunMetadata.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TestRunMetadata.


        :param count: The count of this TestRunMetadata.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def typed_values(self):
        """Gets the typed_values of this TestRunMetadata.  # noqa: E501


        :return: The typed_values of this TestRunMetadata.  # noqa: E501
        :rtype: list[TypedValue]
        """
        return self._typed_values

    @typed_values.setter
    def typed_values(self, typed_values):
        """Sets the typed_values of this TestRunMetadata.


        :param typed_values: The typed_values of this TestRunMetadata.  # noqa: E501
        :type: list[TypedValue]
        """

        self._typed_values = typed_values
