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


class HostDasErrorEventHostDasErrorReasonEnum(str, Enum):
    """
    Possible values: - `configFailed`: Error while configuring/unconfiguring HA - `timeout`: Timeout while communicating with HA agent - `communicationInitFailed`: HA communication initialization failed - `healthCheckScriptFailed`: Health check script failed - `agentFailed`: HA agent has an error - `agentShutdown`: HA agent was shutdown - `isolationAddressUnpingable`: HA isolation address unpingable      ***Since:*** vSphere API 4.1 - `other`: Other reason    ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    CONFIGFAILED = 'configFailed'
    TIMEOUT = 'timeout'
    COMMUNICATIONINITFAILED = 'communicationInitFailed'
    HEALTHCHECKSCRIPTFAILED = 'healthCheckScriptFailed'
    AGENTFAILED = 'agentFailed'
    AGENTSHUTDOWN = 'agentShutdown'
    ISOLATIONADDRESSUNPINGABLE = 'isolationAddressUnpingable'
    OTHER = 'other'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostDasErrorEventHostDasErrorReasonEnum from a JSON string"""
        return cls(json.loads(json_str))

