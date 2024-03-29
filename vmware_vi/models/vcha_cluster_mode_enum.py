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


class VchaClusterModeEnum(str, Enum):
    """
    VchaClusterMode enum defines the possible modes for a VCHA Cluster.  Possible values: - `enabled`: VCHA Cluster is enabled.      State replication between the Active and   Passive node is enabled and automatic failover is allowed. - `disabled`: VCHA Cluster is disabled.      State replication between the Active and   Passive node is disabled and automatic failover is not allowed. - `maintenance`: VCHA Cluster is in maintenance mode.      State replication between the   Active and Passive node is enabled but automatic failover   is not allowed.  ***Since:*** vSphere API 6.5 
    """

    """
    allowed enum values
    """
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    MAINTENANCE = 'maintenance'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VchaClusterModeEnum from a JSON string"""
        return cls(json.loads(json_str))


