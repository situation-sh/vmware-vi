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


class CustomizationSysprepRebootOptionEnum(str, Enum):
    """
    A enum constant specifying what should be done to the guest vm after running sysprep.  Possible values: - `reboot`: Reboot the machine after running sysprep.      This will cause values   specified in the sysprep.xml to be applied immediately. - `noreboot`: Take no action.      Leave the guest os running after running sysprep. This   option can be used to look at values for debugging purposes after   running sysprep. - `shutdown`: Shutdown the machine after running sysprep.      This puts the vm in a   sealed state.  ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    REBOOT = 'reboot'
    NOREBOOT = 'noreboot'
    SHUTDOWN = 'shutdown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CustomizationSysprepRebootOptionEnum from a JSON string"""
        return cls(json.loads(json_str))


