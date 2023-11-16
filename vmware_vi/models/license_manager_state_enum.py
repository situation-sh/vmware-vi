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


class LicenseManagerStateEnum(str, Enum):
    """
    Deprecated as of vSphere API 4.0, this is not used by the system.  State of licensing subsystem.  Possible values: - `initializing`: Setting or resetting configuration in progress. - `normal`: Running within operating parameters. - `marginal`: License source unavailable, using license cache. - `fault`: Initialization has failed or grace period expired.    ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    INITIALIZING = 'initializing'
    NORMAL = 'normal'
    MARGINAL = 'marginal'
    FAULT = 'fault'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LicenseManagerStateEnum from a JSON string"""
        return cls(json.loads(json_str))


