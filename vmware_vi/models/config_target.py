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
from pydantic import StrictBool, StrictInt
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.distributed_virtual_portgroup_info import DistributedVirtualPortgroupInfo
from vmware_vi.models.distributed_virtual_switch_info import DistributedVirtualSwitchInfo
from vmware_vi.models.opaque_network_target_info import OpaqueNetworkTargetInfo
from vmware_vi.models.resource_pool_runtime_info import ResourcePoolRuntimeInfo
from vmware_vi.models.virtual_machine_cdrom_info import VirtualMachineCdromInfo
from vmware_vi.models.virtual_machine_datastore_info import VirtualMachineDatastoreInfo
from vmware_vi.models.virtual_machine_dvx_class_info import VirtualMachineDvxClassInfo
from vmware_vi.models.virtual_machine_dynamic_passthrough_info import VirtualMachineDynamicPassthroughInfo
from vmware_vi.models.virtual_machine_floppy_info import VirtualMachineFloppyInfo
from vmware_vi.models.virtual_machine_ide_disk_device_info import VirtualMachineIdeDiskDeviceInfo
from vmware_vi.models.virtual_machine_legacy_network_switch_info import VirtualMachineLegacyNetworkSwitchInfo
from vmware_vi.models.virtual_machine_network_info import VirtualMachineNetworkInfo
from vmware_vi.models.virtual_machine_parallel_info import VirtualMachineParallelInfo
from vmware_vi.models.virtual_machine_pci_passthrough_info import VirtualMachinePciPassthroughInfo
from vmware_vi.models.virtual_machine_pci_shared_gpu_passthrough_info import VirtualMachinePciSharedGpuPassthroughInfo
from vmware_vi.models.virtual_machine_precision_clock_info import VirtualMachinePrecisionClockInfo
from vmware_vi.models.virtual_machine_scsi_disk_device_info import VirtualMachineScsiDiskDeviceInfo
from vmware_vi.models.virtual_machine_scsi_passthrough_info import VirtualMachineScsiPassthroughInfo
from vmware_vi.models.virtual_machine_serial_info import VirtualMachineSerialInfo
from vmware_vi.models.virtual_machine_sgx_target_info import VirtualMachineSgxTargetInfo
from vmware_vi.models.virtual_machine_sound_info import VirtualMachineSoundInfo
from vmware_vi.models.virtual_machine_sriov_info import VirtualMachineSriovInfo
from vmware_vi.models.virtual_machine_usb_info import VirtualMachineUsbInfo
from vmware_vi.models.virtual_machine_v_flash_module_info import VirtualMachineVFlashModuleInfo
from vmware_vi.models.virtual_machine_vendor_device_group_info import VirtualMachineVendorDeviceGroupInfo
from vmware_vi.models.virtual_machine_vgpu_device_info import VirtualMachineVgpuDeviceInfo
from vmware_vi.models.virtual_machine_vgpu_profile_info import VirtualMachineVgpuProfileInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigTarget(DataObject):
    """
    The ConfigTarget class contains information about \"physical\" devices that can be used to back virtual devices. 
    """ # noqa: E501
    num_cpus: StrictInt = Field(description="Number of logical CPUs that can be used to run virtual machines.  If invoked against a cluster, this is the total number of logical CPUs available in the cluster. ", alias="numCpus")
    num_cpu_cores: StrictInt = Field(description="Number of physical CPU cores that are available to run virtual machines.  If invoked against a cluster, this is the total number of physical CPUs available in the cluster. ", alias="numCpuCores")
    num_numa_nodes: StrictInt = Field(description="Number of NUMA nodes.  If invoked against a cluster, this is the total number of NUMA nodes available in the cluster. ", alias="numNumaNodes")
    max_cpus_per_host: Optional[StrictInt] = Field(default=None, description="Maximum number of CPUs available on a single host.  For standalone hosts, this value will be the same as numCpus.  ***Since:*** vSphere API 7.0 ", alias="maxCpusPerHost")
    smc_present: StrictBool = Field(description="Presence of System Management Controller, indicates the host is Apple hardware, and thus capable of running Mac OS guest as VM.  ***Since:*** vSphere API 5.0 ", alias="smcPresent")
    datastore: Optional[List[VirtualMachineDatastoreInfo]] = Field(default=None, description="List of datastores available for virtual disks and associated storage. ")
    network: Optional[List[VirtualMachineNetworkInfo]] = Field(default=None, description="List of networks available for virtual network adapters. ")
    opaque_network: Optional[List[OpaqueNetworkTargetInfo]] = Field(default=None, description="List of opaque networks available for virtual network adapters.  ***Since:*** vSphere API 5.5 ", alias="opaqueNetwork")
    distributed_virtual_portgroup: Optional[List[DistributedVirtualPortgroupInfo]] = Field(default=None, description="List of networks available from DistributedVirtualSwitch for virtual network adapters.  ***Since:*** vSphere API 4.0 ", alias="distributedVirtualPortgroup")
    distributed_virtual_switch: Optional[List[DistributedVirtualSwitchInfo]] = Field(default=None, description="List of distributed virtual switch available for virtual network adapters.  ***Since:*** vSphere API 4.0 ", alias="distributedVirtualSwitch")
    cd_rom: Optional[List[VirtualMachineCdromInfo]] = Field(default=None, description="List of CD-ROM devices available for use by virtual CD-ROMs.  Used for *VirtualCdromAtapiBackingInfo*. ", alias="cdRom")
    serial: Optional[List[VirtualMachineSerialInfo]] = Field(default=None, description="List of serial devices available to support virtualization.  Used for *VirtualSerialPortDeviceBackingInfo*. ")
    parallel: Optional[List[VirtualMachineParallelInfo]] = Field(default=None, description="List of parallel devices available to support virtualization.  Used for *VirtualParallelPortDeviceBackingInfo*. ")
    sound: Optional[List[VirtualMachineSoundInfo]] = Field(default=None, description="List of sound devices available to support virtualization.  Used for *VirtualSoundCardDeviceBackingInfo*.  ***Since:*** VI API 2.5 ")
    usb: Optional[List[VirtualMachineUsbInfo]] = Field(default=None, description="List of USB devices on the host that are available to support virtualization.  Used for *VirtualUSBUSBBackingInfo*.  ***Since:*** VI API 2.5 ")
    floppy: Optional[List[VirtualMachineFloppyInfo]] = Field(default=None, description="List of floppy devices available for use by virtual floppies.  Used for *VirtualFloppyDeviceBackingInfo*. ")
    legacy_network_info: Optional[List[VirtualMachineLegacyNetworkSwitchInfo]] = Field(default=None, description="Legacy switch names when using the LegacyNetworkBacking types. ", alias="legacyNetworkInfo")
    scsi_passthrough: Optional[List[VirtualMachineScsiPassthroughInfo]] = Field(default=None, description="List of generic SCSI devices. ", alias="scsiPassthrough")
    scsi_disk: Optional[List[VirtualMachineScsiDiskDeviceInfo]] = Field(default=None, description="List of physical SCSI disks that can be used as targets for raw disk mapping backings. ", alias="scsiDisk")
    ide_disk: Optional[List[VirtualMachineIdeDiskDeviceInfo]] = Field(default=None, description="List of physical IDE disks that can be used as targets for raw disk backings. ", alias="ideDisk")
    max_mem_mb_optimal_perf: StrictInt = Field(description="Maximum recommended memory size, in MB, for creating a new virtual machine. ", alias="maxMemMBOptimalPerf")
    supported_max_mem_mb: Optional[StrictInt] = Field(default=None, description="Maximum supported memory size, in MB, for creating a new virtual machine.  Maximum allowed size is smaller of this and limit in *GuestOsDescriptor.supportedMaxMemMB*. When invoked on the cluster, maximum size that can be created on at least one host in the cluster is reported.  ***Since:*** vSphere API 7.0 ", alias="supportedMaxMemMB")
    resource_pool: Optional[ResourcePoolRuntimeInfo] = Field(default=None, alias="resourcePool")
    auto_vmotion: Optional[StrictBool] = Field(default=None, description="Information whether a virtual machine with this ConfigTarget can auto vmotion.  This field is only populated from an Environment browser obtained from a virtual machine. ", alias="autoVmotion")
    pci_passthrough: Optional[List[VirtualMachinePciPassthroughInfo]] = Field(default=None, description="List of generic PCI devices.  ***Since:*** vSphere API 4.0 ", alias="pciPassthrough")
    sriov: Optional[List[VirtualMachineSriovInfo]] = Field(default=None, description="List of SRIOV devices.  ***Since:*** vSphere API 5.5 ")
    v_flash_module: Optional[List[VirtualMachineVFlashModuleInfo]] = Field(default=None, description="List of vFlash modules.  ***Since:*** vSphere API 5.5 ", alias="vFlashModule")
    shared_gpu_passthrough_types: Optional[List[VirtualMachinePciSharedGpuPassthroughInfo]] = Field(default=None, description="List of shared GPU passthrough types.  ***Since:*** vSphere API 6.0 ", alias="sharedGpuPassthroughTypes")
    available_persistent_memory_reservation_mb: Optional[StrictInt] = Field(default=None, description="Maximum available persistent memory reservation on a compute resource in MB.  ***Since:*** vSphere API 6.7 ", alias="availablePersistentMemoryReservationMB")
    dynamic_passthrough: Optional[List[VirtualMachineDynamicPassthroughInfo]] = Field(default=None, description="List of Dynamic DirectPath PCI devices.  ***Since:*** vSphere API 7.0 ", alias="dynamicPassthrough")
    sgx_target_info: Optional[VirtualMachineSgxTargetInfo] = Field(default=None, alias="sgxTargetInfo")
    precision_clock_info: Optional[List[VirtualMachinePrecisionClockInfo]] = Field(default=None, description="List of host clock resources available to support virtual precision clock device.  Used for *VirtualPrecisionClockSystemClockBackingInfo*  ***Since:*** vSphere API 7.0 ", alias="precisionClockInfo")
    sev_supported: Optional[StrictBool] = Field(default=None, description="Indicates whether the compute resource is capable of running AMD Secure Encrypted Virtualization (SEV) enabled virtual machines.  The compute resource supports SEV when this value is set to true.  ***Since:*** vSphere API 7.0.1.0 ", alias="sevSupported")
    vgpu_device_info: Optional[List[VirtualMachineVgpuDeviceInfo]] = Field(default=None, description="List of vGPU device capabilities.  ***Since:*** vSphere API 7.0.3.0 ", alias="vgpuDeviceInfo")
    vgpu_profile_info: Optional[List[VirtualMachineVgpuProfileInfo]] = Field(default=None, description="List of vGPU profile attributes.  ***Since:*** vSphere API 7.0.3.0 ", alias="vgpuProfileInfo")
    vendor_device_group_info: Optional[List[VirtualMachineVendorDeviceGroupInfo]] = Field(default=None, description="List of PCI Vendor Device Groups. ", alias="vendorDeviceGroupInfo")
    max_simultaneous_threads: Optional[StrictInt] = Field(default=None, description="Max SMT (Simultaneous multithreading) threads. ", alias="maxSimultaneousThreads")
    dvx_class_info: Optional[List[VirtualMachineDvxClassInfo]] = Field(default=None, description="List of Device Virtualization Extensions (DVX) classes. ", alias="dvxClassInfo")
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
        """Create an instance of ConfigTarget from a JSON string"""
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
        """Create an instance of ConfigTarget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


