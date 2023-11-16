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


class ValidateMigrationTestTypeEnum(str, Enum):
    """
    Deprecated as of vSphere API 4.0, use *CheckTestType_enum* instead.  Types of tests available for validateMigration.  Possible values: - `sourceTests`: Tests that examine only the configuration   of the virtual machine and its current host; the destination   resource pool and host or cluster are irrelevant. - `compatibilityTests`: Tests that examine both the virtual   machine and the destination host or cluster; the destination   resource pool is irrelevant.      This set excludes tests that fall   into the diskAccessibilityTests group. - `diskAccessibilityTests`: Tests that check that the   destination host or cluster can see the datastores where the virtual   machine's virtual disks are currently located.      The destination   resource pool is irrelevant. If you are planning to relocate the   virtual disks, do not use these tests; instead examine the relevant   datastore objects for your planned disk locations to see if they   are accessible to the destination host. - `resourceTests`: Tests that check that the destination resource   pool can support the virtual machine if it is powered on.      The   destination host or cluster is relevant because it will affect the   amount of overhead memory required to run the virtual machine. 
    """

    """
    allowed enum values
    """
    SOURCETESTS = 'sourceTests'
    COMPATIBILITYTESTS = 'compatibilityTests'
    DISKACCESSIBILITYTESTS = 'diskAccessibilityTests'
    RESOURCETESTS = 'resourceTests'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ValidateMigrationTestTypeEnum from a JSON string"""
        return cls(json.loads(json_str))

