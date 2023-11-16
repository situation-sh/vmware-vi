# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class HostSystemIdentificationInfoIdentifierEnum(str, Enum):
    """
    Possible values: - `AssetTag`: The Asset tag of the system - `ServiceTag`: The Service tag of the system - `OemSpecificString`: OEM specific string      ***Since:*** vSphere API 5.0 - `EnclosureSerialNumberTag`: The Enclosure Serial Number tag of the system      ***Since:*** vSphere API 6.0 - `SerialNumberTag`: The Serial Number tag of the system      ***Since:*** vSphere API 6.0  ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    ASSETTAG = 'AssetTag'
    SERVICETAG = 'ServiceTag'
    OEMSPECIFICSTRING = 'OemSpecificString'
    ENCLOSURESERIALNUMBERTAG = 'EnclosureSerialNumberTag'
    SERIALNUMBERTAG = 'SerialNumberTag'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostSystemIdentificationInfoIdentifierEnum from a JSON string"""
        return cls(json.loads(json_str))


