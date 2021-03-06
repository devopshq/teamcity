# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.vcs_root_entry import VcsRootEntry  # noqa: F401,E501


class VcsRootEntries(TeamCityObject):
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
        'vcs_root_entry': 'list[VcsRootEntry]'
    }

    attribute_map = {
        'count': 'count',
        'vcs_root_entry': 'vcs-root-entry'
    }

    def __init__(self, count=None, vcs_root_entry=None, teamcity=None):  # noqa: E501
        """VcsRootEntries - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._vcs_root_entry = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if vcs_root_entry is not None:
            self.vcs_root_entry = vcs_root_entry
        super(VcsRootEntries, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this VcsRootEntries.  # noqa: E501


        :return: The count of this VcsRootEntries.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this VcsRootEntries.


        :param count: The count of this VcsRootEntries.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def vcs_root_entry(self):
        """Gets the vcs_root_entry of this VcsRootEntries.  # noqa: E501


        :return: The vcs_root_entry of this VcsRootEntries.  # noqa: E501
        :rtype: list[VcsRootEntry]
        """
        return self._vcs_root_entry

    @vcs_root_entry.setter
    def vcs_root_entry(self, vcs_root_entry):
        """Sets the vcs_root_entry of this VcsRootEntries.


        :param vcs_root_entry: The vcs_root_entry of this VcsRootEntries.  # noqa: E501
        :type: list[VcsRootEntry]
        """

        self._vcs_root_entry = vcs_root_entry
