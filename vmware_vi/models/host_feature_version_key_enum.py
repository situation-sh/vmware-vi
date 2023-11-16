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


class HostFeatureVersionKeyEnum(str, Enum):
    """
    Set of possible values for *HostFeatureVersionInfo.key*, which is a unique key that identifies a feature.  Possible values: - `faultTolerance`: VMware Fault Tolerance feature.      For pre-4.1 hosts, the   version value reported will be empty in which case   *AboutInfo.build* should be used. For all   other hosts, the version number reported will be a component-specific   version identifier of the form X.Y.Z, where:   X refers to host agent Fault Tolerance version number,   Y refers to VMX Fault Tolerance version number,   Z refers to VMkernal Fault Tolerance version  ***Since:*** vSphere API 4.1 
    """

    """
    allowed enum values
    """
    FAULTTOLERANCE = 'faultTolerance'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostFeatureVersionKeyEnum from a JSON string"""
        return cls(json.loads(json_str))


