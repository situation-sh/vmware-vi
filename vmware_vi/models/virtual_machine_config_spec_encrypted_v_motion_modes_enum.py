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


class VirtualMachineConfigSpecEncryptedVMotionModesEnum(str, Enum):
    """
    The set of valid encrypted vMotion modes for a VM.  If the VM is encrypted, its encrypted vMotion mode will be required.  Possible values: - `disabled`: Do not use encrypted vMotion, even if available. - `opportunistic`: Use encrypted vMotion if source and destination hosts support it,   fall back to unencrypted vMotion otherwise.      This is the default option. - `required`: Allow only encrypted vMotion.      If the source or destination host does   not support vMotion encryption, do not allow the vMotion to occur.  ***Since:*** vSphere API 6.5 
    """

    """
    allowed enum values
    """
    DISABLED = 'disabled'
    OPPORTUNISTIC = 'opportunistic'
    REQUIRED = 'required'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineConfigSpecEncryptedVMotionModesEnum from a JSON string"""
        return cls(json.loads(json_str))


