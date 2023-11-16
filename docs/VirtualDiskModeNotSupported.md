# VirtualDiskModeNotSupported

The disk mode of the specified virtual disk is not supported.  Typically, this fault is returned as part of a parent fault like *VmConfigIncompatibleForFaultTolerance*, indicating that the virtual disk's mode needs to be changed before fault tolerance can be enabled on the associated virtual machine.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Disk mode that is not supported  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.virtual_disk_mode_not_supported import VirtualDiskModeNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskModeNotSupported from a JSON string
virtual_disk_mode_not_supported_instance = VirtualDiskModeNotSupported.from_json(json)
# print the JSON string representation of the object
print VirtualDiskModeNotSupported.to_json()

# convert the object into a dict
virtual_disk_mode_not_supported_dict = virtual_disk_mode_not_supported_instance.to_dict()
# create an instance of VirtualDiskModeNotSupported from a dict
virtual_disk_mode_not_supported_form_dict = virtual_disk_mode_not_supported.from_dict(virtual_disk_mode_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


