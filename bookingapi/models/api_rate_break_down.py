# coding: utf-8

"""
    APITUDE BOOKINGAPI

    BOOKINGAPI is designed to book hotels in real time as fast as in two steps. It covers the complete booking process; it allows generating lists of hotels, confirming bookings, getting lists of bookings, obtaining booking information, making cancellations and modify existing bookings.   BOOKINGAPI works in combination with CONTENTAPI to obtain content information from the hotels, such as pictures, description, facilities, services, etc. Please refer to the ContentAPI documentation and IO/DOCS for related information.    BOOKINGAPI has been designed for a two steps confirmation, but due the the complexity of client and providers systems a third method has been designed.

    OpenAPI spec version: 1.0
    Contact: apitude@hotelbeds.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApiRateBreakDown(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rate_discount': 'list[ApiRateDiscount]',
        'rate_supplement': 'list[ApiRateSupplement]'
    }

    attribute_map = {
        'rate_discount': 'rateDiscount',
        'rate_supplement': 'rateSupplement'
    }

    def __init__(self, rate_discount=None, rate_supplement=None):
        """
        ApiRateBreakDown - a model defined in Swagger
        """

        self._rate_discount = None
        self._rate_supplement = None

        if rate_discount is not None:
          self.rate_discount = rate_discount
        if rate_supplement is not None:
          self.rate_supplement = rate_supplement

    @property
    def rate_discount(self):
        """
        Gets the rate_discount of this ApiRateBreakDown.

        :return: The rate_discount of this ApiRateBreakDown.
        :rtype: list[ApiRateDiscount]
        """
        return self._rate_discount

    @rate_discount.setter
    def rate_discount(self, rate_discount):
        """
        Sets the rate_discount of this ApiRateBreakDown.

        :param rate_discount: The rate_discount of this ApiRateBreakDown.
        :type: list[ApiRateDiscount]
        """

        self._rate_discount = rate_discount

    @property
    def rate_supplement(self):
        """
        Gets the rate_supplement of this ApiRateBreakDown.

        :return: The rate_supplement of this ApiRateBreakDown.
        :rtype: list[ApiRateSupplement]
        """
        return self._rate_supplement

    @rate_supplement.setter
    def rate_supplement(self, rate_supplement):
        """
        Sets the rate_supplement of this ApiRateBreakDown.

        :param rate_supplement: The rate_supplement of this ApiRateBreakDown.
        :type: list[ApiRateSupplement]
        """

        self._rate_supplement = rate_supplement

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ApiRateBreakDown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other