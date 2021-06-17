# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1210
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class IfRequestHeaderExpression(object):
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
        'header_name': 'str',
        'operator': 'TextOperator',
        'value': 'str'
    }

    attribute_map = {
        'header_name': 'headerName',
        'operator': 'operator',
        'value': 'value'
    }

    required_map = {
        'header_name': 'required',
        'operator': 'required',
        'value': 'optional'
    }

    def __init__(self, header_name=None, operator=None, value=None):  # noqa: E501
        """
        IfRequestHeaderExpression - a model defined in OpenAPI

        :param header_name:  (required)
        :type header_name: str
        :param operator:  (required)
        :type operator: finbourne_access.TextOperator
        :param value: 
        :type value: str

        """  # noqa: E501

        self._header_name = None
        self._operator = None
        self._value = None
        self.discriminator = None

        self.header_name = header_name
        self.operator = operator
        self.value = value

    @property
    def header_name(self):
        """Gets the header_name of this IfRequestHeaderExpression.  # noqa: E501


        :return: The header_name of this IfRequestHeaderExpression.  # noqa: E501
        :rtype: str
        """
        return self._header_name

    @header_name.setter
    def header_name(self, header_name):
        """Sets the header_name of this IfRequestHeaderExpression.


        :param header_name: The header_name of this IfRequestHeaderExpression.  # noqa: E501
        :type: str
        """
        if header_name is None:
            raise ValueError("Invalid value for `header_name`, must not be `None`")  # noqa: E501
        if header_name is not None and len(header_name) > 1024:
            raise ValueError("Invalid value for `header_name`, length must be less than or equal to `1024`")  # noqa: E501
        if header_name is not None and len(header_name) < 1:
            raise ValueError("Invalid value for `header_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._header_name = header_name

    @property
    def operator(self):
        """Gets the operator of this IfRequestHeaderExpression.  # noqa: E501


        :return: The operator of this IfRequestHeaderExpression.  # noqa: E501
        :rtype: TextOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this IfRequestHeaderExpression.


        :param operator: The operator of this IfRequestHeaderExpression.  # noqa: E501
        :type: TextOperator
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this IfRequestHeaderExpression.  # noqa: E501


        :return: The value of this IfRequestHeaderExpression.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IfRequestHeaderExpression.


        :param value: The value of this IfRequestHeaderExpression.  # noqa: E501
        :type: str
        """
        if value is not None and len(value) > 4096:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `4096`")  # noqa: E501
        if value is not None and len(value) < 0:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `0`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, IfRequestHeaderExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
