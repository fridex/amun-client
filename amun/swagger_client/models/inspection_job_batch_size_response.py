# coding: utf-8

"""
    Amun API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.6.0-dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amun.swagger_client.configuration import Configuration


class InspectionJobBatchSizeResponse(object):
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
    """
    openapi_types = {
        'batch_size': 'int',
        'parameters': 'object'
    }

    attribute_map = {
        'batch_size': 'batch_size',
        'parameters': 'parameters'
    }

    def __init__(self, batch_size=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """InspectionJobBatchSizeResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._batch_size = None
        self._parameters = None
        self.discriminator = None

        self.batch_size = batch_size
        self.parameters = parameters

    @property
    def batch_size(self):
        """Gets the batch_size of this InspectionJobBatchSizeResponse.  # noqa: E501

        Batch size of the given inspection.  # noqa: E501

        :return: The batch_size of this InspectionJobBatchSizeResponse.  # noqa: E501
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this InspectionJobBatchSizeResponse.

        Batch size of the given inspection.  # noqa: E501

        :param batch_size: The batch_size of this InspectionJobBatchSizeResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and batch_size is None:  # noqa: E501
            raise ValueError("Invalid value for `batch_size`, must not be `None`")  # noqa: E501

        self._batch_size = batch_size

    @property
    def parameters(self):
        """Gets the parameters of this InspectionJobBatchSizeResponse.  # noqa: E501

        Parameters echoed back to user (with default parameters if omitted).  # noqa: E501

        :return: The parameters of this InspectionJobBatchSizeResponse.  # noqa: E501
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InspectionJobBatchSizeResponse.

        Parameters echoed back to user (with default parameters if omitted).  # noqa: E501

        :param parameters: The parameters of this InspectionJobBatchSizeResponse.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if not isinstance(other, InspectionJobBatchSizeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InspectionJobBatchSizeResponse):
            return True

        return self.to_dict() != other.to_dict()