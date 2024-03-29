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
from vmware_vi.models.v_mware_vspan_port import VMwareVspanPort
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VMwareVspanSession(DataObject):
    """
    The *VMwareVspanSession* data object defines the configuration of a VLAN Services and Protocols for Advanced Networks (VSPAN) session.  You use a VSPAN session for the following operations: - To mirror network traffic (inbound/outbound) from a set of source   entities to a set of destination entities. - To assist in troubleshooting. - As input for security and other network analysis appliances.    The type of entities that you can specify as source or destination is determined by the session type. You can use uplink distributed virtual ports only for mixed destination mirror VSPAN sessions (mixedDestMirror). For all sessions except mixedDestMirror sessions, you cannot use uplink distributed virtual ports as destination ports. sessionType is required for vSphere Distributed Switch 5.1 and later, ignored for prior version if set. <table> <thead> <tr> <th>Session Type</th> <th>Source</th> <th>Destination </th> </tr> </thead> <tbody> <tr> <td>mixedDestMirror</td> <td>Distributed Ports</td> <td>Distributed Ports + Uplink Ports Name</td> </tr> <tr> <td>dvPortMirror</td> <td>Distributed Ports</td> <td>Distributed Ports</td> </tr> <tr> <td>remoteMirrorSource</td> <td>Distributed Ports</td> <td>Uplink Ports Name</td> </tr> <tr> <td>remoteMirrorDest</td> <td>VLAN</td> <td>Distributed Ports</td> </tr> <tr> <td>encapRemoteMirrorSource</td> <td>Distributed Ports</td> <td>IP address</td> </tr> </tbody> </table>  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    key: Optional[StrictStr] = Field(default=None, description="The generated key as the identifier for the session.  ***Since:*** vSphere API 5.0 ")
    name: Optional[StrictStr] = Field(default=None, description="The display name.  ***Since:*** vSphere API 5.0 ")
    description: Optional[StrictStr] = Field(default=None, description="The description for the session.  ***Since:*** vSphere API 5.0 ")
    enabled: StrictBool = Field(description="Whether the session is enabled.  ***Since:*** vSphere API 5.0 ")
    source_port_transmitted: Optional[VMwareVspanPort] = Field(default=None, alias="sourcePortTransmitted")
    source_port_received: Optional[VMwareVspanPort] = Field(default=None, alias="sourcePortReceived")
    destination_port: Optional[VMwareVspanPort] = Field(default=None, alias="destinationPort")
    encapsulation_vlan_id: Optional[StrictInt] = Field(default=None, description="VLAN ID used to encapsulate the mirrored traffic.  ***Since:*** vSphere API 5.0 ", alias="encapsulationVlanId")
    strip_original_vlan: StrictBool = Field(description="Whether to strip the original VLAN tag.  if false, the original VLAN tag will be preserved on the mirrored traffic. If *VMwareVspanSession.encapsulationVlanId* has been set and this property is false, the frames will be double tagged with the original VLAN ID as the inner tag.  ***Since:*** vSphere API 5.0 ", alias="stripOriginalVlan")
    mirrored_packet_length: Optional[StrictInt] = Field(default=None, description="An integer that describes how much of each frame to mirror.  If unset, all of the frame would be mirrored. Setting this property to a smaller value is useful when the consumer will look only at the headers. The value cannot be less than 60.  ***Since:*** vSphere API 5.0 ", alias="mirroredPacketLength")
    normal_traffic_allowed: StrictBool = Field(description="Whether or not destination ports can send and receive \"normal\" traffic.  Setting this to false will make mirror ports be used solely for mirroring and not double as normal access ports.  ***Since:*** vSphere API 5.0 ", alias="normalTrafficAllowed")
    session_type: Optional[StrictStr] = Field(default=None, description="Type of the session.  See *VMwareDVSVspanSessionType_enum* for valid values. Default value is mixedDestMirror if unspecified in a VSPAN create operation.  ***Since:*** vSphere API 5.1 ", alias="sessionType")
    sampling_rate: Optional[StrictInt] = Field(default=None, description="Sampling rate of the session.  If its value is n, one of every n packets is mirrored. Valid values are between 1 to 65535, and default value is 1.  ***Since:*** vSphere API 5.1 ", alias="samplingRate")
    encap_type: Optional[StrictStr] = Field(default=None, description="Encapsulation type of the session.  See *VMwareDVSVspanSessionEncapType_enum* for valid values. Default value is encapProtocolGRE if unspecified in a VSPAN create operation.  ***Since:*** vSphere API 6.5 ", alias="encapType")
    erspan_id: Optional[StrictInt] = Field(default=None, description="ERSPAN ID of the session.  Valid values are between 0 to 0x3ff, and default value is 0. This value is applicable only if encaptType is *erspan2* or *erspan3*  ***Since:*** vSphere API 6.5 ", alias="erspanId")
    erspan_cos: Optional[StrictInt] = Field(default=None, description="Class of Service of the monitored frame.  Valid values are between 0 to 7, and default value is 0. This value is applicable only if encaptType is *erspan2* or *erspan3*  ***Since:*** vSphere API 6.5 ", alias="erspanCOS")
    erspan_gra_nanosec: Optional[StrictBool] = Field(default=None, description="Timestamp Granularity.  If the value is false, timestamp-granularity will be microsecond. Otherwise the timestamp-granularity will be nanosecond This value is applicable only if encaptType is *erspan3*  ***Since:*** vSphere API 6.5 ", alias="erspanGraNanosec")
    netstack: Optional[StrictStr] = Field(default=None, description="Netstack instance of the session.  ***Since:*** vSphere API 6.7 ")
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
        """Create an instance of VMwareVspanSession from a JSON string"""
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
        """Create an instance of VMwareVspanSession from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


