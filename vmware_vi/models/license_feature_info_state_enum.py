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


class LicenseFeatureInfoStateEnum(str, Enum):
    """
    Describes the state of the feature.  Possible values: - `enabled`: The current edition license has implicitly enabled this additional feature. - `disabled`: The current edition license does not allow this additional feature. - `optional`: The current edition license allows this additional feature.      The   *LicenseManager.EnableFeature* and *LicenseManager.DisableFeature* methods can be used to enable or disable   this feature. 
    """

    """
    allowed enum values
    """
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    OPTIONAL = 'optional'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LicenseFeatureInfoStateEnum from a JSON string"""
        return cls(json.loads(json_str))


