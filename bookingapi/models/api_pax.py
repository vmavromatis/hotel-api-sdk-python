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


class ApiPax(object):
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
        'room_id': 'int',
        'type': 'str',
        'age': 'int',
        'name': 'str',
        'surname': 'str'
    }

    attribute_map = {
        'room_id': 'roomId',
        'type': 'type',
        'age': 'age',
        'name': 'name',
        'surname': 'surname'
    }

    def __init__(self, room_id=None, type=None, age=None, name=None, surname=None):
        """
        ApiPax - a model defined in Swagger
        """

        self._room_id = None
        self._type = None
        self._age = None
        self._name = None
        self._surname = None

        if room_id is not None:
          self.room_id = room_id
        self.type = type
        if age is not None:
          self.age = age
        if name is not None:
          self.name = name
        if surname is not None:
          self.surname = surname

    @property
    def room_id(self):
        """
        Gets the room_id of this ApiPax.

        :return: The room_id of this ApiPax.
        :rtype: int
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """
        Sets the room_id of this ApiPax.

        :param room_id: The room_id of this ApiPax.
        :type: int
        """
        if room_id is not None and room_id < 1:
            raise ValueError("Invalid value for `room_id`, must be a value greater than or equal to `1`")

        self._room_id = room_id

    @property
    def type(self):
        """
        Gets the type of this ApiPax.

        :return: The type of this ApiPax.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApiPax.

        :param type: The type of this ApiPax.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["AD", "CH"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def age(self):
        """
        Gets the age of this ApiPax.

        :return: The age of this ApiPax.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """
        Sets the age of this ApiPax.

        :param age: The age of this ApiPax.
        :type: int
        """
        if age is not None and age > 99:
            raise ValueError("Invalid value for `age`, must be a value less than or equal to `99`")
        if age is not None and age < 0:
            raise ValueError("Invalid value for `age`, must be a value greater than or equal to `0`")

        self._age = age

    @property
    def name(self):
        """
        Gets the name of this ApiPax.

        :return: The name of this ApiPax.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApiPax.

        :param name: The name of this ApiPax.
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")

        self._name = name

    @property
    def surname(self):
        """
        Gets the surname of this ApiPax.

        :return: The surname of this ApiPax.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """
        Sets the surname of this ApiPax.

        :param surname: The surname of this ApiPax.
        :type: str
        """
        if surname is not None and len(surname) > 50:
            raise ValueError("Invalid value for `surname`, length must be less than or equal to `50`")
        if surname is not None and len(surname) < 0:
            raise ValueError("Invalid value for `surname`, length must be greater than or equal to `0`")

        self._surname = surname

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
        if not isinstance(other, ApiPax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
