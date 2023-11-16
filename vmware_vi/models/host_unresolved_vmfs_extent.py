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
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_scsi_disk_partition import HostScsiDiskPartition
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostUnresolvedVmfsExtent(DataObject):
    """
    Information about an unresolved VMFS volume extent An unresolved VMFS volume extent is a device partition which is detected to have copy of an extent of a VMFS volume.  Such a copy can be created via replication or snapshots, for example.  See also *HostUnresolvedVmfsVolume*.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    device: HostScsiDiskPartition
    device_path: StrictStr = Field(description="The device path of an VMFS extent  ***Since:*** vSphere API 4.0 ", alias="devicePath")
    vmfs_uuid: StrictStr = Field(description="The UUID of the VMFS volume read from to the partition.  ***Since:*** vSphere API 4.0 ", alias="vmfsUuid")
    is_head_extent: StrictBool = Field(description="Is this a copy of the head extent of the VMFS volume?  ***Since:*** vSphere API 4.0 ", alias="isHeadExtent")
    ordinal: StrictInt = Field(description="A number indicating the order of an extent in a volume.  An extent with a lower ordinal value than another extent provides a range of blocks to a volume at an earlier block address range. Extents with the same ordinal provide the same range of blocks to a volume. A zero ordinal indicates that the extent is a head extent.  In the case each extent in the *HostUnresolvedVmfsVolume* is represented in the list of *HostUnresolvedVmfsExtent* data objects, the ordinal will refer to the absolute index of the extent in the volume. For example, ordinal \"1\" refers to the second extent; ordinal \"2\" refers to the third extent.  In the case that some extents of the volume are not represented in the *HostUnresolvedVmfsExtent* list, the ordinal will not precisely describe the position in the list of extents. A number will be skipped to indicate holes in the extent order. For example, given a volume with five extents with the second and third extents missing, the ordinal values in use will be {0, 2, 3}. The missing second and third extent are represented by the missing ordinal value \"1\" while the fourth and fifth extents will be assigned an ordinal of \"2\" and \"3\" respectively.  The reason the ordinals are not reliable in the case of missing extents is because the extents are identified by their start and end blocks. The ordinals are just a hint used to help indicate extents that correspond to the same start and end blocks.  ***Since:*** vSphere API 4.0 ")
    start_block: StrictInt = Field(description="Index of the first block that this extent provides.  ***Since:*** vSphere API 4.0 ", alias="startBlock")
    end_block: StrictInt = Field(description="Index of the last block that this extent provides.  ***Since:*** vSphere API 4.0 ", alias="endBlock")
    reason: StrictStr = Field(description="Reason as to why the partition is marked as copy of a VMFS volume's extent.  Possible reasons are the disk id is not matching with what the scsi inq is saying or disk uuid is not matching  See also *HostUnresolvedVmfsExtentUnresolvedReason_enum*.  ***Since:*** vSphere API 4.0 ")
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
        """Create an instance of HostUnresolvedVmfsExtent from a JSON string"""
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
        """Create an instance of HostUnresolvedVmfsExtent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


