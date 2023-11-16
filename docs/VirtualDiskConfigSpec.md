# VirtualDiskConfigSpec

The VirtualDiskSpec data object type encapsulates change specifications for an individual virtual disk device.  The virtual disk being added or modified must be fully specified.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_move_type** | **str** | Manner in which to move the virtual disk to the target datastore.  The set of possible values is described in *VirtualMachineRelocateDiskMoveOptions_enum*.  This property can only be set if *HostCapability.deltaDiskBackingsSupported* is true.  If left unset then *moveAllDiskBackingsAndDisallowSharing* is assumed.  ***Since:*** vSphere API 6.0  | [optional] 
**migrate_cache** | **bool** | Deprecated since vSphere 7.0 because vFlash Read Cache end of availability.  Manner in which to transfer the cache associated with the virtual disk to the target host.  If left unset then migrate is used when virtual flash resource on the source host is accessible and when the backing vFlash module version is compatible with the specific vFalsh module on the target host; otherwise flush is used for write back cache, or a no-op for write through cache. This setting can avoid VM migration failure due to incompatibility. If true then migrate is always used. VM migration may fail if the backing vFlash module version is incompatible with the module on the target host. If false then flush is used for write back cache. It is a no-op for write through cache. This setting can avoid VM migration failure due to incompatibility, but cache files have to be rebuilt on the target host. Default is unset.  See also *HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption*.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_config_spec import VirtualDiskConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskConfigSpec from a JSON string
virtual_disk_config_spec_instance = VirtualDiskConfigSpec.from_json(json)
# print the JSON string representation of the object
print VirtualDiskConfigSpec.to_json()

# convert the object into a dict
virtual_disk_config_spec_dict = virtual_disk_config_spec_instance.to_dict()
# create an instance of VirtualDiskConfigSpec from a dict
virtual_disk_config_spec_form_dict = virtual_disk_config_spec.from_dict(virtual_disk_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


