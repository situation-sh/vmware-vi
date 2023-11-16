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


class HostUnresolvedVmfsResolutionSpecVmfsUuidResolutionEnum(str, Enum):
    """
    Possible values: - `resignature`: Resignature the Unresolved VMFS volume.      In the event the volume to be resignatured contains multiple   extents but only a single copy of each extent exists, only the   head extent needs to be specified. - `forceMount`: Keep the original Uuid of the VMFS volume and mount it      In the event the volume to be force mounted contains multiple   extents but only a single copy of each extent exists, only the   head extent needs to be specified.  ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    RESIGNATURE = 'resignature'
    FORCEMOUNT = 'forceMount'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostUnresolvedVmfsResolutionSpecVmfsUuidResolutionEnum from a JSON string"""
        return cls(json.loads(json_str))


