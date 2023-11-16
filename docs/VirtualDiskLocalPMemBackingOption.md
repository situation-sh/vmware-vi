# VirtualDiskLocalPMemBackingOption

This data object type contains the available options when backing a virtualdisk using persistent memory.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_mode** | [**ChoiceOption**](ChoiceOption.md) |  | 
**growable** | **bool** | Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation.  If set to true, reconfiguring this virtual disk with a *VirtualDisk.capacityInKB* value greater than its current value will grow the disk to the newly specified size.  ***Since:*** vSphere API 6.7  | 
**hot_growable** | **bool** | Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation while the virtual machine is powered on.  If set to true, reconfiguring this virtual disk with a *VirtualDisk.capacityInKB* value greater than its current value will grow the disk to the newly specified size while the virtual machine is powered on.  ***Since:*** vSphere API 6.7  | 
**uuid** | **bool** | Flag to indicate whether this backing supports disk UUID property.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.virtual_disk_local_p_mem_backing_option import VirtualDiskLocalPMemBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskLocalPMemBackingOption from a JSON string
virtual_disk_local_p_mem_backing_option_instance = VirtualDiskLocalPMemBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDiskLocalPMemBackingOption.to_json()

# convert the object into a dict
virtual_disk_local_p_mem_backing_option_dict = virtual_disk_local_p_mem_backing_option_instance.to_dict()
# create an instance of VirtualDiskLocalPMemBackingOption from a dict
virtual_disk_local_p_mem_backing_option_form_dict = virtual_disk_local_p_mem_backing_option.from_dict(virtual_disk_local_p_mem_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


