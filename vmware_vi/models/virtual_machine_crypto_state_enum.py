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


class VirtualMachineCryptoStateEnum(str, Enum):
    """
    The crypto state of a encrypted virtual machine.  Possible values: - `unlocked`: The virtual machine is in unlocked state. - `locked`: The virtual machine is in locked state for the configuration key missing   on the ESX host where the VM is registered.    ***Since:*** vSphere API 6.7 
    """

    """
    allowed enum values
    """
    UNLOCKED = 'unlocked'
    LOCKED = 'locked'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineCryptoStateEnum from a JSON string"""
        return cls(json.loads(json_str))

