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
from vmware_vi.models.numeric_range import NumericRange
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DVPortStatus(DataObject):
    """
    The *DVPortStatus* data object contains runtime information about a *DistributedVirtualPort*.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    link_up: StrictBool = Field(description="Indicates whether the port is in linkUp status.  ***Since:*** vSphere API 4.0 ", alias="linkUp")
    blocked: StrictBool = Field(description="Indicates whether the port is blocked by switch implementation.  ***Since:*** vSphere API 4.0 ")
    vlan_ids: Optional[List[NumericRange]] = Field(default=None, description="VLAN ID of the port.  ***Since:*** vSphere API 4.0 ", alias="vlanIds")
    trunking_mode: Optional[StrictBool] = Field(default=None, description="True if the port VLAN tagging/stripping is disabled.  ***Since:*** vSphere API 4.0 ", alias="trunkingMode")
    mtu: Optional[StrictInt] = Field(default=None, description="Maximum transmission unit (MTU) of the port.  You can set the MTU only at the switch level (*VMwareDVSConfigSpec*). If you attempt to change it at the portgroup or port level, the Server throws an exception.  ***Since:*** vSphere API 4.0 ")
    link_peer: Optional[StrictStr] = Field(default=None, description="Name of the connected entity.  ***Since:*** vSphere API 4.0 ", alias="linkPeer")
    mac_address: Optional[StrictStr] = Field(default=None, description="The MAC address that is used at this port.  ***Since:*** vSphere API 4.0 ", alias="macAddress")
    status_detail: Optional[StrictStr] = Field(default=None, description="Additional information regarding the current status of the port.  ***Since:*** vSphere API 4.1 ", alias="statusDetail")
    vm_direct_path_gen2_active: Optional[StrictBool] = Field(default=None, description="Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  Indicates whether VMDirectPath Gen 2 is active on this port.  If false, the reason(s) for inactivity will be provided in one or more of *DVPortStatus.vmDirectPathGen2InactiveReasonNetwork*, *DVPortStatus.vmDirectPathGen2InactiveReasonOther*, and *DVPortStatus.vmDirectPathGen2InactiveReasonExtended*.  If the host software is not capable of VMDirectPath Gen 2, this property will be unset. See *HostCapability*.*HostCapability.vmDirectPathGen2Supported*.  ***Since:*** vSphere API 4.1 ", alias="vmDirectPathGen2Active")
    vm_direct_path_gen2_inactive_reason_network: Optional[List[StrictStr]] = Field(default=None, description="Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *DVPortStatus.vmDirectPathGen2Active* is false, this array will be populated with reasons for the inactivity that are related to network state or configuration.  The reasons are chosen from the *DVPortStatusVmDirectPathGen2InactiveReasonNetwork_enum* values.  Other reasons for inactivity will be provided in *DVPortStatus.vmDirectPathGen2InactiveReasonOther*. If there is a reason for inactivity that cannot be described by the available constants, *DVPortStatus.vmDirectPathGen2InactiveReasonExtended* will be populated with an additional explanation provided by the platform.  Note that this list of reasons is not guaranteed to be exhaustive.  ***Since:*** vSphere API 4.1 ", alias="vmDirectPathGen2InactiveReasonNetwork")
    vm_direct_path_gen2_inactive_reason_other: Optional[List[StrictStr]] = Field(default=None, description="Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *DVPortStatus.vmDirectPathGen2Active* is false, this array will be populated with reasons for the inactivity that are not related to network state or configuration.  The reasons are chosen from the *DVPortStatusVmDirectPathGen2InactiveReasonOther_enum* values.  Network-related reasons for inactivity will be provided in *DVPortStatus.vmDirectPathGen2InactiveReasonNetwork*. If there is a reason for inactivity that cannot be described by the available constants, *DVPortStatus.vmDirectPathGen2InactiveReasonExtended* will be populated with an additional explanation provided by the platform.  Note that this list of reasons is not guaranteed to be exhaustive.  See also *HostCapability.vmDirectPathGen2Supported*.  ***Since:*** vSphere API 4.1 ", alias="vmDirectPathGen2InactiveReasonOther")
    vm_direct_path_gen2_inactive_reason_extended: Optional[StrictStr] = Field(default=None, description="Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *DVPortStatus.vmDirectPathGen2Active* is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) listed in *DVPortStatus.vmDirectPathGen2InactiveReasonNetwork* and/or *DVPortStatus.vmDirectPathGen2InactiveReasonOther*.  ***Since:*** vSphere API 4.1 ", alias="vmDirectPathGen2InactiveReasonExtended")
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
        """Create an instance of DVPortStatus from a JSON string"""
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
        """Create an instance of DVPortStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

