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


class AgentInstallFailedReasonEnum(str, Enum):
    """
    Possible values: - `NotEnoughSpaceOnDevice`: There is not enough storage space on the host to install the agent. - `PrepareToUpgradeFailed`: Failed to initialize the upgrade directory on the host. - `AgentNotRunning`: The agent was installed but is not running. - `AgentNotReachable`: The agent was installed but did not respond to requests. - `InstallTimedout`: The agent install took too long. - `SignatureVerificationFailed`: The signature verification for the installer failed. - `AgentUploadFailed`: Failed to upload the agent installer. - `AgentUploadTimedout`: The agent upload took too long. - `UnknownInstallerError`: The agent installer failed for an unknown reason.    ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    NOTENOUGHSPACEONDEVICE = 'NotEnoughSpaceOnDevice'
    PREPARETOUPGRADEFAILED = 'PrepareToUpgradeFailed'
    AGENTNOTRUNNING = 'AgentNotRunning'
    AGENTNOTREACHABLE = 'AgentNotReachable'
    INSTALLTIMEDOUT = 'InstallTimedout'
    SIGNATUREVERIFICATIONFAILED = 'SignatureVerificationFailed'
    AGENTUPLOADFAILED = 'AgentUploadFailed'
    AGENTUPLOADTIMEDOUT = 'AgentUploadTimedout'
    UNKNOWNINSTALLERERROR = 'UnknownInstallerError'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentInstallFailedReasonEnum from a JSON string"""
        return cls(json.loads(json_str))


