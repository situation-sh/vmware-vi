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
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.fcoe_config import FcoeConfig
from vmware_vi.models.host_rdma_device import HostRdmaDevice
from vmware_vi.models.physical_nic_link_info import PhysicalNicLinkInfo
from vmware_vi.models.physical_nic_spec import PhysicalNicSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PhysicalNic(DataObject):
    """
    This data object type describes the physical network adapter as seen by the primary operating system. 
    """ # noqa: E501
    key: Optional[StrictStr] = Field(default=None, description="The linkable identifier. ")
    device: StrictStr = Field(description="The device name of the physical network adapter. ")
    pci: StrictStr = Field(description="Device hash of the PCI device corresponding to this physical network adapter. ")
    driver: Optional[StrictStr] = Field(default=None, description="The name of the driver.  From command line: esxcli network nic get ")
    driver_version: Optional[StrictStr] = Field(default=None, description="The version of the physical network adapter operating system driver. ", alias="driverVersion")
    firmware_version: Optional[StrictStr] = Field(default=None, description="The version of the firmware running in the network adapter. ", alias="firmwareVersion")
    link_speed: Optional[PhysicalNicLinkInfo] = Field(default=None, alias="linkSpeed")
    valid_link_specification: Optional[List[PhysicalNicLinkInfo]] = Field(default=None, description="The valid combinations of speed and duplexity for this physical network adapter.  The speed and the duplex settings usually must be configured as a pair. This array lists all the valid combinations available for a physical network adapter.  Autonegotiate is not listed as one of the combinations supported. If is implicitly supported by the physical network adapter unless *PhysicalNic.autoNegotiateSupported* is set to false. ", alias="validLinkSpecification")
    spec: PhysicalNicSpec
    wake_on_lan_supported: StrictBool = Field(description="Flag indicating whether the NIC is wake-on-LAN capable  ***Since:*** VI API 2.5 ", alias="wakeOnLanSupported")
    mac: StrictStr = Field(description="The media access control (MAC) address of the physical network adapter.  ***Since:*** VI API 2.5 ")
    fcoe_configuration: Optional[FcoeConfig] = Field(default=None, alias="fcoeConfiguration")
    vm_direct_path_gen2_supported: Optional[StrictBool] = Field(default=None, description="Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  Flag indicating whether the NIC supports VMDirectPath Gen 2.  Note that this is only an indicator of the capabilities of this NIC, not of the whole host.  If the host software is not capable of VMDirectPath Gen 2, this property will be unset, as the host cannot provide information on the NIC capability.  See also *HostCapability.vmDirectPathGen2Supported*.  ***Since:*** vSphere API 4.1 ", alias="vmDirectPathGen2Supported")
    vm_direct_path_gen2_supported_mode: Optional[StrictStr] = Field(default=None, description="Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *PhysicalNic.vmDirectPathGen2Supported* is true, this property advertises the VMDirectPath Gen 2 mode supported by this NIC (chosen from *PhysicalNicVmDirectPathGen2SupportedMode_enum*).  A mode may require that the associated vSphere Distributed Switch have a particular ProductSpec in order for network passthrough to be possible.  ***Since:*** vSphere API 4.1 ", alias="vmDirectPathGen2SupportedMode")
    resource_pool_scheduler_allowed: Optional[StrictBool] = Field(default=None, description="Flag indicating whether the NIC allows resource pool based scheduling for network I/O control.  ***Since:*** vSphere API 4.1 ", alias="resourcePoolSchedulerAllowed")
    resource_pool_scheduler_disallowed_reason: Optional[List[StrictStr]] = Field(default=None, description="If *PhysicalNic.resourcePoolSchedulerAllowed* is false, this property advertises the reason for disallowing resource scheduling on this NIC.  The reasons may be one of *PhysicalNicResourcePoolSchedulerDisallowedReason_enum*  ***Since:*** vSphere API 4.1 ", alias="resourcePoolSchedulerDisallowedReason")
    auto_negotiate_supported: Optional[StrictBool] = Field(default=None, description="If set the flag indicates if the physical network adapter supports autonegotiate.  ***Since:*** vSphere API 4.1 ", alias="autoNegotiateSupported")
    enhanced_networking_stack_supported: Optional[StrictBool] = Field(default=None, description="If set the flag indicates whether a physical nic supports Enhanced Networking Stack driver  ***Since:*** vSphere API 6.7 ", alias="enhancedNetworkingStackSupported")
    ens_interrupt_supported: Optional[StrictBool] = Field(default=None, description="If set the flag indicates whether a physical nic supports Enhanced Networking Stack interrupt mode  ***Since:*** vSphere API 7.0 ", alias="ensInterruptSupported")
    rdma_device: Optional[HostRdmaDevice] = Field(default=None, alias="rdmaDevice")
    dpu_id: Optional[StrictStr] = Field(default=None, description="The identifier of the DPU by which the physical NIC is backed.  When physical NIC is not backed by DPU, dpuId will be unset. ", alias="dpuId")
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
        """Create an instance of PhysicalNic from a JSON string"""
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
        """Create an instance of PhysicalNic from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

