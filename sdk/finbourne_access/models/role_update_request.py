# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1298
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class RoleUpdateRequest(object):
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
        'description': 'str',
        'resource': 'RoleResourceRequest',
        'when': 'WhenSpec'
    }

    attribute_map = {
        'description': 'description',
        'resource': 'resource',
        'when': 'when'
    }

    required_map = {
        'description': 'optional',
        'resource': 'required',
        'when': 'required'
    }

    def __init__(self, description=None, resource=None, when=None):  # noqa: E501
        """
        RoleUpdateRequest - a model defined in OpenAPI

        :param description: 
        :type description: str
        :param resource:  (required)
        :type resource: finbourne_access.RoleResourceRequest
        :param when:  (required)
        :type when: finbourne_access.WhenSpec

        """  # noqa: E501

        self._description = None
        self._resource = None
        self._when = None
        self.discriminator = None

        self.description = description
        self.resource = resource
        self.when = when

    @property
    def description(self):
        """Gets the description of this RoleUpdateRequest.  # noqa: E501


        :return: The description of this RoleUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleUpdateRequest.


        :param description: The description of this RoleUpdateRequest.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def resource(self):
        """Gets the resource of this RoleUpdateRequest.  # noqa: E501


        :return: The resource of this RoleUpdateRequest.  # noqa: E501
        :rtype: RoleResourceRequest
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this RoleUpdateRequest.


        :param resource: The resource of this RoleUpdateRequest.  # noqa: E501
        :type: RoleResourceRequest
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def when(self):
        """Gets the when of this RoleUpdateRequest.  # noqa: E501


        :return: The when of this RoleUpdateRequest.  # noqa: E501
        :rtype: WhenSpec
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this RoleUpdateRequest.


        :param when: The when of this RoleUpdateRequest.  # noqa: E501
        :type: WhenSpec
        """
        if when is None:
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501

        self._when = when

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
        if not isinstance(other, RoleUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
