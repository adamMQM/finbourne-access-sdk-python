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

class RoleResourceRequest(object):
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
        'non_transitive_supervisor_role_resource': 'NonTransitiveSupervisorRoleResource',
        'policy_id_role_resource': 'PolicyIdRoleResource'
    }

    attribute_map = {
        'non_transitive_supervisor_role_resource': 'nonTransitiveSupervisorRoleResource',
        'policy_id_role_resource': 'policyIdRoleResource'
    }

    required_map = {
        'non_transitive_supervisor_role_resource': 'optional',
        'policy_id_role_resource': 'optional'
    }

    def __init__(self, non_transitive_supervisor_role_resource=None, policy_id_role_resource=None):  # noqa: E501
        """
        RoleResourceRequest - a model defined in OpenAPI

        :param non_transitive_supervisor_role_resource: 
        :type non_transitive_supervisor_role_resource: finbourne_access.NonTransitiveSupervisorRoleResource
        :param policy_id_role_resource: 
        :type policy_id_role_resource: finbourne_access.PolicyIdRoleResource

        """  # noqa: E501

        self._non_transitive_supervisor_role_resource = None
        self._policy_id_role_resource = None
        self.discriminator = None

        if non_transitive_supervisor_role_resource is not None:
            self.non_transitive_supervisor_role_resource = non_transitive_supervisor_role_resource
        if policy_id_role_resource is not None:
            self.policy_id_role_resource = policy_id_role_resource

    @property
    def non_transitive_supervisor_role_resource(self):
        """Gets the non_transitive_supervisor_role_resource of this RoleResourceRequest.  # noqa: E501


        :return: The non_transitive_supervisor_role_resource of this RoleResourceRequest.  # noqa: E501
        :rtype: NonTransitiveSupervisorRoleResource
        """
        return self._non_transitive_supervisor_role_resource

    @non_transitive_supervisor_role_resource.setter
    def non_transitive_supervisor_role_resource(self, non_transitive_supervisor_role_resource):
        """Sets the non_transitive_supervisor_role_resource of this RoleResourceRequest.


        :param non_transitive_supervisor_role_resource: The non_transitive_supervisor_role_resource of this RoleResourceRequest.  # noqa: E501
        :type: NonTransitiveSupervisorRoleResource
        """

        self._non_transitive_supervisor_role_resource = non_transitive_supervisor_role_resource

    @property
    def policy_id_role_resource(self):
        """Gets the policy_id_role_resource of this RoleResourceRequest.  # noqa: E501


        :return: The policy_id_role_resource of this RoleResourceRequest.  # noqa: E501
        :rtype: PolicyIdRoleResource
        """
        return self._policy_id_role_resource

    @policy_id_role_resource.setter
    def policy_id_role_resource(self, policy_id_role_resource):
        """Sets the policy_id_role_resource of this RoleResourceRequest.


        :param policy_id_role_resource: The policy_id_role_resource of this RoleResourceRequest.  # noqa: E501
        :type: PolicyIdRoleResource
        """

        self._policy_id_role_resource = policy_id_role_resource

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
        if not isinstance(other, RoleResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
