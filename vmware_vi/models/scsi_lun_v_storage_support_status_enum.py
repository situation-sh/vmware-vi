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


class ScsiLunVStorageSupportStatusEnum(str, Enum):
    """
    Storage array hardware acceleration support status.  When a host boots, the support status is unknown. As a host attempts hardware-accelerated operations, it determines whether the storage device supports hardware acceleration and sets the *ScsiLun.vStorageSupport* property accordingly.  Possible values: - `vStorageSupported`: Storage device supports hardware acceleration.      The ESX host will use the feature to offload certain   storage-related operations to the device. - `vStorageUnsupported`: Storage device does not support hardware acceleration.      The ESX host will handle all storage-related operations. - `vStorageUnknown`: Initial support status value.    ***Since:*** vSphere API 4.1 
    """

    """
    allowed enum values
    """
    VSTORAGESUPPORTED = 'vStorageSupported'
    VSTORAGEUNSUPPORTED = 'vStorageUnsupported'
    VSTORAGEUNKNOWN = 'vStorageUnknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ScsiLunVStorageSupportStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


