# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1320
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class MatchAllSelectorDefinition(object):
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
        'actions': 'list[ActionId]',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'name': 'name',
        'description': 'description'
    }

    required_map = {
        'actions': 'required',
        'name': 'optional',
        'description': 'optional'
    }

    def __init__(self, actions=None, name=None, description=None):  # noqa: E501
        """
        MatchAllSelectorDefinition - a model defined in OpenAPI

        :param actions:  (required)
        :type actions: list[finbourne_access.ActionId]
        :param name: 
        :type name: str
        :param description: 
        :type description: str

        """  # noqa: E501

        self._actions = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.actions = actions
        self.name = name
        self.description = description

    @property
    def actions(self):
        """Gets the actions of this MatchAllSelectorDefinition.  # noqa: E501


        :return: The actions of this MatchAllSelectorDefinition.  # noqa: E501
        :rtype: list[ActionId]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this MatchAllSelectorDefinition.


        :param actions: The actions of this MatchAllSelectorDefinition.  # noqa: E501
        :type: list[ActionId]
        """
        if actions is None:
            raise ValueError("Invalid value for `actions`, must not be `None`")  # noqa: E501

        self._actions = actions

    @property
    def name(self):
        """Gets the name of this MatchAllSelectorDefinition.  # noqa: E501


        :return: The name of this MatchAllSelectorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MatchAllSelectorDefinition.


        :param name: The name of this MatchAllSelectorDefinition.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this MatchAllSelectorDefinition.  # noqa: E501


        :return: The description of this MatchAllSelectorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MatchAllSelectorDefinition.


        :param description: The description of this MatchAllSelectorDefinition.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

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
        if not isinstance(other, MatchAllSelectorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
