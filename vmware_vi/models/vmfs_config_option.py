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
from pydantic import StrictInt
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.long_option import LongOption
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VmfsConfigOption(DataObject):
    """
    VmfsConfigOption
    """ # noqa: E501
    block_size_option: StrictInt = Field(description="Supported values of VMFS block size in kilobytes (KB) *HostVmfsVolume.blockSize*.  ***Since:*** vSphere API 6.5 ", alias="blockSizeOption")
    unmap_granularity_option: Optional[List[StrictInt]] = Field(default=None, description="Supported values of VMFS unmap granularity *HostVmfsVolume.unmapGranularity*.  The unit is KB.  ***Since:*** vSphere API 6.5 ", alias="unmapGranularityOption")
    unmap_bandwidth_fixed_value: Optional[LongOption] = Field(default=None, alias="unmapBandwidthFixedValue")
    unmap_bandwidth_dynamic_min: Optional[LongOption] = Field(default=None, alias="unmapBandwidthDynamicMin")
    unmap_bandwidth_dynamic_max: Optional[LongOption] = Field(default=None, alias="unmapBandwidthDynamicMax")
    unmap_bandwidth_increment: Optional[StrictInt] = Field(default=None, description="Increment value of unmap bandwidth  ***Since:*** vSphere API 6.7 ", alias="unmapBandwidthIncrement")
    unmap_bandwidth_ultra_low: Optional[StrictInt] = Field(default=None, description="Fixed unmap bandwidth ultra low limit value in MB/sec. ", alias="unmapBandwidthUltraLow")
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
        """Create an instance of VmfsConfigOption from a JSON string"""
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
        """Create an instance of VmfsConfigOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


