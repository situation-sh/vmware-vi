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


class StorageDrsPodConfigInfoBehaviorEnum(str, Enum):
    """
    Storage DRS behavior.  Possible values: - `manual`: Specifies that VirtualCenter should generate recommendations for   virtual disk migration and for placement with a datastore,   but should not execute the recommendations automatically. - `automated`: Specifies that VirtualCenter should generate recommendations   for virtual disk migration and for placement with a   datastore.      The recommendations for virtual disk migrations   will be executed automatically, but the placement   recommendations will be done manually.  ***Since:*** vSphere API 5.0 
    """

    """
    allowed enum values
    """
    MANUAL = 'manual'
    AUTOMATED = 'automated'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StorageDrsPodConfigInfoBehaviorEnum from a JSON string"""
        return cls(json.loads(json_str))


