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
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostNatServicePortForwardSpec(DataObject):
    """
    This data object type describes the Network Address Translation (NAT) port forwarding specification.  ***Since:*** VI API 2.5 
    """ # noqa: E501
    type: StrictStr = Field(description="Either \"tcp\" or \"udp\".  ***Since:*** VI API 2.5 ")
    name: StrictStr = Field(description="The user-defined name to identify the service being forwarded.  No white spaces are allowed in the string.  ***Since:*** VI API 2.5 ")
    host_port: StrictInt = Field(description="The port number on the host.  Network traffic sent to the host on this TCP/UDP port is forwarded to the guest at the specified IP address and port.  ***Since:*** VI API 2.5 ", alias="hostPort")
    guest_port: StrictInt = Field(description="The port number for the guest.  Network traffic from the host is forwarded to this port.  ***Since:*** VI API 2.5 ", alias="guestPort")
    guest_ip_address: StrictStr = Field(description="The IP address for the guest.  Network traffic from the host is forwarded to this IP address.  ***Since:*** VI API 2.5 ", alias="guestIpAddress")
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
        """Create an instance of HostNatServicePortForwardSpec from a JSON string"""
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
        """Create an instance of HostNatServicePortForwardSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

