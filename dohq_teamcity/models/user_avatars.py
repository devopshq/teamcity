# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class UserAvatars(TeamCityObject):
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
        'url_to_size20': 'str',
        'url_to_size28': 'str',
        'url_to_size32': 'str',
        'url_to_size40': 'str',
        'url_to_size56': 'str',
        'url_to_size64': 'str',
        'url_to_size80': 'str'
    }

    attribute_map = {
        'url_to_size20': 'urlToSize20',
        'url_to_size28': 'urlToSize28',
        'url_to_size32': 'urlToSize32',
        'url_to_size40': 'urlToSize40',
        'url_to_size56': 'urlToSize56',
        'url_to_size64': 'urlToSize64',
        'url_to_size80': 'urlToSize80'
    }

    def __init__(self, url_to_size20=None, url_to_size28=None, url_to_size32=None, url_to_size40=None, url_to_size56=None, url_to_size64=None, url_to_size80=None, teamcity=None):  # noqa: E501
        """UserAvatars - a model defined in Swagger"""  # noqa: E501

        self._url_to_size20 = None
        self._url_to_size28 = None
        self._url_to_size32 = None
        self._url_to_size40 = None
        self._url_to_size56 = None
        self._url_to_size64 = None
        self._url_to_size80 = None
        self.discriminator = None

        if url_to_size20 is not None:
            self.url_to_size20 = url_to_size20
        if url_to_size28 is not None:
            self.url_to_size28 = url_to_size28
        if url_to_size32 is not None:
            self.url_to_size32 = url_to_size32
        if url_to_size40 is not None:
            self.url_to_size40 = url_to_size40
        if url_to_size56 is not None:
            self.url_to_size56 = url_to_size56
        if url_to_size64 is not None:
            self.url_to_size64 = url_to_size64
        if url_to_size80 is not None:
            self.url_to_size80 = url_to_size80
        super(UserAvatars, self).__init__(teamcity=teamcity)

    @property
    def url_to_size20(self):
        """Gets the url_to_size20 of this UserAvatars.  # noqa: E501


        :return: The url_to_size20 of this UserAvatars.  # noqa: E501
        :rtype: str
        """
        return self._url_to_size20

    @url_to_size20.setter
    def url_to_size20(self, url_to_size20):
        """Sets the url_to_size20 of this UserAvatars.


        :param url_to_size20: The url_to_size20 of this UserAvatars.  # noqa: E501
        :type: str
        """

        self._url_to_size20 = url_to_size20

    @property
    def url_to_size28(self):
        """Gets the url_to_size28 of this UserAvatars.  # noqa: E501


        :return: The url_to_size28 of this UserAvatars.  # noqa: E501
        :rtype: str
        """
        return self._url_to_size28

    @url_to_size28.setter
    def url_to_size28(self, url_to_size28):
        """Sets the url_to_size28 of this UserAvatars.


        :param url_to_size28: The url_to_size28 of this UserAvatars.  # noqa: E501
        :type: str
        """

        self._url_to_size28 = url_to_size28

    @property
    def url_to_size32(self):
        """Gets the url_to_size32 of this UserAvatars.  # noqa: E501


        :return: The url_to_size32 of this UserAvatars.  # noqa: E501
        :rtype: str
        """
        return self._url_to_size32

    @url_to_size32.setter
    def url_to_size32(self, url_to_size32):
        """Sets the url_to_size32 of this UserAvatars.


        :param url_to_size32: The url_to_size32 of this UserAvatars.  # noqa: E501
        :type: str
        """

        self._url_to_size32 = url_to_size32

    @property
    def url_to_size40(self):
        """Gets the url_to_size40 of this UserAvatars.  # noqa: E501


        :return: The url_to_size40 of this UserAvatars.  # noqa: E501
        :rtype: str
        """
        return self._url_to_size40

    @url_to_size40.setter
    def url_to_size40(self, url_to_size40):
        """Sets the url_to_size40 of this UserAvatars.


        :param url_to_size40: The url_to_size40 of this UserAvatars.  # noqa: E501
        :type: str
        """

        self._url_to_size40 = url_to_size40

    @property
    def url_to_size56(self):
        """Gets the url_to_size56 of this UserAvatars.  # noqa: E501


        :return: The url_to_size56 of this UserAvatars.  # noqa: E501
        :rtype: str
        """
        return self._url_to_size56

    @url_to_size56.setter
    def url_to_size56(self, url_to_size56):
        """Sets the url_to_size56 of this UserAvatars.


        :param url_to_size56: The url_to_size56 of this UserAvatars.  # noqa: E501
        :type: str
        """

        self._url_to_size56 = url_to_size56

    @property
    def url_to_size64(self):
        """Gets the url_to_size64 of this UserAvatars.  # noqa: E501


        :return: The url_to_size64 of this UserAvatars.  # noqa: E501
        :rtype: str
        """
        return self._url_to_size64

    @url_to_size64.setter
    def url_to_size64(self, url_to_size64):
        """Sets the url_to_size64 of this UserAvatars.


        :param url_to_size64: The url_to_size64 of this UserAvatars.  # noqa: E501
        :type: str
        """

        self._url_to_size64 = url_to_size64

    @property
    def url_to_size80(self):
        """Gets the url_to_size80 of this UserAvatars.  # noqa: E501


        :return: The url_to_size80 of this UserAvatars.  # noqa: E501
        :rtype: str
        """
        return self._url_to_size80

    @url_to_size80.setter
    def url_to_size80(self, url_to_size80):
        """Sets the url_to_size80 of this UserAvatars.


        :param url_to_size80: The url_to_size80 of this UserAvatars.  # noqa: E501
        :type: str
        """

        self._url_to_size80 = url_to_size80
