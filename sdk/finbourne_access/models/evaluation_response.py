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

class EvaluationResponse(object):
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
        'result': 'EvaluationResult',
        'detailed_message': 'str'
    }

    attribute_map = {
        'result': 'result',
        'detailed_message': 'detailedMessage'
    }

    required_map = {
        'result': 'required',
        'detailed_message': 'optional'
    }

    def __init__(self, result=None, detailed_message=None):  # noqa: E501
        """
        EvaluationResponse - a model defined in OpenAPI

        :param result:  (required)
        :type result: finbourne_access.EvaluationResult
        :param detailed_message:  In the case of the evaluation being denied a message may be returned
        :type detailed_message: str

        """  # noqa: E501

        self._result = None
        self._detailed_message = None
        self.discriminator = None

        self.result = result
        self.detailed_message = detailed_message

    @property
    def result(self):
        """Gets the result of this EvaluationResponse.  # noqa: E501


        :return: The result of this EvaluationResponse.  # noqa: E501
        :rtype: EvaluationResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this EvaluationResponse.


        :param result: The result of this EvaluationResponse.  # noqa: E501
        :type: EvaluationResult
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def detailed_message(self):
        """Gets the detailed_message of this EvaluationResponse.  # noqa: E501

        In the case of the evaluation being denied a message may be returned  # noqa: E501

        :return: The detailed_message of this EvaluationResponse.  # noqa: E501
        :rtype: str
        """
        return self._detailed_message

    @detailed_message.setter
    def detailed_message(self, detailed_message):
        """Sets the detailed_message of this EvaluationResponse.

        In the case of the evaluation being denied a message may be returned  # noqa: E501

        :param detailed_message: The detailed_message of this EvaluationResponse.  # noqa: E501
        :type: str
        """

        self._detailed_message = detailed_message

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
        if not isinstance(other, EvaluationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
