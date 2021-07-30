# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1292
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class EffectiveDateRelative(object):
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
        'date': 'PointInTimeSpecification',
        'adjustment': 'int',
        'unit': 'DateUnit',
        'relative_to_date_time': 'RelativeToDateTime'
    }

    attribute_map = {
        'date': 'date',
        'adjustment': 'adjustment',
        'unit': 'unit',
        'relative_to_date_time': 'relativeToDateTime'
    }

    required_map = {
        'date': 'optional',
        'adjustment': 'optional',
        'unit': 'optional',
        'relative_to_date_time': 'optional'
    }

    def __init__(self, date=None, adjustment=None, unit=None, relative_to_date_time=None):  # noqa: E501
        """
        EffectiveDateRelative - a model defined in OpenAPI

        :param date: 
        :type date: finbourne_access.PointInTimeSpecification
        :param adjustment: 
        :type adjustment: int
        :param unit: 
        :type unit: finbourne_access.DateUnit
        :param relative_to_date_time: 
        :type relative_to_date_time: finbourne_access.RelativeToDateTime

        """  # noqa: E501

        self._date = None
        self._adjustment = None
        self._unit = None
        self._relative_to_date_time = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if adjustment is not None:
            self.adjustment = adjustment
        if unit is not None:
            self.unit = unit
        if relative_to_date_time is not None:
            self.relative_to_date_time = relative_to_date_time

    @property
    def date(self):
        """Gets the date of this EffectiveDateRelative.  # noqa: E501


        :return: The date of this EffectiveDateRelative.  # noqa: E501
        :rtype: PointInTimeSpecification
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this EffectiveDateRelative.


        :param date: The date of this EffectiveDateRelative.  # noqa: E501
        :type: PointInTimeSpecification
        """

        self._date = date

    @property
    def adjustment(self):
        """Gets the adjustment of this EffectiveDateRelative.  # noqa: E501


        :return: The adjustment of this EffectiveDateRelative.  # noqa: E501
        :rtype: int
        """
        return self._adjustment

    @adjustment.setter
    def adjustment(self, adjustment):
        """Sets the adjustment of this EffectiveDateRelative.


        :param adjustment: The adjustment of this EffectiveDateRelative.  # noqa: E501
        :type: int
        """

        self._adjustment = adjustment

    @property
    def unit(self):
        """Gets the unit of this EffectiveDateRelative.  # noqa: E501


        :return: The unit of this EffectiveDateRelative.  # noqa: E501
        :rtype: DateUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this EffectiveDateRelative.


        :param unit: The unit of this EffectiveDateRelative.  # noqa: E501
        :type: DateUnit
        """

        self._unit = unit

    @property
    def relative_to_date_time(self):
        """Gets the relative_to_date_time of this EffectiveDateRelative.  # noqa: E501


        :return: The relative_to_date_time of this EffectiveDateRelative.  # noqa: E501
        :rtype: RelativeToDateTime
        """
        return self._relative_to_date_time

    @relative_to_date_time.setter
    def relative_to_date_time(self, relative_to_date_time):
        """Sets the relative_to_date_time of this EffectiveDateRelative.


        :param relative_to_date_time: The relative_to_date_time of this EffectiveDateRelative.  # noqa: E501
        :type: RelativeToDateTime
        """

        self._relative_to_date_time = relative_to_date_time

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
        if not isinstance(other, EffectiveDateRelative):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
