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


class HostPatchManagerIntegrityStatusEnum(str, Enum):
    """
    The integrity validation status.  Possible values: - `validated`: The update is successfully validated. - `keyNotFound`: The integrity can not be verified since a public key to   verify the update cannot be found. - `keyRevoked`: A public key to verify the update has been revoked. - `keyExpired`: A public key to verify the update is expired. - `digestMismatch`: A digital signature of the update does not match. - `notEnoughSignatures`: Not enough signed signatures on the update. - `validationError`: The integrity validation failed. 
    """

    """
    allowed enum values
    """
    VALIDATED = 'validated'
    KEYNOTFOUND = 'keyNotFound'
    KEYREVOKED = 'keyRevoked'
    KEYEXPIRED = 'keyExpired'
    DIGESTMISMATCH = 'digestMismatch'
    NOTENOUGHSIGNATURES = 'notEnoughSignatures'
    VALIDATIONERROR = 'validationError'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostPatchManagerIntegrityStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


