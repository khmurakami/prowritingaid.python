# coding: utf-8

"""
    ProWritingAid API V2

    Official ProWritingAid API Version 2

    OpenAPI spec version: v2
    Contact: hello@prowritingaid.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class WordCloudApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get(self, task_id, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get(task_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str task_id: (required)
        :return: AsyncResponseWordCloudResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(task_id, **kwargs)
        else:
            (data) = self.get_with_http_info(task_id, **kwargs)
            return data

    def get_with_http_info(self, task_id, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_with_http_info(task_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str task_id: (required)
        :return: AsyncResponseWordCloudResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params) or (params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `get`")


        collection_formats = {}

        path_params = {}
        if 'task_id' in params:
            path_params['taskId'] = params['task_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/async/wordcloud/result/{taskId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AsyncResponseWordCloudResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post(self, requestp, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post(requestp, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WordCloudRequest requestp: (required)
        :return: AsyncResponseWordCloudResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_with_http_info(requestp, **kwargs)
        else:
            (data) = self.post_with_http_info(requestp, **kwargs)
            return data

    def post_with_http_info(self, requestp, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_with_http_info(requestp, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WordCloudRequest requestp: (required)
        :return: AsyncResponseWordCloudResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['requestp']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'requestp' is set
        if ('requestp' not in params) or (params['requestp'] is None):
            raise ValueError("Missing the required parameter `requestp` when calling `post`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'requestp' in params:
            body_params = params['requestp']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/api/async/wordcloud', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AsyncResponseWordCloudResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
