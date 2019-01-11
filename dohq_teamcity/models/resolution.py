# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class Resolution(TeamCityObject):
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
        'time': 'str',
        'type': 'str'
    }

    attribute_map = {
        'time': 'time',
        'type': 'type'
    }

    def __init__(self, time=None, type=None, teamcity=None):  # noqa: E501
        """Resolution - a model defined in Swagger"""  # noqa: E501

        self._time = None
        self._type = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if type is not None:
            self.type = type
        super(Resolution, self).__init__(teamcity=teamcity)

    @property
    def time(self):
        """Gets the time of this Resolution.  # noqa: E501


        :return: The time of this Resolution.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Resolution.


        :param time: The time of this Resolution.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def type(self):
        """Gets the type of this Resolution.  # noqa: E501


        :return: The type of this Resolution.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resolution.


        :param type: The type of this Resolution.  # noqa: E501
        :type: str
        """

        self._type = type
