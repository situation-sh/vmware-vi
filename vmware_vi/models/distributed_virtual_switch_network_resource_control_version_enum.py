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


class DistributedVirtualSwitchNetworkResourceControlVersionEnum(str, Enum):
    """
    Network resource control version types.  Possible values: - `version2`: Network Resource Control API version 2 - `version3`: Network Resource Control API version 3    ***Since:*** vSphere API 6.0 
    """

    """
    allowed enum values
    """
    VERSION2 = 'version2'
    VERSION3 = 'version3'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DistributedVirtualSwitchNetworkResourceControlVersionEnum from a JSON string"""
        return cls(json.loads(json_str))

