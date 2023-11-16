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
from vmware_vi.models.datastore_option import DatastoreOption
from vmware_vi.models.guest_os_descriptor import GuestOsDescriptor
from vmware_vi.models.virtual_device import VirtualDevice
from vmware_vi.models.virtual_hardware_option import VirtualHardwareOption
from vmware_vi.models.virtual_machine_capability import VirtualMachineCapability
from vmware_vi.models.virtual_machine_property_relation import VirtualMachinePropertyRelation
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualMachineConfigOption(DataObject):
    """
    This configuration data object type contains information about the execution environment for a virtual machine.  This includes information about which features are supported, such as: - Which guest operating systems are supported. - How devices are emulated. For example, that a CD-ROM drive can be emulated   with a file or that a serial port can be emulated with a pipe.    VirtualCenter can provide a broader environment than any single physical host. This is a departure from traditional virtualization approaches, which rely on the host system to define the environment for virtual machines. This data object describes environment capabilities and is used by VirtualCenter to choose hosts on which to run virtual machines. 
    """ # noqa: E501
    version: StrictStr = Field(description="The version corresponding to this configOption. ")
    description: StrictStr = Field(description="A description string for this configOption. ")
    guest_os_descriptor: List[GuestOsDescriptor] = Field(description="List of supported guest operating systems.  The choice of guest operating system may limit the set of valid devices. For example, you cannot select Vmxnet with all guest operating systems. ", alias="guestOSDescriptor")
    guest_os_default_index: StrictInt = Field(description="Index into guestOsDescriptor array denoting the default guest operating system. ", alias="guestOSDefaultIndex")
    hardware_options: VirtualHardwareOption = Field(alias="hardwareOptions")
    capabilities: VirtualMachineCapability
    datastore: DatastoreOption
    default_device: Optional[List[VirtualDevice]] = Field(default=None, description="The list of virtual devices that are created on a virtual machine by default.  Clients should not create these devices. ", alias="defaultDevice")
    supported_monitor_type: List[StrictStr] = Field(description="The monitor types supported by a host.  The acceptable monitor types are enumerated by *VirtualMachineFlagInfoMonitorType_enum*.  ***Since:*** VI API 2.5 ", alias="supportedMonitorType")
    supported_ovf_environment_transport: Optional[List[StrictStr]] = Field(default=None, description="Specifies the supported property transports that are available for the OVF environment  ***Since:*** vSphere API 4.0 ", alias="supportedOvfEnvironmentTransport")
    supported_ovf_install_transport: Optional[List[StrictStr]] = Field(default=None, description="Specifies the supported transports for the OVF installation phase.  ***Since:*** vSphere API 4.0 ", alias="supportedOvfInstallTransport")
    property_relations: Optional[List[VirtualMachinePropertyRelation]] = Field(default=None, description="The relations between the properties of the virtual machine config spec.  ***Since:*** vSphere API 6.7 ", alias="propertyRelations")
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
        """Create an instance of VirtualMachineConfigOption from a JSON string"""
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
        """Create an instance of VirtualMachineConfigOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

