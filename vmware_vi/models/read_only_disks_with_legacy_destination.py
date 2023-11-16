# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import StrictBool, StrictInt
from pydantic import Field
from vmware_vi.models.migration_fault import MigrationFault
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ReadOnlyDisksWithLegacyDestination(MigrationFault):
    """
    The virtual machine uses read-only (undoable or nonpersistent) disks that can cause a slower power on at the migration destination.  As a result, VMtion could slow down considerably or timeout. This is an issue only for migration of powered-on virtual machines from an ESX host with version greater than 2.0.x to an ESX host with version 2.0.x. It will be an error if the number of such disks is great enough to cause timeout ( &ge; 3 ), or a warning otherwise. 
    """ # noqa: E501
    ro_disk_count: StrictInt = Field(description="The number of read-only disks in use. ", alias="roDiskCount")
    timeout_danger: StrictBool = Field(description="Whether this number of disks will cause a timeout failure. ", alias="timeoutDanger")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReadOnlyDisksWithLegacyDestination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ReadOnlyDisksWithLegacyDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


