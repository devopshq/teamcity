# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import
from dohq_teamcity.custom.base_model import TeamCityObject

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dohq_teamcity.models.plugin import Plugin  # noqa: F401,E501


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
    base_name = 'default'

    def __init__(self, api_client=None):
        self.api_client = api_client

    def serve_api_version(self, **kwargs):  # noqa: E501
        """serve_api_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serve_api_version(async_req=True)
        >>> result = thread.get()

        :param async_req: bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__serve_api_version_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.__serve_api_version_with_http_info(**kwargs)  # noqa: E501
            return data

    def serve_build_field_short(self, project_locator, bt_locator, build_locator, field, **kwargs):  # noqa: E501
        """serve_build_field_short  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serve_build_field_short(project_locator, bt_locator, build_locator, field, async_req=True)
        >>> result = thread.get()

        :param async_req: bool
        :param str project_locator: (required)
        :param str bt_locator: (required)
        :param str build_locator: (required)
        :param str field: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__serve_build_field_short_with_http_info(project_locator, bt_locator, build_locator, field, **kwargs)  # noqa: E501
        else:
            (data) = self.__serve_build_field_short_with_http_info(project_locator, bt_locator, build_locator, field, **kwargs)  # noqa: E501
            return data

    def serve_plugin_info(self, **kwargs):  # noqa: E501
        """serve_plugin_info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serve_plugin_info(async_req=True)
        >>> result = thread.get()

        :param async_req: bool
        :param str fields:
        :return: Plugin
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__serve_plugin_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.__serve_plugin_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def serve_root(self, **kwargs):  # noqa: E501
        """serve_root  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serve_root(async_req=True)
        >>> result = thread.get()

        :param async_req: bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__serve_root_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.__serve_root_with_http_info(**kwargs)  # noqa: E501
            return data

    def serve_version(self, **kwargs):  # noqa: E501
        """serve_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serve_version(async_req=True)
        >>> result = thread.get()

        :param async_req: bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__serve_version_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.__serve_version_with_http_info(**kwargs)  # noqa: E501
            return data

    def __serve_api_version_with_http_info(self, **kwargs):  # noqa: E501
        """serve_api_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.__serve_api_version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serve_api_version" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/apiVersion', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def __serve_build_field_short_with_http_info(self, project_locator, bt_locator, build_locator, field, **kwargs):  # noqa: E501
        """serve_build_field_short  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.__serve_build_field_short_with_http_info(project_locator, bt_locator, build_locator, field, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_locator: (required)
        :param str bt_locator: (required)
        :param str build_locator: (required)
        :param str field: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_locator', 'bt_locator', 'build_locator', 'field']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serve_build_field_short" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_locator' is set
        if ('project_locator' not in params or
                params['project_locator'] is None):
            raise ValueError("Missing the required parameter `project_locator` when calling `serve_build_field_short`")  # noqa: E501
        # verify the required parameter 'bt_locator' is set
        if ('bt_locator' not in params or
                params['bt_locator'] is None):
            raise ValueError("Missing the required parameter `bt_locator` when calling `serve_build_field_short`")  # noqa: E501
        # verify the required parameter 'build_locator' is set
        if ('build_locator' not in params or
                params['build_locator'] is None):
            raise ValueError("Missing the required parameter `build_locator` when calling `serve_build_field_short`")  # noqa: E501
        # verify the required parameter 'field' is set
        if ('field' not in params or
                params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `serve_build_field_short`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_locator' in params:
            if isinstance(params['project_locator'], TeamCityObject):
                path_params['projectLocator'] = params['project_locator'].locator_id
            else:
                path_params['projectLocator'] = params['project_locator']  # noqa: E501
        if 'bt_locator' in params:
            if isinstance(params['bt_locator'], TeamCityObject):
                path_params['btLocator'] = params['bt_locator'].locator_id
            else:
                path_params['btLocator'] = params['bt_locator']  # noqa: E501
        if 'build_locator' in params:
            if isinstance(params['build_locator'], TeamCityObject):
                path_params['buildLocator'] = params['build_locator'].locator_id
            else:
                path_params['buildLocator'] = params['build_locator']  # noqa: E501
        if 'field' in params:
            if isinstance(params['field'], TeamCityObject):
                path_params['field'] = params['field'].locator_id
            else:
                path_params['field'] = params['field']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/{projectLocator}/{btLocator}/{buildLocator}/{field}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def __serve_plugin_info_with_http_info(self, **kwargs):  # noqa: E501
        """serve_plugin_info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.__serve_plugin_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields:
        :return: Plugin
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serve_plugin_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Plugin',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def __serve_root_with_http_info(self, **kwargs):  # noqa: E501
        """serve_root  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.__serve_root_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serve_root" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def __serve_version_with_http_info(self, **kwargs):  # noqa: E501
        """serve_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.__serve_version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serve_version" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/version', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
