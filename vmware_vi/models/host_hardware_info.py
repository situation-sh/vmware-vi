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
from vmware_vi.models.host_bios_info import HostBIOSInfo
from vmware_vi.models.host_cpu_id_info import HostCpuIdInfo
from vmware_vi.models.host_cpu_info import HostCpuInfo
from vmware_vi.models.host_cpu_package import HostCpuPackage
from vmware_vi.models.host_cpu_power_management_info import HostCpuPowerManagementInfo
from vmware_vi.models.host_dvx_class import HostDvxClass
from vmware_vi.models.host_memory_tier_info import HostMemoryTierInfo
from vmware_vi.models.host_numa_info import HostNumaInfo
from vmware_vi.models.host_pci_device import HostPciDevice
from vmware_vi.models.host_persistent_memory_info import HostPersistentMemoryInfo
from vmware_vi.models.host_reliable_memory_info import HostReliableMemoryInfo
from vmware_vi.models.host_sev_info import HostSevInfo
from vmware_vi.models.host_sgx_info import HostSgxInfo
from vmware_vi.models.host_system_info import HostSystemInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostHardwareInfo(DataObject):
    """
    The HardwareInfo data object type describes the hardware configuration of the host. 
    """ # noqa: E501
    system_info: HostSystemInfo = Field(alias="systemInfo")
    cpu_power_management_info: Optional[HostCpuPowerManagementInfo] = Field(default=None, alias="cpuPowerManagementInfo")
    cpu_info: HostCpuInfo = Field(alias="cpuInfo")
    cpu_pkg: List[HostCpuPackage] = Field(description="Information about each of the physical CPU packages on the host. ", alias="cpuPkg")
    memory_size: StrictInt = Field(description="Total amount of physical memory on the host in bytes. ", alias="memorySize")
    numa_info: Optional[HostNumaInfo] = Field(default=None, alias="numaInfo")
    smc_present: StrictBool = Field(description="Presence of System Management Controller, indicates the host is Apple hardware, and thus capable of running Mac OS guest as VM.  ***Since:*** vSphere API 5.0 ", alias="smcPresent")
    pci_device: Optional[List[HostPciDevice]] = Field(default=None, description="The list of Peripheral Component Interconnect (PCI) devices available on this host. ", alias="pciDevice")
    dvx_classes: Optional[List[HostDvxClass]] = Field(default=None, description="The list of Device Virtualization Extensions (DVX) classes available on this host. ", alias="dvxClasses")
    cpu_feature: Optional[List[HostCpuIdInfo]] = Field(default=None, description="CPU feature set that is supported by the hardware.  This is the intersection of the feature sets supported by the individual CPU packages. This feature set is modified by the *supportedCpuFeature* array in the host capabilities to obtain the feature set supported by the virtualization platform. ", alias="cpuFeature")
    bios_info: Optional[HostBIOSInfo] = Field(default=None, alias="biosInfo")
    reliable_memory_info: Optional[HostReliableMemoryInfo] = Field(default=None, alias="reliableMemoryInfo")
    persistent_memory_info: Optional[HostPersistentMemoryInfo] = Field(default=None, alias="persistentMemoryInfo")
    sgx_info: Optional[HostSgxInfo] = Field(default=None, alias="sgxInfo")
    sev_info: Optional[HostSevInfo] = Field(default=None, alias="sevInfo")
    memory_tiering_type: Optional[StrictStr] = Field(default=None, description="Type of memory tiering configured on this host.  See *HostMemoryTieringType_enum* for supported values. This field will be unset for legacy hosts as well as for hosts that don't support memory tiering.  ***Since:*** vSphere API 7.0.3.0 ", alias="memoryTieringType")
    memory_tier_info: Optional[List[HostMemoryTierInfo]] = Field(default=None, description="Configuration of each memory tier on this host.  The array is populated in the order of tiers (ie, tier 0 at array index 0, tier 1 at array index 1, and so on).  ***Since:*** vSphere API 7.0.3.0 ", alias="memoryTierInfo")
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
        """Create an instance of HostHardwareInfo from a JSON string"""
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
        """Create an instance of HostHardwareInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


