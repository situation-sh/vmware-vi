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


class VirtualMachineWindowsQuiesceSpecVssBackupContextEnum(str, Enum):
    """
    The VSS Snapshot Context VSS\\_SNAPSHOT\\_CONTEXT values not listed below are not implemented.  Possible values: - `ctx_auto`: The context value indicates auto selection of VSS snapshot context.      The ctx\\_backup may make Windows VSS-aware applications quiescing during   backup. The ctx\\_auto makes VMTools select ctx\\_file\\_share\\_backup context   if ctx\\_backup is not available. - `ctx_backup`: Indicate VSS\\_CTX\\_BACKUP. - `ctx_file_share_backup`: Indicate VSS\\_CTX\\_FILE\\_SHARE\\_BACKUP.    ***Since:*** vSphere API 6.5 
    """

    """
    allowed enum values
    """
    CTX_AUTO = 'ctx_auto'
    CTX_BACKUP = 'ctx_backup'
    CTX_FILE_SHARE_BACKUP = 'ctx_file_share_backup'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineWindowsQuiesceSpecVssBackupContextEnum from a JSON string"""
        return cls(json.loads(json_str))

