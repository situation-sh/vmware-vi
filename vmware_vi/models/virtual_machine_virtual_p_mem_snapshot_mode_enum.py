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


class VirtualMachineVirtualPMemSnapshotModeEnum(str, Enum):
    """
    The set of supported snapshot modes for VMs configured with NVDIMMs.  Possible values: - `independent_persistent`: The data on virtual NVDIMMs are not affected by snapshot reverts.      Writes to virtual NVDIMMs after a snapshot is taken cannot be   reverted to the snapshotted state. - `independent_eraseonrevert`: Virtual NVDIMMs are erased and recreated upon snapshot reverts.    ***Since:*** vSphere API 7.0.3.0 
    """

    """
    allowed enum values
    """
    INDEPENDENT_PERSISTENT = 'independent_persistent'
    INDEPENDENT_ERASEONREVERT = 'independent_eraseonrevert'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineVirtualPMemSnapshotModeEnum from a JSON string"""
        return cls(json.loads(json_str))


