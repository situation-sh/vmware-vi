# VirtualDiskSparseVer1BackingOption

This data object type contains the available options when backing a virtual disk using a host file with the sparse file format from GSX Server 2.x. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_modes** | [**ChoiceOption**](ChoiceOption.md) |  | 
**split** | [**BoolOption**](BoolOption.md) |  | 
**write_through** | [**BoolOption**](BoolOption.md) |  | 
**growable** | **bool** | Flag to indicate whether this backing can have its size changed.  | 

## Example

```python
from vmware_vi.models.virtual_disk_sparse_ver1_backing_option import VirtualDiskSparseVer1BackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskSparseVer1BackingOption from a JSON string
virtual_disk_sparse_ver1_backing_option_instance = VirtualDiskSparseVer1BackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDiskSparseVer1BackingOption.to_json()

# convert the object into a dict
virtual_disk_sparse_ver1_backing_option_dict = virtual_disk_sparse_ver1_backing_option_instance.to_dict()
# create an instance of VirtualDiskSparseVer1BackingOption from a dict
virtual_disk_sparse_ver1_backing_option_form_dict = virtual_disk_sparse_ver1_backing_option.from_dict(virtual_disk_sparse_ver1_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


