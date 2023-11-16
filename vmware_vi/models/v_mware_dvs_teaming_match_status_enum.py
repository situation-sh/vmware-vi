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


class VMwareDVSTeamingMatchStatusEnum(str, Enum):
    """
    The teaming health check match status.  Possible values: - `iphashMatch`: The value of 'loadbalance\\_ip' is used in a uplink teaming policy   *VmwareUplinkPortTeamingPolicy.policy*   in the vSphere Distributed Switch, and the external physical switch   has the matching EtherChannel configuration. - `nonIphashMatch`: The value of 'loadbalance\\_ip' is not used in a uplink teaming policy   *VmwareUplinkPortTeamingPolicy.policy*   in the vSphere Distributed Switch, and the external physical switch   does not have EtherChannel configuration. - `iphashMismatch`: The value of 'loadbalance\\_ip' is used in a uplink teaming policy   *VmwareUplinkPortTeamingPolicy.policy*   in the vSphere Distributed Switch, but the external physical switch   does not have the matching EtherChannel configuration. - `nonIphashMismatch`: The value of 'loadbalance\\_ip' is not used in a uplink teaming policy   *VmwareUplinkPortTeamingPolicy.policy*   in the vSphere Distributed Switch, but the external physical switch   has EtherChannel configuration.    ***Since:*** vSphere API 5.1 
    """

    """
    allowed enum values
    """
    IPHASHMATCH = 'iphashMatch'
    NONIPHASHMATCH = 'nonIphashMatch'
    IPHASHMISMATCH = 'iphashMismatch'
    NONIPHASHMISMATCH = 'nonIphashMismatch'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VMwareDVSTeamingMatchStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


