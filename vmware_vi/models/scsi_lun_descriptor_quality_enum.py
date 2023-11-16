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


class ScsiLunDescriptorQualityEnum(str, Enum):
    """
    An indicator of the utility of Descriptor in being used as an identifier that is stable, unique, and correlatable.  Possible values: - `highQuality`: The Descriptor has an identifier that is useful for identification   and correlation across hosts. - `mediumQuality`: The Descriptor has an identifier that may be used for identification   and correlation across hosts. - `lowQuality`: The Descriptor has an identifier that should not be used for   identification and correlation across hosts. - `unknownQuality`: The Descriptor has an identifier that may or may not be useful for   identification and correlation across hosts.    ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    HIGHQUALITY = 'highQuality'
    MEDIUMQUALITY = 'mediumQuality'
    LOWQUALITY = 'lowQuality'
    UNKNOWNQUALITY = 'unknownQuality'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ScsiLunDescriptorQualityEnum from a JSON string"""
        return cls(json.loads(json_str))


