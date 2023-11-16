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


class HostLowLevelProvisioningManagerReloadTargetEnum(str, Enum):
    """
    The target of the disk reload.  Possible values: - `currentConfig`: Specifies the reload of the current config of the virtual machine. - `snapshotConfig`: Specifies the reload of the snapshot config of the virtual machine.      If the virtual machine has multiple snapshots, all of the snapshot's   config will be reloaded.  ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    CURRENTCONFIG = 'currentConfig'
    SNAPSHOTCONFIG = 'snapshotConfig'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostLowLevelProvisioningManagerReloadTargetEnum from a JSON string"""
        return cls(json.loads(json_str))


