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


class HostNvmeDiscoveryLogSubsystemTypeEnum(str, Enum):
    """
    This enum represents the supported NVM subsystem types.  Possible values: - `discovery`: A Discovery service, composed of Discovery controllers. - `nvm`: An NVM subsystem whose controllers may have attached namespaces. 
    """

    """
    allowed enum values
    """
    DISCOVERY = 'discovery'
    NVM = 'nvm'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostNvmeDiscoveryLogSubsystemTypeEnum from a JSON string"""
        return cls(json.loads(json_str))

