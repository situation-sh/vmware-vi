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
from typing_extensions import Annotated
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_cpu_id_info import HostCpuIdInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostCpuPackage(DataObject):
    """
    Information about a physical CPU package. 
    """ # noqa: E501
    index: Annotated[int, Field(le=32767, strict=True, ge=-32768)] = Field(description="Package index, starting from zero. ")
    vendor: StrictStr = Field(description="CPU vendor name, possible names currently are \"Intel\", \"AMD\", \"arm\", \"hygon\", or \"unknown\". ")
    hz: StrictInt = Field(description="CPU speed in HZ. ")
    bus_hz: StrictInt = Field(description="Bus speed in HZ. ", alias="busHz")
    description: StrictStr = Field(description="String summary description of CPU (for display purposes). ")
    thread_id: List[Annotated[int, Field(le=32767, strict=True, ge=-32768)]] = Field(description="The logical CPU threads on this package. ", alias="threadId")
    cpu_feature: Optional[List[HostCpuIdInfo]] = Field(default=None, description="The CPU feature bit on this particular CPU.  This is independent of the product and licensing capabilities. ", alias="cpuFeature")
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
        """Create an instance of HostCpuPackage from a JSON string"""
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
        """Create an instance of HostCpuPackage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


