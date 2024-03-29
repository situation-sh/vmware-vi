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


class EventEventSeverityEnum(str, Enum):
    """
    Severity level constants.  Possible values: - `error`: Something that must be corrected - `warning`: Should be corrected, but the system can continue operating normally - `info`: An informational message - `user`: A user-related message    ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'
    USER = 'user'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EventEventSeverityEnum from a JSON string"""
        return cls(json.loads(json_str))


