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


class LicenseReservationInfoStateEnum(str, Enum):
    """
    Describes the reservation state of a license.  Possible values: - `notUsed`: This license is currently unused by the system, or the feature does not   apply.      For example, a DRS license appears as NotUsed if the host is not   part of a DRS-enabled cluster. - `noLicense`: This indicates that the license has expired or the system attempted to acquire   the license but was not successful in reserving it. - `unlicensedUse`: The LicenseManager failed to acquire a license but the implementation   policy allows us to use the licensed feature anyway.      This is possible, for   example, when a license server becomes unavailable after a license had been   successfully reserved from it. - `licensed`: The required number of licenses have been acquired from the license source. 
    """

    """
    allowed enum values
    """
    NOTUSED = 'notUsed'
    NOLICENSE = 'noLicense'
    UNLICENSEDUSE = 'unlicensedUse'
    LICENSED = 'licensed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LicenseReservationInfoStateEnum from a JSON string"""
        return cls(json.loads(json_str))


