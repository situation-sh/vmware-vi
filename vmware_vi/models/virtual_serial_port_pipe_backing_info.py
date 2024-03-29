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
from pydantic import StrictBool, StrictStr
from pydantic import Field
from vmware_vi.models.virtual_device_pipe_backing_info import VirtualDevicePipeBackingInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualSerialPortPipeBackingInfo(VirtualDevicePipeBackingInfo):
    """
    The <code>*VirtualSerialPortPipeBackingInfo*</code> data object defines information for backing a <code>*VirtualSerialPort*</code> with a named pipe.  You can use a pipe to connect a virtual serial port to a host application or to another virtual machine on the host computer. This is useful for capturing debugging information sent through the virtual serial port. 
    """ # noqa: E501
    endpoint: StrictStr = Field(description="Indicates the role the virtual machine assumes as an endpoint for the pipe.  The valid values are \"client\" or \"server\". ")
    no_rx_loss: Optional[StrictBool] = Field(default=None, description="Enables optimized data transfer over the pipe.  When you use this feature, the ESX server buffers data to prevent data overrun. This allows the virtual machine to read all of the data transferred over the pipe with no data loss. To use optimized data transfer, set <code>noRxLoss</code> to <code>true</code>. To disable this feature, set the property to <code>false.  This property is optional. If this property is not set, the ESX server uses the default value specified in the pipe backing options (noRxLoss.defaultValue - see <code>*VirtualSerialPortPipeBackingOption.noRxLoss*</code> in the pipe backing option object).  To use this property, optimized data transfer must be supported on the host. (See <code>*VirtualSerialPortPipeBackingOption.noRxLoss*</code> in the pipe backing option object.) If the ESX server does not support the option, it ignores the <code>noRxLoss</code> setting in the pipe backing information object.  **Note**: You can use this feature even if the other end of the pipe is not an application, but this is more likely to fail. ", alias="noRxLoss")
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
        """Create an instance of VirtualSerialPortPipeBackingInfo from a JSON string"""
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
        """Create an instance of VirtualSerialPortPipeBackingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


