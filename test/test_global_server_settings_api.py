# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2018.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dohq_teamcity
from dohq_teamcity.api.global_server_settings_api import GlobalServerSettingsApi  # noqa: E501
from dohq_teamcity.rest import ApiException


class TestGlobalServerSettingsApi(unittest.TestCase):
    """GlobalServerSettingsApi unit test stubs"""

    def setUp(self):
        self.api = dohq_teamcity.api.global_server_settings_api.GlobalServerSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_global_settings(self):
        """Test case for get_global_settings

        Get global settings.  # noqa: E501
        """
        pass

    def test_set_global_settings(self):
        """Test case for set_global_settings

        Set global settings.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
