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
from dohq_teamcity.api.mute_api import MuteApi  # noqa: E501
from dohq_teamcity.rest import ApiException


class TestMuteApi(unittest.TestCase):
    """MuteApi unit test stubs"""

    def setUp(self):
        self.api = dohq_teamcity.api.mute_api.MuteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_instance(self):
        """Test case for create_instance

        """
        pass

    def test_create_instances(self):
        """Test case for create_instances

        """
        pass

    def test_delete_instance(self):
        """Test case for delete_instance

        """
        pass

    def test_get_mutes(self):
        """Test case for get_mutes

        """
        pass

    def test_serve_instance(self):
        """Test case for serve_instance

        """
        pass


if __name__ == '__main__':
    unittest.main()
