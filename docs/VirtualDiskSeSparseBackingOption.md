# VirtualDiskSeSparseBackingOption

Backing options for virtual disks that use the space efficient sparse format.  Space for Flex-SE disks is allocated on demand and optimizations are applied to achieve additional space savings.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_mode** | [**ChoiceOption**](ChoiceOption.md) |  | 
**write_through** | [**BoolOption**](BoolOption.md) |  | 
**growable** | **bool** | Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation.  If set to true, reconfiguring this virtual disk with a *VirtualDisk.capacityInKB* value greater than its current value will grow the disk to the newly specified size.  ***Since:*** vSphere API 5.1  | 
**hot_growable** | **bool** | Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation while the virtual machine is powered on.  If set to true, reconfiguring this virtual disk with a *VirtualDisk.capacityInKB* value greater than its current value will grow the disk to the newly specified size while the virtual machine is powered on.  ***Since:*** vSphere API 5.1  | 
**uuid** | **bool** | Flag to indicate whether this backing supports disk UUID property.  ***Since:*** vSphere API 5.1  | 
**delta_disk_formats_supported** | [**List[VirtualDiskDeltaDiskFormatsSupported]**](VirtualDiskDeltaDiskFormatsSupported.md) | Delta disk formats supported for each datastore type.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.virtual_disk_se_sparse_backing_option import VirtualDiskSeSparseBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskSeSparseBackingOption from a JSON string
virtual_disk_se_sparse_backing_option_instance = VirtualDiskSeSparseBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDiskSeSparseBackingOption.to_json()

# convert the object into a dict
virtual_disk_se_sparse_backing_option_dict = virtual_disk_se_sparse_backing_option_instance.to_dict()
# create an instance of VirtualDiskSeSparseBackingOption from a dict
virtual_disk_se_sparse_backing_option_form_dict = virtual_disk_se_sparse_backing_option.from_dict(virtual_disk_se_sparse_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


