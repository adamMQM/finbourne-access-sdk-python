# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1172
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class EntitlementMetadata(object):
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
        'provider': 'str',
        'value': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'value': 'value'
    }

    required_map = {
        'provider': 'optional',
        'value': 'optional'
    }

    def __init__(self, provider=None, value=None):  # noqa: E501
        """
        EntitlementMetadata - a model defined in OpenAPI

        :param provider: 
        :type provider: str
        :param value: 
        :type value: str

        """  # noqa: E501

        self._provider = None
        self._value = None
        self.discriminator = None

        self.provider = provider
        self.value = value

    @property
    def provider(self):
        """Gets the provider of this EntitlementMetadata.  # noqa: E501


        :return: The provider of this EntitlementMetadata.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this EntitlementMetadata.


        :param provider: The provider of this EntitlementMetadata.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def value(self):
        """Gets the value of this EntitlementMetadata.  # noqa: E501


        :return: The value of this EntitlementMetadata.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EntitlementMetadata.


        :param value: The value of this EntitlementMetadata.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, EntitlementMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
