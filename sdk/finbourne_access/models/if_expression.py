# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1326
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class IfExpression(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'if_request_header_expression': 'IfRequestHeaderExpression',
        'if_identity_claim_expression': 'IfIdentityClaimExpression',
        'if_identity_scope_expression': 'IfIdentityScopeExpression'
    }

    attribute_map = {
        'if_request_header_expression': 'ifRequestHeaderExpression',
        'if_identity_claim_expression': 'ifIdentityClaimExpression',
        'if_identity_scope_expression': 'ifIdentityScopeExpression'
    }

    required_map = {
        'if_request_header_expression': 'optional',
        'if_identity_claim_expression': 'optional',
        'if_identity_scope_expression': 'optional'
    }

    def __init__(self, if_request_header_expression=None, if_identity_claim_expression=None, if_identity_scope_expression=None):  # noqa: E501
        """
        IfExpression - a model defined in OpenAPI

        :param if_request_header_expression: 
        :type if_request_header_expression: finbourne_access.IfRequestHeaderExpression
        :param if_identity_claim_expression: 
        :type if_identity_claim_expression: finbourne_access.IfIdentityClaimExpression
        :param if_identity_scope_expression: 
        :type if_identity_scope_expression: finbourne_access.IfIdentityScopeExpression

        """  # noqa: E501

        self._if_request_header_expression = None
        self._if_identity_claim_expression = None
        self._if_identity_scope_expression = None
        self.discriminator = None

        if if_request_header_expression is not None:
            self.if_request_header_expression = if_request_header_expression
        if if_identity_claim_expression is not None:
            self.if_identity_claim_expression = if_identity_claim_expression
        if if_identity_scope_expression is not None:
            self.if_identity_scope_expression = if_identity_scope_expression

    @property
    def if_request_header_expression(self):
        """Gets the if_request_header_expression of this IfExpression.  # noqa: E501


        :return: The if_request_header_expression of this IfExpression.  # noqa: E501
        :rtype: IfRequestHeaderExpression
        """
        return self._if_request_header_expression

    @if_request_header_expression.setter
    def if_request_header_expression(self, if_request_header_expression):
        """Sets the if_request_header_expression of this IfExpression.


        :param if_request_header_expression: The if_request_header_expression of this IfExpression.  # noqa: E501
        :type: IfRequestHeaderExpression
        """

        self._if_request_header_expression = if_request_header_expression

    @property
    def if_identity_claim_expression(self):
        """Gets the if_identity_claim_expression of this IfExpression.  # noqa: E501


        :return: The if_identity_claim_expression of this IfExpression.  # noqa: E501
        :rtype: IfIdentityClaimExpression
        """
        return self._if_identity_claim_expression

    @if_identity_claim_expression.setter
    def if_identity_claim_expression(self, if_identity_claim_expression):
        """Sets the if_identity_claim_expression of this IfExpression.


        :param if_identity_claim_expression: The if_identity_claim_expression of this IfExpression.  # noqa: E501
        :type: IfIdentityClaimExpression
        """

        self._if_identity_claim_expression = if_identity_claim_expression

    @property
    def if_identity_scope_expression(self):
        """Gets the if_identity_scope_expression of this IfExpression.  # noqa: E501


        :return: The if_identity_scope_expression of this IfExpression.  # noqa: E501
        :rtype: IfIdentityScopeExpression
        """
        return self._if_identity_scope_expression

    @if_identity_scope_expression.setter
    def if_identity_scope_expression(self, if_identity_scope_expression):
        """Sets the if_identity_scope_expression of this IfExpression.


        :param if_identity_scope_expression: The if_identity_scope_expression of this IfExpression.  # noqa: E501
        :type: IfIdentityScopeExpression
        """

        self._if_identity_scope_expression = if_identity_scope_expression

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IfExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
