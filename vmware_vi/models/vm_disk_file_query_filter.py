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
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VmDiskFileQueryFilter(DataObject):
    """
    The filter for the virtual disk primary file. 
    """ # noqa: E501
    disk_type: Optional[List[StrictStr]] = Field(default=None, description="If this optional property is set, only the virtual disk primary files that match one of the specified disk types are selected.  If no disk types are specified, this search criteria is ignored.  The specified disk type is one of the backing information types for a virtual disk.  See also *VirtualDisk*. ", alias="diskType")
    match_hardware_version: Optional[List[StrictInt]] = Field(default=None, description="If this optional property is set, only virtual disk primary files that match one of the specified hardware versions are selected.  If no versions are specified, this search criteria is ignored. ", alias="matchHardwareVersion")
    controller_type: Optional[List[StrictStr]] = Field(default=None, description="Deprecated as of vSphere API 5.0, this property is no longer relevant and should not be used. With the current state of emulation, we don't care about the adapter type a disk is connected to, as disks may be shuffled around. For example, a disk may be unplugged from a buslogic controller and plugged into an lsilogic controller.  If this optional property is set, only virtual disk files that have a controller type that matches one of the controller types specified are returned.  If no controller types are specified, this search criteria is ignored.  The specified controller type is one of the controller types for a virtual disk.  See also *VirtualIDEController*, *VirtualSCSIController*.  ***Since:*** VI API 2.5 ", alias="controllerType")
    thin: Optional[StrictBool] = Field(default=None, description="This optional property can be used to filter disks based on whether they are thin-provsioned or not: if set to true, only thin-provisioned disks are returned, and vice-versa.  ***Since:*** vSphere API 4.0 ")
    encrypted: Optional[StrictBool] = Field(default=None, description="This optional property can be used to filter disks based on whether they are encrypted or not.  ***Since:*** vSphere API 6.5 ")
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
        """Create an instance of VmDiskFileQueryFilter from a JSON string"""
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
        """Create an instance of VmDiskFileQueryFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


