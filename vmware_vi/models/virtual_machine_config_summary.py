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
from vmware_vi.models.fault_tolerance_config_info import FaultToleranceConfigInfo
from vmware_vi.models.managed_by_info import ManagedByInfo
from vmware_vi.models.v_app_product_info import VAppProductInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualMachineConfigSummary(DataObject):
    """
    A subset of virtual machine configuration. 
    """ # noqa: E501
    name: StrictStr = Field(description="Name of the virtual machine. ")
    template: StrictBool = Field(description="Flag to determine whether or not this virtual machine is a template. ")
    vm_path_name: StrictStr = Field(description="Path name to the configuration file for the virtual machine ", alias="vmPathName")
    memory_size_mb: Optional[StrictInt] = Field(default=None, description="Memory size of the virtual machine, in megabytes. ", alias="memorySizeMB")
    cpu_reservation: Optional[StrictInt] = Field(default=None, description="Configured CPU reservation in MHz ", alias="cpuReservation")
    memory_reservation: Optional[StrictInt] = Field(default=None, description="Configured Memory reservation in MB ", alias="memoryReservation")
    num_cpu: Optional[StrictInt] = Field(default=None, description="Number of processors in the virtual machine. ", alias="numCpu")
    num_ethernet_cards: Optional[StrictInt] = Field(default=None, description="Number of virtual network adapters. ", alias="numEthernetCards")
    num_virtual_disks: Optional[StrictInt] = Field(default=None, description="Number of virtual disks attached to the virtual machine. ", alias="numVirtualDisks")
    uuid: Optional[StrictStr] = Field(default=None, description="Virtual machine BIOS identification. ")
    instance_uuid: Optional[StrictStr] = Field(default=None, description="VC-specific identifier of the virtual machine  ***Since:*** vSphere API 4.0 ", alias="instanceUuid")
    guest_id: Optional[StrictStr] = Field(default=None, description="Guest operating system identifier (short name). ", alias="guestId")
    guest_full_name: Optional[StrictStr] = Field(default=None, description="Guest operating system name configured on the virtual machine. ", alias="guestFullName")
    annotation: Optional[StrictStr] = Field(default=None, description="Description for the virtual machine. ")
    product: Optional[VAppProductInfo] = None
    install_boot_required: Optional[StrictBool] = Field(default=None, description="Whether the VM requires a reboot to finish installation.  False if no vApp meta-data is configured.  ***Since:*** vSphere API 4.0 ", alias="installBootRequired")
    ft_info: Optional[FaultToleranceConfigInfo] = Field(default=None, alias="ftInfo")
    managed_by: Optional[ManagedByInfo] = Field(default=None, alias="managedBy")
    tpm_present: Optional[StrictBool] = Field(default=None, description="Is TPM present in a VM?  ***Since:*** vSphere API 6.7 ", alias="tpmPresent")
    num_vmiop_backings: Optional[StrictInt] = Field(default=None, description="Number of VMIOP backed devices attached to the virtual machine.  ***Since:*** vSphere API 6.7 ", alias="numVmiopBackings")
    hw_version: Optional[StrictStr] = Field(default=None, description="The hardware version string for this virtual machine.  ***Since:*** vSphere API 6.9.1 ", alias="hwVersion")
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
        """Create an instance of VirtualMachineConfigSummary from a JSON string"""
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
        """Create an instance of VirtualMachineConfigSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


