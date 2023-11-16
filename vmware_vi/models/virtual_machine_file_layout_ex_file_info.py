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

class VirtualMachineFileLayoutExFileInfo(DataObject):
    """
    Basic information about a file.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    key: StrictInt = Field(description="Key to reference this file.  ***Since:*** vSphere API 4.0 ")
    name: StrictStr = Field(description="Name of the file, including the complete datastore path.  ***Since:*** vSphere API 4.0 ")
    type: StrictStr = Field(description="Type of the file.  *VirtualMachineFileLayoutExFileType_enum* lists all valid values.  ***Since:*** vSphere API 4.0 ")
    size: StrictInt = Field(description="Size of the file in bytes.  ***Since:*** vSphere API 4.0 ")
    unique_size: Optional[StrictInt] = Field(default=None, description="Size of the file in bytes corresponding to the file blocks that were allocated uniquely.  In other words, if the underlying storage supports sharing of file blocks across disk files, the property corresponds to the size of the file blocks that were allocated only in context of this file, i.e. it does not include shared blocks that were allocated in other files. This property will be unset if the underlying implementation is unable to compute this information. One example of this is when the file resides on a NAS datastore whose underlying storage doesn't support this metric. In some cases the field might be set but the value could be over-estimated due to the inability of the NAS based storage to provide an accurate value.  ***Since:*** vSphere API 5.1 ", alias="uniqueSize")
    backing_object_id: Optional[StrictStr] = Field(default=None, description="Backing object's durable and unmutable identifier.  Each backing object has a unique identifier which is not settable. This property is applied to the file backed by a storage object, such as vvol.  ***Since:*** vSphere API 6.0 ", alias="backingObjectId")
    accessible: Optional[StrictBool] = Field(default=None, description="Flag which indicates the accessibility of the file when the file info object was created.  ***Since:*** vSphere API 6.0 ")
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
        """Create an instance of VirtualMachineFileLayoutExFileInfo from a JSON string"""
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
        """Create an instance of VirtualMachineFileLayoutExFileInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

