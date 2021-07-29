# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1290
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class SelectorDefinition(object):
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
        'metadata_selector_definition': 'MetadataSelectorDefinition',
        'id_selector_definition': 'IdSelectorDefinition',
        'match_all_selector_definition': 'MatchAllSelectorDefinition',
        'policy_selector_definition': 'PolicySelectorDefinition'
    }

    attribute_map = {
        'metadata_selector_definition': 'metadataSelectorDefinition',
        'id_selector_definition': 'idSelectorDefinition',
        'match_all_selector_definition': 'matchAllSelectorDefinition',
        'policy_selector_definition': 'policySelectorDefinition'
    }

    required_map = {
        'metadata_selector_definition': 'optional',
        'id_selector_definition': 'optional',
        'match_all_selector_definition': 'optional',
        'policy_selector_definition': 'optional'
    }

    def __init__(self, metadata_selector_definition=None, id_selector_definition=None, match_all_selector_definition=None, policy_selector_definition=None):  # noqa: E501
        """
        SelectorDefinition - a model defined in OpenAPI

        :param metadata_selector_definition: 
        :type metadata_selector_definition: finbourne_access.MetadataSelectorDefinition
        :param id_selector_definition: 
        :type id_selector_definition: finbourne_access.IdSelectorDefinition
        :param match_all_selector_definition: 
        :type match_all_selector_definition: finbourne_access.MatchAllSelectorDefinition
        :param policy_selector_definition: 
        :type policy_selector_definition: finbourne_access.PolicySelectorDefinition

        """  # noqa: E501

        self._metadata_selector_definition = None
        self._id_selector_definition = None
        self._match_all_selector_definition = None
        self._policy_selector_definition = None
        self.discriminator = None

        if metadata_selector_definition is not None:
            self.metadata_selector_definition = metadata_selector_definition
        if id_selector_definition is not None:
            self.id_selector_definition = id_selector_definition
        if match_all_selector_definition is not None:
            self.match_all_selector_definition = match_all_selector_definition
        if policy_selector_definition is not None:
            self.policy_selector_definition = policy_selector_definition

    @property
    def metadata_selector_definition(self):
        """Gets the metadata_selector_definition of this SelectorDefinition.  # noqa: E501


        :return: The metadata_selector_definition of this SelectorDefinition.  # noqa: E501
        :rtype: MetadataSelectorDefinition
        """
        return self._metadata_selector_definition

    @metadata_selector_definition.setter
    def metadata_selector_definition(self, metadata_selector_definition):
        """Sets the metadata_selector_definition of this SelectorDefinition.


        :param metadata_selector_definition: The metadata_selector_definition of this SelectorDefinition.  # noqa: E501
        :type: MetadataSelectorDefinition
        """

        self._metadata_selector_definition = metadata_selector_definition

    @property
    def id_selector_definition(self):
        """Gets the id_selector_definition of this SelectorDefinition.  # noqa: E501


        :return: The id_selector_definition of this SelectorDefinition.  # noqa: E501
        :rtype: IdSelectorDefinition
        """
        return self._id_selector_definition

    @id_selector_definition.setter
    def id_selector_definition(self, id_selector_definition):
        """Sets the id_selector_definition of this SelectorDefinition.


        :param id_selector_definition: The id_selector_definition of this SelectorDefinition.  # noqa: E501
        :type: IdSelectorDefinition
        """

        self._id_selector_definition = id_selector_definition

    @property
    def match_all_selector_definition(self):
        """Gets the match_all_selector_definition of this SelectorDefinition.  # noqa: E501


        :return: The match_all_selector_definition of this SelectorDefinition.  # noqa: E501
        :rtype: MatchAllSelectorDefinition
        """
        return self._match_all_selector_definition

    @match_all_selector_definition.setter
    def match_all_selector_definition(self, match_all_selector_definition):
        """Sets the match_all_selector_definition of this SelectorDefinition.


        :param match_all_selector_definition: The match_all_selector_definition of this SelectorDefinition.  # noqa: E501
        :type: MatchAllSelectorDefinition
        """

        self._match_all_selector_definition = match_all_selector_definition

    @property
    def policy_selector_definition(self):
        """Gets the policy_selector_definition of this SelectorDefinition.  # noqa: E501


        :return: The policy_selector_definition of this SelectorDefinition.  # noqa: E501
        :rtype: PolicySelectorDefinition
        """
        return self._policy_selector_definition

    @policy_selector_definition.setter
    def policy_selector_definition(self, policy_selector_definition):
        """Sets the policy_selector_definition of this SelectorDefinition.


        :param policy_selector_definition: The policy_selector_definition of this SelectorDefinition.  # noqa: E501
        :type: PolicySelectorDefinition
        """

        self._policy_selector_definition = policy_selector_definition

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
        if not isinstance(other, SelectorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
