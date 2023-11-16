# VirtualDiskFlatVer2BackingOption

This data object type contains the available options when backing a virtual disk using a host file with the flat file format used in VMware Server and in ESX Server 2.x and greater.  Flat disks are pre-allocated, whereas sparse disks are grown as needed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_mode** | [**ChoiceOption**](ChoiceOption.md) |  | 
**split** | [**BoolOption**](BoolOption.md) |  | 
**write_through** | [**BoolOption**](BoolOption.md) |  | 
**growable** | **bool** | Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation.  If set to true, reconfiguring this virtual disk with a *VirtualDisk.capacityInKB* value greater than its current value will grow the disk to the newly specified size.  | 
**hot_growable** | **bool** | Indicates whether or not this disk backing can be extended to larger sizes through a reconfigure operation while the virtual machine is powered on.  If set to true, reconfiguring this virtual disk with a *VirtualDisk.capacityInKB* value greater than its current value will grow the disk to the newly specified size while the virtual machine is powered on.  ***Since:*** VI API 2.5  | 
**uuid** | **bool** | Flag to indicate whether this backing supports disk UUID property.  ***Since:*** VI API 2.5  | 
**thin_provisioned** | [**BoolOption**](BoolOption.md) |  | 
**eagerly_scrub** | [**BoolOption**](BoolOption.md) |  | 
**delta_disk_format** | [**ChoiceOption**](ChoiceOption.md) |  | 
**delta_disk_formats_supported** | [**List[VirtualDiskDeltaDiskFormatsSupported]**](VirtualDiskDeltaDiskFormatsSupported.md) | Delta disk formats supported for each datastore type.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.virtual_disk_flat_ver2_backing_option import VirtualDiskFlatVer2BackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskFlatVer2BackingOption from a JSON string
virtual_disk_flat_ver2_backing_option_instance = VirtualDiskFlatVer2BackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDiskFlatVer2BackingOption.to_json()

# convert the object into a dict
virtual_disk_flat_ver2_backing_option_dict = virtual_disk_flat_ver2_backing_option_instance.to_dict()
# create an instance of VirtualDiskFlatVer2BackingOption from a dict
virtual_disk_flat_ver2_backing_option_form_dict = virtual_disk_flat_ver2_backing_option.from_dict(virtual_disk_flat_ver2_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


