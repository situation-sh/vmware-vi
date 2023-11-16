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


class ProfileExecuteResultStatusEnum(str, Enum):
    """
    Defines the result status values for a *HostProfile*.*HostProfile.ExecuteHostProfile* operation.  The result data is contained in the *ProfileExecuteResult* data object.  Possible values: - `success`: Profile execution was successful.      You can use the output configuration data   to apply the profile to a host. - `needInput`: Additional data is required to complete the operation.      The data requirements are defined in the list of policy options for the profile   (*ApplyProfile*.*ApplyProfile.policy*\\[\\]). - `error`: Profile execution generated an error.      See *ProfileExecuteResult*.*ProfileExecuteResult.error*.  ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    SUCCESS = 'success'
    NEEDINPUT = 'needInput'
    ERROR = 'error'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProfileExecuteResultStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


