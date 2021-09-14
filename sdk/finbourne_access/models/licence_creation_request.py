# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1377
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_access.configuration import Configuration


class LicenceCreationRequest(object):
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
        'code': 'str',
        'description': 'str',
        'applications': 'list[str]',
        'selectors': 'list[LicenceSelectorDefinition]',
        'when': 'WhenSpec',
        '_for': 'list[ForSpec]',
        'how': 'HowSpec',
        '_if': 'list[IfExpression]'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'applications': 'applications',
        'selectors': 'selectors',
        'when': 'when',
        '_for': 'for',
        'how': 'how',
        '_if': 'if'
    }

    required_map = {
        'code': 'required',
        'description': 'required',
        'applications': 'required',
        'selectors': 'required',
        'when': 'required',
        '_for': 'optional',
        'how': 'optional',
        '_if': 'optional'
    }

    def __init__(self, code=None, description=None, applications=None, selectors=None, when=None, _for=None, how=None, _if=None, local_vars_configuration=None):  # noqa: E501
        """LicenceCreationRequest - a model defined in OpenAPI"
        
        :param code:  The code of the licence. (required)
        :type code: str
        :param description:  A description of the licence's purpose. (required)
        :type description: str
        :param applications:  The applications that the licence refers to. (required)
        :type applications: list[str]
        :param selectors:  The selectors affected by the licence. (required)
        :type selectors: list[finbourne_access.LicenceSelectorDefinition]
        :param when:  (required)
        :type when: finbourne_access.WhenSpec
        :param _for:  The ForSpecs of the licence.
        :type _for: list[finbourne_access.ForSpec]
        :param how: 
        :type how: finbourne_access.HowSpec
        :param _if:  The IfSpecs of the licence.
        :type _if: list[finbourne_access.IfExpression]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._description = None
        self._applications = None
        self._selectors = None
        self._when = None
        self.__for = None
        self._how = None
        self.__if = None
        self.discriminator = None

        self.code = code
        self.description = description
        self.applications = applications
        self.selectors = selectors
        self.when = when
        self._for = _for
        if how is not None:
            self.how = how
        self._if = _if

    @property
    def code(self):
        """Gets the code of this LicenceCreationRequest.  # noqa: E501

        The code of the licence.  # noqa: E501

        :return: The code of this LicenceCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LicenceCreationRequest.

        The code of the licence.  # noqa: E501

        :param code: The code of this LicenceCreationRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 100):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 3):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9-_ +]{2,100}$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9-_ +]{2,100}$/`")  # noqa: E501

        self._code = code

    @property
    def description(self):
        """Gets the description of this LicenceCreationRequest.  # noqa: E501

        A description of the licence's purpose.  # noqa: E501

        :return: The description of this LicenceCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LicenceCreationRequest.

        A description of the licence's purpose.  # noqa: E501

        :param description: The description of this LicenceCreationRequest.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def applications(self):
        """Gets the applications of this LicenceCreationRequest.  # noqa: E501

        The applications that the licence refers to.  # noqa: E501

        :return: The applications of this LicenceCreationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this LicenceCreationRequest.

        The applications that the licence refers to.  # noqa: E501

        :param applications: The applications of this LicenceCreationRequest.  # noqa: E501
        :type applications: list[str]
        """
        if self.local_vars_configuration.client_side_validation and applications is None:  # noqa: E501
            raise ValueError("Invalid value for `applications`, must not be `None`")  # noqa: E501

        self._applications = applications

    @property
    def selectors(self):
        """Gets the selectors of this LicenceCreationRequest.  # noqa: E501

        The selectors affected by the licence.  # noqa: E501

        :return: The selectors of this LicenceCreationRequest.  # noqa: E501
        :rtype: list[finbourne_access.LicenceSelectorDefinition]
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """Sets the selectors of this LicenceCreationRequest.

        The selectors affected by the licence.  # noqa: E501

        :param selectors: The selectors of this LicenceCreationRequest.  # noqa: E501
        :type selectors: list[finbourne_access.LicenceSelectorDefinition]
        """
        if self.local_vars_configuration.client_side_validation and selectors is None:  # noqa: E501
            raise ValueError("Invalid value for `selectors`, must not be `None`")  # noqa: E501

        self._selectors = selectors

    @property
    def when(self):
        """Gets the when of this LicenceCreationRequest.  # noqa: E501


        :return: The when of this LicenceCreationRequest.  # noqa: E501
        :rtype: finbourne_access.WhenSpec
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this LicenceCreationRequest.


        :param when: The when of this LicenceCreationRequest.  # noqa: E501
        :type when: finbourne_access.WhenSpec
        """
        if self.local_vars_configuration.client_side_validation and when is None:  # noqa: E501
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501

        self._when = when

    @property
    def _for(self):
        """Gets the _for of this LicenceCreationRequest.  # noqa: E501

        The ForSpecs of the licence.  # noqa: E501

        :return: The _for of this LicenceCreationRequest.  # noqa: E501
        :rtype: list[finbourne_access.ForSpec]
        """
        return self.__for

    @_for.setter
    def _for(self, _for):
        """Sets the _for of this LicenceCreationRequest.

        The ForSpecs of the licence.  # noqa: E501

        :param _for: The _for of this LicenceCreationRequest.  # noqa: E501
        :type _for: list[finbourne_access.ForSpec]
        """

        self.__for = _for

    @property
    def how(self):
        """Gets the how of this LicenceCreationRequest.  # noqa: E501


        :return: The how of this LicenceCreationRequest.  # noqa: E501
        :rtype: finbourne_access.HowSpec
        """
        return self._how

    @how.setter
    def how(self, how):
        """Sets the how of this LicenceCreationRequest.


        :param how: The how of this LicenceCreationRequest.  # noqa: E501
        :type how: finbourne_access.HowSpec
        """

        self._how = how

    @property
    def _if(self):
        """Gets the _if of this LicenceCreationRequest.  # noqa: E501

        The IfSpecs of the licence.  # noqa: E501

        :return: The _if of this LicenceCreationRequest.  # noqa: E501
        :rtype: list[finbourne_access.IfExpression]
        """
        return self.__if

    @_if.setter
    def _if(self, _if):
        """Sets the _if of this LicenceCreationRequest.

        The IfSpecs of the licence.  # noqa: E501

        :param _if: The _if of this LicenceCreationRequest.  # noqa: E501
        :type _if: list[finbourne_access.IfExpression]
        """

        self.__if = _if

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LicenceCreationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicenceCreationRequest):
            return True

        return self.to_dict() != other.to_dict()
