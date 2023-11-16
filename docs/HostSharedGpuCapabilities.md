# HostSharedGpuCapabilities

Capability vector indicating the available shared graphics features.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vgpu** | **str** | Name of a particular VGPU available as a shared GPU device.  See also *VirtualMachinePciSharedGpuPassthroughInfo*.  ***Since:*** vSphere API 6.7  | 
**disk_snapshot_supported** | **bool** | Indicates whether the GPU plugin on this host is capable of disk-only snapshots when VM is not powered off.  Disk Snaphosts on powered off VM are always supported.  ***Since:*** vSphere API 6.7  | 
**memory_snapshot_supported** | **bool** | Indicates whether the GPU plugin on this host is capable of memory snapshots.  ***Since:*** vSphere API 6.7  | 
**suspend_supported** | **bool** | Indicates whether the GPU plugin on this host is capable of suspend-resume.  ***Since:*** vSphere API 6.7  | 
**migrate_supported** | **bool** | Indicates whether the GPU plugin on this host is capable of migration.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.host_shared_gpu_capabilities import HostSharedGpuCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of HostSharedGpuCapabilities from a JSON string
host_shared_gpu_capabilities_instance = HostSharedGpuCapabilities.from_json(json)
# print the JSON string representation of the object
print HostSharedGpuCapabilities.to_json()

# convert the object into a dict
host_shared_gpu_capabilities_dict = host_shared_gpu_capabilities_instance.to_dict()
# create an instance of HostSharedGpuCapabilities from a dict
host_shared_gpu_capabilities_form_dict = host_shared_gpu_capabilities.from_dict(host_shared_gpu_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


