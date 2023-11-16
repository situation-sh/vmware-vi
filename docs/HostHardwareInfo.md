# HostHardwareInfo

The HardwareInfo data object type describes the hardware configuration of the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_info** | [**HostSystemInfo**](HostSystemInfo.md) |  | 
**cpu_power_management_info** | [**HostCpuPowerManagementInfo**](HostCpuPowerManagementInfo.md) |  | [optional] 
**cpu_info** | [**HostCpuInfo**](HostCpuInfo.md) |  | 
**cpu_pkg** | [**List[HostCpuPackage]**](HostCpuPackage.md) | Information about each of the physical CPU packages on the host.  | 
**memory_size** | **int** | Total amount of physical memory on the host in bytes.  | 
**numa_info** | [**HostNumaInfo**](HostNumaInfo.md) |  | [optional] 
**smc_present** | **bool** | Presence of System Management Controller, indicates the host is Apple hardware, and thus capable of running Mac OS guest as VM.  ***Since:*** vSphere API 5.0  | 
**pci_device** | [**List[HostPciDevice]**](HostPciDevice.md) | The list of Peripheral Component Interconnect (PCI) devices available on this host.  | [optional] 
**dvx_classes** | [**List[HostDvxClass]**](HostDvxClass.md) | The list of Device Virtualization Extensions (DVX) classes available on this host.  | [optional] 
**cpu_feature** | [**List[HostCpuIdInfo]**](HostCpuIdInfo.md) | CPU feature set that is supported by the hardware.  This is the intersection of the feature sets supported by the individual CPU packages. This feature set is modified by the *supportedCpuFeature* array in the host capabilities to obtain the feature set supported by the virtualization platform.  | [optional] 
**bios_info** | [**HostBIOSInfo**](HostBIOSInfo.md) |  | [optional] 
**reliable_memory_info** | [**HostReliableMemoryInfo**](HostReliableMemoryInfo.md) |  | [optional] 
**persistent_memory_info** | [**HostPersistentMemoryInfo**](HostPersistentMemoryInfo.md) |  | [optional] 
**sgx_info** | [**HostSgxInfo**](HostSgxInfo.md) |  | [optional] 
**sev_info** | [**HostSevInfo**](HostSevInfo.md) |  | [optional] 
**memory_tiering_type** | **str** | Type of memory tiering configured on this host.  See *HostMemoryTieringType_enum* for supported values. This field will be unset for legacy hosts as well as for hosts that don&#39;t support memory tiering.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**memory_tier_info** | [**List[HostMemoryTierInfo]**](HostMemoryTierInfo.md) | Configuration of each memory tier on this host.  The array is populated in the order of tiers (ie, tier 0 at array index 0, tier 1 at array index 1, and so on).  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_hardware_info import HostHardwareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostHardwareInfo from a JSON string
host_hardware_info_instance = HostHardwareInfo.from_json(json)
# print the JSON string representation of the object
print HostHardwareInfo.to_json()

# convert the object into a dict
host_hardware_info_dict = host_hardware_info_instance.to_dict()
# create an instance of HostHardwareInfo from a dict
host_hardware_info_form_dict = host_hardware_info.from_dict(host_hardware_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


