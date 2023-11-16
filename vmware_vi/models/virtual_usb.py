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
from vmware_vi.models.virtual_device import VirtualDevice
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualUSB(VirtualDevice):
    """
    The *VirtualUSB* data object describes the USB device configuration for a virtual machine.  You can attach a USB device to an ESX host. The device is available to only one virtual machine at a time. When you remove the device from the virtual machine, it becomes available to other virtual machines located on the host. You can add up to 20 USB devices to a virtual machine. Virtual USB support requires virtual machine hardware version 7 or later.  The *VirtualUSB* object represents either a configuration to be applied to the virtual machine or the current device configuration on the virtual machine. - To configure a USB connection for the virtual machine, add a *VirtualUSB*   object to the *VirtualDeviceConfigSpec*.   Use USB backing (*VirtualUSBUSBBackingInfo*) to establish   a connection with a virtual machine that will remain on the host to which   the USB device is attached.   The vSphere Server does not support vMotion for standard USB backing.   To configure vMotion support for a virtual machine with a USB connection,   use remote host backing for the USB connection   (*VirtualUSBRemoteHostBackingInfo*).      To configure a USB device for a virtual machine, the virtual machine   must have a USB controller. To add a controller, include a   *VirtualUSBController* object in the virtual device   specification for your virtual machine configuration. You can add only one   USB controller to a virtual machine. - To determine USB device configuration status for the virtual machine,   check the virtual hardware device list   (*VirtualHardware*.*VirtualHardware.device*).   The presence of the *VirtualUSB* object in the hardware device list   indicates that the virtual machine is configured to use a USB device.   The *VirtualUSB.connected* property indicates   whether the virtual machine is connected to the device.    To determine the USB options available on the host, use the *EnvironmentBrowser.QueryConfigOption* method to retrieve the virtual machine configuration. The presence of the *VirtualUSBOption* object in the retrieved configuration (*VirtualMachineConfigOption*.*VirtualMachineConfigOption.hardwareOptions*.*VirtualHardwareOption.virtualDeviceOption*) indicates that the host supports USB connections.  The following operations will disconnect a USB device, losing data if data transfer is in progress over the USB connection. - Hot add of memory, CPU, or PCI devices. A hot add operation disconnects only   USB devices for virtual machines that use a local connection to the device   (*VirtualUSBUSBBackingInfo*). - Suspend and resume on a virtual machine. - vMotion of a virtual machine with a USB connection,   if you are not using remote host USB backing.    The following services do not support USB connections. - Fault Tolerance virtual machines cannot use USB devices. - DPM (Distributed Power Management) will put a host into standby,   regardless of any connections to USB devices on the host. - DRS (Distributed Resource Scheduling) may power-off hosts that have   USB connections to virtual machines. 
    """ # noqa: E501
    connected: StrictBool = Field(description="Flag indicating whether the device is currently connected.  The virtual machine is not connected to the device if the autoconnect pattern specified in the USB device backing (*VirtualDeviceDeviceBackingInfo*.*VirtualDeviceDeviceBackingInfo.deviceName*) can not be satisfied, either because there is no such device, or the matching device is not available. Valid only while the virtual machine is running.  ***Since:*** VI API 2.5 ")
    vendor: Optional[StrictInt] = Field(default=None, description="Vendor ID of the USB device.  ***Since:*** vSphere API 4.1 ")
    product: Optional[StrictInt] = Field(default=None, description="Product ID of the USB device.  ***Since:*** vSphere API 4.1 ")
    family: Optional[List[StrictStr]] = Field(default=None, description="Device class families.  For possible values see *VirtualMachineUsbInfoFamily_enum*.  ***Since:*** vSphere API 4.1 ")
    speed: Optional[List[StrictStr]] = Field(default=None, description="Device speeds detected by server.  For possible values see *VirtualMachineUsbInfoSpeed_enum*.  ***Since:*** vSphere API 4.1 ")
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
        """Create an instance of VirtualUSB from a JSON string"""
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
        """Create an instance of VirtualUSB from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


