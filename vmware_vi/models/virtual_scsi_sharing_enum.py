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


class VirtualSCSISharingEnum(str, Enum):
    """
    Sharing describes three possible ways of sharing the SCSI bus: One of these values is assigned to the sharedBus object to determine if or how the SCSI bus is shared.  Possible values: - `noSharing`: The virtual SCSI bus is not shared. - `virtualSharing`: The virtual SCSI bus is shared between two or more virtual machines.      In this case, no physical machine is involved. - `physicalSharing`: The virtual SCSI bus is shared between two or more virtual machines   residing on different physical hosts. 
    """

    """
    allowed enum values
    """
    NOSHARING = 'noSharing'
    VIRTUALSHARING = 'virtualSharing'
    PHYSICALSHARING = 'physicalSharing'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualSCSISharingEnum from a JSON string"""
        return cls(json.loads(json_str))


