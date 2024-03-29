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


class HostPatchManagerReasonEnum(str, Enum):
    """
    Reasons why an update is not applicable to the ESX host.  Possible values: - `obsoleted`: The update is made obsolete by other patches installed on the host. - `missingPatch`: The update depends on another update that is neither installed   nor in the scanned list of updates. - `missingLib`: The update depends on certain libraries or RPMs that are not   available. - `hasDependentPatch`: The update depends on an update that is not installed but is   in the scanned list of updates. - `conflictPatch`: The update conflicts with certain updates that are already   installed on the host. - `conflictLib`: The update conflicts with RPMs or libraries installed on the   host. 
    """

    """
    allowed enum values
    """
    OBSOLETED = 'obsoleted'
    MISSINGPATCH = 'missingPatch'
    MISSINGLIB = 'missingLib'
    HASDEPENDENTPATCH = 'hasDependentPatch'
    CONFLICTPATCH = 'conflictPatch'
    CONFLICTLIB = 'conflictLib'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostPatchManagerReasonEnum from a JSON string"""
        return cls(json.loads(json_str))


