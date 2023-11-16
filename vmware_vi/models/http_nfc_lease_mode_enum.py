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


class HttpNfcLeaseModeEnum(str, Enum):
    """
    List of supported modes by HttpNfcLease  Possible values: - `pushOrGet`: Client pushes or downloads individual files from/to   each host/url provided by this lease in *HttpNfcLease.info* - `pull`: Mode where hosts itself pull files from source URLs.      See *HttpNfcLease.HttpNfcLeasePullFromUrls_Task*  ***Since:*** vSphere API 6.7 
    """

    """
    allowed enum values
    """
    PUSHORGET = 'pushOrGet'
    PULL = 'pull'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HttpNfcLeaseModeEnum from a JSON string"""
        return cls(json.loads(json_str))


