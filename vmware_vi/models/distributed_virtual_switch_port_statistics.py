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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DistributedVirtualSwitchPortStatistics(DataObject):
    """
    Statistic data of a DistributedVirtualPort.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    packets_in_multicast: StrictInt = Field(description="The number of multicast packets received.  ***Since:*** vSphere API 4.0 ", alias="packetsInMulticast")
    packets_out_multicast: StrictInt = Field(description="The number of multicast packets forwarded.  ***Since:*** vSphere API 4.0 ", alias="packetsOutMulticast")
    bytes_in_multicast: StrictInt = Field(description="The number of bytes received from multicast packets.  ***Since:*** vSphere API 4.0 ", alias="bytesInMulticast")
    bytes_out_multicast: StrictInt = Field(description="The number of bytes forwarded from multicast packets.  ***Since:*** vSphere API 4.0 ", alias="bytesOutMulticast")
    packets_in_unicast: StrictInt = Field(description="The number of unicast packets received.  ***Since:*** vSphere API 4.0 ", alias="packetsInUnicast")
    packets_out_unicast: StrictInt = Field(description="The number of unicast packets forwarded.  ***Since:*** vSphere API 4.0 ", alias="packetsOutUnicast")
    bytes_in_unicast: StrictInt = Field(description="The number of bytes received from unicast packets.  ***Since:*** vSphere API 4.0 ", alias="bytesInUnicast")
    bytes_out_unicast: StrictInt = Field(description="The number of bytes forwarded from unicast packets.  ***Since:*** vSphere API 4.0 ", alias="bytesOutUnicast")
    packets_in_broadcast: StrictInt = Field(description="The number of broadcast packets received.  ***Since:*** vSphere API 4.0 ", alias="packetsInBroadcast")
    packets_out_broadcast: StrictInt = Field(description="The number of broadcast packets forwarded.  ***Since:*** vSphere API 4.0 ", alias="packetsOutBroadcast")
    bytes_in_broadcast: StrictInt = Field(description="The number of bytes received from broadcast packets.  ***Since:*** vSphere API 4.0 ", alias="bytesInBroadcast")
    bytes_out_broadcast: StrictInt = Field(description="The number of bytes forwarded from broadcast packets.  ***Since:*** vSphere API 4.0 ", alias="bytesOutBroadcast")
    packets_in_dropped: StrictInt = Field(description="The number of received packets dropped.  ***Since:*** vSphere API 4.0 ", alias="packetsInDropped")
    packets_out_dropped: StrictInt = Field(description="The number of packets to be forwarded dropped.  ***Since:*** vSphere API 4.0 ", alias="packetsOutDropped")
    packets_in_exception: StrictInt = Field(description="The number of packets received that cause an exception.  ***Since:*** vSphere API 4.0 ", alias="packetsInException")
    packets_out_exception: StrictInt = Field(description="The number of packets to be forwarded that cause an exception.  ***Since:*** vSphere API 4.0 ", alias="packetsOutException")
    bytes_in_from_pnic: Optional[StrictInt] = Field(default=None, description="The number of bytes received at a pnic on the behalf of a port's connectee (inter-host rx).  ***Since:*** vSphere API 6.5 ", alias="bytesInFromPnic")
    bytes_out_to_pnic: Optional[StrictInt] = Field(default=None, description="The number of bytes transmitted at a pnic on the behalf of a port's connectee (inter-host tx).  ***Since:*** vSphere API 6.5 ", alias="bytesOutToPnic")
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
        """Create an instance of DistributedVirtualSwitchPortStatistics from a JSON string"""
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
        """Create an instance of DistributedVirtualSwitchPortStatistics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


