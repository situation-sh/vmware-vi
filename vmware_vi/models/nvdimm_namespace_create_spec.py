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
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NvdimmNamespaceCreateSpec(DataObject):
    """
    Deprecated as of vSphere 6.7u1, use PMemNamespaceCreateReq.  Arguments for creating a namespace.  ***Since:*** vSphere API 6.7 
    """ # noqa: E501
    friendly_name: Optional[StrictStr] = Field(default=None, description="Friendly name of the namespace to be created.  A friendly name can be provided by user to assosiate a name to the created namespace, but such a name is not mandatory and is empty string by default.  ***Since:*** vSphere API 6.7 ", alias="friendlyName")
    block_size: StrictInt = Field(description="Size of block in the namespace.  For persistent region type, block size is one. For block region, block size represents one of the logical block sizes of 512, 4096 etc.  ***Since:*** vSphere API 6.7 ", alias="blockSize")
    block_count: StrictInt = Field(description="Number of blocks in the namespace.  For persistent region type, blockCount is the size of persistent region in bytes. For block region type, block count represent number of bytes per block size.  ***Since:*** vSphere API 6.7 ", alias="blockCount")
    type: StrictStr = Field(description="Type of the namespace to be created - block or persistent.  Must be one of the values in *NvdimmNamespaceType_enum*  ***Since:*** vSphere API 6.7 ")
    location_id: StrictInt = Field(description="This identifier is the interleave set ID if the namespace is being used in persistent mode.  If in block mode, this is a device handle.  ***Since:*** vSphere API 6.7 ", alias="locationID")
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
        """Create an instance of NvdimmNamespaceCreateSpec from a JSON string"""
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
        """Create an instance of NvdimmNamespaceCreateSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


