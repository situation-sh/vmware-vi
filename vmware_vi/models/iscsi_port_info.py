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
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_virtual_nic import HostVirtualNic
from vmware_vi.models.iscsi_status import IscsiStatus
from vmware_vi.models.physical_nic import PhysicalNic
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IscsiPortInfo(DataObject):
    """
    The *IscsiPortInfo* data object describes the Virtual NIC that are bound to an iSCSI adapter and also it describes the candidate Virtual NICs that can be bound to a given iSCSI adapter.  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    vnic_device: Optional[StrictStr] = Field(default=None, description="Virtual NIC Name.  Contains the name of the Virtual NIC device. This may be unset in case where the bound Virtual NIC doesn't have the system object or where a candidate Physical NIC isn't associated with any Virtual NIC.  ***Since:*** vSphere API 5.0 ", alias="vnicDevice")
    vnic: Optional[HostVirtualNic] = None
    pnic_device: Optional[StrictStr] = Field(default=None, description="Physical NIC Name.  ***Since:*** vSphere API 5.0 ", alias="pnicDevice")
    pnic: Optional[PhysicalNic] = None
    switch_name: Optional[StrictStr] = Field(default=None, description="Name of the virtual switch this Physical/Virtual NIC belongs.  May be unset if the vnicDevice and/or pnicDevice do not have a virtual switch associated with them.  ***Since:*** vSphere API 5.0 ", alias="switchName")
    switch_uuid: Optional[StrictStr] = Field(default=None, description="UUID of the virtual switch this Physical/Virtual NIC belongs.  May be unset if the vnicDevice and/or pnicDevice do not have a virtual switch associated with them or the associated switch is not VDS.  ***Since:*** vSphere API 5.0 ", alias="switchUuid")
    portgroup_name: Optional[StrictStr] = Field(default=None, description="Name of the portgroup to which this Virtual NIC belongs.  May be unset if the vnicDevice and/or pnicDevice do not have a Portgroup associated with them.  ***Since:*** vSphere API 5.0 ", alias="portgroupName")
    portgroup_key: Optional[StrictStr] = Field(default=None, description="Portgroup key to which this Virtual NIC belongs.  May be unset if the vnicDevice and/or pnicDevice do not have a Portgroup associated with them or the associated portgroup does is not of VDS type.  ***Since:*** vSphere API 5.0 ", alias="portgroupKey")
    port_key: Optional[StrictStr] = Field(default=None, description="portkey to which this Virtual NIC belongs.  May be unset if the vnicDevice is not assigned to a specific port or the switch is not VDS.  ***Since:*** vSphere API 5.0 ", alias="portKey")
    opaque_network_id: Optional[StrictStr] = Field(default=None, description="ID of the Opaque network to which the virtual NIC is connected.  This property is set only when vnicDevice is associated with an opaque network.  ***Since:*** vSphere API 6.5 ", alias="opaqueNetworkId")
    opaque_network_type: Optional[StrictStr] = Field(default=None, description="Type of the Opaque network to which the virtual NIC is connected.  This property is set only when vnicDevice is associated with an opaque network.  ***Since:*** vSphere API 6.5 ", alias="opaqueNetworkType")
    opaque_network_name: Optional[StrictStr] = Field(default=None, description="Name of the Opaque network to which the virtual NIC is connected.  This property is set only when vnicDevice is associated with an opaque network.  ***Since:*** vSphere API 6.5 ", alias="opaqueNetworkName")
    external_id: Optional[StrictStr] = Field(default=None, description="An ID assigned to the vmkernel adapter by external management plane or controller.  This property is set only when vnicDevice is associated with an opaque network.  ***Since:*** vSphere API 6.5 ", alias="externalId")
    compliance_status: Optional[IscsiStatus] = Field(default=None, alias="complianceStatus")
    path_status: Optional[StrictStr] = Field(default=None, description="A status, as defined in *IscsiPortInfoPathStatus_enum*, indicating the existing storage paths dependency level on a given Virtual NIC.  May be unset in the candidate NIC list.  ***Since:*** vSphere API 5.0 ", alias="pathStatus")
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
        """Create an instance of IscsiPortInfo from a JSON string"""
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
        """Create an instance of IscsiPortInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


