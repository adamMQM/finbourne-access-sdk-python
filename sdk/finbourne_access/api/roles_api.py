# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.815
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from finbourne_access.api_client import ApiClient
from finbourne_access.exceptions import (
    ApiTypeError,
    ApiValueError
)


class RolesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_role(self, role_creation_request, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Create Role  # noqa: E501

        Creates a Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role(role_creation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param RoleCreationRequest role_creation_request: The definition of the Role (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RoleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_role_with_http_info(role_creation_request, **kwargs)  # noqa: E501

    def create_role_with_http_info(self, role_creation_request, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Create Role  # noqa: E501

        Creates a Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_with_http_info(role_creation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param RoleCreationRequest role_creation_request: The definition of the Role (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RoleResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['role_creation_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_role" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'role_creation_request' is set
        if ('role_creation_request' not in local_var_params or
                local_var_params['role_creation_request'] is None):
            raise ApiValueError("Missing the required parameter `role_creation_request` when calling `create_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'role_creation_request' in local_var_params:
            body_params = local_var_params['role_creation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.815'

        return self.api_client.call_api(
            '/api/roles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RoleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_role(self, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Delete Role  # noqa: E501

        Deletes an identified Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: The code of the Role (required)
        :param str scope: >Optional. Will use default scope if not supplied. The scope of the Role
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_role_with_http_info(code, **kwargs)  # noqa: E501

    def delete_role_with_http_info(self, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Delete Role  # noqa: E501

        Deletes an identified Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: The code of the Role (required)
        :param str scope: >Optional. Will use default scope if not supplied. The scope of the Role
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['code', 'scope']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_role" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `delete_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.815'

        return self.api_client.call_api(
            '/api/roles/{code}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_role(self, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Get Role  # noqa: E501

        Gets an identified Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: The code of the Role (required)
        :param datetime as_at: Optional. The AsAt date time of the data
        :param str scope: Optional. Will use default scope if not supplied. The scope of the Role
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RoleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_role_with_http_info(code, **kwargs)  # noqa: E501

    def get_role_with_http_info(self, code, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Get Role  # noqa: E501

        Gets an identified Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: The code of the Role (required)
        :param datetime as_at: Optional. The AsAt date time of the data
        :param str scope: Optional. Will use default scope if not supplied. The scope of the Role
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RoleResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['code', 'as_at', 'scope']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `get_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.815'

        return self.api_client.call_api(
            '/api/roles/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RoleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_roles(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] List Roles  # noqa: E501

        Gets all Roles in a scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_roles(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: Optional. Will use all scopes if not supplied. The requested scope
        :param datetime as_at: Optional. The AsAt date time of the data
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param str filter: Optional. Expression to filter the result set
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[RoleResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_roles_with_http_info(**kwargs)  # noqa: E501

    def list_roles_with_http_info(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] List Roles  # noqa: E501

        Gets all Roles in a scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_roles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: Optional. Will use all scopes if not supplied. The requested scope
        :param datetime as_at: Optional. The AsAt date time of the data
        :param list[str] sort_by: Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName
        :param int start: Optional. When paginating, skip this number of results
        :param int limit: Optional. When paginating, limit the number of returned results to this many.
        :param str filter: Optional. Expression to filter the result set
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[RoleResponse], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'as_at', 'sort_by', 'start', 'limit', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_roles" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))  # noqa: E501
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'sort_by' in local_var_params:
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
            collection_formats['sortBy'] = 'multi'  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.815'

        return self.api_client.call_api(
            '/api/roles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RoleResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_role(self, code, role_update_request, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Update Role  # noqa: E501

        Updates a Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_role(code, role_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: The code of the Role (required)
        :param RoleUpdateRequest role_update_request: The updated definition of the Role (required)
        :param str scope: >Optional. Will use default scope if not supplied. The scope of the Role
        :param str before_scope: Optional. The scope of the Role. Will use default scope if not supplied.
        :param str before_code: Optional. The code of the Role
        :param str after_scope: Optional. The scope of the Role. Will use default scope if not supplied.
        :param str after_code: Optional. The code of the Role
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RoleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_role_with_http_info(code, role_update_request, **kwargs)  # noqa: E501

    def update_role_with_http_info(self, code, role_update_request, **kwargs):  # noqa: E501
        """[EARLY ACCESS] Update Role  # noqa: E501

        Updates a Role  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_role_with_http_info(code, role_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str code: The code of the Role (required)
        :param RoleUpdateRequest role_update_request: The updated definition of the Role (required)
        :param str scope: >Optional. Will use default scope if not supplied. The scope of the Role
        :param str before_scope: Optional. The scope of the Role. Will use default scope if not supplied.
        :param str before_code: Optional. The code of the Role
        :param str after_scope: Optional. The scope of the Role. Will use default scope if not supplied.
        :param str after_code: Optional. The code of the Role
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RoleResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['code', 'role_update_request', 'scope', 'before_scope', 'before_code', 'after_scope', 'after_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_role" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `update_role`")  # noqa: E501
        # verify the required parameter 'role_update_request' is set
        if ('role_update_request' not in local_var_params or
                local_var_params['role_update_request'] is None):
            raise ApiValueError("Missing the required parameter `role_update_request` when calling `update_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))  # noqa: E501
        if 'before_scope' in local_var_params:
            query_params.append(('beforeScope', local_var_params['before_scope']))  # noqa: E501
        if 'before_code' in local_var_params:
            query_params.append(('beforeCode', local_var_params['before_code']))  # noqa: E501
        if 'after_scope' in local_var_params:
            query_params.append(('afterScope', local_var_params['after_scope']))  # noqa: E501
        if 'after_code' in local_var_params:
            query_params.append(('afterCode', local_var_params['after_code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'role_update_request' in local_var_params:
            body_params = local_var_params['role_update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.815'

        return self.api_client.call_api(
            '/api/roles/{code}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RoleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
