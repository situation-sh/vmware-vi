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
from typing_extensions import Annotated
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostDiskPartitionAttributes(DataObject):
    """
    Information about a single disk partition.  A partition is a contiguous set of blocks on a disk that is marked for use. The typeId identifies the purpose of the data in the partition. 
    """ # noqa: E501
    partition: StrictInt = Field(description="The partition number.  Must be a positive integer. ")
    start_sector: StrictInt = Field(description="The start sector. ", alias="startSector")
    end_sector: StrictInt = Field(description="The end sector. ", alias="endSector")
    type: StrictStr = Field(description="Type of data in the partition.  If it is a well-known partition type, it will be one of the defined types. If it is not, then it will be reported as a hexadecimal number. For example, \"none\", \"vmfs\", \"linux\", and \"0x20\" are all valid values.  See also *HostDiskPartitionInfoType_enum*. ")
    guid: Optional[StrictStr] = Field(default=None, description="Globally Unique Identifier of the partition, as defined by the GUID Partition Table (GPT) format.  This is available only for GPT formatted disks.  ***Since:*** vSphere API 5.0 ")
    logical: StrictBool = Field(description="The flag to indicate whether or not the partition is logical.  If true, the partition number should be greater than 4. ")
    attributes: Annotated[int, Field(le=127, strict=True, ge=-128)] = Field(description="The attributes on the partition. ")
    partition_alignment: Optional[StrictInt] = Field(default=None, description="Partition alignment in bytes.  If unset, partition alignment value is unknown.  ***Since:*** vSphere API 5.0 ", alias="partitionAlignment")
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
        """Create an instance of HostDiskPartitionAttributes from a JSON string"""
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
        """Create an instance of HostDiskPartitionAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

