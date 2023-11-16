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


from typing import Any, ClassVar, Dict, List, Optional

from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_vmfs_rescan_result import HostVmfsRescanResult
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostResignatureRescanResult(DataObject):
    """
    The *HostResignatureRescanResult* data object identifies the newly created volume that is the result of a resignature operation.  This data object is contained in the task object returned by the *HostDatastoreSystem.ResignatureUnresolvedVmfsVolume_Task* method.  When a client calls the resignature method, the Server resignatures the volume, rescans the specified list of hosts, and auto-mounts the volume on the other hosts that share the same underlying storage LUNs.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    rescan: Optional[List[HostVmfsRescanResult]] = Field(default=None, description="Deprecated as of vSphere API 5.1, the results of the operation are available when the task completes. That is, for shared volumes, the new volume is mounted on all of the connected hosts.  List of VMFS Rescan operation results.  ***Since:*** vSphere API 4.0 ")
    result: ManagedObjectReference
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
        """Create an instance of HostResignatureRescanResult from a JSON string"""
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
        """Create an instance of HostResignatureRescanResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


