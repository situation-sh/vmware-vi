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


class DatastoreSummaryMaintenanceModeStateEnum(str, Enum):
    """
    Defines the current maintenance mode state of the datastore.  Possible values: - `normal`: Default state. - `enteringMaintenance`: Started entering maintenance mode, but not finished.      This could happen when waiting for user input or for   long-running vmotions to complete. - `inMaintenance`: Successfully entered maintenance mode.    ***Since:*** vSphere API 5.0 
    """

    """
    allowed enum values
    """
    NORMAL = 'normal'
    ENTERINGMAINTENANCE = 'enteringMaintenance'
    INMAINTENANCE = 'inMaintenance'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DatastoreSummaryMaintenanceModeStateEnum from a JSON string"""
        return cls(json.loads(json_str))

