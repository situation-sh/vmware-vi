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


class DistributedVirtualPortgroupMetaTagNameEnum(str, Enum):
    """
    The meta tag names recognizable in the *DVPortgroupConfigInfo.portNameFormat* string.  Possible values: - `dvsName`: This tag will be expanded to the name of the switch. - `portgroupName`: This tag will be expanded to the name of the portgroup. - `portIndex`: This tag will be expanded to the current index of the port.    ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    DVSNAME = 'dvsName'
    PORTGROUPNAME = 'portgroupName'
    PORTINDEX = 'portIndex'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DistributedVirtualPortgroupMetaTagNameEnum from a JSON string"""
        return cls(json.loads(json_str))

